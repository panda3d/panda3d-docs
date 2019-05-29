.. _multifiles:

Multifiles
==========

This section describes that Multifiles are, how to use them and patch them.
The multifiles can store multiple resources like models, textures, sounds,
shaders, and so on, and Panda can load them from directly from the multifiles
without having to unpack them first.

Multifiles can also be used in patching, zipping and encrypting your data.
Multifiles are similar to ".egg" for python libraries or .jar files for java
platform. Many games employ a similar concept of "data" file such as .upk for
Unreal Engine and .pak for Quake Engine.

The key to Multifiles is that they are very easy to use. Almost none of the
game loading logic has to change when switching to multifiles except for a few
lines at the top to mount some multifiles into the Panda3D virtual file
system.


.. toctree::
   :maxdepth: 2

   creating-multifiles
   patching
   loading-resources-from-nonstandard-sources
