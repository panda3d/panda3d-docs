.. _converting-to-egg:

Converting to Egg
=================

If a file format cannot be loaded directly by a supported plug-in, it needs to
be converted to a supported format first. This can be done using a conversion
utility or with a plug-in. Panda3D provides various tools and plug-ins that can
be used to convert a model to the Egg format.

.. contents::
   :local:

Autodesk Maya
-------------

Panda3D provides a series of utility programs for converting Maya models (.ma
or .mb) to Panda3D. One such utility exists for each supported version of Maya.
For example, the utility for Maya 2019 is called ``egg2maya2019.exe``.

Furthermore, a script is provided that can be used to export .egg files directly
from the Maya user interface.

For more information, see :ref:`converting-from-maya`.

Blender
-------

There are various community-contributed exporters available for exporting models
from Blender to Egg. For Blender versions 2.5x through 2.7x, the tool of choice
is YABEE:

https://github.com/09th/YABEE

For newer versions of Blender (2.8 and up), it is recommended to export via the
glTF format instead, see :ref:`converting-from-blender` for more information.

.. caution::

   There are some community-made ports of YABEE for newer versions of Blender
   floating around the internet. These ports are not officially supported as
   they are often tailored to the author's own purposes and may not produce the
   expected output in the general case.

Wavefront .obj
--------------

There is a tool provided with Panda3D called ``obj2egg`` which can convert
Wavefront .obj files to .egg. However, this tool is extremely limited and
does not support materials and textures. It is recommended to convert the .obj
file to another format first, or to load the .obj file directly into Panda3D
(using the Assimp plug-in that is provided by default).

Other Formats
-------------

There are several tools included with Panda that can convert various file
formats into egg file format:

* lwo2egg
* dxf2egg
* flt2egg
* vrml2egg
* x2egg

Note that Panda can load any of these file formats without conversion, doing so
causes the conversion to occur at runtime.

Also, be aware that many of these file formats are limited. Most do not include
bone or animation data. Some do not store normals. Currently the DirectX (.x)
format is the only one of these that stores bones, joints and animations.
