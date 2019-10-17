.. _attaching-an-object-to-a-joint:

Attaching an Object to a Joint
==============================

If an actor has a skeleton, then it is possible to locate one of the joints,
and attach an object to that joint:

.. code-block:: python

   myNodePath = actorNodePath.exposeJoint(None, "modelRoot", "Joint Name")

This function returns a nodepath which is attached to the joint. By reparenting
any object to this nodepath, you can cause it to follow the movement of the
joint.

The string "modelRoot" represents the name of the model node - the string
"modelRoot" is usually the correct value.

The string "Joint Name" represents the name of the joint. Typically it would be
something like "Femur", or "Neck", or "L Finger1". This is usually set inside
the modeling package. For example, in MAX, each object in the scene has a name,
including the bones. If necessary, you can determine the joint names by scanning
the egg file for strings like ``<Joint> Femur``.
