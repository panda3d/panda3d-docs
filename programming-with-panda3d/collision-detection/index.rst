.. _collision-detection:

Collision Detection
===================

Collision detection allows for two objects to bump into each other and react.
This includes not only sending messages for events, but also to keep the
objects from passing through each other. Collision detection is a very
powerful tool for immersion, but it is somewhat complex.

There are two ways to go about collision detection. One is to create special
collision geometry, such as spheres and polygons, to determine collisions. The
other is to allow collisions against all geometry. While the first is somewhat
more complex and takes more effort to implement, it is much faster to execute
and is a better long-term solution. For quick-and-dirty applications, though,
collision with geometry can be a fine solution.

This section of the manual will address both methods.


.. toctree::
   :maxdepth: 2

   collision-solids
   collision-handlers
   collision-entries
   collision-traversers
   collision-bitmasks
   rapidly-moving-objects
   pusher-example
   event-example
   bitmask-example
   clicking-on-3d-objects
