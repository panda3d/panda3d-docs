.. _packageinstaller:

PackageInstaller
================

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

The PackageInstaller class is used to download and install a Panda3D package,
as built by the ppackage.p3d utility, at runtime. It is similar to
base.appRunner.installPackage(), but it is capable of downloading a package in
the background, while the rest of your game continues. You can get
notifications as the package is being downloaded.

PackageInstaller is itself an abstract class, and its callback notifications
are defined as methods. To use PackageInstaller, you should subclass from it
and override any of the six callback methods: downloadStarted(),
packageStarted(), packageProgress(), downloadProgress(), packageFinished(),
downloadFinished(). See the generated API documentation for more information.

You might find the DWBPackageInstaller class, which stands for "DirectWaitBar
PackageInstaller", even more convenient--it multiply inherits from
PackageInstaller and DirectWaitBar, and defines the callback methods to update
the GUI automatically as the package is downloading. For example, the following
code will automatically download and install a package, and call your method
packageInstalled when the download has finished. See the generated API
documentation for more information.

.. code-block:: python

   from direct.p3d.DWBPackageInstaller import DWBPackageInstaller

   self.pi = DWBPackageInstaller(base.appRunner,
                                 parent = base.a2dTopRight,
                                 scale = 0.5, pos = (-0.6, 0, -0.1),
                                 finished = self.packageInstalled)
   self.pi.addPackage('myPackage', 'myVersion',
                      hostUrl = 'http://myhost.com/packages')
   self.pi.donePackages()
