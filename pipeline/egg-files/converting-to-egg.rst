.. _converting-to-egg:

Converting to Egg
=================

If a file format cannot be loaded directly by a supported loader plug-in, it
needs to be converted to a supported format first. This can be done using a
conversion utility or with a plug-in for the modelling program. Panda3D provides
various such tools and plug-ins for converting models to the Egg format.

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

COLLADA (.dae)
--------------

COLLADA is a standardized interchange file format that can be exported by
many different authoring tools. These files have the .dae or .zae extension.

Panda3D ships a tool called ``dae2egg`` that can be used to convert these models
to the Egg format. However, it is based on the FCollada library, which has been
discontinued, so it is possible that this tool will be removed from a future
version of Panda3D. There are currently no plans to rewrite this tool, as the
games industry has moved on to prefer the newer glTF format.

Wavefront .obj
--------------

There is a tool provided with Panda3D called ``obj2egg`` which can convert
Wavefront .obj files to .egg. However, this tool is extremely limited and
does not support scene hierarchy, materials, or textures, among other things.
It is recommended to convert the .obj file to another format first, or to load
the .obj file directly into Panda3D using the
:ref:`Assimp plug-in <assimp-loader>`.

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
