.. _the-package-system:

The package system
==================

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

The Panda3D plugin uses a system of "packages" to manage additional content
needed by p3d files.

A package is a Panda multifile, similar to a p3d file. Like a p3d file, it can
contain Python code, C++ code, models, and textures, or really anything an
application might need to run; but unlike a p3d file, it does not
(necessarily) contain an application.

Everything that the Panda3D plugin downloads, other than the p3d file itself,
is downloaded as part of a package file. For instance, if your applicationm
makes use of audio, you will build it with "-r audio" on the packp3d command
line, which tells Panda3D to download and install the audio package before
beginning your application. Even Panda3D itself, which the plugin downloads to
run your application, is downloaded in a package.

A package is identified with four pieces of information:

-  The package name
-  The package "version" name, may be empty
-  The current platform string, empty for any platform
-  The host URL

It all starts with the host URL. The host URL is used throughout the Panda3D
plugin system to refer to a particular download server. It is possible to
build and host your own packages that the plugin can download; you will need
to supply a host URL. You should be careful to always specify the host URL
with precisely the same string, because that is a unique identifier within the
plugin system; for instance, don't use
"http://myhost.mydomain.net:/my/root_dir" in one place, and
"http://myhost.mydomain.net:/my/root_dir/" in another, even though the two
URL's are technically equivalent.

This can be any URL, but there must exist a file called contents.xml at that
URL, e.g. if the host URL is "http://myhost.mydomain.net/my/root_dir", then
there must exist a file "http://myhost.mydomain.net/my/root_dir/contents.xml".
This file is the key piece of information that the plugin uses to determine
which packages are provided by that host, and whether they need to be updated
for a particular user.

The package name and version are used together to uniquely identify a
particular package file on a given host URL.

Note that the "version" is not intended to represent sequential releases made
for a package. The version is not a number that you increment with each update
you make to a package; rather, the version is a completely arbitrary string
that differentiates mutually-incompatible variations of the package. A p3d
file will reference a package by its name and version, and it will
automatically download the most recent update available for a particular
name/version combination. However, if you release a different version of a
particular package using a different version string, existing p3d files will
not download that different version--it's considered a different series.

The platform string is either empty if the package can be used on any
platform, or it is a string such as "win32" or "osx_i386" to indicate the
particular platform for which this version of the package is built. If a
package contains platform-specific content such as compiled dll's or exe's,
its platform string should be nonempty. There may be a different form of the
package for each supported platform on a given host. The Panda3D runtime will
automatically download the platform-appropriate package, if available.


.. toctree::
   :maxdepth: 2

   standard-packages
   installing-packages
   more-about-referencing-packages
   user-packages/index
