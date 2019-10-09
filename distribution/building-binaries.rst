.. _building-binaries:

Building Binaries
=================

Overview
--------

The ``build_apps`` command uses `pip <https://pip.pypa.io/en/stable/>`__ to
fetch any binary packages (including Panda3D) as wheels that are necessary to
build the applications for other platforms. In order for pip to know which
wheels to fetch(including the correct panda3d wheel), a `requirements file
<https://pip.pypa.io/en/stable/user_guide/#requirements-files>`__ (or a Pipfile
if `pipenv <https://pipenv.readthedocs.io/en/latest/>`__ is being used) is
required. After collecting dependencies, platform-specific binaries (e.g., exe
on Windows) are built for each listed application for each listed platform.

Options
-------

The following options can be used with the ``build_apps`` command:

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
platforms
   A list of
   `PEP 425 platform tags <https://www.python.org/dev/peps/pep-0425/>`__ to
   build applications for (defaults to
   ``['manylinux1_x86_64', 'macosx_10_6_x86_64', 'win_amd64']``); other options
   are 'win32', 'manylinux1_i686' and 'macosx_10_6_i686'.
plugins
   A list of dynamically loaded Panda3D plugins include with the built
   applications (available plugins are listed below)
requirements_paths
   A path to a requirements.txt file to use with PIP when fetching wheels
   (defaults to ./requirements.txt)
use_optimized_wheels
   If set, try to download optimized wheels using an extra index url (defaults
   to True)
optimized_wheel_index
   The extra index url to use to find optimized wheels (Panda3D will try to set
   a reasonable default if this is not set)
file_handlers
   A dictionary with keys matching extensions and values being functions of the
   form:

   .. code-block:: python

      def func(build_cmd, srcpath, dstpath)


Default File Handlers
---------------------

File handlers defined by the ``file_handlers`` option are added to a list of
default file handlers. User-defined file handlers for an extension overrides the
default file handler. By default, there is only one file handler registered: for
.egg files, which runs egg2bam.

Available Plugins
-----------------

p3ffmpeg
   Adds support for additional audio, image, and video formats beyond what is
   built into Panda3D by default
p3openal_audio
   Audio (including 3D audio) support using OpenAL
p3fmod_audio
   Audio (including 3D audio) support using FMOD
p3ptloader
   Adds support for additional model formats beyond BAM
p3assimp
   Adds support for additional model formats beyond BAM by using Assimp
p3tinydisplay
   Software renderer
pandagl
   OpenGL renderer
pandagles
   OpenGL ES renderer
pandagles2
   OpenGL ES 2 renderer
pandadx9
   Direct 3D 9 renderer (Windows only)

More information about some of the libraries used by these plugins can be found
:ref:`here <thirdparty-licenses>`.

Optimized Builds
----------------

By default, Panda3D is built with extra debug information and code (sometimes
referred to as an SDK build of Panda3D). While this extra debug information and
code is very useful for developing a Panda3D application, it takes up more disk
space and runs slower. To solve this, optimized wheels are available that strip
out this debug information and code.

If ``use_optimized_wheels`` is set to ``True``, then ``build_app`` will
automatically try to find an optimized wheel that meets the Panda3D version
requirements of the application. It does this by exposing an extra index URL to
pip. Optimized wheels are versioned such that they will have higher priority
than regular wheels of the same version, but will have less priority than a
newer version of a regular wheel.

If PyPI or `archive.panda3d.org <https://archive.panda3d.org/>`__ are used as
the index for the regular Panda3D wheel, then ``build_apps`` can pick an
appropriate index URL for optimized wheels. Otherwise, set
``optimized_wheel_index`` to point to the index that contains the optimized
wheels.
