.. _texturing:

Texturing
=========

At its simplest, texturing merely consists of applying a texture in your
modeling program. When you export the model, the path to the texture and some
options for it like filtering or repeat-method (see next pages) are saved into
the egg file. The texture paths can be either relative (as seen from the egg
file) or absolute (full path). See :ref:`filename-syntax` for more info about
Panda's filename syntax. In most cases the relative path makes more sense.

Panda can load JPG, PNG, TIF, and a number of other file formats.

More advanced texturing methods are described in the following sections.


.. toctree::
   :maxdepth: 2

   simple-texturing
   choosing-a-texture-size
   texture-wrap-modes
   texture-filter-types
   simple-texture-replacement
   multitexture-introduction
   texture-modes
   texture-order
   texture-combine-modes
   texture-transforms
   multiple-texture-coordinate-sets
   automatic-texture-coordinates
   projected-textures
   simple-environment-mapping
   3d-textures
   cube-maps
   environment-mapping-with-cube-maps
   automatic-texture-animation
   playing-mpg-and-avi-files
   multiview-textures
   transparency-and-blending
   texture-management
   texture-compression
   creating-textures
