.. _running-your-program:

Running your Program
====================

.. only:: python

   Using Command Prompt to Run your Program
   ----------------------------------------

   You can run your script by using your computer’s ‘Command Prompt’. You can
   access this by clicking ‘Start > All Programs > Accessories > Command
   Prompt’, or by going to 'Start > Run' and typing 'cmd'. When it opens, it
   should look something like this:

   .. image:: running-your-program-1.PNG

   At the moment it’s pointing to its default directory, which in my case is
   ‘Documents and Settings’ (it doesn’t matter if yours is different). We need
   to change the directory to the one where we saved our script. To do this, we
   use the ``cd`` command. This stands for ‘change directory’. Type the
   following text behind the > symbol:

   .. code-block:: bat

      cd C:\Panda3D-1.10.7-x64\mystuff\

   Instead of version 1.10.7-x64, you should type the version number of Panda3D
   that you have downloaded and installed. Please note that this folder name is
   case-sensitive and must match exactly (other than the version number, of
   course). Then, press the ‘Enter’ key on your keyboard. You should now have
   the following on the Command Prompt:

   .. image:: running-your-program-2.PNG

   This means that it’s now pointing to the right directory. To run your script
   and start Panda3D, type the following text behind the > symbol:

   .. code-block:: bash

      ppython myscript.py

   .. image:: running-your-program-3.PNG

   Press the ‘Enter’ key on your keyboard. This will run the version of Python
   that is distributed with Panda3D. If all is well, Panda3D will start and you
   should see the main rendering window appear.

   .. image:: running-your-program-4.PNG

   This is a empty program, it won't do anything. The next step is to add
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
   also work for 2017.

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

   ::

      C:\Panda3D-1.10.7-x64\include

   .. rubric:: Library Directories

   ::

      C:\Panda3D-1.10.7-x64\lib

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
   warnings; these are harmless, and you can may suppress them in your project
   settings.

   There is one more step that needs to be done in order to run the project,
   though. We need to tell Windows where to find the Panda3D DLLs when we run
   the project from Visual Studio. Go back to the project configuration, and
   under "Debugging", open the "Environment" option. Add the following setting,
   once again adjusting for your specific Panda3D installation directory:

   ::

      PATH=C:\Panda3D-1.10.7-x64\bin;%PATH%

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
   on Ubuntu or the XCode Command-Line Tools on Mac OS X.

   The following pages describe how this is accomplished:

   -  :ref:`Linux version <how-to-compile-a-c++-panda3d-program-on-linux>`
   -  :ref:`macOS version <how-to-compile-a-c++-panda3d-program-on-macos>`
