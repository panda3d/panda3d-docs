.. _collision-filtering:

Bullet Collision Filtering
==========================

By default all Bullet collision objects collide with all other Bullet
collision objects. Here the term "collision objects" refers to objects which
are derived from :class:`.BulletBodyNode`, namely
:class:`.BulletRigidBodyNode`, :class:`.BulletGhostNode`, and
:class:`.BulletSoftBodyNode`.

Bullet collision objects won't collide with visible geometry, that is objects
of type :class:`.GeomNode`!

Sometime we need more control over who collides with whom. This can be
achieved by setting up collision filtering properly. Collision filtering is
done using bitmasks, which get assigned to every collision object.

Bit Masks
---------

Bullet makes use of the regular Panda3D collide masks, which are instances of
:class:`.BitMask32`. Two objects collide if
the two masks have at least one bit in common. The following example shows a
selection of common ways to set up a bit mask. For more information please
refer to the manual page on :ref:`collision-bitmasks`.

.. only:: python

   .. code-block:: python

      from panda3d.core import BitMask32

      mask1 = BitMask32.allOn()
      mask2 = BitMask32.allOff()
      mask3 = BitMask32.bit(2)
      mask4 = BitMask32.bit(5)
      mask5 = BitMask32(0x3)

.. only:: cpp

   .. code-block:: cpp

      #include "panda3d/bitMask.h"

      BitMask32 mask1 = BitMask32::all_on();
      BitMask32 mask2 = BitMask32::all_off();
      BitMask32 mask3 = BitMask32::bit(2);
      BitMask32 mask4 = BitMask32::bit(5);
      BitMask32 mask5 = BitMask32(0x3);

Given the above bit masks we would get the following results for collision:

::

   mask1 and mask2 = false
   mask1 vs. mask3 = true
   mask3 vs. mask4 = false
   mask3 vs. mask5 = true
   mask4 vs. mask5 = false

Group Masks
-----------

Sometimes BitMasks alone are not flexible enough to represent the
relationships between a large number of groups of objects. Group masks are
similar to bit masks in that each object belongs to a group, but instead of
collisions only occurring between objects that belong to the same group,
collision relationships are instead represented by a collision matrix. This
means that a larger number of groups can be represented in the same 32 bits of
a :class:`.BitMask32`.

To use group mask filtering instead of the default bit mask filtering
mentioned above, set the ``bullet-filter-algorithm`` configuration variable
to ``groups-mask``. The default
collision matrix is set to only collide objects that are in the same group. As
you make changes, the collision matrix is kept symmetrical along the line of
the diagonal for you. So if you set Group 0 to collide with Group 1, then
Group 1 will also automatically collide with Group 0.

The following collision matrix shows that the only collisions that occur are
between group 1 and group 2, and group 2 with itself.

======= ======= ======= =======
\       Group 0 Group 1 Group 2
======= ======= ======= =======
Group 0 False   False   False
Group 1 -       False   True
Group 2 -       -       True
======= ======= ======= =======

The following code segment shows how this matrix is represented in code.

.. only:: python

   .. code-block:: python

      # Group 0 never collides
      world.setGroupCollisionFlag(0, 0, False)
      world.setGroupCollisionFlag(0, 1, False)
      world.setGroupCollisionFlag(0, 2, False)

      # Group 1 only collides with Group 2
      world.setGroupCollisionFlag(1, 1, False)
      world.setGroupCollisionFlag(1, 2, True)

      # Group 2 only collides with itself
      world.setGroupCollisionFlag(2, 2, True)

.. only:: cpp

   .. code-block:: cpp

      // Group 0 never collides
      physics_world->set_group_collision_flag(0, 0, false);
      physics_world->set_group_collision_flag(0, 1, false);
      physics_world->set_group_collision_flag(0, 2, false);

      // Group 1 only collides with Group 2
      physics_world->set_group_collision_flag(1, 1, false);
      physics_world->set_group_collision_flag(1, 2, true);

      // Group 2 only collides with itself
      physics_world->set_group_collision_flag(2, 2, true);

Please note that this group matrix is ignored by :ref:`queries <queries>`,
which take a mask that directly indicates which groups to match against.

Group Assignment
----------------

The example below shows a typical setup for a rigid body. Only the last line
of the code block is new. Here we set the collide mask which specifies which
collision groups the object belongs to.

.. only:: python

   .. code-block:: python

      shape = shape = BulletBoxShape(Vec3(0.5, 0.5, 0.5))

      body = BulletRigidBodyNode('Body')
      body.addShape(shape)

      world.attachRigidBody(body)

      bodyNP = self.worldNP.attachNewNode(body)
      bodyNP.setPos(0, 0, -1)

      # Set it to be a part of group 0
      bodyNP.setCollideMask(BitMask32.bit(0))

.. only:: cpp

   .. code-block:: cpp

      BulletBoxShape *box_shape = new BulletBoxShape(LVecBase3(0.5, 0.5, 0.5));
      BulletRigidBodyNode *body_rigid_node = new BulletRigidBodyNode("Body");
      body_rigid_node->add_shape(box_shape);
      physics_world->attach(box_rigid_node);

      NodePath np_body = window->get_render().attach_new_node(box_rigid_node);
      np_body.set_pos(0, 0, 2);

      // Set it to be a part of group 0
      np_body.set_collide_mask(BitMask32::bit(0));

PandaNodes have two kinds of collide masks, a "from" collide mask and an
"into" collide mask. Panda3D's internal collision system requires both masks
set, but when using Bullet physics only the "into" collide mask is used. The
following line is an alternate way to set the collide mask:

.. only:: python

   .. code-block:: python

      bodyNP.node().setIntoCollideMask(mask)

.. only:: cpp

   .. code-block:: cpp

      np_box.node()->set_into_collide_mask(mask);

This way of setting collide masks can be used for rigid bodies and ghost
objects. Soft body collisions (and soft body vs. rigid body collisions) are
more complex. Please see the manual pages about soft body configuration for
details.

Multiple Group Assignment
-------------------------

It it is also possible for an object to be part of multiple groups. The object
is considered to collide with another object if it does so as part of any of
the individual groups that it is a member of.

To make an object part of multiple groups, use the bitwise OR operator to
combine multiple bitmasks.

.. only:: python

   .. code-block:: python

      # Set it to be a part of groups 0 and 2
      bodyNP.setCollideMask(BitMask32.bit(0) | BitMask32.bit(2))

.. only:: cpp

   .. code-block:: cpp

      // Set it to be a part of groups 0 and 2
      np_body.set_collide_mask(BitMask32::bit(0) | BitMask32::bit(2));
