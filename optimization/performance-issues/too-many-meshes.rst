.. _too-many-meshes:

Too Many Meshes
===============

If you have too many nodes/meshes in your scene, this might result in slow
performance. You can check your Geom count in
:ref:`PStats <measuring-performance-with-pstats>`, or by calling
:meth:`.NodePath.analyze()` on your object or scene.

Panda3D provides a function to reduce the mesh count:
:meth:`.NodePath.flattenStrong()`.
This will reduce the NodePath to only one node. Be careful with this function:
Usage without care might cause your game to crash, since you will not be able to
move individual subnodes of a flattened node around anymore. Also note that
flattening your whole world like this is a bad idea, as you will break culling,
which will cause your whole world to be rendered even if your camera is
rendering only a small part of it. You will need to find a balance.

:meth:`.NodePath.flattenMedium()` and :meth:`~.NodePath.flattenLight()` are not
as rigorous as :meth:`~.NodePath.flattenStrong()`, but may be worth considering.

Though, if you have multiple independently-moving rigid nodes, the flattening
functions might not suit your needs, because, since the flattening functions
flatten everything to one node you won't be able to move individual sub-nodes
around. An alternative is
:ref:`the Rigid Body Combiner <the-rigid-body-combiner>`, which can combine
multiple nodes while you can still change the transforms on the sub-nodes.

If you are using the :ref:`GeoMipTerrain <geometrical-mipmapping>` for terrain
rendering, that might also result in a large mesh count. (You can check the
block count by calling ``terrain.getRoot().analyze()``.) If it is too high,
try increasing the block size, or enable AutoFlattening, which will reduce the
block count to only one. The autoflatten function was created because normally
you can't flatten a terrain using the normal flattenX methods, because this
will interfere with the GeoMipTerrain's updating system.
