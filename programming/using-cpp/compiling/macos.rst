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
   Panda3D include files and to the Python include files. Note: only i386 arch
   is supported for Panda3D versions before 1.9.0, so for those versions you
   need to include the ``arch i386`` flag.

   .. code-block:: bash

      clang++ -c filename.cxx -o filename.o -std=gnu++11 -g -O2 -I{pythoninclude} -I{panda3dinclude}

   Please change the paths in these commands to the appropriate locations. A
   list of locations is at the end of the page.

   Secondly, we need to generate an executable, you can use the following
   command:

   .. code-block:: bash

      clang++ filename.o -o filename -L{panda3dlibs} -lp3framework -lpanda -lpandaexpress -lp3dtoolconfig -lp3dtool -lp3pystub -lp3direct

   As mentioned above, we need to change the paths accordingly, the paths for
   macOS are listed below:

   {pythoninclude}
      The path to your Python include folder. For version 2.7, this is
      ``/usr/include/python2.7`` by default.

   {panda3dinclude}
      Change this to the path to your Panda3D include directory. This would
      probably look like ``/Developer/Panda3D/include/``

   {panda3dlibs}
      Change this to the path to your Panda3D libraries. This is
      ``/Developer/Panda3D/lib``.

   And lastly, to run the created executable, type:

   .. code-block:: bash

      ./filename

   * If you get warnings like "missing required architecture x86_64 in file" or
     "Undefined symbols: "_main", referenced from:" you need to use the
     ``-arch i386`` flag.

   * If you get errors like "Undefined symbols: "TypedObject::_type_handle",
     referenced from: " you are not including some panda3d libraries needed or
     missing the ``-arch i386`` flag.

   * If you get an error running your executable like "dyld: Library not loaded:
     @executable_path/../Library/Frameworks/Cg.framework/Cg" means you need to
     install Cg library from https://developer.nvidia.com/cg-toolkit-download
