.. _notes-and-caveats:

Notes and caveats
=================

Here are some caveats, quirks, and behaviors to be aware of when working with
the physics engine:

#. You can add the same force to an object multiple times with repeated calls
   to addLinearForce or addAngularForce. The result will be that the total
   effect will be the effect of the force applied once times the number of
   times it is applied. Note, however, that to remove the force's effect on
   the object, you must call remove*Force the same number of times add*Force
   was called; each call to remove only removes one instance of the force. Of
   course, it is more efficient to use a single force with magnitude (n x # of
   copies) than to use the same force multiple times.
#. If a NodePath that is controlled by an ActorNode also needs collision
   calculations done upon it, be sure to use the PhysicsCollisionHandler
   instead of CollisionHandlerPusher. More info can be found in the section on
   :ref:`collision-handlers`. If you intend to use a PhysicsCollisionHandler to
   prevent a model from falling through a floor (for example, if the scene has
   gravity applied), be sure to look at the friction coefficient options on
   the :class:`~panda3d.physics.PhysicsCollisionHandler`.
