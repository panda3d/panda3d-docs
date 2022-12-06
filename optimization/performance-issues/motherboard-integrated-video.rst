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

Forcing Use of Discrete GPU on Windows
--------------------------------------

On Windows, it is possible to force the NVIDIA and AMD graphics drivers to
automatically select the high-peformance dedicated graphics card, by compiling
special symbols into the main executable.

.. only:: python

   While developing, the main executable is ``python.exe``, which does not set
   these symbols. But when :ref:`building an application <distribution>`,
   build_apps can automatically add these special symbols. Simply add this
   option to the build_apps options block in setup.py:

   .. code-block:: python

      'prefer_discrete_gpu': True,

   This option is available as of Panda3D 1.10.13.

.. only:: cpp

   Simply copy-paste the following symbols into the source file containing your
   main entry point:

   .. code-block:: cpp

      #ifdef _WIN32
      extern "C" {
        __declspec(dllexport) DWORD AmdPowerXpressRequestHighPerformance = 0x00000001;
        __declspec(dllexport) DWORD NvOptimusEnablement = 0x00000001;
      }
      #endif

Forcing Use of Discrete GPU on Linux
------------------------------------

On Linux, some drivers can be told to use the discrete GPU by setting
``DRI_PRIME=1`` in the environment. However, this is not considered reliable at
this time, so it is not done by Panda3D automatically. It is suggested to
document this as a possibility for your end-users or add an option for this
setting that can be disabled.

When distributing a .desktop file, it is also possible to add the following key
to the file::

   PrefersNonDefaultGPU=true
