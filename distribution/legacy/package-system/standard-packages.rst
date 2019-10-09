.. _standard-packages:

Standard packages
=================

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

There are a number of packages hosted at the standard Panda3D host URL,
http://runtime.panda3d.org : panda3d, fmod, openal, audio, egg, ode, wx, tk
and more - visit the link for a full list (every subdirectory represents a
package).

Each of these has a package version string that is updated with each new
major.minor.0 release of Panda, for instance, the 1.7.x series of Panda3D is
hosted with the package version "cmu_1_7". As the 1.7.1 and later bugfix
releases are made, they are made in-place under the same version string, so
that p3d files that reference the package version "cmu_1_7" will automatically
download the bugfix release version. However, when the 1.8.0 release is made,
it will be made under the version "cmu_1_8", and the "cmu_1_7" branch will
remain unchanged thereafter, so that p3d files that reference that version can
continue to use it without being affected by possible changes in the 1.8.x
series.

When you reference a package by name with the -r parameter, the default is to
reference one of the standard packages offered by the same host URL that built
packp3d.p3d itself. If you wish to reference a different package on another
host, or a different version of a particular package, you can specify the full
package with "-r name,version,hostURL".

The "panda3d" package is special. This is the package that includes the core
part of the Panda3D code, the code necessary to open a graphics window and
begin rendering. It is not optional. Every p3d file must reference some
package called "panda3d", though it can be with any version string, and any
host URL. (You can even build and host your own package named "panda3d" if
your application requires a custom build of Panda3D for some reason, though we
don't recommend doing this unless there is a good reason to.) The panda3d
package must contain the executable program p3dpython, which is used to start
the p3d application running in a child process.
