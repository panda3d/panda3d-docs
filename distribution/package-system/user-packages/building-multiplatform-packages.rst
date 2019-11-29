.. _building-multiplatform-packages:

Building multiplatform packages
===============================

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

When your packages include some compiled C++ code, including dll's or exe's,
you will need to produce a different version package for each operating
system/hardware platform that you wish to support.

By default, ppackage will detect when a package includes platform-specific
files such as dll's, and will automatically write the platform string into the
package specification. This allows you to build the same package on multiple
different platforms, and build a different version for each platform. All of
the versions can be stored in the same output directory and hosted at the same
host URL.

Each time you run ppackage, it is designed to add its contents to an existing
directory (or create a new one). It assumes that the output directory
represents the complete and current package contents at the time you started.

In order to build multiple packages with different platforms, you will
probably need to run ppackage on different machines, one at a time, and direct
them all to populate the same output directory. This means either that your
output directory should be a shared volume, or you will have to copy the
entire output directory from one machine to another between invocations of
ppackage. (I find that rsync is a particularly good tool for copying entire
directory structures efficiently, but there are many tools that do this in
different ways.)

You can also use ppackage to create several different output directories, and
merge those output directories into one using the pmerge utility.
