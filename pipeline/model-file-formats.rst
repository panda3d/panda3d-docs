.. _supported-model-formats:

Supported Model Formats
=======================

Panda3D contains an extensible plug-in system for loading model files. These
plug-ins enable Panda3D to load models in a variety of formats, without
requiring an explicit conversion step. This page lists the formats and plug-ins
available for loading models into Panda3D.

.. contents::
   :local:

BAM Format
----------

The most powerful file format that Panda3D supports is BAM. This is a direct
binary representation of the internal object structure of Panda3D. As such it
supports almost all of the objects you can create in Panda3D, and any model can
be converted to BAM without loss of information. You can also save any scene
graph structure in Panda3D back to a BAM file using the
:meth:`~.NodePath.write_bam_file()` call.

But because BAM files are a reflection of the internal memory structure of
Panda3D, it's theoretically possible for a BAM file created using one version
of Panda3D to no longer work in a future version of Panda3D. Therefore, if you
choose to work directly with BAM files, you should make sure to always preserve
the source assets and information about the pipeline so that you can reconvert
the model as needed.

Because it is such an efficient format, it is very well-suited for shipping
with a copy of a game for end-users. This allows the finished game to load
models very quickly, and the plug-ins for loading models can be excluded.
This format is very well-suited for shipping with a copy of a game for
end-users, with the further advantage that the additional plug-ins do not need
to be included with the installed game. The distribution tools therefore
automatically convert files to the BAM format.

With a few exceptions, most tools and plug-ins do not directly export to the
BAM format. To create a BAM file manually, you can use a tool like
:ref:`egg2bam <converting-egg-to-bam>`, or you can simply load or create the
model in Panda3D and use the :meth:`~.NodePath.write_bam_file()` method.

Egg Format
----------

The second-best-supported file format in Panda3D is the Egg format, a text-based
format that is unique to Panda3D. There are many tools available to manipulate
Egg files, and you can even open an Egg file in a text editor to see what it
contains. See the :ref:`egg-files` section for more detailed information about
this format.

An Egg file can contain static geometry, but it can also contain information
for animating the model, as well as information about the model's material, ie.
what color the material has, and how this color changes under the influence of
lighting). However, unlike BAM, it cannot represent all of the things that are
possible in Panda3D. For instance, light sources are not represented.

Panda3D provides various tools for
:ref:`converting models to the Egg format <converting-to-egg>`.
Furthermore, there are exporter plug-ins for various modelling packages that
are able to produce Egg files.

The plug-in for loading .egg files is provided with Panda3D out of the box.
Panda3D also provides an API for manipulating Egg files programmatically.
The :class:`.EggData` class is the main entry point of this API.

glTF Plug-In
------------

An increasingly commonly used format for 3D models is the glTF format. This is a
standard format that is very widely supported by many modelling suites. There
are also many models available on the internet in this format.

A particular advantage of this format is its support for PBR (physically-based
rendering) materials, which are better supported with glTF than with Egg. It is
also the format of choice when exporting models from newer versions of Blender.

In the future, Panda3D will contain native support for loading glTF models.
Until then, there is a high quality third party plug-in that can be installed
that can be used to load glTF models:

https://github.com/Moguri/panda3d-gltf

.. only:: python

   After installing this plug-in using the "pip" package manager, no extra steps
   are needed. You can simply give Panda a path to a file with a .gltf extension
   and it will load via this plug-in.

.. caution::

   You may notice Panda3D will still load .gltf files if you do not install this
   plug-in. That is because Panda3D will try to load the model via the Assimp
   plug-in instead. However, it is recommended to use panda3d-gltf instead, as
   it contains a more well-tested and better-maintained converter.

Assimp Plug-In
--------------

Panda3D also provides a plug-in out of the box that integrates with the Assimp
library. This third-party library supports a broad range of different formats,
such as .obj, .stl and .dxf, allowing them to be loaded into Panda3D without a
conversion step.

The full list of supported formats is available on this page:

https://assimp-docs.readthedocs.io/en/latest/about/introduction.html

The quality of support varies substantially from format to format, and it is
preferred to use a more specific plug-in if one is available for that format.
For example, Assimp includes support for .gltf files, but the panda3d-gltf
plug-in (mentioned above) is considered to be higher-quality.

Please note that while skeletal animations are supported, morph targets (also
known as shape keys) are not currently supported by the Assimp plug-in.

.. caution::

   Models loaded with the Assimp plug-in may appear rotated around the X axis,
   due to the fact that Assimp uses a Y-up coordinate system whereas Panda3D
   uses a Z-up coordinate system. A future version of Panda3D will correct this
   automatically, but for now, you will need to manually rotate your models.

The following Config.prc settings can be used to control the behavior of the
Assimp loader. Note that you will need to clear the model cache after changing
one of these variables for these changes to take effect.

.. list-table::
   :widths: 30 5 65
   :header-rows: 1

   * - Variable name
     - Default
     - Description
   * - notify-level-assimp
     - ``warning``
     - Sets the verbosity of debug messages (spam, debug, info, warning, error)
   * - assimp-calc-tangent-space
     - ``false``
     - Calculates tangent and binormal vectors, useful for normal mapping.
   * - assimp-join-identical-vertices
     - ``true``
     - Merges duplicate vertices. Set this to false if you want each vertex to
       only be in use on one triangle.
   * - assimp-improve-cache-locality
     - ``true``
     - Improves rendering performance of the loaded meshes by reordering
       triangles for better vertex cache locality.  Set this to false if you
       need geometry to be loaded in the exact order that it was specified in
       the file, or to improve load performance.
   * - assimp-remove-redundant-materials
     - ``true``
     - Removes redundant/unreferenced materials from assets.
   * - assimp-fix-infacing-normals
     - ``false``
     - Determines which normal vectors are facing inward and inverts them so
       that they are facing outward.
   * - assimp-optimize-meshes
     - ``true``
     - Reduces the number of draw calls by unifying geometry with the same
       materials. Especially effective in conjunction with assimp-optimize-graph
       and assimp-remove-redundant-materials.
   * - assimp-optimize-graph
     - ``false``
     - Optimizes the scene geometry by flattening the scene hierarchy. This is
       very efficient (combined with assimp-optimize-meshes), but it may result
       the hierarchy to become lost, so it is disabled by default.
   * - assimp-flip-winding-order
     - ``false``
     - Set this true to flip the winding order of all loaded geometry.
   * - assimp-gen-normals
     - ``false``
     - Set this true to generate normals (if absent from file) on import.
   * - assimp-smooth-normal-angle
     - ``0.0``
     - Set this to anything other than 0.0 in degrees (so 180.0 is PI) to
       specify the maximum angle that may be between two face normals at the
       same vertex position that are smoothed together. Sometimes referred to
       as 'crease angle'. Only has effect if assimp-gen-normals is set to true
       and the file does not contain normals. Note that you may need to clear
       the model-cache after changing this.

Other Formats
-------------

Other file formats need to be converted first to a supported format. Panda3D
provides various utilities that can be used to
:ref:`convert models to the Egg format <converting-to-egg>`.

For several formats for which Panda3D ships with a to-egg conversion tool,
Panda3D can automatically do the step of converting the model to .egg on load.
For example, Panda3D ships with a flt2egg converter, which can convert
OpenFlight models to the Egg format. If you try to load a .flt file, Panda3D
will implicitly invoke flt2egg behind the scenes.

The formats supported by this plug-in are OpenFlight (.flt), LightWave (.lwo),
AutoCAD (.dxf), VRML (.wrl), Direct X (.x), and Wavefront OBJ (.obj).
However, note that some of these formats can be loaded by the Assimp loader, in
which case this plug-in is only used if the Assimp plug-in is not available.
Also note that the obj2egg converter is extremely limited and does not support
materials or textures, so it is not recommended to load .obj files via this
route.

Supported Feature Table
-----------------------

This table lists the most commonly used supported file formats and the various
features that are supported by these formats.

===================== ==== ==== ===== ==== ==== ===
\                     .bam .egg .gltf .obj .dae .x
===================== ==== ==== ===== ==== ==== ===
Node hierarchy        ✔️   ✔️   ✔️    ✔️   ✔️   ✔️
Custom object tags    ✔️   ✔️   ✔️    ❌   ❌   ❌
**Geometry**
---------------------------------------------------
Triangle meshes       ✔️   ✔️   ✔️    ✔️   ✔️   ✔️
Higher-order polygons ❌   ✔️   ✔️    ❌   ✔️   ✔️
Lines and segments    ✔️   ✔️   ✔️    ✔️   ✔️   ❌
Vertex colors         ✔️   ✔️   ✔️    ✔️   ✔️   ✔️
**Materials and Textures**
---------------------------------------------------
Basic materials       ✔️   ✔️   ✔️    ✔️   ✔️   ✔️
Basic textures        ✔️   ✔️   ✔️    ✔️   ✔️   ✔️
Texture blending      ✔️   ✔️   ❌    ❌   ❌   ❌
Gloss maps            ✔️   ✔️   ❌    ❌   ✔️   ❌
Normal maps           ✔️   ✔️   ✔️    ❌   ✔️   ❌
Height maps           ✔️   ✔️   ❌    ✔️   ❌   ❌
Emission maps         ✔️   ✔️   ✔️    ✔️   ✔️   ❌
Roughness/metal maps  ✔️   ❌   ✔️    ✔️   ❌   ❌
Texcoord transforms   ✔️   ✔️   ✔️    ❌   ❌   ❌
**Animation**
---------------------------------------------------
Object animations     ❌   ❌   ❌    ❌   ❌   ❌
Skeletal animations   ✔️   ✔️   ✔️    ❌   ✔️   ✔️
Morph targets         ✔️   ✔️   ✔️    ❌   ❌   ❌
Split animation files ✔️   ✔️   ❌    ❌   ❌   ❌
**Other**
---------------------------------------------------
Collision shapes      ✔️   ✔️   ❌    ❌   ❌   ❌
Light sources         ✔️   ❌   ✔️    ❌   ✔️   ❌
Level of detail (LOD) ✔️   ✔️   ❌    ❌   ❌   ❌
External references   ❌   ✔️   ❌    ❌   ❌   ❌
NURBS curves          ❌   ✔️   ❌    ❌   ❌   ❌
Shaders               ❌   ❌   ❌    ❌   ❌   ❌
===================== ==== ==== ===== ==== ==== ===
