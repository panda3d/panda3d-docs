.. _how-to-compile-a-c++-panda3d-program-on-macos:

How to compile a C++ Panda3D program on macOS
=============================================

.. only:: python

   This page is related to C++ usage of Panda3D and not to Python usage. If you
   are a Python user, please skip this page. For C++ users, please toggle to the
   C++ version of this page.

.. only:: cpp

   This short guide explains how to build a Panda3D game written in C++ game
   under Mac OS.

   In order to compile you need also to have the Clang compiler. The compiler is
   not pre-installed in macOS; you will need to install Xcode command-line tools
   which comes with the macOS installer CDs or DVDs. You can alternatively
   download it from the `Apple developer site <https://developer.apple.com/>`__.
   You will need to register for an account.

   Having these two components, we can proceed to compile:

   First we must create .o file from our cxx file. We need to link to the
   Panda3D include files.

   .. code-block:: bash

      clang++ -c filename.cxx -o filename.o -std=gnu++11 -g -O2 -I{panda3dinclude}

   Please change the paths in these commands to the appropriate locations. A
   list of locations is at the end of the page.

   Secondly, we need to generate an executable, you can use the following
   command:

   .. code-block:: bash

      clang++ filename.o -o filename -L{panda3dlibs} -lp3framework -lpanda -lpandaexpress -lp3dtoolconfig -lp3dtool -lp3direct

   As mentioned above, we need to change the paths accordingly, the paths for
   macOS are listed below:

   {panda3dinclude}
      Change this to the path to your Panda3D include directory. This would
      probably look like ``/Library/Developer/Panda3D/include/`` (in Panda3D
      1.10.5 and higher) or ``/Developer/Panda3D/include/`` in older versions.

   {panda3dlibs}
      Change this to the path to your Panda3D libraries. This is
      ``/Library/Developer/Panda3D/lib`` or ``/Developer/Panda3D/lib``,
      depending on your version of Panda3D.

   And lastly, to run the created executable, type:

   .. code-block:: bash

      ./filename

   .. note::

      Panda3D versions 1.10.4.1 and below were compiled with libstdc++, and so
      require passing ``-stdlib=libstdc++`` to the compiler.  Panda3D 1.10.5
      offers a choice: the download marked "MacOSX10.6" is compiled with
      libstdc++, whereas the download marked "MacOSX10.9" is compiled with
      libc++.  It is recommended to use the download marked "MacOSX10.9".
