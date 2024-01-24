.. _controlling-a-joint-procedurally:

Controlling a Joint Procedurally
================================

.. only:: python

   Sometimes one wishes to procedurally take control of a model's joint. For
   example, if you wish to force a character model's eyes to follow the mouse,
   you will need to procedurally take control of the neck and head. To achieve
   this, use :py:meth:`~direct.actor.Actor.Actor.controlJoint()`.

   .. code-block:: python

      dummy = actor.controlJoint(None, "modelRoot", "Joint Name")

.. only:: cpp

   Sometimes one wishes to procedurally take control of a model's joint. For
   example, if you wish to force a character model's eyes to follow the mouse,
   you will need to procedurally take control of the neck and head. To achieve
   this, use :meth:`.PartBundle.control_joint()`.

   .. code-block:: cpp

      NodePath dummy = model.attach_new_node("dummy");
      if (bundle->control_joint("Joint Name", dummy)) {
        std::cerr << "Success!\n";
      }

This creates a dummy node. Every frame, the transform is copied from the dummy
node into the joint. By setting the transform of the dummy node, you can control
the joint. Normally, one would want to use :meth:`~.NodePath.set_hpr` to rotate
the joint without moving it. The dummy node is initialized in such a way that
the joint is in its default location, the one specified in the model file.

You must store a local (not global) transform in the dummy node. In other
words, the transform is relative to the joint's parent bone. If you are
controlling the forearm of a model, for instance, the transform will be
relative to the upper arm.

.. only:: python

   The string "modelRoot" represents the name of the model node - the string
   "modelRoot" is usually the correct value.

   The string "Joint Name" represents the name of the joint. Typically it would
   be something like "Femur", or "Neck", or "L Finger1". This is usually set
   inside the modeling package. For example, in MAX, each object in the scene
   has a name, including the bones. If necessary, you can determine the joint
   names by scanning the egg file for strings like ``<Joint> Femur`` or, in the
   case of a glTF file, by looking at the "name" property in the "nodes" array.
   The call :py:meth:`actor.listJoints() <direct.actor.Actor.Actor.listJoints>`
   can also be used to show the complete hierarchy of joints.

.. only:: python

   To undo a previous :py:meth:`~direct.actor.Actor.Actor.controlJoint()` call,
   use the :py:meth:`~direct.actor.Actor.Actor.releaseJoint()` method:

   .. code-block:: python

      actor.releaseJoint("modelRoot", "Joint Name")

.. only:: cpp

   To undo a previous :meth:`~.PartBundle.control_joint()` call, pass the name
   of the joint to the :meth:`~.PartBundle.release_joint()` method:

   .. code-block:: cpp

      bundle->release_joint("Joint Name");
