.. _using-the-legacy-distribution-method:

Using the legacy distribution method
====================================

Beginning in Panda3D version 1.7.0, Panda provides a packaging and
distribution system designed to make it very easy to distribute your Panda3D
application to the world, either embedded within a web page or distributed as
a standalone application.

This system is no longer supported as of Panda3D 1.10.0. Starting with 1.10,
Python applications using Panda3D can be packaged in a distributable form
(e.g., zip archives, Windows installers, tarballs) using
`Setuptools <https://setuptools.readthedocs.io/en/latest/>`__. These packages
can then be hosted on a website or store front for distribution to end users.
Using this new Setuptools-based process is recommended over the legacy
ppackage/pdeploy system since it is simpler, easier to maintain, uses the
standard tools of the Python packaging ecosystem, and provides better support
for Python 3.

The following section is for users who are unable to update to 1.10.0 only.


.. toctree::
   :maxdepth: 2

   introduction-to-p3d-files/index
   distributing-via-the-web/index
   p3d-file-config-settings
   distributing-as-a-self-contained-installer
   the-runtime-panda3d-directory
   the-package-system/index
   advanced-scripting-techniques/index
