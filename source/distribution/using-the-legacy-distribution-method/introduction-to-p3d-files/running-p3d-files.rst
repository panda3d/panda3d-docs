.. _running-p3d-files:

Running p3d files
=================

Note: This article describes a deprecated feature as of Panda3D 1.10.0.

Once you have built a p3d file, you may run it immediately with the panda3d
program:



.. code-block:: bash

    panda3d myapp.p3d



Remember, you may need to add panda3d to your PATH first. On Windows, this is
installed into c:\Program Files\Panda3D by default. If you are running on
Linux or Mac, or running Cygwin on Windows, you can omit "panda3d" and simply
run your p3d file directly as its own command, if it has executable
permissions.

You may also double-click the p3d file's icon on your desktop, or in the
Explorer or Finder browser, which automatically invokes panda3d.

You may now choose to distribute this p3d file directly to your friends. If
they have installed the Panda3D plugin, they can also run it by
double-clicking on its icon. This is an easy, no-nonsense way to distribute
your application, and saves you from having to mess around with embedding your
p3d file into a web page, or packaging it as a self-contained application.
