.. _motherboard-integrated-video:

Motherboard Integrated Video
============================

Motherboard video is very misleading. The chips have names like "Radeon" and
"GeForce" that we have come to associate with speed, but these chips are an
order of magnitude slower than real video cards. Programming for these chips
requires special consideration.

Many computers nowadays have two video chips: the integrated motherboard video
chip and a dedicated video card. The operating system is responsible for
automatically switching the application to the appropriate card. If it is
selecting the integrated chip, the application may run excessively slow. It is
important to detect if this is the case and instruct the user to configure their
operating system to select the appropriate video card.

The following code can be used to determine which GPU is in use:

.. only:: python

   .. code-block:: python

      print(base.win.gsg.driver_vendor)
      print(base.win.gsg.driver_renderer)

.. only:: cpp

   .. code-block:: cpp

      std::cerr << win->get_gsg()->get_driver_vendor() << "\n"
                << win->get_gsg()->get_driver_renderer() << "\n";
