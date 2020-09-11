.. _the-default-camera-driver:

The Default Camera Driver
=========================

By default, panda runs a task that enables you to move the camera using the
mouse. This task will conflict with any code you write to move the camera. The
task controls the camera by updating the camera's position every frame to
where the mouse thinks it should be. This means that any other code that
directly controls the camera will not seem to work, because it will be
fighting the mouse for control.

If you want to move the camera directly under show control, you must first
disable the camera control task and then the camera will move as expected.

.. code-block:: python

   base.disableMouse()

The ShowBase class contains some handy methods to allow the user control over
the camera. The :py:meth:`~direct.showbase.ShowBase.ShowBase.useDrive()` command
enables keyboard and mouse control. Both control systems move only on the x
and y axes, so moving up and down along the z axis is impossible with these
systems.

The keyboard system uses the arrow keys. Up moves the camera forward, and down
move it back. The left and right arrows turn the camera.

The mouse system responds whenever any button is held. If the pointer is
towards the top of the screen, the camera moves forward. If it is towards the
bottom, the camera moves backwards. If it is on either side, the camera
rotates to that direction. The speed the camera moves is determined by how far
from the center the mouse pointer is. Additionally, there is another command
that allows control based on trackball mice.

.. code-block:: python

   base.useDrive()
   base.useTrackball()

ShowBase also provides the method
:py:meth:`~direct.showbase.ShowBase.ShowBase.oobe()` to give you to control
of the basic camera node (base.cam) with the mouse/trackball while the code
continues to move the camera node (base.camera). This can be useful for
debugging purposes. The word stands for "out-of-body experience" and is handy
for giving you a God's-eye view of your application at any point in
development. The method is a toggle; call it once to enable OOBE mode, and
then again to disable it.

.. code-block:: python

   base.oobe()

:py:meth:`~direct.showbase.ShowBase.ShowBase.oobeCull()` is a variant on
:py:meth:`~direct.showbase.ShowBase.ShowBase.oobe()`, and it works
similarly, except that it still culls the scene as if the camera were still in
its original position, while drawing the scene from the point of view of your
camera's new position. So now you can view the scene from your "out of body"
placement, and walk around, and you can see things popping in and out of view
as your view frustum moves around the world.
