.. _enabling-physics-on-a-node:

Enabling physics on a node
==========================

The :class:`~panda3d.physics.ActorNode` is the component of the physics system
that tracks interactions and applies them to a model. The calculations factor in
the amount of time elapsed between frames, so the physics will be robust against
changes in framerate.

To enable a node for physics, attach it to an ActorNode. An ActorNode's
position and orientation can be updated automatically by the physics system,
and so any children of the ActorNode will inherit that position and
orientation as well.

(Do not confuse ActorNode with the :ref:`Actor <animated-models>` class, which
is used to play animations. They are completely unrelated classes with similar
names.)

When an ActorNode is created, it must be associated with a PhysicsManager. The
PhysicsManager will handle the physics calculations every frame and update the
ActorNode with any changes. Panda provides a default physics manager,
base.physicsMgr, which will often be suitable for most applications.

.. only:: python

   .. code-block:: python

      node = NodePath("PhysicsNode")
      node.reparentTo(render)
      an = ActorNode("jetpack-guy-physics")
      anp = node.attachNewNode(an)
      base.physicsMgr.attachPhysicalNode(an)
      jetpackGuy = loader.loadModel("models/jetpack_guy")
      jetpackGuy.reparentTo(anp)

.. only:: cpp

   .. code-block:: cpp

      NodePath node("PhysicsNode");
      node.reparent_to(render);
      PT(ActorNode) an = new ActorNode("jetpack-guy-physics");
      NodePath anp = node.attach_new_node(an);
      physics_mgr->attach_physical_node(an);
      NodePath jetpackGuy = window->load_model(anp, "models/jetpack_guy");

Now, the "jetpackGuy" model will be updated every frame with the physics
applied to it.

The ActorNode also serves as a repository for the PhysicsObject that describes
the physical properties (i.e. mass) of the object. To modify these properties,
use the getPhysicsObject call.

.. only:: python

   .. code-block:: python

      an.getPhysicsObject().setMass(136.077)   # about 300 lbs

.. only:: cpp

   .. code-block:: cpp

      an->get_physics_object()->set_mass(136.077);   // about 300 lbs
