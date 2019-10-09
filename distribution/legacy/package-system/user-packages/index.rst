.. _building-and-hosting-your-own-packages:

Building and hosting your own packages
======================================

.. warning::

   This section describes a deprecated feature as of Panda3D 1.10.0.

Putting your entire application into a p3d file is a useful way to distribute
small applications, but there are times when you need to distribute your code
a little more intelligently. Large applications may need to be divided into
several smaller pieces for download at runtime; or you might have a large
C++-based library that you want to make available to several different
applications, without having to re-download it for each one.

For these purposes, you should consider using packages. A package has several
advantages over a simple p3d file:

-  It can be downloaded on demand, either automatically at startup, or during
   runtime if desired.

-  One package can be downloaded once and shared by multiple p3d files.

-  Packages will be cached in the user's Panda3D directory. (p3d files, on the
   other hand, are saved in the browser cache only, where there may be less
   space.)

-  Patching can be used to automatically update a package with a new version,
   so that your users need download only the incremental changes, instead of
   having to completely redownload the package at every change.

-  There can be a different version of a package for each hardware/OS platform
   that you wish to support. This is the easiest way to provide multiplatform
   support with C++-based applications.

On the other hand, setting up packages requires a little more work than simply
building a p3d file.


.. toctree::
   :maxdepth: 2

   using-ppackage
   pdef-syntax
   creating-multiple-packages
   hosting-packages
   ssl-hosting
   building-multiplatform-packages
   building-patches
