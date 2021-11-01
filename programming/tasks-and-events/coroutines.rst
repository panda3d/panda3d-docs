.. _coroutines:

Coroutines
==========

.. only:: python

   Coroutines are a special kind of function introduced in Python 3.5 that can
   be temporarily suspended, pending the completion of an :term:`asynchronous`
   operation, to be resumed after this operation is complete. Panda3D's task
   system has full support for Python's coroutines.

   This feature can be hard to understand at first, but it is tremendously
   useful and powerful, since it makes it easy to write lag-free applications.
   Heavy operations that would otherwise cause the application to lag or hang
   can be performed in the background without adding significant complexity to
   the code.

   To turn a regular function into a coroutine, it is marked with the ``async``
   keyword. The ``await`` keyword can then be used within the function to pause
   it while some :term:`asynchronous` operation runs in the background. In the
   meantime, other parts of the application can continue to run, eliminating any
   lag that may otherwise manifest itself.

   To understand how async functions run, you must understand that you cannot
   simply invoke an async function as though it were a regular function. Some
   process needs to be in charge of the lifetime of a coroutine, resuming it
   whenever necessary. In regular Python, this is the :mod:`asyncio` event loop,
   but Panda3D already has the task manager to schedule the execution of
   functions, which (unlike asyncio) is thread-safe, and integrates cleanly with
   the rest of Panda3D.

   Let's take this Python function as an example of a regular, *synchronous*
   function that generates undesirable lag. It counts down a given number of
   seconds and then prints "Launch!" to the console.

   .. code-block:: python

      import time


      def launchRocket(countdown):
          print("Beginning countdown…")

          while countdown > 0:
             print(countdown)

             # Suspend the application for a second
             time.sleep(1.0)
             countdown -= 1

          print("Launch!")

      launchRocket(countdown=3)

   The problem with the above code is that :py:func:`time.sleep()` will block
   the main thread while it is waiting, meaning that other tasks (including
   Panda3D's rendering loop) will not get a chance to run in the meantime. The
   entire application will appear to have frozen until the countdown is
   complete!

   It is certainly possible to use multiple tasks with delays in order to solve
   this problem. However, this will quickly make the code a lot more complex,
   with multiple functions and state variables that need to be stored somewhere.
   Instead, let us see how we can turn this into a coroutine with minimal
   modifications:

   .. code-block:: python

      from direct.task.Task import Task


      async def launchRocket(countdown):
          print("Beginning countdown…")

          while countdown > 0:
             print(countdown)

             # Suspend the task for a second
             await Task.pause(1.0)
             countdown -= 1

          print("Launch!")

      taskMgr.add(launchRocket(countdown=3))

   The moment we use ``await`` in the above code, the function is paused until
   the given operation completes. We use ``Task.pause(1.0)`` here, which creates
   a task that simply finishes after 1 second. In the meantime, other tasks can
   continue to run, including Panda3D's render loop, so the lag is eliminated.

   Coroutine Tasks
   ---------------

   Please note that even though the coroutine is added to the task manager, it
   is not the same thing as a task, since it is invoked only once and it does
   not receive the ``task`` argument. We can in fact create a recurring task
   that is also a coroutine by simply prepending the ``async`` keyword to a
   regular task, as demonstrated by this pseudo-code:

   .. code-block:: python

      from direct.task.Task import Task


      async def damageTask(task):
          if player just collided with invincibility item:
              # Suspend damage task until invincibility is no longer active
              await Task.pause(10.0)

          return task.cont

      # Note the lack of parentheses here!
      taskMgr.add(damageTask)

   This behaves identically to a regular task, except that it permits use of the
   ``await`` keyword.

.. only:: cpp

   Coroutines are a feature introduced in C++20 that allow a function to be
   temporarily suspended, pending the completion of an :term:`asynchronous`
   operation.

   At the time of writing, Panda3D does not yet integrate support for the C++20
   coroutine feature into the library. If you are feeling adventurous, see this
   forum thread for a way to use C++20 coroutines with the Panda3D task system:

   https://discourse.panda3d.org/t/using-c-20-coroutines-with-panda3d/27323

Awaitables
----------

.. only:: python

   In the examples so far have only used ``Task.pause()``, but there are in fact
   many things that can be used as our argument to ``await``:

   * All :ref:`intervals`. This is very useful for transitions or cutscenes,
     where it is desirable to disable user input, await a sequence of intervals,
     and then re-enable user input when they are done. With coroutines, this can
     all happen in a single function.
   * All :ref:`tasks`. When awaiting a task, it is automatically scheduled with
     the task manager (on the current task chain), if not already.
   * Any :class:`.AsyncFuture` object. Such an object is returned by various
     Panda3D operations that take a long time to complete.
   * Any Python object that implements a suitable ``__await__`` method.

   Some examples of operations that satisfy one or more of the above conditions:

   * Model load operations, see :ref:`async-loading`.
   * ``messenger.future('event')``, to suspend the coroutine until an event is
     fired from outside the coroutine.
   * :meth:`tex.prepare() <.Texture.prepare>`, to wait for a texture to finish
     uploading to the graphics card. The returned value is the
     prepared :class:`.TextureContext` object.

.. only:: cpp

   Panda3D provides the :class:`.AsyncFuture` class to represent an operation
   that is currently underway. Any operation that returns this class is
   considered an asynchronous operation.

Experimental feature
--------------------

As of Panda3D 1.10, this is still an experimental feature, and some behavior may
change in future versions. The upcoming version of Panda3D, 1.11, will improve
support for cancellation of futures in particular.
