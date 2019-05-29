.. _more-about-referencing-packages:

More about referencing packages
===============================

Note: This article describes a deprecated feature as of Panda3D 1.10.0.

A p3d file may include a reference to one or more packages, which means that
those package(s) will be downloaded and installed before the application even
begins. This is specified with the -r parameter to packp3d, or with the
requires() call in a pdef file.

It is also possible to download and install one or more packages at runtime,
after the application has already started. To do this, instead of referencing
the package with the -r parameter, you can call
:ref:`base.appRunner.installPackage() <other-apprunner-members>` at runtime,
or you can use the
:ref:`PackageInstaller or DWBPackageInstaller <packageinstaller>` class to
download and install it asynchronously.
