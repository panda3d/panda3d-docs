.. _polygon-occluder-culling:

Polygon Occluder Culling
========================

Introduction
------------

One method of occlusion culling is to explicitly define a shape which will block
out objects behind it. This is called a *Polygon Occluder* and is represented in
Panda by the :class:`.OccluderNode`.

Creating an OccluderNode
------------------------

An occluder is defined by four vertices. The order of the vertices is important
as this defines which way the normal of the polygon is facing.

.. only:: python

   .. code-block:: python

      occluder = OccluderNode('my occluder', Point3(0, 0, 0), Point3(1, 0, 0),
                                             Point3(1, 1, 0), Point3(0, 1, 0))
      occluder_nodepath = render.attachNewNode(occluder)
      render.setOccluder(occluder_nodepath)

.. only:: cpp

   .. code-block:: cpp

      PT(OccluderNode) occluder = new OccluderNode("my occluder",
         LPoint3(0, 0, 0), LPoint3(1, 0, 0), LPoint3(1, 1, 0), LPoint3(0, 1, 0));
      NodePath occluder_nodepath = render.attach_new_node(occluder);
      render.set_occluder(occluder_nodepath);

It is hidden by default, but can be shown for debug purposes using the
:meth:`~.NodePath.show()` method on its NodePath. The occluder only needs to be
parented into the scene if you want to show it, or if it needs to move with an
object in the scene. Use the :meth:`~.NodePath.set_occluder()` method on any
NodePath to make the occluder active on that NodePath and its children. It is
much more efficient to call :meth:`~.NodePath.set_occluder()` on a parent node
with children as opposed to calling :meth:`~.NodePath.set_occluder()` on many
different nodes.

Occluder Configuration
----------------------

Besides the shape of the occluder, there are other settings which affect how the
occluder behaves. Use the :meth:`~.OccluderNode.set_double_sided()` method on
the OccluderNode to enable the occluder to work on both sides. This is desirable
for example if the occluder is placed inside of a wall. A double-sided occluder
is more efficient than creating two occluders with opposite normals. Use the
:meth:`~.OccluderNode.set_min_coverage()` method to ignore an occluder that
doesn't take up at least a certain amount of screen space.

General Occluder Advice
-----------------------

More is not always better. Occluders do have a cost, so use them sparingly where
they will make the biggest difference. If you have a lot of occluders, it might
help to evaluate your occluders every once in a while and only use the closest
ones. The optimal amount and configuration of occluders depends on the makeup of
your scene. Test different configurations and compare the frame rates.
