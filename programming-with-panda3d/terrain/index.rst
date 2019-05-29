.. _terrain:

Terrain
=======

Panda3D also provides classes for terrain generation. Those classes take a
height field image, and generate visible geometry from the provided height
field.

If you work with very large terrains, the renderer may not be able to handle
such a great amount of triangles. To solve that issue, Panda3D provides LOD
(Level of Detail), this means that it will generate the terrain at high
quality near the focal point (which is usually the camera), but will provide
lower quality terrain - that is, less triangles - because those far away parts
are not as much visible as the closer parts.

Panda3D provides two classes for terrain generation and LOD handling:

-  The :ref:`HeightfieldTesselator <the-heightfield-tesselator>`. This class
   can take a grayscale height field image and generate a terrain. It uses a
   linear LOD system, and, of course, because when the camera moves away from
   the focal point, the terrain needs to be regenerated to 'focus' on the new
   focal point. On extremely large terrains, this might lead to complications,
   because regenerating the entire terrain takes time, and the player might
   experience some lag when it is regenerated. That is why this class is not
   very suitable for extremely large terrains.
-  The :ref:`GeoMipTerrain <geometrical-mipmapping>`, formerly known as PGMM.
   This is a community-contributed terrain system and has been included since
   Panda3D 1.5.1. This algorithm takes a height field and also converts it
   into geometry, but it splits the terrain up in smaller chunks, so when the
   focal point changes, not all chunks have to be regenerated. This is to
   prevent lagging when the focal point moves. For smaller terrains, however,
   you might not need such extensive terrain calculations, and use the
   HeightfieldTesselator instead.

The GeoMipTerrain also provides a way to generate terrain bruteforce, that
means without LOD and at full quality.

Various other terrain generators have been contributed by the community:

-  `SoarX <https://www.panda3d.org/forums/viewtopic.php?t=2265>`__
-  `chombee's terrain
   renderer <https://www.panda3d.org/forums/viewtopic.php?t=1200>`__
-  `snaptotheterrain <https://www.panda3d.org/forums/viewtopic.php?t=4408>`__


.. toctree::
   :maxdepth: 2

   the-heightfield-tesselator
   geometrical-mipmapping
