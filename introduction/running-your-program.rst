.. _running-your-program:

Running your Program
====================

.. only:: python

   Using Command Prompt to Run your Program
   ----------------------------------------

   You can run your script by using your computer's "Terminal" or
   "Command Prompt". When you open it, it should look something like this:

   .. image:: running-your-program-1.png

   At the moment it’s pointing to its default directory, which is typically the
   user directory in ``C:\Users\username``, ``/home/user`` or ``/Users/user``,
   depending on your operating system. We need to change the directory to the
   one where we saved our script. To do this, we use the ``cd`` command. This
   stands for ‘change directory’. For example, if the script is saved in a
   MyProject folder inside the home directory, we should type this:

   .. code-block:: bat

      cd MyProject

   Please note that this folder name is case-sensitive and must match exactly.
   Then, press the ‘Enter’ key on your keyboard. You should now have the
   following on the Command Prompt:

   .. image:: running-your-program-2.png

   This means that it’s now pointing to the right directory. Assuming the script
   has been named ``main.py``, type the following text after the > symbol:

   .. code-block:: bash

      python main.py

   .. image:: running-your-program-3.png

   Press the ‘Enter’ key on your keyboard. If all is well, Panda3D will start
   and you should see the main rendering window appear.

   .. image:: running-your-program-4.png

   This is an empty program, it won't do anything. The next step is to add
   additional commands to the program, as described in one of the following
   tutorials.

.. only:: cpp

   This section will explain how to compile a C++ program that uses the Panda3D
   libraries. On Windows, this is done using the Microsoft Visual C++ compiler;
   on all other systems, this can be done with either the Clang or the GCC
   compiler. Choose the section that is appropriate for your operating system.

   Compiling your Program with Visual Studio
   -----------------------------------------

   The descriptions below assume Microsoft Visual Studio 2015, but they should
   also work for 2017, 2019 and 2022.

   Setting up the project
   ~~~~~~~~~~~~~~~~~~~~~~

   When creating a new project in Visual Studio, be sure to select the template
   for a "Win32 Console application" under the Visual C++ templates category. We
   recommend disabling "Precompiled headers" for now. (Don't worry, you can
   still change these things later.)

   When you created your project, the first thing you'll need to do is change
   "Debug" to "Release" below the menu bar, as shown in the image below. This is
   because the SDK builds of Panda3D are compiled in Release mode as well. The
   program will crash mysteriously if the setting doesn't match up with the
   setting that was used to compile Panda3D. This goes for the adjacent platform
   selector as well; select "x64" if you use the 64-bit Panda3D SDK, and "x86"
   if you use the 32-bit version.

   .. image:: msvc-2015-release-x64.png

   Now, open up the project configuration pages. Change the "Platform Toolset"
   in the "General" tab to "v140_xp" (if you wish your project to be able to
   work on Windows XP) or "v140".

   Furthermore, we need to go to C/C++ -> "Preprocessor Definitions" and remove
   the ``NDEBUG`` symbol from the preprocessor definitions. This was
   automatically added when we switched to "Release" mode, but having this
   setting checked removes important debugging checks that we still want to keep
   until we are ready to publish the application.

   Now we are ready to add the paths to the Panda3D directories. Add the
   following paths to the appropriate locations (replace the path to Panda3D
   with the directory you installed Panda3D into, of course):

   .. rubric:: Include Directories

   .. parsed-literal::

      C:\\Panda3D-\ |release|\ -x64\\include

   .. rubric:: Library Directories

   .. parsed-literal::

      C:\\Panda3D-\ |release|\ -x64\\lib

   Then, you need to add the appropriate Panda3D libraries to the list of
   "Additional Dependencies" your project should be linked with. The exact set
   to use varies again depending on which features of Panda3D are used. This
   list is a reasonable default set:

   ::

      libp3framework.lib
      libpanda.lib
      libpandaexpress.lib
      libp3dtool.lib
      libp3dtoolconfig.lib
      libp3direct.lib

   .. image:: msvc-2015-additional-deps.png

   This should be enough to at least build the project. Press F7 to build your
   project and start the compilation process. You may see several C4267
   warnings; these are harmless, and you may suppress them in your project
   settings.

   There is one more step that needs to be done in order to run the project,
   though. We need to tell Windows where to find the Panda3D DLLs when we run
   the project from Visual Studio. Go back to the project configuration, and
   under "Debugging", open the "Environment" option. Add the following setting,
   once again adjusting for your specific Panda3D installation directory:

   .. parsed-literal::

      PATH=C:\\Panda3D-\ |release|\ -x64\\bin;%PATH%

   Now, assuming that the project built successfully, you can press F5 to run
   the program. Of course, not much will happen yet, because we don't have any
   particularly interesting code added. The following tutorial will describe the
   code that should be added to open a Panda3D window and start rendering
   objects.

   Compiling your Program with GCC or Clang
   ----------------------------------------

   On platforms other than Windows, we use the GNU compiler or a compatible
   alternative like Clang. Most Linux distributions ship with GCC out of the
   box; some provide an easily installable package such as ``build-essential``
   on Ubuntu or the XCode Command-Line Tools on macOS. To obtain the latter, you
   may need to register for an account on the
   `Apple developer site <https://developer.apple.com/>`__.

   Having these two components, we can proceed to compile. The first step is to
   create an .o file from our .cxx file. We need to specify the location of the
   Panda3D include files. Please change the paths in these commands to the
   appropiate locations. If using clang, use ``clang++`` instead of ``g++``.

   .. code-block:: bash

      g++ -c filename.cxx -o filename.o -std=gnu++11 -O2 -I{panda3dinclude}

   You will need to replace ``{panda3dinclude}`` with the location of the
   Panda3D header files. On Linux, this is likely ``/usr/include/panda3d/``.
   On macOS, this will be in ``/Library/Developer/Panda3D/include/`` in Panda3D
   1.10.5 and higher or ``/Developer/Panda3D/include/`` in older versions.

   To generate an executable, you can use the following command:

   .. code-block:: bash

      g++ filename.o -o filename -L{panda3dlibs} -lp3framework -lpanda -lpandafx -lpandaexpress -lp3dtoolconfig -lp3dtool -lp3direct

   As above, change `{panda3dlibs}` to point to the Panda3D libraries. On Linux
   this will be ``/usr/lib/panda3d`` or ``/usr/lib/x86_64-linux-gnu/panda3d``,
   whereas on macOS it will be ``/Library/Developer/Panda3D/lib`` or
   ``/Developer/Panda3D/lib``, depending on your exact version of Panda3D.

   Here is an equivalent SConstruct file, organized for clarity:

   .. code-block:: python

      pandaInc = '/usr/include/panda3d'
      pandaLib = '/usr/lib/panda3d'

      Program('filename.cpp',
          CCFLAGS=['-fPIC', '-O2', '-std=gnu++11'],
          CPPPATH=[pandaInc],
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

   .. note::

      On macOS, Panda3D versions 1.10.4.1 and below were compiled with
      libstdc++, and so require passing ``-stdlib=libstdc++`` to the compiler.
      Panda3D 1.10.5 offers a choice: the download marked "MacOSX10.6" is
      compiled with libstdc++, whereas the download marked "MacOSX10.9" is
      compiled with libc++.
      It is recommended to use the download marked "MacOSX10.9".
