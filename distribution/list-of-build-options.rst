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
   build applications for (defaults to
   ``['manylinux1_x86_64', 'macosx_10_6_x86_64', 'win_amd64']``); other options
   are 'win32', 'manylinux1_i686' and 'macosx_10_6_i686'.
plugins
   A list of dynamically loaded Panda3D plug-ins included with the built
   applications (available plug-ins are listed below)
requirements_paths
   A path to a requirements.txt file to use with PIP when fetching wheels
   (defaults to ./requirements.txt)
use_optimized_wheels
   If set, try to download optimized wheels using an extra index url (defaults
   to True)
optimized_wheel_index
   The extra index url to use to find optimized wheels (Panda3D will try to set
   a reasonable default if this is not set)
icons
   New in Panda3D 1.10.4. A dictionary mapping gui_apps/console_apps keys to a
   list of images from which an icon file is generated.
file_handlers
   A dictionary with keys matching extensions and values being functions of the
   form:

   .. code-block:: python

      def func(build_cmd, srcpath, dstpath):


Default File Handlers
---------------------

File handlers defined by the ``file_handlers`` option are added to a list of
default file handlers. User-defined file handlers for an extension overrides the
default file handler. By default, there is only one file handler registered: for
.egg files, which runs egg2bam.
