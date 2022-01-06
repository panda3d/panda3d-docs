.. _troubleshooting:

Troubleshooting
===============

If you are encountering issues with ``build_apps``, please first make sure you
are using the latest release of Panda3D. A large number of improvements and bug
fixes have been made to this system since it was first released.

This page lists a number of common issues encountered when packaging using
``build_apps``.

Executable closes right away when run
   Was it built via ``gui_apps``? In this case, you need to make sure to specify
   a log file via ``log_filename``, and then find and open the written log file
   to read out the error messages. Usually, it is something simple like a
   missing file, but you need to be able to see the error message to find out.
   Alternatively, you can build it with ``console_apps`` without specifying a
   log file, and read the error from the console.

Exception: No graphics pipe is available!
   Have you included a render plug-in, such as ``pandagl``, in your ``setup.py``
   file?

No audio in compiled application
   Have you included an audio plug-in, such as ``p3openal_audio``, in your
   ``setup.py`` file?

Application crashes without a helpful error message
   By default, ``build_apps`` will use a version of Panda3D that is built with
   optimizations enabled. This also means that many checks and error messages
   are disabled. It may help when debugging an application that only crashes in
   its compiled form to use a non-optimized build of Panda3D. This can be done
   by adding ``'use_optimized_wheels': False`` to ``setup.py``.

No wheels available for dependency package
   The standard way to distribute Python packages is via .whl files uploaded to
   `PyPI <https://pypi.org/>`__. Nevertheless, it is possible that a .whl file
   for a package cannot be found. Check the list of downloads on PyPI for a
   package to see what the problem might be, which is usually one of the
   following:

   The package does not publish wheel files for your version of Python.
      Some packages are compiled for a specific version of Python. If no wheel
      is published for the version of Python you are using, you may need to
      switch to using a different version, or choose an alternative package.

   The package has wheel files for a newer version of the platform.
      For example, the latest version of numpy provides wheels for
      ``manylinux2010_x86_64``, but not for ``manylinux1_x86_64``. You may need
      to adjust the ``platforms`` list in your ``setup.py`` to bump the minimum
      version of the given platform.

   The package does not publish wheel files for one of the target platforms.
      Some packages provide wheels for some platforms, but not all. If you do
      not care about the platform, you can simply drop it from the ``platforms``
      list in ``setup.py``, otherwise you will have to look for an alternative
      package or build the wheel yourself for the given platform.

   The package does not publish wheel files at all.
      If it is a pure-Python package without platform-specific C extensions, it
      is easy to build a .whl yourself by downloading the package, running
      ``python setup.py bdist_wheel``, and then adding ``-f path/to/directory/``
      on a blank line to your ``requirements.txt`` pointing pip to the directory
      containing the .whl file. If it is a package with compiled C extensions,
      then this becomes more difficult. The easiest option at this point is to
      choose a different package that does publish wheel files, but otherwise,
      you must build the package manually for each individual platform.

AttributeError: module 'nt' has no attribute '_path_splitroot'
   This was a compatibility issue with Python 3.8.10, which is fixed as of
   Panda3D 1.10.10. If you cannot upgrade to Panda3D 1.10.10 (or higher), you
   need to downgrade to an older version of Python.

Cryptic FileNotFoundError when using virtualenv
   The build process is tested and known to work with the built-in :mod:`venv`
   module that has been part of Python since version 3.3 as well as with
   the ``pipenv`` tool.

   There has been an `issue <https://github.com/panda3d/panda3d/issues/747>`__
   reported that an error was encountered when using the
   `virtualenv <https://pypi.org/project/virtualenv/>`__ package from PyPI
   instead of the :mod:`venv` module included with Python. This issue has been
   addressed as of Panda3D version **1.10.5**, but we recommend using the
   built-in :mod:`venv` module instead.
