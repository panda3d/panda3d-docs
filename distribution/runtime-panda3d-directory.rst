.. _the-runtime-panda3d-directory:

The runtime Panda3D directory
=============================

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

When the Panda3D runtime (including the web plugin) runs a p3d file, it must
download key files into a particular directory on your hard disk. This
directory's location depends on the operating system (and, to a certain
extent, the browser) in use.

On Windows, the Panda3D directory is %LocalAppData%\\Panda3D. This usually
translates to:

-  C:\\Documents and Settings\\<your name>\\Local Settings\\Application
   Data\\Panda3D on Windows XP, or
-  C:\\Users\\<your name>\\AppData\\Local\\Panda3D on newer versions.

However, when you are running via IE on Windows Vista or Windows 7, the
operating system remaps %LocalAppData% to a new location, which is:

-  C:\\Users\\<your name>\\AppData\\LocalLow\\Panda3D

On Mac OSX, the Panda3D directory is ~/Library/Caches/Panda3D, which is:

-  /Users/<your name>/Library/Caches/Panda3D

On Linux, the Panda3D directory is ~/.panda3d .

The contents of the Panda3D directory will gradually fill up over time as new
packages are downloaded and installed. Later versions of the Panda3D runtime
will automatically manage this space and remove old packages as needed, but at
the moment, the current release of the runtime does not do this; thus, you may
need to occasionally clean up this directory by hand.

There are several subdirectories within the Panda3D directory. They are:

certs
   This contains any certificates you have approved in the past. If you remove
   this directory and all its contents, you will have to re-approve any
   certificates before running any p3d files.
coreapi
   This is a temporary cache that stores the "core API" used to manage the
   runtime code itself. If you remove this directory, it will automatically be
   re-downloaded the next time you run.
hosts
   This contains the packages downloaded and installed from various
   webservers. Each server will have its own subdirectory within this
   directory. This is likely to be the largest directory in this structure.
   You can remove any or all of these host subdirectories at will; if needed
   again, the required data will be re-downloaded automatically.
log
   This contains the various log files created by past executions of the
   runtime. In particular, "p3dsession.log" is the output from the Python
   session of the most recent p3d file you have run (unless the p3d file
   specifies a different, custom logfile name). You may find this file useful
   to help debug issues while you are developing your own p3d files.
prc
   This is an empty directory in which you may place your own custom prc files
   to customize the Panda3D runtime for all p3d files. For instance, if you
   know your graphics card runs better in DirectX9 than in OpenGL, you can
   place a prc file in this directory with the line "load-display pandadx9" to
   specify that DirectX9 should be used by preference in all p3d files.
start
   This is the default working directory when a p3d file starts up. Some p3d
   files may record their game state information in files in this directory.
   If you remove this directory and its contents, it may reset some of your
   p3d files to their initial state.
