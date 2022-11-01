.. _collision-solids:

Collision Solids
================

The CollisionSolid is the fundamental object of the collision system.
CollisionSolids represent special invisible geometry that is created solely for
the purpose of performing collision tests; these CollisionSolids are stored in
the scene graph alongside the normal visible geometry.

The CollisionSolids are specifically optimized for performing collision tests
quickly. Collisions can be performed against visible geometry as well, but this
is more expensive since visible geometry is not optimized for this sort of
thing.

You can create CollisionSolids interactively in program code, or you can
construct them in your modeling package and load them up from an egg or bam file
along with the rest of your scene.

When you create a CollisionSolid interactively, you must also create a
CollisionNode to hold the solid. (When you load your CollisionSolids in from an
egg file, the CollisionNodes are created for you.) Often, a CollisionNode will
be used to hold only one solid, but in fact a CollisionNode can contain any
number of solids, and this is sometimes a useful optimization, especially if you
have several solids that always move together as a unit.

.. only:: python

   .. code-block:: python

      cs = CollisionSphere(0, 0, 0, 1)
      cnodePath = avatar.attachNewNode(CollisionNode('cnode'))
      cnodePath.node().addSolid(cs)

.. only:: cpp

   .. code-block:: cpp

      PT(CollisionSphere) cs = new CollisionSphere();
      cSphere_node= new CollisionNode("Sphere");
      cSphere_node->add_solid(cs);

CollisionNodes are hidden by default, but they may be shown for debugging
purposes:

.. only:: python

   .. code-block:: python

      cnodePath.show()

.. only:: cpp

   .. code-block:: cpp

      cSphere_node->show();

.. note::

   Be aware that the collision algorithm has only limited awareness of scaling
   transforms applied to CollisionSolids. This particularly applies to non-
   uniform scales, ie. when the X, Y and Z components of a scale transform are
   not all the same. If unequal scaling is applied between a "from" collider and
   an "into" collider, unexpected results may occur. In general, strive to have
   as few scaling transforms applied to your collision solids as possible.

There are several kinds of CollisionSolids available.

CollisionSphere
---------------

The sphere is the workhorse of the collision system. Spheres are the fastest
primitives for any collision calculation; and the sphere calculation is
particularly robust. If your object is even vaguely spherical, consider wrapping
a sphere around it.

Also, a sphere is a particularly good choice for use as a "from" object, because
a sphere can reliably be tested for collision with most of the other solid
types. The "from" objects are the objects that are considered the active objects
in the world; see :ref:`collision-traversers`. A sphere is usually the best
choice to put around the player's avatar, for instance. The sphere also makes a
good "into" object; it is the only object type that is a good choice for both
"from" and "into" objects.

A sphere is defined in terms of a center and a radius. Note that, like any
object, the sphere's coordinates are defined in the sphere's own coordinate
space, so that often the center is (0, 0, 0).

.. code-block:: python

   sphere = CollisionSphere(cx, cy, cz, radius)

CollisionCapsule
----------------

A "capsule" is a cylinder with hemispherical endcaps, also known as a
spherocylinder. Note that before Panda3D 1.10, this shape was called
"CollisionTube", and this name remains as an alias for backward compatibility.

The capsule is good as an "into" object, for objects that are largely
cylindrical. It can also be used as a "from" object, but keep in mind that it
can be significantly more expensive to use a capsule in tests than a sphere.

.. image:: tube.jpg

A capsule is defined with its two endpoints, and the cylindrical radius.

.. code-block:: python

   capsule = CollisionCapsule(ax, ay, az, bx, by, bz, radius)

CollisionInvSphere
------------------

The inverse sphere is a special-purpose solid that is rarely used, but
occasionally it is very useful. It is an inside-out sphere: the solid part of
the sphere is on the outside. Any object that is on the outside of the sphere is
considered to be colliding with it; any object on the inside is not colliding.

Think of the inverse sphere as a solid mass that fills the whole universe in
all directions, except for a bubble of space in the middle. It's useful for
constraining an object within a particular space, since nothing can get out of
an inverse sphere.

.. code-block:: python

   inv = CollisionInvSphere(cx, cy, cz, radius)

CollisionPlane
--------------

The CollisionPlane is an infinite plane extending in all directions. It is not
often used, but it can be useful in certain cases, for instance as a trigger
placed below the ground to detect when an avatar has accidentally slipped
through a crack in the world. You can also build a box out of six planes to keep
objects perfectly constrained within a rectangular region, similar to an inverse
sphere; such a box is much more reliable than one constructed of six polygons.

The plane actually divides the universe into two spaces: the space behind the
plane, which is all considered solid, and the space in front of the plane, which
is all empty. Thus, if an object is anywhere behind a plane, no matter how far,
it is considered to be intersecting the plane.

Although it can only be used as an "into" solid, it is the most reliable of the
"into" solids; tests are implemented for every "from" solid, and since it
extends out infinitely, there is no possibility of glitching through it. This
makes it an excellent choice for a ground plane in games where the ground is
mostly level.

A CollisionPlane is constructed using a Panda3D Plane object, which itself has
a number of constructors, including the A, B, C, D plane equation, or a list
of three points, or a point and a normal.

.. code-block:: python

   plane = CollisionPlane(Plane(Vec3(0, 0, 1), Point3(0, 0, 0)))

CollisionPolygon
----------------

A CollisionPolygon is the most general of the collision solids, since it is
easy to model any shape with polygons (especially using a modeling package).
However, it is also the most expensive solid, and the least robust--there may
be numerical inaccuracies with polygons that allow collisions to slip through
where they shouldn't.

Like a plane and a capsule, a CollisionPolygon is only a good choice as an
"into" object. It doesn't support collision tests as a "from" object.

In general, if you must use CollisionPolygons to model your shape, you should
use as few polygons as possible. Use quads instead of triangles if possible,
since two triangles take twice as much time to compute as a single quad. This
does mean that you need to ensure that your quads are perfectly coplanar.

You can also make higher-order polygons like five-sided and six-sided polygons
or more, but you cannot make concave polygons. If you create a concave or
non-coplanar CollisionPolygon in your modeling package, Panda will automatically
triangulate it for you (but this might result in a suboptimal representation,
so it is usually better to subdivide a concave polygon by hand).

Unlike a plane, a CollisionPolygon is infinitely thin; an object is only
considered to be colliding with the polygon while it is overlapping it.

When you create a CollisionPolygon interactively, you can only create triangles
or quads (the higher-order polygons can only be loaded from an egg file).
Simply specify the three or four points to the constructor, in counter-clockwise
order.

.. code-block:: python

   quad = CollisionPolygon(Point3(0, 0, 0), Point3(0, 0, 1),
                           Point3(0, 1, 1), Point3(0, 1, 0))

CollisionRay
------------

The ray is a special collision solid that is useful only as a "from" object;
since the object has no volume, nothing will collide "into" a ray. The same is
true for line, parabola, and segment listed below.

The CollisionRay represents an infinite ray that begins at a specific point,
and stretches in one direction to infinity.

It is particularly useful for picking objects from the screen, since you can
create a ray that starts at the camera's point of view and extends into the
screen, and then determine which objects that ray is intersecting. (In fact,
there is a method on CollisionRay called ``setFromLens()`` that automatically
sets up the ray based on a 2-d onscreen coordinate; this is used by the
"picker". See :ref:`clicking-on-3d-objects`.)

The CollisionRay is also useful in conjunction with the CollisionHandlerFloor;
see :ref:`collision-handlers`.

A CollisionRay is created by specifing an origin point, and a direction vector.
The direction vector need not be normalized.

.. code-block:: python

   ray = CollisionRay(ox, oy, oz, dx, dy, dz)

CollisionLine
-------------

This is essentially the same as a CollisionRay, except it extends to infinity in
both directions. It is constructed with the same parameters, an origin point and
a direction vector.

.. code-block:: python

   line = CollisionLine(ox, oy, oz, dx, dy, dz)

CollisionSegment
----------------

A segment is another variant on the CollisionRay that does not extend to
infinity, but only goes to a certain point and stops. It is useful when you want
to put a limit on how far the CollisionRay would otherwise reach.

A CollisionSegment is constructed by specifying the two end points.

.. code-block:: python

   segment = CollisionSegment(ax, ay, az, bx, by, bz)

CollisionParabola
-----------------

A parabola is another variant on the CollisionRay that bends. It is useful when
you want to test with arcs, such as a cannonball shot.

CollisionBox
------------

Finally, a box represents a cuboid. It consists of three pairs of rectangles,
with adjacent sides meeting each other at a right angle. This can be employed
where ever a necessity arises for using six intersecting planes. A box can be
both a 'from' and 'into' object for the shapes specified in the chart. A box can
only be constructed as an Axis-Aligned Bounding Box (AABB). That is, each side
of the box is parallel to one of the coordinate axes. Once constructed, all
collision tests are performed on the box as though it was an Oriented-Bounding
Box (OBB).

There are two constructors for the Box. One of them specifies the center for the
box as well as the distance of each of the sides from the center.

.. code-block:: python

   box = CollisionBox(center, dx, dy, dz)

The second form of constructor takes the two diagonally opposite end points of
the AABB.

.. code-block:: python

   box = CollisionBox(Point3(minx, miny, minz), Point3(maxx, maxy, maxz))

Collision System Chart
----------------------

Here is a table of the Collision Solids that can be used as "from" and "into"
objects in a Collision.

At noted above, with no volume CollisionRay, CollisionLine, CollisionParabola,
CollisionSegment are only "from", never "into" and hence not listed as columns
in the table below.

At present, CollisionFloorMesh, CollisionInvSphere, CollisionPlane, and
CollisionPolygon are only "into" and never "from" and hence are not listed as
rows in the table below.

In the table below, the solid is listed without its "Collision" preface, e.g.,
"Sphere" instead of "CollisionSphere", to save on space.

================ ============= ============= ========= =========== ========== =========== ========
**From \\ Into** **FloorMesh** **InvSphere** **Plane** **Polygon** **Sphere** **Capsule** **Box**
Line                           **Yes**       **Yes**   **Yes**     **Yes**    **Yes**     **1.10**
Parabola                                     **Yes**   **Yes**     **Yes**    **Yes**
Ray              **Yes\***     **Yes**       **Yes**   **Yes**     **Yes**    **Yes**     **Yes**
Segment                        **Yes**       **Yes**   **Yes**     **Yes**    **Yes**     **Yes**
Sphere           **Yes**       **Yes**       **Yes**   **Yes**     **Yes**    **Yes**     **Yes**
Capsule                        **1.10.2**    **1.10**  **1.10.13** **1.10**   **1.10**    **1.10**
Box                            **1.10.2**    **1.10**  **1.10**    **Yes**                **1.10**
================ ============= ============= ========= =========== ========== =========== ========
