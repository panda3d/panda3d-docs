.. _converting-from-blender:

Converting from Blender
=======================

Currently, there are several ways to get data from Blender into Panda3D. The
most popular has always been the YABEE exporter, but it is no longer recommended
as it is not compatible with the latest version of Blender, 2.80.  Instead, we
recommend the use of blend2bam, or to export to the glTF 2.0 format.

Option 1: Blend2bam
-------------------

Blend2bam is a CLI command that converts blend files into bam files. By default
it uses Blender's built-in glTF exporter for version 2.80 and up, a custom glTF
exporter for older versions of Blender and can even be set up to use YABEE.

You can simply add this to your Panda3D installation using pip::

   python -m pip install panda3d-blend2bam

To convert a model, enter the blend2bam command on the command-line::

   blend2bam myfile.blend myfile.bam

For more information, and issue reports, visit the GitHub page for blend2bam:

https://github.com/Moguri/blend2bam

For best reproduction of the Blender materials, you can use the simplepbr
package, which provides a set of shaders that are designed to approximate the
Principled BSDF shading model used in Blender:

https://github.com/Moguri/panda3d-simplepbr

Option 2: The Export Plugins for Blender
----------------------------------------

Blender (2.80 and above) can export to glTF files without plugins, and a
Python module called panda3d-gltf can be used to load glTF files in Panda3D.

Blend2bam uses the panda3d-gltf package under the hood to convert to bam. It's
still recommended to use blend2bam instead since it uses default options that
work well with Panda3D.

https://github.com/Moguri/panda3d-gltf

Also, there are several Blender plugins contributed by Panda3D users.

YABEE is an exporter for Blender 2.5x, 2.6x and 2.7x, but does not work with
Blender 2.8x at the moment of writing. It is documented and feature complete.
YABEE can export:

-  Meshes
-  UV layers
-  Materials and textures (Partially)
-  Armature (skeleton) animation
-  ShapeKeys (morph) animation
-  <Tag> and Collision options export through Blender's "Game logic" -> "Properties"
-  Non-cyclic NURBS Curves

https://github.com/09th/YABEE

If you observe any problem, or find a bug, you can report it on official
thread that can be found here:
https://discourse.panda3d.org/t/yet-another-blender-egg-exporter-yabee/10702

Why do my colors look different in Panda3D?
-------------------------------------------

It is important to note that Blender uses a linear workflow, meaning all colors
are converted from the sRGB color encoding to the "linearized sRGB" color space
before being used for lighting and blending.  After the render process, the
colors in the framebuffer are converted back to sRGB for display on the screen.

Panda3D by default does not perform any color conversion, meaning that all the
input colors are rendered as-is into the window.  However, this can mean that
colors defined in Blender will not appear the same way in Panda3D, as they have
not undergone the same color conversion as Blender performs.

If you use blend2bam in conjunction with the panda3d-simplepbr package, this
will be handled for you automatically.  Otherwise, you will need to configure
Panda3D to also use the linear workflow.  This requires two steps:

#. Set your textures to use the ``Texture.F_srgb`` or ``Texture.F_srgb_alpha``
   texture format, which automatically linearizes the colors before they are
   used in the rendering process.
#. Tell Panda3D to ask the graphics driver for an "sRGB framebuffer", which
   causes the GPU to automatically convert colors back to sRGB before they are
   displayed on the monitor.  This is achieved by enabling ``framebuffer-srgb``
   in Config.prc, or by adding a post-processing filter as described in
   :ref:`common-image-filters`.
