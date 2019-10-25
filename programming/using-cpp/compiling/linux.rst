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

   First of all, download the following files:

   #. `Python <https://www.python.org/>`__, the development package (not needed
      as of Panda3D 1.10.0)
   #. The GNU G++ compiler. On most Linux versions, this is already
      pre-installed.

   Now, first of all, we need to create a .o file from our cxx file. We need to
   link to the Panda3D include files and to the Python include files. Please
   change the paths in these commands to the appropiate locations.

   .. code-block:: bash

      g++ -c filename.cxx -o filename.o -std=gnu++11 -O2 -I{pythoninclude} -I{panda3dinclude}

   To generate an executable, you can use the following command:

   .. code-block:: bash

      g++ filename.o -o filename -L{panda3dlibs} -lp3framework -lpanda -lpandafx -lpandaexpress -lp3dtoolconfig -lp3dtool -lp3pystub -lp3direct

   Note: In these two commands, you need to change a few paths:

   -  {pythoninclude}: The path to your Python include folder. For version 2.7,
      this is /usr/include/python2.7 by default.
   -  {panda3dinclude}: Change this to the path to your Panda3D include
      directory. This would probably look like /usr/include/panda3d/.
   -  {panda3dlibs}: Change this to the path to your Panda3D libraries. Usually
      this is just /usr/lib/panda3d or sometimes /usr/lib.

   Here is an equivalent SConstruct file, organized for clarity:

   .. code-block:: python

      pyInc = '/usr/include/python2.7'
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
              'libp3pystub',
              'libp3direct'])

   To run your newly created executable, type:

   .. code-block:: bash

      ./filename

   If it runs, congratulations! You have successfully compiled your own Panda3D
   program!
