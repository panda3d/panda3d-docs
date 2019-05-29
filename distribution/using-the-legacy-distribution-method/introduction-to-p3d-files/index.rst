.. _introduction-to-p3d-files:

Introduction to p3d files
=========================

Note: This article describes a deprecated feature as of Panda3D 1.10.0.

The p3d file is the heart of Panda's packaging system. When you package your
application for distribution, you will pack it into a p3d file. This file
contains everything you need to run your application: Python code, models,
textures, prc files, even compiled dll's or pyd's if part of your application
is written in C++.

The p3d file is really a Panda multifile object; you can inspect its contents
or add and remove components with the multify command, as with any multifile.
However, a p3d file is a special kind of multifile that is specifically
intended to contain a Panda application. The file extension ".p3d" is used to
differentiate it from a generic multifile (which may contain anything
whatsoever).

Although it is possible to build a p3d file up by hand using the multify
command, it's usually easier to use one of the packaging tools provided, such
as packp3d or ppackage, to create a new p3d file from an application on disk.

The p3d file indicates the particular version of Panda3D that should be used
to run your application. This allows you to write an application using a
particular version of Panda3D, without being forced to update it when a new
version of Panda3D is released.


.. toctree::
   :maxdepth: 2

   using-packp3d
   referencing-packages
   running-p3d-files
