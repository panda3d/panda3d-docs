.. _how-to-compile-a-c++-panda3d-program-on-linux:

How to compile a C++ Panda3D program on Linux
=============================================

.. only:: python

   This page is related to C++ usage of Panda3D and not to Python usage. If you
   are a Python user, please skip this page. For C++ users, please toggle to the
   C++ version of this page.

.. only:: cpp

   This short guide explains how to build a Panda3D game written in C++ game
   under Linux.

   First of all, you should install a suitable compiler.  We recommend either
   the LLVM Clang compiler or the GNU G++ compiler.  These are usually provided
   by the Linux distribution (on Ubuntu, they can be installed via the
   build-essential package).

   Now, we need to create a .o file from our cxx file. We need to specify the
   location of the Panda3D include files. Please change the paths in these
   commands to the appropiate locations.

   .. code-block:: bash

      g++ -c filename.cxx -o filename.o -std=gnu++11 -O2 -I{panda3dinclude}

   To generate an executable, you can use the following command:

   .. code-block:: bash

      g++ filename.o -o filename -L{panda3dlibs} -lp3framework -lpanda -lpandafx -lpandaexpress -lp3dtoolconfig -lp3dtool -lp3direct

   Note: In these two commands, you need to change a few paths:

   -  {panda3dinclude}: Change this to the path to your Panda3D include
      directory. This would probably look like /usr/include/panda3d/.
   -  {panda3dlibs}: Change this to the path to your Panda3D libraries. Usually
      this is just /usr/lib/panda3d or sometimes /usr/lib.

   Here is an equivalent SConstruct file, organized for clarity:

   .. code-block:: python

      pyInc = '/usr/include/python3.7m'
      pandaInc = '/usr/include/panda3d'
      pandaLib = '/usr/lib/panda3d'

      Program('filename.cpp',
          CCFLAGS=['-fPIC', '-O2', '-std=gnu++11'],
          CPPPATH=[pyInc, pandaInc],
          LIBPATH=pandaLib,
          LIBS=[
              'libp3framework',
              'libpanda',
              'libpandafx',
              'libpandaexpress',
              'libp3dtoolconfig',
              'libp3dtool',
              'libp3direct'])

   To run your newly created executable, type:

   .. code-block:: bash

      ./filename

   If it runs, congratulations! You have successfully compiled your own Panda3D
   program!
