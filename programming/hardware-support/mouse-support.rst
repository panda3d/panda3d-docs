.. _mouse-support:

Mouse Support
=============

Panda3D has mouse support built in.

.. only:: python

   In Python, the default action of the mouse is to control the camera. If you
   want to disable this functionality you can use the command:

   .. code-block:: python

      base.disableMouse()

   This function's name is slightly misleading. It only disables the task that
   drives the camera around, it doesn't disable the mouse itself. You can still
   get the position of the mouse, as well as the mouse clicks.

.. only:: cpp

   In C++, you need to do the following if you want the mouse to control the
   camera:

   .. code-block:: cpp

      window->setup_trackball();

   You don't need to do this to enable the mouse itself, only to enable a task
   that drives the camera around. You can still get the position of the mouse, as
   well as the mouse clicks, even if you don't enable this "trackball mode".

To get the position:

.. only:: python

   .. code-block:: python

      if base.mouseWatcherNode.hasMouse():
        x = base.mouseWatcherNode.getMouseX()
        y = base.mouseWatcherNode.getMouseY()

.. only:: cpp

   .. code-block:: cpp

      if (mouseWatcher->has_mouse()) {
        if (window->get_graphics_window()) {
          int x = window->get_graphics_window()->get_pointer(0).get_x();
          int y = window->get_graphics_window()->get_pointer(0).get_y();
        }
      }

The mouse clicks generate "events." To understand what events are, and how to
process them, you will need to read the
:ref:`Event Handling <tasks-and-event-handling>` section. The names of the
events generated are:

========== ============================
mouse1     Mouse Button 1 Pressed
mouse2     Mouse Button 2 Pressed
mouse3     Mouse Button 3 Pressed
mouse1-up  Mouse Button 1 Released
mouse2-up  Mouse Button 2 Released
mouse3-up  Mouse Button 3 Released
wheel_up   Mouse Wheel rolled upwards
wheel_down Mouse Wheel rolled downwards
========== ============================

If you want to hide the mouse cursor, you want the line: ``cursor-hidden true``
in your :ref:`Config.prc <configuring-panda3d>` or this section of code:

.. only:: python

   .. code-block:: python

      from pandac.PandaModules import WindowProperties
      props = WindowProperties()
      props.setCursorHidden(True)
      base.win.requestProperties(props)

Re-enabling mouse control
-------------------------

If you need to re-enable the mouse control of the camera, you have to adjust
mouseInterfaceNode to the current camera transformation:

.. only:: python

   .. code-block:: python

      mat = Mat4(camera.getMat())
      mat.invertInPlace()
      base.mouseInterfaceNode.setMat(mat)
      base.enableMouse()

Otherwise the camera would be placed back to the last position when the mouse
control was enabled.

Mouse modes
-----------

You may configure the mouse mode, which controls how the mouse cursor operates
in the window.

Absolute mouse mode
^^^^^^^^^^^^^^^^^^^

By default, the mouse is in "absolute" mode, meaning the cursor can freely
move outside the window. This mode is typical for desktop applications.

In a first person game where the mouse controls the camera ("mouselook"),
however, you usually want the mouse cursor to stay inside the window, so you can
get movement events no matter how far the user moves the mouse.

Two other mouse modes can help with this.

Relative mouse mode
^^^^^^^^^^^^^^^^^^^

In relative mode, the mouse cursor is kept at the center of the window, and
only relative movement events are reported.

Typically you want to hide the mouse cursor in this case, since otherwise it
distractingly "sticks" to the center of the window.

.. only:: cpp

   .. code-block:: cpp

      // To set relative mode and hide the cursor:
      WindowProperties props = window->get_graphics_window()->get_properties();
      props.set_cursor_hidden(true);
      props.set_mouse_mode(WindowProperties::M_relative);
      window->get_graphics_window()->request_properties(props);

      // To revert to normal mode:
      WindowProperties props = window->get_graphics_window()->get_properties();
      props.set_cursor_hidden(false);
      props.set_mouse_mode(WindowProperties::M_absolute);
      window->get_graphics_window()->request_properties(props);

.. only:: python

   .. code-block:: python

      # To set relative mode and hide the cursor:
      props = WindowProperties()
      props.setCursorHidden(True)
      props.setMouseMode(WindowProperties.M_relative)
      self.base.win.requestProperties(props)

      # To revert to normal mode:
      props = WindowProperties()
      props.setCursorHidden(False)
      props.setMouseMode(WindowProperties.M_absolute)
      self.base.win.requestProperties(props)

Confined mouse mode
^^^^^^^^^^^^^^^^^^^

In Panda3D version 1.9.1 there is a new mode called "confined." In this mode,
panda will try to use the desktop's native facilities to constrain the mouse
to the borders of the window.

This is effectively the same as "absolute" mode, but you can be assured the
mouse will remain within the window as long as the mode is in effect and the
window remains open.

The mouse will report events continuously, but it will stick to the edges of
the window. So, for a game, this is probably still not desirable.

To accommodate this, you can schedule a Task to fetch the current mouse
position, manually re-center the mouse afterward, and otherwise behave as if
the mouse events were generated by the relative mode.

For example:

.. only:: python

   .. code-block:: python

      mw = base.mouseWatcherNode

      if mw.hasMouse():
          # get the position, which at center is (0, 0)
          x, y = mw.getMouseX(), mw.getMouseY()

          # move mouse back to center
          props = base.win.getProperties()
          base.win.movePointer(0,
                               props.getXSize() // 2,
                               props.getYSize() // 2)
          # now, x and y can be considered relative movements

Of course, the mouse must initially be centered, or else the first event will
yield a large "movement" depending where the cursor happened to be at program
start.

Validating mouse mode
^^^^^^^^^^^^^^^^^^^^^

Note that not all desktops support relative or confined modes. Unfortunately,
you cannot tell in a portable way if a given mode is supported; also, since
the window properties request is asynchronous, you will not be able to
immediately detect if it took effect.

The way to test this is to check whether your request was honored, after
events have been processed, using the TaskManager method
:py:meth:`~direct.task.Task.TaskManager.doMethodLater()`.

.. only:: python

   For example:

   .. code-block:: python

      def setMouseMode(...):
          ...
          base.win.requestProperties(props)
          base.taskMgr.doMethodLater(0, resolveMouse, "Resolve mouse setting")
          ...

      def resolveMouse(task):
          props = base.win.getProperties()

          actualMode = props.getMouseMode()
          if actualMode != WindowProperties.M_relative:
              # did not get requested mode... perhaps try another.

Multiple Mice
-------------

If you have multiple mice connected to a single machine, it is possible to get
mouse movements and buttons for each individual mouse. This is called raw
mouse input. It is really only useful if you are building an arcade machine
that has lots of trackballs or spinners.

In order to use raw mouse input, you first need to enable it. To do so, add
the following line to your panda configuration file::

   read-raw-mice #t

This causes the panda main window to be created with the "raw_mice" window
property. That window property, in turn, causes the window to track and store
the positions and buttons of the raw mice. Then, that data is extracted from
the main window by objects of class :class:`.MouseWatcher`. The application program can
fetch the mouse data from the MouseWatchers. The global variable
``base.pointerWatcherNodes`` contains the ``MouseWatcher`` s.

The first MouseWatcher on the list always represents the system mouse pointer
- a virtual mouse that moves around whenever any of the physical mice do.
Usually, you do not want to use this virtual mouse. If you're accessing raw
mice, you usually want to access the real, physical mice. The list
``base.pointerWatcherNodes`` always contains the
virtual system mouse first, followed by all the physical mice.

So to print out the positions of the mice, use this:

.. only:: python

   .. code-block:: python

      for mouse in base.pointerWatcherNodes:
        print("NAME=", mouse.getName())
        print("X=", mouse.getMouseX())
        print("Y=", mouse.getMouseY())

Each mouse will have a name-string, which might be something along the lines
of "Micrologic High-Precision Gaming Mouse 2.0 #20245/405". The name is the
only way to tell the various mice apart. If you have two different mice of
different brands, you can easily tell them apart by the names. If you have two
mice of the same make and manufacture, then their names will be very similar,
but still unique. This is not because the mice contain serial numbers, but
rather because they are uniquefied based on the USB port into which they are
plugged. That means that if you move a mouse from one USB port to another, it
will have a new name. For all practical purposes, that means that you will
need to store a config file that maps mouse name to intended purpose.

Raw mouse buttons generate events. The event names are similar to the ones for
the system mouse, except that they have a "mousedevX" prefix. Ie, an example
event might be ``mousedev3-mouse1-up``. In this
example, the "mousedev3" specifier means that the mouse sending the event is
``base.pointerWatcherNode[3]``.

Multiple Mice under Linux
^^^^^^^^^^^^^^^^^^^^^^^^^

To use raw mouse input under Linux, the panda program needs to open the device
files /dev/input/event\*. On many Linux distributions, the permission bits are
set such that this is not possible.

It is not a good idea to just change the permission bits. Doing so introduces a
huge security hole in which any logged in user can monitor the mice, the
joysticks, and the keyboard --- including any passwords that may be typed.
The correct solution is to change the ownership of the input devices whenever a
user sits down at the console. There is a module, pam_console, that does this,
but it is now obsoleted, and has been removed from several distros.
The `Fedora pam_console removal <https://fedoraproject.org/wiki/Releases/FeatureRemovePAMConsole>`__
page states that ACLs set by the HAL should replace pam_console's functionality.
Currently, since it does not seem that HAL provides this yet, the best course of
action is to make an 'input' group as described on
`this page <https://puredata.info/docs/faq/how-can-i-set-permissions-so-hid-can-read-devices-in-gnu-linux>`__.

If you are building a stand-alone arcade machine that does not allow remote
login and probably doesn't even have a net connection, then changing the
permission bits isn't going to hurt you.
