.. _physics:

Physics
=======

Panda3D offers four built-in choices to use for Physics:

-  :ref:`Panda's Built-in Physics Engine <panda3d-physics-engine>`: Panda3D
   has a very basic physics engine built-in that may apply forces to classes.
   The physics engine can handle angular or linear forces, as well as
   viscosity.
-  :ref:`Bullet Physics Engine <bullet>`: New in 1.8.0. This is a good choice
   for more advanced physics in most games.
-  :ref:`The Open Dynamics Engine <ode>`: This is another option provided as
   part of the Panda3D binaries, but does not support as many features as
   Bullet.

When you have a very simple simulation, you will most likely want to use the
built-in physics, which works with Panda's collision system. Although, when
the built-in engine doesn't offer enough functionality for you, the Bullet
system may be a better choice.


.. toctree::
   :maxdepth: 2

   builtin/index
   bullet/index
   ode/index
