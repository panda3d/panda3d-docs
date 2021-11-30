.. _async-loading:

Asynchronous Loading
====================

We've seen a basic way to load models in :ref:`model-files` using
:py:meth:`loader.loadModel() <direct.showbase.Loader.Loader.loadModel>`.
The major problem with this call is that it blocks the main thread while the
model is being loaded, which means that all other tasks on the main thread
(including Panda's rendering task) are blocked until the model has finished
loading. This is noticeable by the user as a jarring lag, especially when the
application freezes for longer periods of time.

.. only:: python

   The following example demonstrates the naive way to load the scene models:

   .. code-block:: python

      class Game(ShowBase):
          def __init__(self):
              ShowBase.__init__(self)

              self.loadScene()

          def loadScene(self):
              text = OnscreenText("Loading…")

              self.terrainModel = loader.loadModel("terrain")
              self.terrainModel.reparentTo(render)
              self.cityModel = loader.loadModel("city")
              self.cityModel.reparentTo(render)

              text.destroy()

   You may notice that the "Loading" screen will never appear, because Panda3D
   never gets a chance to render it! We could force Panda3D to render a frame
   after creating the text object, but still, any operation that requires a
   re-render (such as resizing the window, or alt-tabbing to another
   application) would cause the window to become black and may even prompt the
   operating system to warn that the application is not responding.

Clearly, this does not provide a good user experience. Therefore, it is
recommended that models are loaded in an :term:`asynchronous` manner, in a
separate thread of execution, so that the application can continue rendering
while the load operation occurs in the background. Panda3D provides several
ways of doing so.

.. only:: python

   Loading with callback
   ---------------------

   One of the ways to achieve asynchronous loading is with the callback argument
   to :py:meth:`loader.loadModel() <direct.showbase.Loader.Loader.loadModel>`.
   If callback is not None, then the model load will be performed
   asynchronously.
   In this case, :py:meth:`~direct.showbase.Loader.Loader.loadModel()` will
   initiate a background load and return immediately. The return value will be
   an object that you may call ``.cancel()`` on to cancel the asynchronous
   request. At some later point, when the requested model(s) have finished
   loading, the callback function will be invoked with the n loaded models
   passed as its parameter list.
   It is possible that the callback will be invoked immediately, even before
   :py:meth:`~direct.showbase.Loader.Loader.loadModel()` returns.

   If you use a callback, you may also specify a priority, which specifies the
   relative importance over this model over all of the other asynchronous load
   requests (higher numbers are loaded first).

   The following example shows how to use this feature.

   .. code-block:: python

      class Game(ShowBase):
          def __init__(self):
              ShowBase.__init__(self)

              self.accept('escape', self.quit)

              self.loadRequest = None
              self.startLoading()

          def startLoading(self):
              self.loadingText = OnscreenText("Loading…")

              self.loadRequest = loader.loadModel(["terrain", "city"], callback=self.finishLoading)

          def finishLoading(self, models):
              # Get rid of temporary objects
              self.loadRequest = None
              self.loadingText.destroy()
              del self.loadingText

              # Process the models that finished loading
              self.terrainModel, self.cityModel = models

              self.terrainModel.reparentTo(render)
              self.cityModel.reparentTo(render)

          def quit(self):
              if self.loadRequest:
                  self.loadRequest.cancel()

              sys.exit()

Loading in a coroutine
----------------------

.. only:: python

   As you can see, the previous approach made the code quite a bit more
   convoluted. We had to split up the load process into two methods, and also
   take special care to ensure that the load request was cancelled when
   necessary, and take care of where the intermediate variables were stored
   during the load operation. If we also wanted to handle exceptions in the load
   operation properly, it would get more complicated still!

   A far more convenient way to do this is using :ref:`coroutines`, introduced
   in Python 3.5 and supported as of Panda3D 1.10. These are special functions
   that can be suspended temporarily and resumed at a later point (pending the
   completion of an :term:`asynchronous` operation). Instead, we can write our
   code as though it were synchronous, but we insert the ``await`` keyword where
   we want the task to be suspended while waiting for the following operation.

   To make this possible, a few things are necessary:

   1. We need to put ``async`` in front of our function.
   2. We can no longer call the function directly, but rather need to schedule
      its execution using the task manager.
   3. The asynchronous operation needs to return a :term:`future` object. To get
      :py:meth:`loader.loadModel() <direct.showbase.Loader.Loader.loadModel>` to
      do so, we need to pass the ``blocking=False`` parameter.
   4. We need to use ``await`` on this future object to suspend the task while
      the operation is not yet done.

   This may seem complicated at first, but it really allows us to write much
   more straightforward code:

   .. code-block:: python

      class Game(ShowBase):
          def __init__(self):
              ShowBase.__init__(self)

              self.accept('escape', self.quit)

              self.taskMgr.add(self.loadScene())

          async def loadScene(self):
              text = OnscreenText("Loading…")

              # Load the models in the background, each time suspending this
              # method until they are done
              self.terrainModel = await loader.loadModel("terrain", blocking=False)
              self.cityModel = await loader.loadModel("city", blocking=False)

              self.terrainModel.reparentTo(render)
              self.cityModel.reparentTo(render)

              text.destroy()

          def quit(self):
              sys.exit()

.. only:: cpp

   A convenient way to do this would be by using :ref:`coroutines`, introduced
   in C++20. These are special functions that can be suspended temporarily and
   resumed at a later point (pending the completion of an :term:`asynchronous`
   operation). Instead, we could write our code as though it were synchronous,
   but we insert the ``co_await`` keyword where we want the task to be suspended
   while waiting for the following operation.

   Unfortunately, as of Panda3D 1.10, this feature of C++20 is not yet supported
   by Panda3D. If you are feeling adventurous, see this forum thread for a way
   to use C++20 coroutines with the Panda3D task system:

   https://discourse.panda3d.org/t/using-c-20-coroutines-with-panda3d/27323

Loading in a thread
-------------------

Alternatively, it is possible to use a separate thread to initiate the model
load. Panda3D's scene graph is thread-safe and can safely handle model
operations from any thread. See the :ref:`threading` page for more details.

One thing to note is that you may want to make sure that you complete all model
operations (positioning, material assignments, etc.) before attaching it into
the scene graph. Otherwise, if Panda3D happens to render a frame in between
those calls, there is a chance that the model may briefly appear in its
original state.

On-demand texture loading
-------------------------

In addition, you can further ask textures to be loaded to the graphics card
asynchronously. This means that the first time you look at a particular model,
the texture might not be available; but instead of holding up the frame while we
wait for it to be loaded, Panda can render the model immediately, with a very
low-resolution version of the texture or even a flat color, and start loading of
the full-resolution version in the background.
When the texture is eventually loaded, it will be applied. This results in fewer
frame-rate chugs, but it means that the model looks a little weird at first. It
has the greatest advantage when you are using lazy-load textures as well as
texture compression, because it means these things will happen in the
background. Use these configuration options to enable this behavior::

   preload-textures 0
   preload-simple-textures 1
   simple-image-size 16 16
   compressed-textures 1
   allow-incomplete-render 1

When converting models to .bam with ``preload-simple-textures`` active, simple
textures will be baked into the model, so that Panda (starting with version
1.10.11) doesn't need to load the textures from disk at all until they first
come into view.

To test this process, you can set ``async-load-delay`` with a value in seconds,
which artificially delays each individual texture load by the given amount.
This is useful for simulating the user experience on older computers with slower
hard drives.  Set it to a value like ``0.1`` and you should see the textures pop
in as you move around the scene.

You can use :meth:`.DisplayRegion.set_texture_reload_priority()` if you want
ensure that textures in some scenes are loaded with higher priority than other
scenes.

Animation loading
-----------------

A similar behavior can be enabled for Actors, so that when you have an Actor
with a large number of animations (too many to preload them all at once), you
can have the Actor load them on-demand, so that when you play an animation, the
animation may not start playing immediately, but will instead be loaded in the
background. Until it is ready, the actor will hold its last pose, and then when
the animation is fully loaded, the actor will start playing where it would have
been had the animation been loaded from the beginning. To make this work, you
have to run all of the animations through ``egg-optchar`` with the ``-preload``
option, and you might also want to set::

   allow-async-bind 1
   restore-initial-pose 0

Configuration
-------------

All of the above asynchronous operations will take place on a separate
:ref:`task chain <task-chains>`, automatically created by :class:`.Loader`.
By default, one low-priority thread is created to serve these requests.
To increase the number of available threads, or to increase their priority,
these configuration variables can be changed::

   # default is 1
   loader-num-threads 2
   # default is low
   loader-thread-priority normal
