.. _ode:

Using ODE with Panda3D
======================

Panda3D also provides integration for the Open Dynamics Engine. This is a
platform-independent open-source physics engine with advanced types and built-in
collision detection. Panda3D provides support for ODE because sometimes Panda's
limited built-in physics system might not always be enough to suit more complex
needs.

This section will explain how to use this ODE system with Panda3D.

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2

   worlds-bodies-masses
   simulating-physics-world
   attaching-bodies-using-joints
   collision-detection

More information
----------------

-  The :mod:`panda3d.ode` page in the API Reference can list the classes and
   methods available (all of the classes are prefixed with ``Ode``), although the
   function descriptions are lacking. It might also be useful to look at the
   `PyODE API reference <http://pyode.sourceforge.net/api-1.2.0/public/ode-module.html>`__,
   which uses very similar class and method names.
-  Developers from Walt Disney VR Studio have held a lecture about using the
   ODE system with Panda3D. Click
   `here <https://www.youtube.com/watch?v=9qgPyk22Zls>`__
   to watch a video recording of it. (Recorded June 18, 2008)
