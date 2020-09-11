.. _backface-culling-and-frontface-culling:

Backface Culling and Frontface Culling
======================================

Backface and Frontface Culling
------------------------------

By default, Panda3D automatically culls (doesn't render) backfaces of polygons.
In other words, the polygon acts like a one-way mirror: you can see it from one
side, but from the other side, it's see-through. Backface culling is a very
useful performance optimization. Without it, the 3D engine would have to render
the inside surface of 3D models. Since this surface is not visible anyhow, this
is entirely wasted work. Since the surface area of the inside is equal to the
surface area of the outside, this would roughly double the amount of work the
video card has to do. This is why backface culling is enabled by default.

Interestingly, this means that if you move the camera inside of a closed 3D
model, you can usually see out. This is actually pretty convenient most of the
time.

However, there are cases when you do want to be able to see backfaces. There are
also very rare cases when you don't want to see front-faces. Therefore, backface
and frontface culling can be controlled.

.. caution::

   Inexperienced 3D modelers sometimes create models with the polygons facing
   inward: ie, the visible side of the polygon is on the inside of the 3D model,
   and the see-through side is on the outside. As a result, the 3D model can
   look very weird - it can have holes, or it can look inside-out. Turning off
   backface culling can sort of "fix" these models, at a heavy cost: first, it
   makes them render half as fast, and second, it causes weird lighting
   artifacts (because the video card is calculating the lighting for the inside
   of the model, not the outside). This is not a real solution to bad 3D
   modeling: the only real fix is to make the 3D models correctly in the first
   place.

   In other words, don't alter the backface or frontface culling unless you're
   using an algorithm that requires it, such as stencil shadows.

Rendering Double-Sided
----------------------

There is a quick way to render a certain :ref:`NodePath <the-scene-graph>` in
your scene double-sided, which means no culling is performed at all and both
sides are visible, without hassling with attribs:

.. only:: python

   .. code-block:: python

      nodePath.setTwoSided(True)

.. only:: cpp

   .. code-block:: cpp

      nodePath.set_two_sided(true);

If you want more advanced control over the culling you might want to look at the
:class:`.CullFaceAttrib`:

Controlling Backface and Frontface Culling
------------------------------------------

There are three valid settings for culling:

.. only:: python

   .. code-block:: python

      nodePath.setAttrib(CullFaceAttrib.make(CullFaceAttrib.MCullNone))
      nodePath.setAttrib(CullFaceAttrib.make(CullFaceAttrib.MCullClockwise))
      nodePath.setAttrib(CullFaceAttrib.make(CullFaceAttrib.MCullCounterClockwise))

.. only:: cpp

   .. code-block:: cpp

      // Includes: "cullFaceAttrib.h"

      nodePath.set_attrib(CullFaceAttrib::make(CullFaceAttrib::M_cull_none));
      nodePath.set_attrib(CullFaceAttrib::make(CullFaceAttrib::M_cull_clockwise));
      nodePath.set_attrib(CullFaceAttrib::make(CullFaceAttrib::M_cull_counter_clockwise));

None means that all faces are visible, both back and front. Clockwise is the
default setting, it causes backfaces to be culled. Counter-clockwise is the
reverse setting, it causes frontfaces to be culled.
