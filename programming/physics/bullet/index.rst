.. _bullet:

Using Bullet with Panda3D
=========================

Bullet is a modern and open source physics engine used in many games or
simulations. Bullet can be compiled on many platforms, among them Windows, Linux
and macOS. Bullet features include collision detection, rigid body dynamics,
soft body dynamics and a kinematic character controller.

This section is about how to use the Panda3D Bullet module.

Table of Contents
-----------------

.. toctree::
   :maxdepth: 1

   hello-world
   debug-renderer
   collision-shapes
   collision-filtering
   ccd
   queries
   ghosts
   character-controller
   constraints
   vehicles
   softbodies
   softbody-rope
   softbody-patch
   softbody-triangles
   softbody-tetrahedron
   softbody-config
   config-options
   faq
   samples

All Bullet classes are prefixed with "Bullet". A list of all classes and their
methods can be found from the :mod:`panda3d.bullet` page of the API Reference.
However, the class and function descriptions are still missing.

.. note::

   The Panda3D Bullet module makes great effort to integrate Bullet physics as
   tightly as reasonably possible with the core Panda3D classes. However, when
   implementing collision detection and physics, you can not mix Panda3D's
   internal physics & collision system, ODE, and Bullet. More explicitly:
   Bullet bodies won't collide with ODE bodies and CollisionNodes.

Samples on how to use the Panda3D Bullet module can be found in the following
archive: https://www.panda3d.org/download/noversion/bullet-samples.zip

.. only:: cpp

   Note: All samples are currently available in Python code only.
