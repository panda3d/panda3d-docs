.. _using-packp3d:

Using packp3d
=============

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

The easiest way to create a p3d file is to use the packp3d tool. This program
is distributed with the development distribution of Panda3D. (It happens to be
a p3d file itself, but that's just a detail.) You should use the packp3d
program that comes with the version of Panda3D you were using to develop your
application, because packp3d is tied to its own particular version of Panda3D,
and will build a p3d file that runs with that particular version.

You have to run packp3d from the command line. From the command shell, run the
command:

.. code-block:: bash

   packp3d -o myapp.p3d -d c:/myapp

where "myapp.p3d" is the p3d file you want to produce, and "c:/myapp" is the
folder containing your application, including all of its code and models.

Note that you need to have the panda3d executable on your PATH in order for
the above to work. The panda3d executable should have been installed when you
installed the Panda3D runtime (this is a separate download from the Panda3D
SDK). You might need to extend your PATH variable to locate it automatically
on the command line, by adding the plugin installation folder to your PATH. On
Windows, this is the folder c:\Program Files\Panda3D by default.

The above command will scan the contents of c:/myapp and add all relevant
files found in that directory and below into the p3d file myapp.p3d, creating
a packaged application. There are some conventions you need to understand.

-  packp3d assumes that the starting point of your application is in the
   Python file "main.py", which is found within the toplevel of the
   application folder. If you have a different Python file that starts the
   application, you can name this file with the -m parameter to packp3d, e.g.
   "-m mystart.py".

-  If your application is written entirely in C++, it must still have a Python
   entry point to be used by the Panda3D plugin system, so you will need to
   provide a trivial bit of Python code to load and start your C++
   application.

-  Any prc files within the toplevel of the application folder will be loaded
   automatically at runtime, as if $PANDA_PRC_DIR were set to your application
   folder name; you don't need to load them explicitly in your Python code.

-  Any egg files found within the application folder will be automatically
   converted to bam files for storing in the p3d file. Bam files are usually a
   much better choice for distributing an application, because they're smaller
   and they load much faster. However, this does mean that you can't specify
   the ".egg" extension to your model files when you load your models in code,
   because they won't have that extension within the p3d file; you must omit
   the filename extension altogether. If you want to keep some of your egg
   files as they are, without converting them to bam files, you must use the
   more advanced ppackage utility to create your p3d file.

-  Any model files that your application loads from some source outside of the
   application folder won't be found. You must ensure that these are copied
   into the application folder and loaded from there. (However, texture files
   that are referenced by egg or bam files within the application folder will
   automatically be copied into the p3d file, no matter where they were found
   on disk.)

-  There are additional options to packp3d for more advanced usage. As with
   any Panda3D command-line application, you may specify "-h" on the command
   line to list the full set of available options.
