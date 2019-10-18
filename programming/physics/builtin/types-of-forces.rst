.. _types-of-forces:

Types of forces
===============

Panda3D provides two types of forces that you can apply to an object.

LinearVectorForce
-----------------

A ``LinearVectorForce`` treats the object as a point mass. It applies an
acceleration in Newtons to the center of mass of the object it was added to. The
direction of this force is relative to the orientation of the ``ForceNode`` that
the ``LinearVectorForce`` was applied to.

.. note::

   Since ``LinearVectorForce`` treats the object as a point mass, it is not
   possible to apply a rotation of any kind to your object. For rotational
   forces, see ``AngularVectorForce`` below.

.. rubric:: Example:

.. code-block:: python

   lvf = LinearVectorForce(1, 0, 0)  # Push 1 newton in the positive-x direction
   forceNode.addForce(lvf)  # Determine coordinate space of this force node
   actorNode.getPhysical(0).addLinearForce(lvf) # Add the force to the object

AngularVectorForce
------------------

The ``AngularVectorForce`` applies a torque to the object it is attached to. The
acceleration is in Newtons, and ``AngularVectorForce`` may be treated in much
the same way as ``LinearVectorForce``. There are, however, some minor
differences that that should be taken into account.

``AngularVectorForce`` does not have a ``.setDependantMass()``. The reason for
this is simple: mass **must** be used in the torque calculations. As such, you
will want to make sure your forces are sufficiently small or your masses are
sufficiently large to keep your rotational velocity sane.

.. rubric:: Example:

.. code-block:: python

   avf = AngularVectorForce(1, 0, 0) # Spin around the positive-x axis
   forceNode.addForce(avf) # Determine which positive-x axis we use for calculation
   actorNode.getPhysical(0).addAngularForce(avf) # Add the force to the object

One additional caveat with ``AngularVectorForce``: Angular forces will not be
processed on your object until an ``AngularIntegrator`` is added to the
``PhysicsManager``.

.. rubric:: Example:

.. only:: python

   .. code-block:: python

      from panda3d.physics import AngularEulerIntegrator

      # Instantiate an AngleIntegrator()
      angleInt = AngularEulerIntegrator()

      # Attach the AngleIntegrator to the PhysicsManager
      base.physicsMgr.attachAngularIntegrator(angleInt)

*Editor's Note: Each type of force should be given it's own page with much more
in depth examples, and perhaps a small sample program.*
