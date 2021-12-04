.. _distribution:

Distributing Panda3D Applications
=================================

.. only:: python

   Starting with Panda3D 1.10.0, Panda3D provides new tools that make it easy to
   compile Python applications using Panda3D into a self-contained executable
   file, which can then be hosted on a website or store front for distribution
   to end-users.

   These tools are unique among packaging tools in that they will automatically
   produce binaries for Windows, Linux and macOS. You do not need to own those
   systems in order to compile a binary for them. In the future, we will extend
   this list as we add support for more platforms.

   Furthermore, they are able to automatically pull in a special optimized
   version of Panda3D that is lighter and faster than the builds on the website,
   since they are built without debugging aids and error messages enabled.
   Building Panda3D from source code is therefore not necessary to create an
   optimized build.

   The old system that shipped with Panda3D 1.9 and operated on .p3d files is no
   longer supported. It was too complex to use and maintain, required special
   builds of Panda3D, and did not work with Python 3.

   These tools are implemented as plug-ins to setuptools, which is the standard
   build system for packaging Python applications. You can read more about it in
   `its documentation <https://setuptools.pypa.io/en/latest/>`__, but the basic
   idea is that you create a ``setup.py`` or ``setup.cfg`` file describing the
   application with a list of files that need to be compiled into the
   distribution. Then, ``setup.py`` is run with a command that tells it what
   plug-in to invoke to do the appropriate packaging operation.

   Panda3D adds two new commands to setuptools:

   :ref:`build_apps <building-binaries>`: compile the application into one or
   more stand-alone executable files

   :ref:`bdist_apps <packaging-binaries>`: runs ``build_apps``, then packages
   the compiled executables into various archives and installers for
   distribution

   Thus, the basic steps to deploy a Panda3D application are:

   #. Create a ``setup.py`` or ``setup.cfg`` file for your application
   #. Execute ``python setup.py bdist_apps``
   #. Upload the resulting files (e.g. zip, tar.gz, exe) to a store front or web
      site

.. only:: cpp

   To produce a distributable C++ Panda3D application, it is recommended to
   build Panda3D from source with optimizations enabled. This disables assertion
   messages and other debugging aids to create a more optimized, slimmer and
   faster version of Panda3D. You can also choose to omit the features of
   Panda3D that you don't need, or exclude the third-party packages that have
   incompatible licensing terms.

   You can do so by checking out the source code of Panda3D and running the
   ``makepanda.py`` build script with the ``--optimize 4`` flag. Run it with
   ``--help`` to see a list of packages and components that can be excluded.

   After building Panda3D from source, it will be necessary to take the files
   in the ``built/bin`` directory (and, on platforms other than Windows, the
   ``built/lib`` directory) and ship them together with the executable file of
   the game. You can alternatively choose to compile Panda3D statically, using
   the ``--static`` flag. This allows you to link the Panda3D libraries into the
   executable, obviating the need to ship them separately. However, this method
   is only advisable if the application consists of a single executable, and is
   not divided up into multiple libraries or executable files that all use the
   Panda3D API.

   The rest of this section focuses on explaining the distribution tools
   available to Python users of the engine, and is not relevant for C++ users.

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2

   building-binaries
   list-of-build-options
   packaging-binaries
   troubleshooting
   thirdparty-licenses
