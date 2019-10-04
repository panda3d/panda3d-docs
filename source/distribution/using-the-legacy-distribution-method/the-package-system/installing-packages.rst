.. _installing-packages:

Installing packages
===================

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

A package file is a Panda3D multifile. When a package is installed onto a
user's machine, it means the multifile is downloaded and placed in its own
subdirectory of the Panda3D installation directory (e.g.
~/Library/Caches/Panda3d, on Mac). This directory name is then stored in the
environment variable PACKAGENAME_ROOT, where PACKAGENAME is the name of the
package converted to uppercase, e.g. PANDA3D_ROOT or ODE_ROOT. (You can query
this environment variable name at runtime with
ExecutionEnvironment.getEnvironmentVariable('PANDA3D_ROOT').)

The multifile is also automatically "mounted" using Panda's VirtualFileSystem,
onto the same directory, so that it is as if all of the contents of the
multifile are actually available as individual files within the
PACKAGENAME_ROOT directory, even though the individual files may not actually
appear on disk at all. Furthermore, the PACKAGENAME_ROOT directory is added to
Python's sys.path, as well as to Panda's model-path, so that any Python
modules can be imported, and any model files can be imported, directly from
the package. In addition, any prc files in the PACKAGENAME_ROOT directory will
be automatically loaded.

Some file types, such as DLL files, really do need to be extracted to disk to
be used, because they are loaded directly by the operating system and not by
Panda. These files are extracted automatically when the package is installed
and left within the PACKAGENAME_ROOT directory (or within a subdirectory if
the filename so indicates).
