.. _panda3d-physics-engine:

Panda3D Physics Engine
======================

Panda3D has a very basic physics engine that may apply forces to classes. The
physics engine can handle angular or linear forces, as well as viscosity. To
make use of the physics engine, first enable the particle system. The particle
system relies upon the physics engine to move and update particles, so
enabling the particle system adds the tasks in the engine that monitor and
update the interactions of physics-enabled objects in the scene.

.. code-block:: python

   base.enableParticles()

The rest of this section will address how to prepare a model for physical
interactions and apply forces to the model.

.. toctree::
   :maxdepth: 2

   enabling-physics-on-a-node
   applying-physics-to-a-node
   types-of-forces
   notes-and-caveats
