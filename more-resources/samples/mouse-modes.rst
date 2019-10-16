.. _mouse-modes:

Sample Programs: Mouse Modes
============================

To run a sample program, you need to install Panda3D.
If you're a Windows user, you'll find the sample programs in your start menu.
If you're a Linux user, you'll find the sample programs in /usr/share/panda3d.

.. rubric:: Explanation

This sample program shows usage of different mouse modes, which control how the
mouse cursor interacts with a Panda3D window.

For the purposes of first-person games with "mouselook," it's important to use a
mode other than the default ("absolute"), because in that mode, the mouse cursor
may easily leave the window, and your game will stop receiving mouse events.

To maintain a consistent stream of pointer events no matter how much the user
moves the mouse, the "relative" mode and "confined" mode (new in 1.9.1) will
keep the pointer inside the window.

These latter two modes may not be available on all platforms, though, so the
sample demonstrates how to account for switching modes and provide a consistent
sense of control no matter which mode is in use.

.. rubric:: Usage

In the sample, a pretty cube lies near the center of the window, which you may
rotate by moving the mouse.

You may select between three possible mouse modes with the '0', '1', or '2' keys
to see how the block moves depending on the mouse movement. Note the center
status line will tell which mode actually got applied.

The 'c' key toggles automatic re-centering of the mouse cursor, which is a
strategy to avoid allowing the cursor to leave the window. This is on by
default, so any one of the three modes will generally provide a smooth mouse
experience, but with rapid enough movements, the mouse can leave the window in
"absolute" mode.

Finally, the 's' key toggles the visibility of the mouse cursor.

The :ref:`mouse-support` section of the manual covers the mouse modes,
detecting whether a mouse mode is supported, and a strategy for re-centering
the mouse, as used by this sample.

.. rubric:: Back to the List of Sample Programs:

:ref:`samples`
