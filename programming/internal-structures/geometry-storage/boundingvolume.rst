.. _boundingvolume:

BoundingVolume
==============

A :class:`~.BoundingVolume` is a solid enclosing all the geometry of a node and
its children that is used for culling and collision detection.
(If the BoundingVolume for a node is not visible, there is no need to render
that node.) Panda will generate "bounds" for each node automatically by creating
bounding volumes.

Panda defines the "bounds" of a node to be a geometric bounding volume, of an
arbitrary shape (but usually a sphere) that is no smaller than its enclosed
geometry.  The :meth:`~.PandaNode.get_bounds()` method returns an acceptable
bounding volume. It is indeed no smaller than the enclosed geometry. This makes
it suitable for use in culling operations and so on. To check the size of the
bounding volume, use :meth:`~.NodePath.show_bounds()`.

Note that this BoundingVolume is not the smallest possible. For instance, a
sphere of radius 1 has a :class:`.BoundingSphere` with radius 1.73205. Panda
doesn't bother going through all the trouble it would take to compute a tight
spherical bounds, because the loose bounds that it computes is good enough for
Panda's needs. The extra performance gain you'd get for having a tighter culling
bounds isn't worth the effort it would take to compute it.

Although it doesn't use it, Panda can create a tighter bounding box. This
"tight" bounding box is the smallest axis-aligned box that is no smaller than
its enclosed geometry. Thus, it satisfies its definition as a "tight" bounds,
because you will not find a tighter bounding volume that is also a box. You
can retrieve the bounding box using the :meth:`~.NodePath.get_tight_bounds()`
method. This box can be shown with :meth:`~.NodePath.show_tight_bounds()`.

Further tweaking of the bounding volume used must be done manually

-  If all you care about is Panda's usage of bounding boxes, you can create a
   BoundingVolume for the node you want and tell Panda to use that one with
   :meth:`set_final(1) <.PandaNode.set_final>`.

   .. only:: python

      .. code-block:: python

         node.setBounds(BoundingVolume(...))
         node.final = True

   .. only:: cpp

      .. code-block:: cpp

         node->set_bounds(new BoundingVolume(...));
         node->set_final(true);

   This will tell Panda to stop calculating bounds and use the one you gave
   it instead.

-  If you want to have a node with a manual bounding box set for your own
   nefarious purposes, set the bounds at the bottom: on the :class:`.Geom`
   within a :class:`.GeomNode`. This will propagate upwards, assuming there are
   no other nodes with bounding volumes above it.
