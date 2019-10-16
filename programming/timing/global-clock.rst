.. _the-global-clock:

The Global Clock
================

The global clock is an instance of the
`ClockObject <https://www.panda3d.org/reference/python/class!panda3d.core.ClockObject>`__
class.

.. only:: python

   It gets imported into the global namespace when you load the
   DirectStart/Showbase modules.

.. only:: cpp

   There's a single instance of it already initialized that you can access
   statically.

To get the time (in seconds) since the last frame was drawn:

.. only:: python

   .. code-block:: python

      dt = globalClock.getDt()

.. only:: cpp

   .. code-block:: cpp

      double dt = ClockObject::get_global_clock()->get_dt();

Another useful function is the frame time (in seconds, since the program
started):

.. only:: python

   .. code-block:: python

      frameTime = globalClock.getFrameTime()

.. only:: cpp

   .. code-block:: cpp

      double frame_time = ClockObject::get_global_clock()->get_frame_time();


.. note:: This section is incomplete. It will be updated soon.
