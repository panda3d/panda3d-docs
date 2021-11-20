.. _model-export:

Model Export
============

Panda3D uses a custom file format for its models, called egg. To create an egg
file, you will need to use a modeling program (like 3D Studio Max, Blender or
Maya) combined with either an export plugin or a file format converter. You
can read more about this process in the following sections. Panda3D also
provides a binary file format bam, which is quicker to load.

Both file formats contain:

-  Vertices
-  Triangles and larger polygons
-  Joints (aka Bones)
-  Vertex weights
-  Texture pathnames (textures are not stored)
-  Bone-based animation keyframes
-  Morph targets (aka Blend targets)
-  Morph animation keyframes
-  Many control flags

The paths (e.g. for textures) can be either relative (as seen from the egg
file) or absolute (full path). See :ref:`filename-syntax` for more info about
Panda's Filename Syntax. In most cases the relative path makes more sense.

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2

   converting-from-3d-studio-max
   converting-from-maya
   converting-from-blender
   converting-from-milkshape-3d
   converting-from-gmax
   converting-from-other-formats
   converting-egg-to-bam
   parsing-and-generating-egg-files
   egg-syntax
