.. _controlling-the-camera:

Controlling the Camera
======================

Default Camera Control System
-----------------------------

By default, Panda3D runs a task that allows you to move the camera using the
mouse.

.. only:: cpp

   To enable it, use the following command:

   .. code-block:: cpp

      window->setup_trackball();

The keys to navigate are:

======================== ============================================
Mouse Button             Action
======================== ============================================
Left Button              Pan left and right.
Right Button             Move forwards and backwards.
Middle Button            Rotate around the origin of the application.
Right and Middle Buttons Roll the point of view around the view axis.
======================== ============================================

Go ahead and try this camera control system. The problem with it is that it is
sometimes awkward. It is not always easy to get the camera pointed in the
direction we want.

:ref:`Tasks <tasks>`
--------------------

Update the Code
~~~~~~~~~~~~~~~

Instead, we are going to write a *task* that controls the camera's position
explicitly. A *task* is nothing but a procedure that gets called every frame.
Update your code as follows:

.. only:: python

   .. literalinclude:: controlling-the-camera.py
      :language: python
      :linenos:

.. only:: cpp

   .. literalinclude:: controlling-the-camera.cxx
      :language: cpp
      :linenos:

.. only:: python

   The procedure :py:meth:`taskMgr.add()` tells Panda3D's task manager to call
   the procedure ``spinCameraTask()`` every frame. This is a procedure that we
   have written to control the camera. As long as the procedure
   ``spinCameraTask()`` returns the constant ``Task.cont``, the task manager
   will continue to call it every frame.

.. only:: cpp

   The procedure :meth:`taskMgr->add() <.AsyncTaskManager.add>` tells Panda3D's
   task manager to call the procedure ``spinCameraTask()`` every frame. This is
   a procedure that we have written to control the camera. As long as the
   procedure ``spinCameraTask()`` returns the constant ``AsyncTask.DS_cont``,
   the task manager will continue to call it every frame.

   The object passed to :meth:`taskMgr->add() <.AsyncTaskManager.add>` is an
   :class:`.AsyncTask` object. We can use ``GenericAsyncTask`` to wrap a global
   function or static method around a task. We can also pass an additional
   ``void*`` parameter that we can cast into a pointer of any data type we like,
   which is passed as argument to the task function. A GenericAsyncTask function
   must look like the following:

   .. code-block:: cpp

      AsyncTask::DoneStatus your_task(GenericAsyncTask *task, void *data) {
        // Do your stuff here.

        // Tell the task manager to continue this task the next frame.
        // You can also pass DS_done if this task should not be run again.
        return AsyncTask::DS_cont;
      }

   For more advanced usage, you can subclass AsyncTask and override the
   ``do_task`` method to make it do what you want.

In our code, the procedure ``spinCameraTask()`` calculates the desired position
of the camera based on how much time has elapsed. The camera rotates 6 degrees
every second. The first two lines compute the desired orientation of the camera;
first in degrees, and then in radians. The :meth:`~.NodePath.set_pos()` call
actually sets the position of the camera. (Remember that Y is horizontal and Z
is vertical, so the position is changed by animating X and Y while Z is left
fixed at 3 units above ground level.) The :meth:`~.NodePath.set_hpr()` call
actually sets the orientation.

Run the Program
~~~~~~~~~~~~~~~

The camera should no longer be underground; and furthermore, it should now be
rotating about the clearing:

.. image:: tutorial2.jpg
