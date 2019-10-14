.. _using-ppackage:

Using ppackage
==============

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

The ppackage utility is Panda's utility for building packages. You can also
use ppackage to build a p3d file; this gives you much more control over the
p3d file than packp3d's simple interface.

To use ppackage, you must first create a pdef file, or a package definition
file. This is a file that defines precisely what package(s) or p3d file(s) are
to be produced, and what contents should go into each one. The syntax of the
pdef file is described on the next page.

Once you have the pdef file, you can run ppackage as follows:

.. code-block:: bash

    ppackage -i c:/output_dir myfile.pdef

The directory named with -i is the directory into which the contents of the
package(s) named in the pdef file will be placed. It doesn't have to exist
before you run ppackage, but if it does already exist from a previous ppackage
session, new contents will be added to it. You must eventually copy this
directory to a web host to make the packages available for use; see Hosting
packages, below.

As with packp3d, you must have panda3d on your path; and you can omit the
panda3d prefix on Linux and Mac.

Also like packp3d, you should use the version of ppackage.p3d that is
distributed with the particular version of Panda3D that you are using for
development--ppackage.p3d is associated with the version of Panda3D that was
used to produce it, and by default will generate packages that depend on that
version of Panda3D.
