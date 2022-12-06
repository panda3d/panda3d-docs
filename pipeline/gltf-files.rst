.. _gltf-files:

glTF Files
==========

The glTF format is the industry standard file format for delivering 3D assets
(models and scenes) to 3D engines. It is an open standard maintained by the
Khronos Group, with contributors across the industry. It is widely supported as
an export format by 3D modelling programs and an import format by game engines.

The format is based around JSON, a common text-based data interchange format.
Like .egg, a file with the .gltf extension can be inspected using a text
editor, or it can be programmatically manipulated by any JSON parsing library.
There is also a binary variant of the format, .glb, which is used if you wish to
pack the textual JSON tree together with any external binary data into the same
file efficiently.

At the time of writing, there are two versions of the glTF standard, version 1.0
and version 2.0, with substantial differences between them. It is recommended to
use version 2.0, which is much more prevalent than 1.0.

A particular advantage of this format is its support for PBR (physically-based
rendering) materials, which are better supported with glTF than with Egg,
although at the moment you will need a custom shader or a third-party add-on
such as `panda3d-simplepbr <https://github.com/Moguri/panda3d-simplepbr>`__ to
render these materials correctly. glTF is also the format of choice when
exporting models from Blender 2.80 and above, as explained
:ref:`here <converting-from-blender>`.

.. contents::
   :local:

Installing the Plug-In
----------------------

There are two ways to load glTF files. By default, Panda3D will load glTF files
via the :ref:`Assimp plug-in <assimp-loader>`, but the quality of its converter
is not very good. Instead, there is a high quality third-party plug-in for this
purpose called `panda3d-gltf <https://github.com/Moguri/panda3d-gltf>`__.
It can be installed by typing the following pip command::

   python -m pip install -U panda3d-gltf

.. only:: python

   After installing this plug-in, no extra steps are needed.
   You can simply pass any filename with a .gltf extension to the
   :py:meth:`loader.loadModel() <direct.showbase.Loader.Loader.loadModel>` call
   and it will be loaded using this plug-in. Of course, Panda's model cache
   ensures that the conversion step is only run the first time a particular
   model is loaded, or whenever it is modified on disk.

.. only:: cpp

   The plug-in can register itself with Panda's loader system, but since it is
   written in Python, this functionality is not available to C++ applications.
   You will need to use the included ``gltf2bam`` utility to convert the glTF
   models to .bam first.

Previewing glTF Models
----------------------

Since the :ref:`pview <pview>` utility is written in C++, it cannot take
advantage of the panda3d-gltf plug-in. If you try to load a glTF model in pview,
it will always be loaded via the Assimp plug-in, which is usually not what you
want.

You should instead use the ``gltf-viewer`` utility that is included with
panda3d-gltf, since it ensures that the panda3d-gltf plug-in is being used.
It also includes a default PBR shader that is able to render any PBR materials
that are specified by the glTF asset.

Embedding Binary Data
---------------------

While the glTF format is a text-based format, some data that is part of a model
is required to be in a binary form. This concerns such things as vertex and
animation data, which would use considerably more space if it were written out
a text form. The glTF standard provides three ways to store this binary data:

Separate .bin file
   The binary data can be stored in a separate .bin file that is referred to by
   the main .gltf file. This is the most typical approach, and will work for
   most purposes, but having a separate .bin file can be inconvenient for some.

Embedded
   The binary data is encoded as base64 and embedded in the .gltf file.
   This method keeps the JSON structure of the file intact, at the cost of a
   (roughly) 33 % increase in file size due to the inefficiency of base64.

Binary glTF (.glb)
   Instead of a .gltf file, both the JSON and the binary data are packed
   together into a .glb file. This is a more efficient manner of embedding
   binary data, but the file is no longer human-readable.

The choice of these options is usually available in the exporter plug-in for
the modelling program. Which option you choose is up to you; all three are
supported by Panda3D.

Extensions
----------

The glTF format is defined as an extensible format. A glTF asset can opt-in to
a number of externally defined extensions that add additional functionality not
provided by the base standard.

Both the panda3d-gltf and Assimp plug-ins support the following extensions,
among others:

- `KHR_lights_punctual <https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos/KHR_lights_punctual>`__ - adds support for light sources
- `KHR_texture_transform <https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos/KHR_texture_transform>`__ - adds support for :ref:`texture transformations <texture-transforms>`
- `KHR_materials_ior <https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos/KHR_materials_ior>`__ - makes it possible to specify the index of refraction of a material

Tangent and Binormal Vectors
----------------------------

glTF files do not contain binormal vectors, even if normal mapping is used.
This may be an issue when using custom shaders that expect a binormal vector to
be present for normal mapping. Instead, binormal vectors are intended to be
derived from the cross product of the normal and tangent vectors.

The cross product is not sufficient to indicate the direction of the binormal
vector, so the tangent is stored as a 4-component value, with the w component
indicating the sign of the binormal vector. This component always contains
either the value 1 or -1.

With this information, the binormal vector can be reconstructed as follows in
the vertex shader:

.. code-block:: glsl

   binormal = cross(p3d_Normal, p3d_Tangent.xyz) * p3d_Tangent.w

Distributing glTF Models
------------------------

.. only:: python

   When :ref:`building your application <distribution>`, the plug-ins
   responsible for loading glTF models are not distributed along by default.
   It is much better to convert the model to the optimized .bam format for this
   purpose. As of Panda3D 1.10.13, this can be done automatically, by adding the
   extensions to the ``bam_model_extensions`` list:

   .. code-block:: python

      options = {
          'build_apps': {
              ...
              'include_patterns': [
                  # Make sure the gltf/glb file is being found
                  '**/*.gltf',
                  '**/*.glb',
                  '**/*.jpg',
                  ...
              ],
              # Models with these extensions are converted to .bam automatically
              'bam_model_extensions': ['.gltf', '.glb', '.egg'],
              ...

.. only:: cpp

   To avoid having to include the plug-ins with a distributed application, use
   the gltf2bam utility (provided with panda3d-gltf) or write a script to
   convert the model to .bam using :meth:`.NodePath.write_bam_file()` and ship
   the converted .bam file instead of the original source file.

External Links
--------------

For more information on panda3d-gltf, or to report issues, see the project's
`GitHub page <https://github.com/Moguri/panda3d-gltf>`__.

The full text of the glTF specification can be found on the Khronos website:

https://registry.khronos.org/glTF/specs/2.0/glTF-2.0.html

Sample models in the glTF format are available from this GitHub repository:

https://github.com/KhronosGroup/glTF-Sample-Models
