.. _collision-traversers:

Collision Traversers
====================

A :class:`.CollisionTraverser` object performs the actual work of checking all
solid objects for collisions. Normally, you will create a single
CollisionTraverser object and assign it to ``base.cTrav``; this traverser will
automatically be run every frame. It is also possible to create additional
CollisionTraversers if you have unusual needs; for instance, to run a second
pass over a subset of the geometry. If you create additional
CollisionTraversers, you must run them yourself.

The CollisionTraverser maintains a list of the active objects in the world,
sometimes called the "colliders" or "from objects". The remaining collidable
objects in the world that are not added to a CollisionTraverser are the "into
objects". Each of the "from objects" is tested for collisions with all other
objects in the world, including the other from objects as well as the into
objects.

Note that it is up to you to decide how to divide the world into "from
objects" and "into objects". Typically, the from objects are the moving
objects in the scene, and the static objects like walls and floors are into
objects, but the collision system does not require this; it is perfectly
legitimate for a from object to remain completely still while an into object
moves into it, and the collision will still be detected.

It is a good idea for performance reasons to minimize the number of from
objects in a particular scene. For instance, the user's avatar is typically a
from object; in many cases, it may be the only from object required--all of
the other objects in the scene, including the walls, floors, and other
avatars, might be simply into objects. If your game involves bullets that need
to test for collisions with the other avatars, you will need to make either
the bullets or the other avatars be from objects, but probably not both.

In order to add a from object to the CollisionTraverser, you must first create
a CollisionHandler that defines the action to take when the collision is
detected; then you pass the NodePath for your from object, and its
CollisionHandler, to :meth:`~.CollisionTraverser.add_collider()`.

.. only:: python

   .. code-block:: python

      traverser = CollisionTraverser('traverser name')
      base.cTrav = traverser
      traverser.addCollider(fromObject, handler)

You only need to add the "from" objects to your traverser! Don't try to add
the "into" objects to the CollisionTraverser. Adding an object to a
CollisionTraverser makes it a "from" object. On the other hand, every object
that you put in the scene graph, whether it is added to a CollisionTraverser
or not, is automatically an "into" object.

Note that all of your "from" objects are typically "into" objects too (because
they are in the scene graph), although you may choose to make them not behave
as into objects by setting their :ref:`CollideMask <collision-bitmasks>` to
zero.

The CollisionTraverser can visually show the collisions that are occurring by
using the following line of code:

.. only:: python

   .. code-block:: python

      trav.showCollisions(render)

.. only:: cpp

   .. code-block:: cpp

      trav->show_collisions(window->get_render());
