.. _too-many-polygons:

Too Many Polygons
=================

Even though modern GPUs can handle millions of polygons and vertex data takes
little space in RAM, there is still a limit and it's not very difficult to
reach it.

First thing you should make sure is that your performance issue is indeed
caused by too many polygons. Even though modern GPUs can render millions of
polygons in realtime, they still can't render more than few hundred meshes
(Geoms) at the same speed. So you won't have problem rendering 300 polygons as
1 Geom in realtime, but you will torture your GPU if you'll try to render 300
Geoms, even if each has a single polygon. There are few ways to find out the
Geom count and many solutions for lowering it which are discussed in the
:ref:`appropriate page <too-many-meshes>`. Another issue might be using too
many polygons on animated meshes (Actors). When you play an animation, Panda
or your GPU need to calculate the new position of each vertex associated with
a joint, even though the GPU will render the mesh at the same speed, the
calculations done for the animation can get expensive themselves. You can
easily find out the time spent on skinning with PStats:

.. image:: pstats-skinning-time.png

Other factors might affect the performance which are not solely based on the
polygon count. Is your mesh textured? is it shaded? Does it have the
ShaderGenerator enabled on it or does it use custom shaders? Does it have
normal/gloss/glow maps? Is backface culling enabled? These all can affect the
performance. If you are sure that your performance issue is caused by too many
polygons, there are few optimizations you can do.

-  The first obvious solution is to just make your models low-poly or not use
   two polygons where you can use one. However, you should also note that
   per-vertex lightning uses vertices to shade the mesh, so a wall consisting
   of one single quad won't shade the same way as a wall consisting of
   multiple quads. You'll need to find a balance or use per-pixel lightning.

-  You can have :ref:`multiple levels of detail <level-of-detail>` for your
   mesh.

-  If you have a high-poly model, you can create a low-poly version of it and
   generate a normal map from the high-poly model which you can assign to your
   low-poly version in Panda. Normal mapping requires lightning and the
   ShaderGenerator or a custom shader.

-  Sometimes it's possible to represent a mesh as a textured plane
   :ref:`billboard <billboard-effects>`. This can be combined with
   :ref:`LOD <level-of-detail>` by using a billboard for the lowest levels of
   detail.

-  If a lot of time is taken up by vertex animation, then you may obtain some
   benefit from enabling hardware skinning, which causes the vertex
   transformation to be performed on the GPU instead of the CPU. To enable this,
   set the following variables in your :ref:`Config.prc <configuring-panda3d>`::

      hardware-animated-vertices true
      basic-shaders-only false

   For this to work, you will need to have a shader applied that supports
   hardware skinning, or you need to have :ref:`the-shader-generator` enabled.
   Otherwise, Panda will silently continue to perform the animation on the CPU.

-  See if you can lower the
   :ref:`far distance or far plane <lenses-and-field-of-view>` of the camera
   lens. Anything farther than the far plane of the camera lens won't be
   rendered. You can use :ref:`fog <fog>` to hide the clipping.
