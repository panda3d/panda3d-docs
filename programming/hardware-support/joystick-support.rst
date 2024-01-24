.. _joystick-support:

Joystick Support
================

As of version 1.10, Panda3D gained built-in support for various input devices
including but not limited to joysticks, gamepads and steering wheels.

We'll be starting with a little bit of theory to get you some knowledge of the
underlying system to be able to understand how gamepad support works. The
support for devices is given through evdev, the joystick api or xinput
dependent on the OS you are using. Hence all devices that are recognized by
your system will be available by the engine. Each connected device will be
classified by one of the following device classes:

.. code-block:: python

   # It is not known what type of device this is.
   unknown

   # This means that the device doesn't correspond to a physical
   # device, but rather to a dynamic source of input events.
   virtual_device

   # A physical, alphabetical keyboard.
   keyboard
   mouse
   touch

   # A gamepad with action buttons, a D-pad, and thumbsticks.
   gamepad

   flight_stick
   steering_wheel
   dance_pad

   # Head-mounted display.
   hmd

   # 3D mouse, such as produced by 3Dconnexion.
   spatial_mouse

These DC's are stored within the ``InputDevice.DeviceClass`` enum which can be
imported from :mod:`panda3d.core`.

.. note::

   Linux users may need to be in the "input" user group to get access to the
   full range of available device functionality.

Buttons
-------

Just like the already existing keyboard support, you can catch button events
of each device connected to your system. Unlike keyboard button events, each
device will send its button events with a specific prefix. These prefixes need
to be set by the developer when a device is attached for usage, which can be
done with a call to ``self.attachInputDevice(device, prefix="[your-prefix]")``.
The device that needs to be passed to this function can be obtained using
:meth:`self.devices.get_devices() <.InputDeviceManager.get_devices>`, which will
give you all devices of a given device class.
After the device has been attached, you can catch events like for example,
``"[prefix]-face_a"`` which will be thrown
whenever the 'A' button on the device with the specified prefix is hit. As
with keyboard support, there also is the '-up' postfix which can be added to
catch the event which will be thrown when a previously pressed button is
released again. Note, if a button with an to the engine unknown code was
pressed, an event like the following will be thrown.
``"[prefix]-none"``

In addition to events, you can also check for specific buttons to be pressed
with the :meth:`~.InputDevice.find_button()` method of a device object.

Here we'll check for the right thumbstick to be pressed

.. code-block:: python

   gamepad = base.devices.getDevices(InputDevice.DeviceClass.gamepad)[0]
   right_stick = gamepad.findButton("rstick")
   if right_stick.pressed:
       # Do whatever you want when this button is pressed

If you want to check which events are thrown on specific device input, you can
set the following config variable for debugging.
``notify-level-device debug``

Alternatively you can also add this line somewhere in your application

.. code-block:: python

   messenger.toggleVerbose()

Axes
----

The above mechanism works well for digital buttons, which can only be in an on
or off state. Many game controllers also have analog controls, often referred
to as "axes", which can have a variable value. In Panda3D, these values will
be 0.0 when the respective control is in its default or resting position, and
1.0 when it is in its maximum position. Some controls can move in two
directions, and can have a value of down to -1.0.

This sample will show how to get the left analog stick of the first gamepad
device

.. code-block:: python

   gamepad = base.devices.getDevices(InputDevice.DeviceClass.gamepad)[0]
   left_x = gamepad.findAxis(InputDevice.Axis.left_x)

   # Access and use the value for whatever you need it
   left_x.value

With the :meth:`~.InputDevice.find_axis()` method we tell the device which axis
we are interested in and finally get the axis value using the ``value`` member.
The ``state`` member will give you a double precision representation of the
control's current position and should be called within a task method to get a
constant update of the controls position changes if desired. It sometimes is
also prudent to store the centered position of each control early in an
application to simplify the calculation of the distance the control has been
moved in any direction. Some applications and devices also do this automatically
in a given idle time or provide the user a dedicated re-calibrate action.

.. note::

   :meth:`~.InputDevice.find_axis()` will return a dummy object if the axis
   doesn't exist. You can check for the boolean value of the returned object
   (ie. ``if left_x:``) to see if the returned axis has a known value.
