.. _the-global-clock:

The Global Clock
================

The global clock is an instance of the :class:`~panda3d.core.ClockObject` class.

.. only:: python

   It gets imported into the global namespace when you import the
   :py:mod:`direct.directbase.DirectStart` module or create an instance of the
   :py:class:`~direct.showbase.ShowBase.ShowBase` class.

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
