.. _egg-files:

Egg Files
=========

The Egg format is a file format unique to Panda3D. It is a text-based format,
which means it can be opened in a text editor to inspect its contents.

An Egg file can contain static geometry, but it can also contain information
for animating the model, as well as information about the model's material, ie.
what color the material has, and how this color changes under the influence of
lighting). However, unlike Bam, it cannot represent all of the things that are
possible in Panda3D. For instance, light sources are not represented.

To create an Egg file, you will need to use a modeling program (like Autodesk
Maya or 3ds Max) combined with either an export plugin or a file format
converter. You can read more about this process in the following sections.

The Egg format supports, among other things:

-  Vertices
-  Triangles and larger polygons
-  Joints (aka Bones)
-  Vertex weights
-  Texture pathnames (textures are not stored)
-  Bone-based animation keyframes
-  Morph targets (aka Blend targets)
-  Morph animation keyframes
-  Many control flags

Notably, these things are not represented:

-  Light sources
-  Shaders

The paths (e.g. for textures) can be either relative (as seen from the Egg
file) or absolute (full path). See :ref:`filename-syntax` for more info about
Panda's Filename Syntax. In most cases the relative path makes more sense.

Animations
----------

The EGG format is somewhat unique in that animations can be stored in a separate
Egg file. In fact, the most common approach is to have one Egg file containing
the model and its joint hierarchy, and to have a separate Egg file for each
animation that acts on this joint hierarchy. These files are then specified
together when :ref:`loading the animated model <loading-actors-and-animations>`
into Panda3D. This is what you will see in the models that are shipped with the
sample programs.

However, this is not strictly necessary, and an Egg file can be produced that
contains both the model and its associated animations.

Limitations
-----------

Egg files are less suitable as a format for storing whole scenes, because they
lack the ability to store information about light sources. However, if need be,
this information can still be passed from the modelling program via custom tags
added to dummy objects.

Sample Files
------------

There are a few models provided in the "models" folder of the Panda3D SDK
installation that can be used as example files or as temporary stand-ins.
Other models are provided with the sample programs available on the download
page.

In addition, here are two sources containing an assortment of models in the
Egg format:

https://www.panda3d.org/download/noversion/art-gallery.zip

https://www.alice.org/pandagallery/

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2
   :titlesonly:

   converting-to-egg
   converting-egg-to-bam
   parsing-and-generating-egg-files
   syntax
