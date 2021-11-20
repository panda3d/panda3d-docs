.. _filename-syntax:

Panda Filename Syntax
=====================

The path used in all calls to the Panda3D API must abide by Panda3D's filename
conventions. For easier portability, Panda3D uses Unix-style pathnames, even on
Microsoft Windows. This means that the directory separator character is always a
forward slash, not the Windows backslash character, and there is no leading
drive letter prefix. (Instead of a leading drive letter, Panda uses an initial
one-letter directory name to represent the drive.)

There is a fairly straightforward conversion from Windows filenames to panda
filenames. Always be sure to use Panda filename syntax when using a Panda3D
library function, or one of the panda utility programs:

.. only:: python

   .. code-block:: python

      # WRONG:
      loader.loadModel("c:\\Program Files\\My Game\\Models\\Model1.egg")

      # RIGHT:
      loader.loadModel("/c/Program Files/My Game/Models/Model1.egg")

.. only:: cpp

   .. code-block:: cpp

      # WRONG:
      window->load_model(framework.get_models(), "c:\\Program Files\\My Game\\Models\\Model1.egg");

      # RIGHT:
      window->load_model(framework.get_models(), "/c/Program Files/My Game/Models/Model1.egg");

Panda uses the :class:`.Filename` class to store Panda-style filenames; many
Panda functions expect a Filename object as a parameter. The Filename class also
contains several useful methods for path manipulation and file access, as well
as for converting between Windows-style filenames and Panda-style filenames; see
the :class:`.Filename` page in the API Reference for a more complete list.

Normally, you can just use forward slashes in your paths and don't need to worry
about anything else, since absolute paths should not be used in the program.
However, when converting paths from the Python standard library or other
libraries, special care is required to ensure that the application will continue
to work on Windows correctly.

To convert a Windows filename to a Panda pathname, use code similar to the
following:

.. only:: python

   .. code-block:: python

      from panda3d.core import Filename
      winfile = "c:\\MyGame\\Model1.egg"
      pandafile = Filename.fromOsSpecific(winfile)
      print(pandafile)

.. only:: cpp

   .. code-block:: cpp

      #include "filename.h"

      const std::string winfile = "c:\\MyGame\\Model1.egg";
      Filename pandafile = Filename::from_os_specific(winfile);
      std::cout << pandafile.get_fullpath() << "\n";

To convert a Panda filename into a Windows filename, use code like this:

.. only:: python

   .. code-block:: python

      from panda3d.core import Filename
      pandafile = Filename("/c/MyGame/Model1.egg")
      winfile = pandafile.toOsSpecific()
      print(winfile)

.. only:: cpp

   .. code-block:: cpp

      #include "filename.h"

      Filename pandafile("/c/MyGame/Model1.egg");
      const std::string winfile = pandafile.to_os_specific();
      std::cout << winfile << "\n";

.. only:: python

   Starting with Python 3.6, the :class:`.Filename` class is fully interoperable
   with the filesystem manipulation functions in the Python standard library.
   Conversely, :py:mod:`pathlib` paths will seamlessly work in all Panda3D calls
   that accept a :class:`.Filename` object.

Let's say, for instance, that you want to load a model, and the model is in the
"model" directory that is in the same directory as the program's main file.

Here is how you would load the model:

.. only:: python

   .. code-block:: python

      import sys, os
      import direct.directbase.DirectStart
      from panda3d.core import Filename

      # Get the location of the 'py' file I'm running:
      mydir = os.path.dirname(os.path.abspath(__file__))

      # Convert that to panda's unix-style notation.
      mydir = Filename.fromOsSpecific(mydir)

      # Now load the model:
      model = loader.loadModel(mydir / "models/mymodel.egg")

.. only:: cpp

   .. code-block:: cpp

      #include "filename.h"
      #include "executionEnvironment.h"

      // Get the location of the executable file I'm running:
      Filename mydir = ExecutionEnvironment::get_binary_name();
      mydir = mydir.get_dirname();

      // Now load the model:
      window->load_model(framework.get_models(), mydir + "/models/mymodel.egg");

You need to keep in mind that standard library functions provided by the system
or the programming language runtime work with OS-specific paths. So do not
forget to convert your Panda paths to OS-specific paths when using these built-
in functions. In cases where Panda's API offers equivalent functions through the
:class:`.Filename` or :class:`.VirtualFileSystem` class, however, it is
recommended to use those instead, as they will natively understand Panda
Filenames.
