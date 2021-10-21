.. _physics:

Physics
=======

While :ref:`collision-detection` addresses the problem of preventing objects
from intersecting each other adequately for most applications, some games and
simulations may need to model more realistic dynamic interactions between
objects, taking into account such things as an object's mass, friction,
elasticity and external forces.

These uses may require the use of a :term:`physics` engine. This is a system
that can model interactions between objects using physics equations, taking
into account far more parameters than a simple collision response system can.

Panda3D offers several choices to use for :term:`physics`. Before you choose
one, however, think carefully whether you need the additional complexity,
performance and authoring cost of a physics simulation, and whether perhaps
:ref:`collision-detection` on its own might be adequate for your use-cases.

-  :ref:`Panda's Built-in Physics Engine <panda3d-physics-engine>`: Panda3D
   has a very basic physics engine built-in that may apply forces to classes.
   The physics engine can handle angular or linear forces, as well as
   viscosity.
-  :ref:`Bullet Physics Engine <bullet>`: This is a good choice for more
   advanced physics in most games.
-  :ref:`The Open Dynamics Engine <ode>`: This is another option provided as
   part of the Panda3D binaries, but does not support as many features as
   Bullet.

When you have a very simple simulation, you will most likely want to use the
built-in physics, which works with Panda's collision system. However, many
applications that need physics simulations may find it inadequate, as the
Bullet system is far more full-featured.


.. toctree::
   :maxdepth: 2

   builtin/index
   bullet/index
   ode/index
