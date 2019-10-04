.. _creating-multiple-packages:

Creating multiple packages
==========================

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

A pdef file can contain multiple package and/or p3d file definitions. Each
package named in a pdef file is created and placed in the output directory you
specify with -i on the ppackage command line, and the contents.xml file at the
root of the output directory is updated to describe all of the packages
within.

You can also run ppackage multiple times, with a different pdef file each
time, and specify the same output directory. Each time, additional packages
can be built, and the output directory is updated accordingly.
