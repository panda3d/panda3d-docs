.. _enabling-physics-on-a-node:

Enabling physics on a node
==========================

The ActorNode is the component of the physics system that tracks interactions
and applies them to a model. The calculations factor in the amount of time
elapsed between frames, so the physics will be robust against changes in
framerate.

To enable a node for physics, attach it to an ActorNode. An ActorNode's
position and orientation can be updated automatically by the physics system,
and so any children of the ActorNode will inherit that position and
orientation as well.

(Do not confuse ActorNode with the :ref:`Actor <models-and-actors>` class,
which is used to play animations. They are completely unrelated classes with
similar names.)

When an ActorNode is created, it must be associated with a PhysicsManager. The
PhysicsManager will handle the physics calculations every frame and update the
ActorNode with any changes. Panda provides a default physics manager,
base.physicsMgr, which will often be suitable for most applications.

.. code-block:: python

   node = NodePath("PhysicsNode")
   node.reparentTo(render)
   an = ActorNode("jetpack-guy-physics")
   anp = node.attachNewNode(an)
   base.physicsMgr.attachPhysicalNode(an)
   jetpackGuy = loader.loadModel("models/jetpack_guy")
   jetpackGuy.reparentTo(anp)

Now, the "jetpackGuy" model will be updated every frame with the physics
applied to it.

The ActorNode also serves as a repository for the PhysicsObject that describes
the physical properties (i.e. mass) of the object. To modify these properties,
use the getPhysicsObject call.

.. code-block:: python

   an.getPhysicsObject().setMass(136.077)   # about 300 lbs
