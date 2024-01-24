.. _animated-models:

Animated Models
===============

There are two classes in Panda3D for 3D Geometry: the 'Model', which is for
non-animated geometry, and the 'Actor', which is for animated geometry.

Note that a geometry is only considered animated if it changes shape. So for
example, a baseball wouldn't be considered animated: it may fly all over the
place, but it stays a sphere. A baseball would be a model, not an actor.

The following sections of the manual explain how to load and manipulate an
animated model. They assume that you have a valid egg file (or other compatible
format) which has an animatable model, and some additional egg files containing
animations. To learn how to convert a model into an egg file see the
:ref:`asset-pipeline` section.

To learn how to load a regular, non-animated model, see the :ref:`model-files`
section.

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2

   loading-actors-and-animations
   actor-animations
   multi-part-actors
   attaching-objects-to-joints
   controlling-joints
