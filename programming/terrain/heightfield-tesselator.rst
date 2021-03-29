.. _heightfield-tesselator:

The Heightfield Tesselator
==========================

The HeightfieldTesselator converts a height field in the form of a greyscale
image into a scene consisting of a number of GeomNodes. The tesselation uses an
LOD algorithm. You supply a "focal point" (X,Y) which tells the tesselator where
the bulk of the detail should be concentrated. The intent is that as the player
walks around the terrain, you should occasionally move the focal point to
wherever the player is. You should not move the focal point every frame:
tesselation is not that fast. Also, changing the focal point may cause popping,
so it is best to minimize the number of changes. There are a number of
parameters that you can use to control tesselation, such as a target polygon
count, and a visibility radius.

The heightfield needs to be a multiple of 128 pixels in each dimension. It does
not need to be square, and it does not need to be a power of two. For example, a
384 x 640 heightfield is fine. Be aware that tesselation time is proportional to
heightfield area, so if you plan to use a size larger than about 512x512, it may
be desirable to benchmark.

Altering parameters, such as the poly count, the view radius, or the focal
point, does not alter any GeomNodes already generated. Parameter changes only
affect subsequently-generated GeomNodes. It is possible to cache many different
tesselations of the same terrain.


