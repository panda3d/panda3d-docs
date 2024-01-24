.. _building-binaries:

Building Binaries
=================

Overview
--------

Panda3D adds a ``build_apps`` command to setuptools that can compile a Panda3D
application into a self-contained executable for all supported operating
systems. This command uses `pip <https://pip.pypa.io/en/stable/>`__ to fetch the
dependencies, downloaded in the form of .whl files ("wheels"), then compiles all
of the bytecode into an executable file and bundles it with the assets, any DLLs
and other files that may be required by the application or its dependencies.

The tool also needs to fetch a wheel for Panda3D itself. It needs to do this
because the already-installed version will not work on other platforms, and
furthermore it is built with debugging tools enabled and not optimized for
distribution.

In order for pip to know which dependencies to fetch, a
`requirements file <https://pip.pypa.io/en/stable/user_guide/#requirements-files>`__
is required. This should list all of the dependencies that are packaged along
with the application, including Panda3D itself. Third-party dependencies
available via pip are therefore supported, as long as they provide wheel files
for the different supported platforms (as the vast majority of packages do).

Example
-------

At minimum, a ``requirements.txt`` file needs to be present with a reference to
Panda3D, such as the following, which tells pip that a release of Panda3D 1.10
of at least 1.10.9 is required::

   panda3d~=1.10.9

This is an example ``setup.py`` showing how to package the
:ref:`Asteroids <asteroids>` sample program into a self-contained executable:

.. code-block:: python

   from setuptools import setup

   setup(
       name='asteroids',
       options={
           'build_apps': {
               # Build asteroids.exe as a GUI application
               'gui_apps': {
                   'asteroids': 'main.py',
               },

               # Set up output logging, important for GUI apps!
               'log_filename': '$USER_APPDATA/Asteroids/output.log',
               'log_append': False,

               # Specify which files are included with the distribution
               'include_patterns': [
                   '**/*.png',
                   '**/*.jpg',
                   '**/*.egg',
               ],

               # Include the OpenGL renderer and OpenAL audio plug-in
               'plugins': [
                   'pandagl',
                   'p3openal_audio',
               ],
           }
       }
   )

To compile the executable, run the following command::

   python setup.py build_apps

The resulting binaries will be stored in the ``build`` folder with one
sub-folder per targeted platform, together with all the requisite files needed
to run the application.

GUI and Console Apps
--------------------

It is possible to build two kinds of executables, ``gui_apps`` and
``console_apps``. This distinction is especially important on Windows and macOS,
whereas there is no difference on other operating systems.

GUI apps are expected to be run from a file browser, start menu or straight from
the desktop. They communicate back to the user via graphical windows, not via
command-line output. On Windows, it is necessary to build as a GUI app to avoid
a Command Prompt being opened when run. However, there is no command-line output
at all on Windows or macOS when run as a GUI app! To be able to see error
messages, you *must* set up logging to a file via ``log_filename``, such as in
the example above.

Console apps, on the other hand, are expected to be run from the command-line.
On Windows, they will always spawn a Command Prompt when run. They can take
command-line arguments, display output directly to the console and do not
require setting ``log_filename``.

Including Assets
----------------

Most applications have assets that need to be included separately with the
application. These are not included by default, since Panda3D doesn't know which
files are necessary for an application or which ones are source assets or
development files that should not be distributed.

The ``include_patterns`` key can be used to specify a list of files or patterns
to include with the application. This does not need to be used for Python files,
which are compiled into the executable itself, and are not included separately.
The pattern is quite flexible:

.. code-block:: python

   'include_patterns': [
       # Path to a specific file
       'CREDITS.txt',

       # All files in the assets/textures/ directory, but not in subdirectories
       # (use ** instead of * if that is desirable)
       'assets/textures/*',

       # All files with the .jpg extension in any subdirectory under assets/,
       # even if nested under multiple directories
       'assets/**/*.jpg',

       # A file with the .egg extension anywhere in the hierarchy
       '**/*.egg',
   ],

Similarly, you can define an ``exclude_patterns`` set with the same format
containing files to exclude from the set above. An alternative approach is to
create a pattern that includes all files, and only specify extensions to exclude
using ``exclude_patterns``.

Some extensions, such as ``.egg``, have special handlers associated with them.
The handler for ``.egg`` will automatically run ``egg2bam`` to compile it into a
``.bam`` file. BAM files are smaller and load more efficiently, and allow the
EGG loading plug-in to be excluded from the Panda3D build.

Custom file handlers can be defined as well, as explained on the
:ref:`list-of-build-options` page.

Including Plug-Ins
------------------

Much Panda3D functionality is available via optional plug-ins. For example, to
enable the ability to render graphics on screen, you must choose at least one
of the graphics API plug-ins. Similarly, if you want to play sound and music,
you need to include either the OpenAL or FMOD audio plug-in. The most common
combination is:

.. code-block:: python

   'plugins': ['pandagl', 'p3openal_audio'],

.. list-table:: List of Plug-Ins
   :widths: 20, 80

   * - pandagl
     - OpenGL renderer (recommended)
   * - pandagles
     - OpenGL ES 1 renderer
   * - pandagles2
     - OpenGL ES 2/3 renderer
   * - pandadx9
     - Direct 3D 9 renderer (Windows only)
   * - p3tinydisplay
     - Software renderer
   * - p3ffmpeg
     - Adds support for additional audio, image, and video formats beyond what
       is built into Panda3D by default. Not necessary for .ogg and .wav.
   * - p3openal_audio
     - Audio (including 3D audio) support using OpenAL
   * - p3fmod_audio
     - Audio (including 3D audio) support using FMOD (note the licensing!)
   * - pandaegg
     - Enables support for reading .egg files. Generally, you should not include
       this, since .egg files are automatically converted to .bam during build.
   * - p3ptloader
     - Adds support for additional model formats. You probably want to instead
       add those model extensions to the ``bam-model-extensions`` list.
   * - p3assimp
     - Adds support for additional model formats. You probably want to instead
       add those model extensions to the ``bam-model-extensions`` list.

Note that some plug-ins use third-party libraries that may have different
licensing terms from Panda3D. More information about these libraries can be
found :ref:`here <thirdparty-licenses>`. Please review the licensing terms of
these libraries before including the respective plug-in!

Platform Tags
-------------

By default, Panda3D will build for 64-bit versions of Windows, macOS and Linux.
More specifically, *platform tags* are used to specify the minimum version and
architecture of the operating system supported by a Python package. You can
specify these platforms explicitly to customize the targeted platforms and their
versions. The default set, as of Python 3.7, is as follows:

.. code-block:: python

   'platforms': ['manylinux1_x86_64', 'macosx_10_6_x86_64', 'win_amd64'],

On more recent versions of Python, newer defaults are used. See the list below
for details.

Sometimes, it is desirable to use third-party packages that do not provide
wheels for a given platform. For example, the latest version of numpy no longer
publishes wheels for ``manylinux1_x86_64`` or ``macosx_10_6_x86_64``. If you
wish to use the latest version of numpy, then you need to therefore set the
platform tags to increase these versions:

.. code-block:: python

   'platforms': ['manylinux2010_x86_64', 'macosx_10_9_x86_64', 'win_amd64'],

.. list-table:: List of Platforms
   :widths: 20, 80

   * - win_amd64
     - 64-bit Windows systems (including Intel x64 processors).
   * - win32
     - 32-bit Windows systems, rarely used nowadays.
   * - manylinux1_x86_64
     - Set this to target the oldest 64-bit Linux distributions. No longer
       supported as of Python 3.10, where manylinux2010_x86_64 is silently used
       as default.
   * - manylinux1_i686
     - Set this to target the oldest 32-bit Linux distributions.
   * - manylinux2010_x86_64
     - Target 64-bit Linux distributions more recent than (more or less) 2010.
       No longer supported by Python 3.11, which uses manylinux2014_x86_64.
   * - manylinux2010_i686
     - Target 32-bit Linux distributions more recent than (more or less) 2010.
   * - manylinux2014_x86_64
     - Target 64-bit Linux distributions more recent than (more or less) 2014.
   * - manylinux2014_i686
     - Target 32-bit Linux distributions more recent than (more or less) 2014.
   * - macosx_10_9_x86_64
     - Target Intel Macs running OS X Mavericks or higher. Recommended.
   * - macosx_10_6_x86_64
     - Target 64-bit Intel Macs running Mac OS X Snow Leopard or above.
       No longer supported as of Python 3.8.
   * - macosx_10_6_i386
     - Target 32-bit Intel Macs running Mac OS X Snow Leopard or above.
       No longer supported as of Python 3.8.

.. note::

   Python 3.9 no longer supports Windows 7. If you need to target Windows 7 in
   your application, use Python 3.8, unless you also need to support macOS
   versions older than 10.9, in which case you should use Python 3.7 or older.

Icons
-----

On Windows and macOS, it is possible to change the icon that is shown in file
browsers or the dock for the compiled executable. This feature requires Panda3D
1.10.4 or later. To use this feature, modify the ``setup.py`` file to something
like the following:

.. code-block:: python

   "gui_apps": {
       "asteroids": "src/main.py",
   },
   "icons": {
       # The key needs to match the key used in gui_apps/console_apps.
       # Alternatively, use "*" to set the icon for all apps.
       "asteroids": ["icon-256.png", "icon-128.png", "icon-48.png", "icon-32.png", "icon-16.png"],
   },

You can provide a single image file of at least 256×256 and Panda3D will scale
it down to smaller sizes as needed, but because automatic scaling can make the
icon look illegible at smaller sizes, we highly recommend providing
custom-scaled versions at resolutions 16, 32, 48, 128, and 256.
For best results, it also doesn't hurt to provide icons in additional
resolutions, such as 24, 64, 96, 512, and 1024.
