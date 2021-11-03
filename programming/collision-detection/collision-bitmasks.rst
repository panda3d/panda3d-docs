.. _collision-bitmasks:

Collision Bitmasks
==================

By default, every "from" object added to a CollisionTraverser will test for
collisions with every other CollisionNode in the scene graph, and will not
test for collisions with visible geometry. For simple applications, this is
sufficient, but often you will need more control.

This control is provided with the collide masks. Every CollisionNode has two
collide masks: a "from" mask, which is used when the CollisionNode is acting
as a "from" object (i.e. it has been added to a
:ref:`CollisionTraverser <collision-traversers>`), and an "into" mask, which
is used when the node is acting as an "into" object (i.e. it is in the scene
graph, and a from object is considering it for collisions).

In addition, visible geometry nodes--that is, GeomNodes--also have an "into"
mask, so that visible geometry can serve as an "into" object also. (However,
only a CollisionNode can serve as a "from" object.)

Before the solids in a "from" CollisionNode are tested for collisions with
another CollisionNode or with a GeomNode, the collide masks are compared.
Specifically, the "from" mask of the from object, and the "into" mask of the
into object, are ANDed together. If the result is not zero--meaning the two
masks have at least one bit in common--then the collision test is attempted;
otherwise, the two objects are ignored.

The collide masks are represented using a :class:`.BitMask32` object, which is
really just a 32-bit integer with some additional methods for getting and
setting particular bits.

You can only set the from collide mask on a collision node, and you must set
it directly on the node itself, not on the NodePath:

.. only:: python

   .. code-block:: python

      nodePath.node().setFromCollideMask(BitMask32(0x10))

.. only:: cpp

   .. code-block:: cpp

      node_path.node()->set_from_collide_mask(BitMask32(0x10));

However, the into collide mask may be set on the NodePath, for convenience;
this recursively modifies the into collide mask for all the nodes at the given
NodePath level and below.

.. only:: python

   .. code-block:: python

      nodePath.setCollideMask(newMask, bitsToChange, nodeType)

.. only:: cpp

   .. code-block:: cpp

      node_path.set_collide_mask(new_mask, bits_to_change, node_type);

The parameter newMask specifies the new mask to apply. The remaining
parameters are optional; if they are omitted, then every node at nodePath
level and below is assigned newMask as the new into collide mask. However, if
bitsToChange is specified, it represents the set of bits that are to be
changed from the original; bits that are 0 in bitsToChange will not be
modified at each node level. If nodeType is specified, it should be a
TypeHandle that represents the type of node that will be modified, e.g.
:meth:`.CollisionNode.get_class_type()` to affect only CollisionNodes.

Examples:

.. only:: python

   .. code-block:: python

      nodePath.setCollideMask(BitMask32(0x10))

.. only:: cpp

   .. code-block:: cpp

      node_path.set_collide_mask(BitMask32(0x10));

This sets the into collide mask of nodePath, and all children of nodePath, to
the hexadecimal value 0x10, regardless of the value each node had before.

.. only:: python

   .. code-block:: python

      nodePath.setCollideMask(BitMask32(0x04), BitMask32(0xff))

.. only:: cpp

   .. code-block:: cpp

      node_path.set_collide_mask(BitMask32(0x04), BitMask32(0xff));

This replaces the lower 8 bits of nodePath and all of its children with the
value 0x04, leaving the upper 24 bits of each node unchanged.

The default value for both from and into collide masks for a new CollisionNode
can be retrieved by :meth:`.CollisionNode.get_default_collide_mask()`, and the
default into collide mask for a new GeomNode is
:meth:`.GeomNode.get_default_collide_mask()`. Note that you can create a
CollisionNode that collides with visible geometry by doing something like this:

.. only:: python

   .. code-block:: python

      nodePath.node().setFromCollideMask(GeomNode.getDefaultCollideMask())

.. only:: cpp

   .. code-block:: cpp

      node_path.set_collide_mask(GeomNode::get_default_collide_mask());

The :meth:`.NodePath.get_collide_mask()` method returns a union of all the
collide masks for itself and its children. Since the
:meth:`.NodePath.set_collide_mask()` method is called recursively on its
children, the following code can have a profound effect, even though it looks
like it's doing nothing:

.. only:: python

   .. code-block:: python

      nodePath.setCollideMask(nodePath.getCollideMask())

.. only:: cpp

   .. code-block:: cpp

      node_path.set_collide_mask(node_path.get_collide_mask());

The above code actually calculates the collide mask for its children, and sets
all of its children to that same collide mask, wiping out what was there
before.

If you need to have only entities with a certain collision mask to be able to
collide with a model, it is helpful to open the model's egg file and see where
the collisions are enabled (see :ref:`Egg Syntax <egg-syntax>`). Then you would
set the collide mask for only that child node, using :meth:`.NodePath.find()`
(see :ref:`NodePath <the-scene-graph>`). For example, to create a box into only
"ralph" can collide:

.. only:: python

   .. code-block:: python

      ralph = loader.loadModel("ralph")
      ralph.setCollideMask(BitMask32.bit(0))

      box = loader.loadModel("box")
      box.find("**/Cube;+h").setCollideMask(BitMask32.bit(0))

.. only:: cpp

   .. code-block:: cpp

      NodePath ralph = window->load_model(render, "ralph");
      ralph.set_collide_mask(BitMask32::bit(0));

      NodePath box = window->load_model(render, "box");
      box.find("**/Cube;+h").set_collide_mask(BitMask32::bit(0));
