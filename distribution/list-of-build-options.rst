.. _list-of-build-options:

List of Build Options
=====================

This page lists the full set of options that can be used with the ``build_apps``
command:

build_base
   The directory to build the applications in (defaults to "build" in the
   current working directory)
gui_apps
   A dictionary of applications that can open a window with executable names as
   keys and the path to the main/entry-point script as the value
console_apps
   A dictionary of applications that do not open a window with executable names
   as keys and the path to the main/entry-point script as the value
include_patterns
   A list of patterns of files to include in the built applications
exclude_patterns
   A list of patterns of files to not include in the build application (takes
   precedence over include_patterns)
rename_paths
   A dictionary with keys being a path to match and the value being the path to
   replace it with
include_modules
   A dictionary with keys being an application (use ``'*'`` to denote all
   applications) and values being lists of Python modules to freeze into the
   application regardless of whether FreezeTool detects it as a dependency
   (useful for "hidden" imports that FreezeTool may not be able to follow)
exclude_modules
   A dictionary with keys being an applications (use ``'*'`` to denote all
   applications) and values being lists of Python modules to not freeze into the
   application regardless of whether FreezeTool detects it as a dependency
log_filename
   If specifies, all of the output (such as print statemetns and error messages)
   is written to a file. The ``$USER_APPDATA/`` prefix can be used to write
   refer to the AppData directory of the current user.
log_append
   The default is to erase the log file every time the application is re-run.
   If this is set to True, it will instead preserve the existing contents and
   instead append to the end of the log file.
log_filename_strftime
   New in Panda3D 1.10.9. If set to true, the ``log_filename`` string can
   contain additional formatting parameters containing the current date or time,
   such as ``$USER_APPDATA/My Game/logs/%Y-%m-%d.log``.
platforms
   A list of
   `PEP 425 platform tags <https://www.python.org/dev/peps/pep-0425/>`__ to
   build applications for. The default differs on the version of Python used.
   See :ref:`building-binaries` for an explanation and a list of options.
plugins
   A list of dynamically loaded Panda3D plug-ins included with the built
   applications. A list is available on :ref:`building-binaries`.
requirements_path
   A path to a requirements.txt file to use with PIP when fetching wheels
   (defaults to ./requirements.txt)
use_optimized_wheels
   If set, try to download optimized wheels for Panda3D using an extra index url
   (defaults to True). These optimized builds of Panda3D are built without extra
   debug information and error checks; these are useful when developing a
   Panda3D application, but take up more disk space and run slower, so they are
   disabled in the optimized wheels.

   Optimized wheels are versioned such that they will have higher priority than
   regular wheels of the same version, but will have less priority than a newer
   version of a regular wheel. In other words, if the latest available version
   does not have an optimized wheel available, a regular wheel is used instead.
optimized_wheel_index
   The extra index url to use to find optimized wheels (Panda3D will try to set
   a reasonable default if this is not set)
icons
   New in Panda3D 1.10.4. A dictionary mapping gui_apps/console_apps keys to a
   list of images from which an icon file is generated. This list should contain
   versions the same image at different resolutions. Panda3D will automatically
   resize the image to provide for missing resolutions if necessary, so it is
   possible (but not recommended) to specify only one high-resolution image.

   If "*" is used as key, sets the icons for all included apps.
file_handlers
   A dictionary with keys matching extensions and values being functions of the
   form:

   .. code-block:: python

      def func(build_cmd, srcpath, dstpath):

   The function is run when encountering a file with the given extension.
   User-defined file handlers for an extension override the default handler.
   By default, there is only one file handler registered: for .egg files, which
   runs egg2bam.

bam_model_extensions
   New in Panda3D 1.10.13. A list of model extensions that are automatically
   converted to .bam during build. Add extensions to this if you are using other
   file formats than .egg (such as .gltf and .glb for
   :ref:`glTF files <gltf-files>`).

strip_docstrings
   New in Panda3D 1.10.13. If true, which is the default, all docstrings will be
   removed as an optimization, and any use of ``__doc__`` will return ``None``.
   Set this to false if you need to keep these docstrings for some reason.

prefer_discrete_gpu
   New in Panda3D 1.10.13. On systems with both an integrated and dedicated
   GPUs, tells the driver that the application prefers to use the dedicated GPU,
   which usually provides higher performance. At the moment, this option is only
   implemented on Windows, and only for NVIDIA and AMD graphics cards.
