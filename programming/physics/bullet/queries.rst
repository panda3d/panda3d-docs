.. _queries:

Bullet Queries
==============

Bullet offers a bunch of different queries for retrieving information about
collision objects. A common usecase is sensors needed by game logic components.
For example to find out if the space in front of an NPC object is blocked by a
solid obstacle, or to find out if an NPC can see some other object.

Ray Test
--------

Raycasting is to shoot a ray from one position (the from-position) to another
position (the to-position). Both the from-position and the to-position have to
be specified in global coordinates. The ray test methods will then return a
result object which contains information about which objects the ray has hit.

There are two different ray test method: The first method (``rayTestAll``)
returns all collision objects hit by the ray. But sometimes we are only
interested in the first collision object hit by the ray. Then we can use the
second ray test method (``rayTestClosest``).

Example for closest hit:

.. only:: python

   .. code-block:: python

      pFrom = Point3(0, 0, 0)
      pTo = Point3(10, 0, 0)

      result = world.rayTestClosest(pFrom, pTo)

      print(result.hasHit())
      print(result.getHitPos())
      print(result.getHitNormal())
      print(result.getHitFraction())
      print(result.getNode())

.. only:: cpp

   .. code-block:: cpp

      LPoint3 pFrom(0, 0, 0);
      LPoint3 pTo(10, 0, 0);
      BulletAllHitsRayResult result = world->ray_test_closest(pFrom, pTo);

Example for all hits:

.. only:: python

   .. code-block:: python

      pFrom = Point3(0, 0, 0)
      pTo = pFrom + Vec3(1, 0, 0) * 99999

      result = world.rayTestAll(pFrom, pTo)

      print(result.hasHits())
      print(result.getClosestHitFraction())
      print(result.getNumHits())

      for hit in result.getHits():
          print(hit.getHitPos())
          print(hit.getHitNormal())
          print(hit.getHitFraction())
          print(hit.getNode())

.. only:: cpp

   .. code-block:: cpp

      LPoint3 pFrom = LPoint3(0, 0, 0);
      LPoint3 pTo = pFrom + LVector3d(1, 0, 0) * 99999;
      BulletAllHitsRayResult result = world->ray_test_all(pFrom, pTo);

Often users want to pick or select an object by clicking on it with the mouse.
We can use the ``rayTestClosest`` to find the collision object which is "under"
the mouse pointer, but we have to convert the coordinates in camera space to
global coordinates world space. The following example shows how this can be
done.

.. only:: python

   .. code-block:: python

      # Get to and from pos in camera coordinates
      pMouse = base.mouseWatcherNode.getMouse()
      pFrom = Point3()
      pTo = Point3()
      base.camLens.extrude(pMouse, pFrom, pTo)

      # Transform to global coordinates
      pFrom = render.getRelativePoint(base.cam, pFrom)
      pTo = render.getRelativePoint(base.cam, pTo)

.. only:: cpp

   .. code-block:: cpp

      TODO

Sweep Test
----------

The sweep test is similar to the ray test. There are two differences: (1) The
sweep test does not use an infinite thin ray, like the ray test, but checks for
collisions with a convex shape which is "moved" along the from from-position to
to-position. (2) The sweep test wants to have "from" and "to" specified as
``TransformState``. The sweep test can for example be used to predict if an
object would collide with something else if it was moving from it's current
position to some other position.

The sweep test can only be used with shapes that are convex, otherwise the call
will fail. Many primitive shapes (sphere, box, etc.) are convex, but a triangle
mesh is not. (If you have geometry that is convex, use a BulletConvexHullShape
instead of a BulletTriangleMeshShape.)

.. only:: python

   Example for sweep testing:

   .. code-block:: python

      tsFrom = TransformState.makePos(Point3(0, 0, 0))
      tsTo = TransformState.makePos(Point3(10, 0, 0))

      shape = BulletSphereShape(0.5)
      penetration = 0.0

      result = world.sweepTestClosest(shape, tsFrom, tsTo, penetration)

      print(result.hasHit())
      print(result.getHitPos())
      print(result.getHitNormal())
      print(result.getHitFraction())
      print(result.getNode())

Contact Test
------------

There are two contact tests. One which checks if a collision objects is in
contact with other collision objects, and another which checks for a pair of
collision objects if they are in contact.

.. only:: python

   Example for contact testing:

   .. code-block:: python

      body1 = BulletRigidBodyNode("body1")
      ...

      body2 = BulletRigidBodyNode("body2")
      ...

      result = world.contactTest(node1)
      result = world.contactTestPair(node1, node2)

      print(result.getNumContacts())

      for contact in result.getContacts():
        print(contact.getNode0())
        print(contact.getNode1())

        mpoint = contact.getManifoldPoint()
        print(mpoint.getDistance())
        print(mpoint.getAppliedImpulse())
        print(mpoint.getPositionWorldOnA())
        print(mpoint.getPositionWorldOnB())
        print(mpoint.getLocalPointA())
        print(mpoint.getLocalPointB())

Filtering
---------

The test methods on BulletWorld also take an optional ``mask`` argument that can
be used to limit which groups are matched against (see
:ref:`collision-filtering` for information about collision groups). The default
is ``BitMask32.allOn()``, which indicates that bodies in all groups are
considered for the test.

For example, the following query will consider object A and C, but ignore
object B:

.. code-block:: python

   # These three bodies are in different groups
   objA.setCollideMask(BitMask32.bit(0))
   objB.setCollideMask(BitMask32.bit(1))
   objC.setCollideMask(BitMask32.bit(2))

   fro = (0, 0, 0)
   to = (1, 0, 0)
   mask = BitMask32.bit(0) | BitMask32.bit(2)
   result = world.rayTestClosest(fro, to, mask)

Of particular note if you are using the ``groups-mask`` filter algorithm is that
the mask matches directly against the collide mask of the bodies, ignoring the
group matrix entirely. For example, if you specify ``BitMask32.bit(1)``, it will
consider all bodies that have a collide mask with this bit enabled (ie. all
bodies that are in group 1). It does not behave as though the ray itself were a
body in group 1.
