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

https://github.com/Moguri/blend2bam

Blend2bam uses the panda3d-gltf package under the hood to convert to bam. If
this is installed you could also simply load .gltf files directly into Panda3D
as you would a bam or egg. It's still recommended to use blend2bam instead since
it uses default options that work well with Panda3D.

https://github.com/Moguri/panda3d-gltf

Option 2: The Export Plugins for Blender
----------------------------------------

Blender can export to glTF files without plugins, and a Python module called
panda3d-gltf can be used to load glTF files in Panda3D.
https://github.com/Moguri/panda3d-gltf

Also, there are several Blender plugins contributed by Panda3D users.

YABEE is an exporter for Blender 2.5, 2.6 and 2.7, but does not work with
Blender 2.80 at the moment of writing. It is documented and feature complete.
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

----

Chicken is the old and no longer updated, but documented and feature complete
exporter for Blender 2.4. It supports static meshes and armature animation,
materials, vertex colors, alpha textures, tags, object types, etc. It also has
advanced features such as automatic invocation of Panda tools (egg2bam,
egg-optchar and pview) and Motion Extraction. You can find it at
https://sourceforge.net/projects/chicken-export/

--------------

Another exporter for Blender 2.4 that only supports static meshes can be found
at http://xoomer.virgilio.it/glabro1/panda.html

Option 3: The "X" File format
-----------------------------

There exists a free plugin for Blender that can export "X" (DirectX native)
file format. Save the file from blender as an X file, then load it directly
into Panda3D, which can read X file format. Alternately, if you're concerned
about long load times (panda has to translate the file at load time), then
pre-convert the model from X to Egg to Bam using the conversion programs
supplied with Panda3D (x2egg, egg2bam).

Whenever you save a model in a non-native file format, you need to ask
yourself: "does this file format support everything I need?" For example, when
you save out a model in 3DS file format, you automatically lose all bone and
animation data, because the 3DS file format doesn't contain bone and animation
data. In the case of the X file format, you're in good shape: it's a fairly
powerful file format, supporting vertices and triangles, bones and animation.

Note however, when an animated X file is converted to egg, the resulting egg
file only plays the keyframes, but not whats supposed to be in between. For
example, an animation could exist that should spawn 200 frames, gets sized
down to about 40, and playback looks shakey. This shakeyness happens because
the X file format supports the concept of keyframes, with implicit frames
interpolated between them. The egg file format is explicit. An egg file must
give all of the frames of an animation, even the frames that appear between
"keyframes".

Therefore, a run of x2egg with an X file that omits a lot of frames between
keyframes, will product a shapekey animation. The only solution is to ensure
your X files are generated with all frames. Testing of different X file
exporters may be required.

Further, panda's native egg file format supports some esoteric things. For
example, it supports blend targets (morph animations) and motion path curves,
which are not supported by the X file format.

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
