.. _collision-system-misuse:

Collision System Misuse
=======================

The collision system can detect most types of collisions very rapidly. However,
it is possible to construct situations that the collision detection system just
can't handle. This page lists a few of these things, and how to improve them.

Colliding with Visible Geometry
-------------------------------

Panda3D supports calculating collisions against visible scene geometry. However,
this method is not at all efficient. It is far more efficient to construct
specific :ref:`collision-solids` to represent the various objects in the scene.
Even collision geometry constructed from :class:`.CollisionPolygon` objects is
significantly more efficient than colliding against the renderable geometry!

Various exporters are able to automatically generate optimized collision
geometry during the export process. Consult the documentation for your exporter
to find out how to do this.

When you have constructed the optimized collision geometry, don't forget to
disable checking for collision against the visible geometry, by setting the
:ref:`collision-bitmasks` appropriately.

Lack of Hierarchy
-----------------

A naive approach for exporting collisions for a large scene is just to put all
of the collision solids under a single :class:`.CollisionNode`, or perhaps many
:class:`.CollisionNode` objects under a single parent node.

This is very inefficient for a large number of solids. Panda3D will need to test
for collisions against every single object in a row.

It is far more efficient to structure your collision scene in the form of a
*quadtree* or *octree*, or even a *binary tree*, grouping close collision nodes
together under a common parent node. This allows Panda3D to test against the
parent node, and only proceed to test the child nodes if this passes.

.. only:: python

   There is a method on the :class:`.NodePath` class to automate the process of
   partitioning the scene for optimal collision checking:

   .. code-block:: python

      model.subdivideCollisions(4)

   The argument is the number of solids to put in the leaves of the hierarchy.
   You can experiment with this number to find the value that gives the best
   performance.

Excessive Detail
----------------

If the collision geometry is constructed from the version of the mesh that is
used for rendering, it is possible that there are so many triangles in the mesh
that it is slow to test against. In these situations, it is recommended to
instead construct a simplified version of the mesh. Ideally, this simplified
mesh consists of :ref:`collision-solids` such as spheres, boxes and capsules,
but in some situations it is necessary to build it up from individual polygons.
A low-poly version of the mesh can then be used instead, either by constructing
it manually or by using an automatic quality reduction algorithm (such as the
Decimate modifier in Blender) to create a collision mesh with fewer polygons.
