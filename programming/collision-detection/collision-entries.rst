.. _collision-entries:

Collision Entries
=================

For each collision detected, a new :class:`.CollisionEntry` object is created.
This CollisionEntry stores all the information about the collision, including
the two objects (nodes) involved in the collision, and the point of impact and
the surface normal of the into object at that point.

The CollisionEntry object is passed to the event handler method by the
:class:`.CollisionHandlerEvent` and its derivatives; it is also the object
stored in the queue of collisions maintained by the
:class:`.CollisionHandlerQueue`.

However you get a handle to CollisionEntry object, you can query it for
information using the following methods:

.. only:: python

   entry.getFromNodePath()
      Returns the NodePath of the “from” object. This NodePath will contain a
      CollisionNode.

   entry.getIntoNodePath()
      Returns the NodePath of the “into” object. This NodePath will contain a
      CollisionNode, or if the collision was made with visible geometry, a
      GeomNode.

   entry.getFrom()
      Returns the actual CollisionSolid of the “from” object. This is useful if
      there were more than one CollisionSolid in the “from” CollisionNode.

   entry.getInto()
      Returns the actual CollisionSolid of the “into” object. However, if the
      collision was made with visible geometry, there is no CollisionSolid, and
      this will be an invalid call.

   entry.hasInto()
      Returns true if the collision was made into a CollisionSolid as opposed to
      visible geometry, and thus the above call will be valid.

   entry.getSurfacePoint(nodePath)
      Returns the 3-D point of the collision, in the coordinate space of the
      supplied NodePath. This point will usually be on the surface of the “into”
      object.

   entry.getSurfaceNormal(nodePath)
      Returns the 3-D surface normal of the “into” object at the point of the
      collision, in the coordinate space of the supplied NodePath.

   entry.getInteriorPoint(nodePath)
      Returns the 3-D point, within the interior of the “into” object, that
      represents the depth to which the “from” object has penetrated.

.. only:: cpp

   entry->get_from_node_path()
      Returns the NodePath of the “from” object. This NodePath will contain a
      CollisionNode.

   entry->get_into_node_path()
      Returns the NodePath of the “into” object. This NodePath will contain a
      CollisionNode, or if the collision was made with visible geometry, a
      GeomNode.

   entry->get_from()
      Returns the actual CollisionSolid of the “from” object. This is useful if
      there were more than one CollisionSolid in the “from” CollisionNode.

   entry->get_into()
      Returns the actual CollisionSolid of the “into” object. However, if the
      collision was made with visible geometry, there is no CollisionSolid, and
      this will be an invalid call.

   entry->has_into()
      Returns true if the collision was made into a CollisionSolid as opposed to
      visible geometry, and thus the above call will be valid.

   entry->get_surface_point(nodePath)
      Returns the 3-D point of the collision, in the coordinate space of the
      supplied NodePath. This point will usually be on the surface of the “into”
      object.

   entry->get_surface_normal(nodePath)
      Returns the 3-D surface normal of the “into” object at the point of the
      collision, in the coordinate space of the supplied NodePath.

   entry->get_interior_point(nodePath)
      Returns the 3-D point, within the interior of the “into” object, that
      represents the depth to which the “from” object has penetrated.

The three methods that return points or vectors all accept a NodePath as a
parameter. This can be any NodePath in the scene graph; it represents the
coordinate space in which you expect to receive the answer. For instance, to
receive the point of intersection in the coordinate space of the "into"
object, use:

.. only:: python

   .. code-block:: python

      point = collisionEntry.getSurfacePoint(collisionEntry.getIntoNodePath())

.. only:: cpp

   .. code-block:: cpp

      point = collisionEntry->get_surface_point(collisionEntry->get_into_node_path());

If you wanted to put an axis at the point of the collision to visualize it,
you might do something like this:

.. only:: python

   .. code-block:: python

      axis = loader.loadModel('zup-axis.egg')
      axis.reparentTo(render)
      point = collisionEntry.getSurfacePoint(render)
      normal = collisionEntry.getSurfaceNormal(render)
      axis.setPos(point)
      axis.lookAt(point + normal)
