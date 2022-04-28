.. _loading-the-grassy-scenery:

Loading the Grassy Scenery
==========================

:ref:`The Scene Graph <the-scene-graph>`
----------------------------------------

Panda3D contains a data structure called the *Scene Graph*. The Scene Graph is a
tree containing all objects that need to be rendered. At the root of the tree is
an object named `render`. Nothing is rendered until it is first inserted into
the Scene Graph.

.. only:: cpp

   You can get the NodePath of `render` by calling
   :cpp:func:`window->get_render() <WindowFramework::get_render>`.

To install the grassy scenery model into the Scene Graph, we use the method
:meth:`~.NodePath.reparent_to()`. This sets the parent of the model, thereby
giving it a place in the Scene Graph. Doing so makes the model visible in the
scene.

Finally, we adjust the position and scale of the model. In this particular case,
the environment model is a little too large and somewhat offset for our
purposes. The :meth:`~.NodePath.set_scale()` and :meth:`~.NodePath.set_pos()`
procedures rescale and center the model.

Panda3D uses the "geographical" coordinate system where position (-8, 42, 0)
means map coordinates (8, 42) and height 0. If you are used to OpenGL/Direct3D
coordinates, then hold up your right hand in the classical position with thumb
as X, fingers as Y, and palm as Z facing toward you; then tilt backward until
your hand is level with the fingers pointing away and palm facing up. Moving
"forward" in Panda3D is a positive change in Y coordinate.

The Program
-----------

Update the Code
~~~~~~~~~~~~~~~

With Panda3D running properly, it is now possible to load some grassy scenery.
Update your code as follows:

.. only:: python

   .. literalinclude:: loading-the-grassy-scenery.py
      :language: python
      :linenos:

   The ShowBase procedure :py:meth:`loader.loadModel()
   <direct.showbase.Loader.Loader.loadModel>` loads the specified file, in this
   case the environment.egg file in the models folder. The return value is an
   object of the :class:`.NodePath` class, effectively a pointer to the model.
   Note that :ref:`filename-syntax` uses the forward-slash, even under Windows.

.. only:: cpp

   .. literalinclude:: loading-the-grassy-scenery.cxx
      :language: cpp
      :linenos:

   The WindowFramework procedure
   :cpp:func:`window->load_model() <WindowFramework::load_model>` loads the
   specified file, in this case the environment.egg file in the models folder.
   The return value is an object of the :class:`.NodePath` class, effectively a
   pointer to the model. Note that :ref:`filename-syntax` uses the
   forward-slash, even under Windows.

Run the Program
~~~~~~~~~~~~~~~

Go ahead and run the program. You should see this:

.. image:: tutorial1.jpg

The rock and tree appear to be hovering. The camera is slightly below ground,
and back-face culling is making the ground invisible to us. If we reposition the
camera, the terrain will look better.
