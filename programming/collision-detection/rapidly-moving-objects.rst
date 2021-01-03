.. _rapidly-moving-objects:

Rapidly-Moving Objects
======================

Panda3D's collision system works by testing the current state of the world
every frame for a possible intersection. If your objects are moving so quickly
that they might pass completely through another object in the space of one
frame, however, that collision might never be detected.

To avoid this problem, the Panda3D scene graph supports an advanced feature:
it can record the previous frame's position of each moving object for the
benefit of the CollisionTraverser. The CollisionTraverser can then take
advantage of this information when it is testing for collisions. If it sees
that a moving object was on one side of an object last frame, and on the
opposite side this frame, it can trigger the collision detection even though
the two objects might not currently be intersecting.

There are a few things you need to do to activate this mode.

1. First, you must tell the CollisionTraverser that you intend to use this
mode; by default, it ignores the previous position information. To activate
this mode, call:

.. only:: python

   .. code-block:: python

      base.cTrav.setRespectPrevTransform(True)

.. only:: cpp

   .. code-block:: cpp

      traverser->set_respect_prev_transform(true);

You only need to make this call once, at the beginning of your application (or
whenever you create the CollisionTraverser). That switches the
CollisionTraverser into the new mode. If you create any additional
CollisionTraversers, you should make the call for them as well.

2. Ensure that :meth:`PandaNode.reset_all_prev_transform()` is called every
frame. Actually, this is already done for you automatically by ShowBase.py, so
normally you don't need to do anything for this step.

The :meth:`~.PandaNode.reset_prev_transform()` call should be made once per
frame, at the very beginning of the frame. It ensures that the current frame's
position is copied to the previous frame's position, before beginning the
processing for that frame. Note that if you have multiple CollisionTraversers
handling the same scene graph, you still only need to (and only should) call
this function once.

3. Whenever you move an object from one point to another in your scene (except
when you put it into your scene the first time), instead of using:

.. only:: python

   .. code-block:: python

      object.setPos(newPos)

.. only:: cpp

   .. code-block:: cpp

      object.set_pos(new_pos);

You should use:

.. only:: python

   .. code-block:: python

      object.setFluidPos(newPos)

.. only:: cpp

   .. code-block:: cpp

      object.set_fluid_pos(new_pos);

In general, :meth:`~.NodePath.set_pos()` means "teleport the object here" and
:meth:`~.NodePath.set_fluid_pos()` means "slide the object here, testing for
collisions along the way". It is important to make a clear distinction between
these two calls, and make the appropriate call for each situation.

If you are moving an object with a :ref:`LerpInterval <lerp-intervals>`, and
you want collisions to be active (and fluid) during the lerp, you should pass
the keyword parameter ``fluid = 1`` to the LerpInterval constructor.
It is rare to expect collisions to be active while an object is moving under
direct control of the application, however.

Visualizing the previous transform
----------------------------------

When you are using the :meth:`~.NodePath.set_fluid_pos()` call, and you have
called :meth:`~.NodePath.show()` on your CollisionNode to make it visible, you
will see the CollisionNode itself each frame, plus a ghosted representation of
where it was the previous frame. This can help you visually see that the
previous-transform mechanism is working. (It does not guarantee that the
:meth:`~.CollisionTraverser.set_respect_prev_transform()` call has been made on
your CollisionTraverser, however.)

Caveats
-------

At the present, the CollisionTraverser only uses the previous transform
information when the "from" object is a CollisionSphere. Other kinds of
collision solids currently do not consider the previous transform.

Enabling the previous transform mode helps reduce slipping through walls
considerably. However, it's not perfect; no collision system is. If your
object is moving tremendously fast, or just happens to get lucky and slip
through a tiny crack between adjacent polygons, it may still get through
without detecting a collision. Any good application will be engineered so that
the occasional collision slip does not cause any real harm.

The CollisionHandlerFloor is especially bad about allowing objects to slip
through floors, in spite of the previous transform state, especially when you
avatar is walking up a sloping path. This is just because of the way the
CollisionHandlerFloor works. If you are having problems with the
CollisionHandlerFloor, consider reducing the slope of your floors, increasing
the height of the ray above the ground, and/or reducing the speed of your
avatar.
