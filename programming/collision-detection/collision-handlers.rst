.. _collision-handlers:

Collision Handlers
==================

You will need to create a CollisionHandler that specifies what to do when a
collision event is detected. Each object can only have one collision handler
associated with it. There are several possible kinds of CollisionHandler
available.

CollisionHandlerQueue
---------------------

The simplest kind of CollisionHandler, this object simply records the collisions
that were detected during the most recent traversal. You can then iterate
through the list using :meth:`queue.entries <.CollisionHandlerQueue.entries>`:

.. only:: python

   .. code-block:: python

      queue = CollisionHandlerQueue()
      traverser.addCollider(fromObject, queue)
      traverser.traverse(render)

      for entry in queue.entries:
          print(entry)

.. only:: cpp

   .. code-block:: cpp

      PT(CollisionHandlerQueue) queue = new CollisionHandlerQueue;
      CollisionTraverser traverser;
      traverser.add_collider(fromObject, queue);
      traverser.traverse(get_render());

      for (int i = 0; i < queue->get_num_entries(); ++i) {
        CollisionEntry *entry = queue->get_entry(i);
        std::cout << *entry << endl;
      }

By default, the :ref:`collision-entries` appear in the queue in no particular
order. You can arrange them in order from nearest to furthest by calling
:meth:`queue.sort_entries() <.CollisionHandlerQueue.sort_entries>` after the
traversal.

CollisionHandlerEvent
---------------------

This is another simple kind of CollisionHandler. Rather than saving up the
collisions, it generates a :ref:`Panda event <tasks-and-event-handling>` when
collision events are detected.

There are three kinds of events that may be generated: the "in" event, when a
particular object collides with another object that it didn't in the previous
pass, the "out" event, when an object is no longer colliding with an object it
collided with in the previous pass, and the "again" event, when an object is
still colliding with the same object that it did in the previous pass.

For each kind of event, the CollisionHandlerEvent will construct an event name
out of the names of the from and into objects that were involved in the
collision. The exact event name is controlled by a pattern string that you
specify. For instance:

.. only:: python

   .. code-block:: python

      handler.addInPattern('%fn-into-%in')
      handler.addAgainPattern('%fn-again-%in')
      handler.addOutPattern('%fn-out-%in')

.. only:: cpp

   .. code-block:: cpp

      handler->add_in_pattern("%fn-into-%in");
      handler->add_again_pattern("%fn-into-%in");
      handler->add_out_pattern("%fn-into-%in");

In the pattern string, the following sequences have special meaning:

======== ===================================================================
%fn      the name of the "from" object's node
%in      the name of the "into" object's node
%fs      't' if "from" is declared to be tangible, 'i' if intangible
%is      't' if "into" is declared to be tangible, 'i' if intangible
%ig      'c' if "into" is a CollisionNode, 'g' if it is an ordinary GeomNode
%(tag)fh generate event only if "from" node has the indicated tag
%(tag)fx generate event only if "from" node does not have the indicated tag
%(tag)ih generate event only if "into" node has the indicated tag
%(tag)ix generate event only if "into" node does not have the indicated tag
%(tag)ft the indicated tag value of the "from" node.
%(tag)it the indicated tag value of the "into" node.
======== ===================================================================

You may use as many of the above sequences as you like, or none, in the pattern
string. In the tag-based sequences, the parentheses around (tag) are literal;
the idea is to write the name of the tag you want to look up, surrounded by
parentheses. The tag is consulted using the
:meth:`nodePath.get_net_tag() <.NodePath.get_net_tag>` interface.

In any case, the event handler function that you write to service the event
should receive one parameter (in addition to self, if it is a method): the
:ref:`CollisionEntry <collision-entries>`. For example:

.. only:: python

   .. code-block:: python

      class MyObject(DirectObject.DirectObject):
          def __init__(self):
              self.accept('car-into-rail', handleRailCollision)

          def handleRailCollision(self, entry):
              print(entry)

Note that all of the following versions of CollisionHandler also inherit from
CollisionHandlerEvent, so any of them can be set up to throw events in the same
way.

CollisionHandlerPusher
----------------------

This is the first of the more sophisticated handlers. The
CollisionHandlerPusher, in addition to inheriting all of the event logic from
CollisionHandlerEvent, will automatically push back on its from object to keep
it out of walls. The visual effect is that your object will simply stop moving
when it reaches a wall if it hits the wall head-on, or it will slide along the
wall smoothly if it strikes the wall at an angle.

The CollisionHandlerPusher needs to have a handle to the NodePath that it will
push back on, for each from object; you pass this information to
:meth:`pusher.add_collider() <.CollisionHandlerPusher.add_collider>`.
This should be the node that is actually moving. This is often, but not always,
the same NodePath as the CollisionNode itself, but it might be different if the
CollisionNode is set up as a child of the node that is actually moving.

.. only:: python

   .. code-block:: python

      smiley = loader.loadModel('smiley.egg')
      fromObject = smiley.attachNewNode(CollisionNode('colNode'))
      fromObject.node().addSolid(CollisionSphere(0, 0, 0, 1))

      pusher = CollisionHandlerPusher()
      pusher.addCollider(fromObject, smiley)

.. only:: cpp

   .. code-block:: cpp

      smiley = window->load_model(framework.get_models(), "smiley.egg");
      fromObject = smiley.attach_new_node(new CollisionNode("colNode"));
      fromObject->add_solid(new CollisionSphere(0, 0, 0, 1));

      PT(CollisionHandlerPusher) pusher = new CollisionHandlerPusher;
      pusher->add_collider(fromObject, smiley);

Don't be confused by the call to
:meth:`pusher.add_collider() <.CollisionHandlerPusher.add_collider>`; it looks a
lot like the call to
:meth:`traverser.add_collider() <.CollisionTraverser.add_collider>`, but it's
not the same thing, and you still need to add the collider and its handler to
the traverser:

.. only:: python

   .. code-block:: python

      traverser.addCollider(fromObject, pusher)
      smiley.setPos(x, y, 0)

.. only:: cpp

   .. code-block:: cpp

      traverser.add_collider(fromObject, pusher);
      smiley.set_pos(x, y, 0);

If you are using Panda's drive mode to move the camera around (or some other
node), then you also need to tell the pusher about the drive node, by adding
it into the :meth:`pusher.add_collider() <.CollisionHandlerPusher.add_collider>`
call:

.. only:: python

   .. code-block:: python

      fromObject = base.camera.attachNewNode(CollisionNode('colNode'))
      fromObject.node().addSolid(CollisionSphere(0, 0, 0, 1))

      pusher = CollisionHandlerPusher()
      pusher.addCollider(fromObject, base.camera, base.drive.node())

.. only:: cpp

   .. code-block:: cpp

      fromObject = cam.attach_new_node(new CollisionNode("colNode"))
      fromObject.node()->add_solid(new CollisionSphere(0, 0, 0, 1));

      PT(CollisionHandlerPusher) pusher = new CollisionHandlerPusher;
      pusher.add_collider(fromObject, cam);

PhysicsCollisionHandler
-----------------------

This kind of handler further specializes CollisionHandlerPusher to integrate
with Panda's :ref:`Physics Engine <panda3d-physics-engine>`. It requires that
the NodePath you pass as the second parameter to
:meth:`pusher.add_collider() <panda3d.physics.PhysicsCollisionHandler.add_collider>`
actually contains an ActorNode, the type of node that is moved by forces in the
physics system.

.. only:: python

   .. code-block:: python

      anp = render.attachNewNode(ActorNode('actor'))
      fromObject = anp.attachNewNode(CollisionNode('colNode'))
      fromObject.node().addSolid(CollisionSphere(0, 0, 0, 1))

      pusher = PhysicsCollisionHandler()
      pusher.addCollider(fromObject, anp)

.. only:: cpp

   .. code-block:: cpp

      anp = window->get_render().attach_new_node(new ActorNode("actor"));
      fromObject = anp.attach_new_node(new CollisionNode("colNode"));
      fromObject.node()->add_solid(new CollisionSphere(0, 0, 0, 1))

      PT(PhysicsCollisionHandler) pusher = new PhysicsCollisionHandler;
      pusher->add_collider(fromObject, anp);

Whenever you have an ActorNode that you want to respond to collisions, we
recommend that you use a PhysicsCollisionHandler rather than an ordinary
CollisionHandlerPusher. The PhysicsCollisionHandler will keep the object out of
walls, just like the CollisionHandlerPusher does, but it will also update the
object's velocity within the physics engine, which helps to prevent the physics
system from becoming unstable due to large accumulated velocities.

CollisionHandlerFloor
---------------------

This collision handler is designed to serve one very specialized purpose: it
keeps an object on the ground, or falling gently onto the ground, even if the
floor is not level, without involving physics.

It is intended to be used with a ``CollisionRay`` or ``CollisionSegment``. The
idea is that you attach a ray to your object, pointing downward, such that the
topmost intersection the ray detects will be the floor your object should be
resting on. Each frame, the CollisionHandlerFloor simply sets your object's z
value to the detected intersection point (or, if it is so configured, it slowly
drops the object towards this point until it reaches it).

Using the CollisionHandlerFloor can be an easy way to simulate an avatar walking
over uneven terrain, without having to set up a complicated physics simulation
(or involve physics in any way). Of course, it does have its limitations.

.. only:: python

   .. code-block:: python

      smiley = loader.loadModel('smiley.egg')
      fromObject = smiley.attachNewNode(CollisionNode('colNode'))
      fromObject.node().addSolid(CollisionRay(0, 0, 0, 0, 0, -1))

      lifter = CollisionHandlerFloor()
      lifter.addCollider(fromObject, smiley)

.. only:: cpp

   .. code-block:: cpp

      smiley = window->load_model(framework.get_models(), "smiley.egg");
      fromObject = smiley.attach_new_node(new CollisionNode("colNode"));
      fromObject.node()->add_solid(new CollisionRay(0, 0, 0, 0, 0, -1));

      PT(CollisionHandlerFloor) lifter = new CollisionHandlerFloor;
      lifter->add_collider(fromObject, smiley);

CollisionHandlerGravity
-----------------------

This handler is very similar to CollisionHandlerFloor, but rather than
positioning objects directly at the floor, it can apply an acceleration to make
them fall gradually to the ground.

The main parameter to adjust is the ``gravity`` property, which sets the
acceleration.  If your scene unit is metres, and your simulation takes place on
earth, then you will want to set this to a value of around 9.81.

For the full list of parameters, see :class:`.CollisionHandlerGravity` in the
API reference.
