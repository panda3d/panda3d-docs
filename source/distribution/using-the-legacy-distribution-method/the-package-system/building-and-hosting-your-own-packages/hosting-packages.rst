.. _hosting-packages:

Hosting packages
================

Note: This article describes a deprecated feature as of Panda3D 1.10.0.

After you build one or more packages, you have to make them available for
download. This means you must copy the entire contents of the output directory
(the directory named with -i on the ppackage command line) to a web server
where it will be visible for download under a particular URL.

The root URL that contains the output directory, including the contents.xml
file therein, is called the "host URL". This is the URL that you must use when
referencing your package in your p3d file(s).

When the Panda3D plugin system downloads a package, it first downloads the
contents.xml file at the root of the host URL, and it uses this file to
determine which packages are defined at this host and whether any packages
need to be redownloaded. So it is important to copy the entire contents of the
output directory, and not to change any parts of it other than with the
ppackage tool.

Although not strictly necessary, it is helpful to tell the package, at the
time you build it, what its final host URL will be. You can do this by calling
packager.setHost() at the top of the pdef file (before the first class
definition), like this:



.. code-block:: python

    packager.setHost('http://myhost.com/myrootdir/')


