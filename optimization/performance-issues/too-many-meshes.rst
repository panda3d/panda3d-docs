.. _too-many-meshes:

Too Many Meshes
===============

If a scene needs to be rendered and has multiple nodes, Panda has to send each
node to the graphics hardware as a separate batch of polygons (because the nodes
might move independently, or have different state changes on them). Modern
graphics hardware hasn't made any improvements recently in handling large
numbers of batches, just in handling large numbers of polygons per batch. So if
a scene is composed of a large number of nodes with a small number of polygons
per node, the frame rate will suffer. This problem is not specific to Panda; any
graphics engine will have the same problem. The problem is due to the nature of
the PC and the AGP bus.

For example, though your graphics card may claim it can easily handle a million
polygons, this may be true in practice only if all of those polygons are sent in
one batch--that is, just a single :ref:`geom`. If, however, your scene consists
of 1,000 nodes with 1,000 polygons each, it may not have nearly as good a frame
rate.

You can check your Geom count in
:ref:`PStats <measuring-performance-with-pstats>`, or by calling
:meth:`.NodePath.analyze()` on your object or scene. The former method will tell
you how many Geoms are actually being sent to the graphics card, whereas the
latter will count all the Geoms that exist in this part of the scene graph, even
those that are out of view.

Static Objects
--------------

If a scene is composed of many static objects, for example boxes, and the intent
of all of these boxes to just sit around and be part of the background, or to
move as a single unit, they can flattened together into a handful of nodes (or
even one node). To do this, parent them all to the same node, and use:

.. only:: python

   .. code-block:: python

      node.flattenStrong()

.. only:: cpp

   .. code-block:: cpp

      node.flatten_strong();

This will cause Panda to try to reduce the NodePath to as few nodes as possible.
But be careful with this function:
Usage without care might cause your game to crash, since you may not be able to
move individual subnodes of a flattened node around anymore. Also note that
flattening your whole world like this is a bad idea, as you will break culling,
which will cause your whole world to be rendered even if your camera is
rendering only a small part of it. You will need to find a balance.

:meth:`.NodePath.flatten_medium()` and :meth:`~.NodePath.flatten_light()` are
not as rigorous as :meth:`~.NodePath.flatten_strong()`, but may be worth
considering.

By default, Panda3D prevents separate models from being flattened together, so
that they can still be moved independently.
If you wish to do this anyway, it is necessary to first call
:meth:`~.NodePath.clear_model_nodes()` to allow a model to be combined with
other models.

You should call :meth:`~.NodePath.analyze()` again after performing the flatten
operation, to see how effective it was. There are some scenarios in which
Panda3D cannot flatten together multiple models effectively, for example because
they all have a unique texture applied, or contain other unique state changes
that prevent flattening. See :ref:`too-many-state-changes` for more details.

Independently Moving Objects
----------------------------

Flattening a node will cause that scene graph to become one static unit. This
means that you will no longer be able to independently manipulate parts of a
flattened scene anymore.

You can still flatten the nodes that need to move individually, or protect them
using ModelNodes (as Panda does by default to individually loaded models), but
this may not be sufficient if there are too many nodes that move independently.

An alternative is :ref:`the Rigid Body Combiner <the-rigid-body-combiner>`,
which can combine multiple nodes while you can still change the transforms on
the sub-nodes. This still combines the nodes into a single mesh as
:meth:`~.NodePath.flatten_strong()` does, but uses the vertex animation system
so that the individual nodes can still be moved. However, this method can come
with its own performance caveats, creating strain on the animation system.
It is intended to be used as a last resort.

Terrain
-------

If you are using the :ref:`GeoMipTerrain <geometrical-mipmapping>` for terrain
rendering, that might also result in a large mesh count. (You can check the
block count by calling ``terrain.getRoot().analyze()``.) If it is too high,
try increasing the block size, or enable AutoFlattening, which will reduce the
block count to only one. The autoflatten function was created because normally
you can't flatten a terrain using the normal flattenX methods, because this
will interfere with the GeoMipTerrain's updating system.
