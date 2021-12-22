.. _list-of-build-options:

List of Build Options
=====================

This page lists the full set of options that can be used with the ``build_apps``
and ``bdist_apps`` commands.

build_apps
----------

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
   If specifies, all of the output (such as print statements and error messages)
   is written to a file. The ``$USER_APPDATA/`` prefix can be used to write
   refer to the AppData directory of the current user.

   This string may contain additional formatting parameters containing the
   current date or time, such as ``$USER_APPDATA/My Game/logs/%Y-%m-%d.log``.
log_append
   The default is to erase the log file every time the application is re-run.
   If this is set to True, it will instead preserve the existing contents and
   instead append to the end of the log file.
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

application_id
   This field is required by Android and uniquely identifies the application.
   It is usually based on the inverse of the developer's domain name (e.g.
   "gamestudio.com" becomes "com.gamestudio"), followed by any other components
   as needed to further identify the application.
   As an example, we might publish the Asteroids example on the Play store as
   ``org.panda3d.samples.asteroids``.

   .. caution::

      Once the application has been uploaded to the Google Play Store, it is no
      longer possible to change the identifier.

android_version_code
   This should be an integer that starts at 1 and is incremented with every app
   update. This is just internal, whereas the ``version`` metadata field is used
   to show an arbitrary dot-separated version string to the user. Every time you
   upload a new release to the Play Console, this number must be increased.

android_min_sdk_version
   Overrides the lowest version of Android that the game will still operate on.
   The default is the minimum version of Android that Panda3D supports (19).

android_max_sdk_version
   Overrides the highest version of Android that the game will still operate on.
   There is normally no need to set this.

android_target_sdk_version
   Overrides the version of Android targeted by the application. This affects
   various behaviors and optimizations applied by Android, but does not affect
   the minimum version of Android supported by the application.
   This should be at least 30 to be able to upload the game to the Play Store.

bdist_apps
----------

installers
   See :ref:`packaging-binaries`.
signing_certificate
   Path to a .pem file that is used to sign the package. Currently, this is only
   used on Android.
signing_private_key
   Path to a .pem file that contains the private key matching the certificate
   specified with ``signing_certificate``.
signing_passphrase
   If the private key is encrypted, sets the password necessary to decrypt it.
   If no password is provided, it will be prompted on the command-line.
