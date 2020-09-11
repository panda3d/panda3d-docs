.. _environment-mapping-with-cube-maps:

Environment Mapping with Cube Maps
==================================

Although there are other applications for cube maps, one very common use of cube
maps is as an environment map, similar to
:ref:`sphere mapping <simple-environment-mapping>`. In fact, it works very much
the same as sphere mapping.

Just as with a sphere map, you can have Panda3D generate a cube map for you:

.. code-block:: python

   scene = loader.loadModel('bvw-f2004--streetscene/street-scene.egg')
   scene.reparentTo(render)
   scene.setZ(-2)
   base.saveCubeMap('streetscene_cube_#.jpg', size = 256)

With the cube map saved out as above, you could apply it as an environment map
to the teapot like this:

.. code-block:: python

   tex = loader.loadCubeMap('streetscene_cube_#.jpg')
   teapot.setTexGen(TextureStage.getDefault(), TexGenAttrib.MEyeCubeMap)
   teapot.setTexture(tex)

And the result looks very similar to the sphere map:

|The cube map on a teapot.|

In fact, it looks so similar that one might wonder why we bothered. So far, a
cube map looks pretty similar to a sphere map, except that it consumes six times
the texture memory. Hardly impressive.

But as we mentioned :ref:`earlier <simple-environment-mapping>`, there are two
problems with sphere maps that cube maps can solve. One of these problems is
that the point-of-view is permanently baked into the sphere map. Cube maps don't
necessarily have the same problem. In fact, we can solve it with one simple
variation:

.. code-block:: python

   tex = loader.loadCubeMap('streetscene_cube_#.jpg')
   teapot.setTexGen(TextureStage.getDefault(), TexGenAttrib.MWorldCubeMap)
   teapot.setTexture(tex)

By changing ``MEyeCubeMap`` to ``MWorldCubeMap``, we have indicated that we
would like this cube map to vary its point-of-view as the camera moves. Now the
reflected environment will vary according to the direction we are looking at it,
so that it shows what is behind the camera at runtime, instead of always showing
the area behind the camera when the cube map was generated, as a sphere map must
do. In order for this to work properly, you should ensure that your camera is
unrotated (that is, :meth:`set_hpr(0, 0, 0) <.NodePath.set_hpr>`) when you
generate the cube map initially.

Even with MWorldCubeMap, though, the image is still generated ahead of time, so
the reflection doesn't actually show what is behind the camera at runtime. It
just uses the current camera direction to figure out what part of the reflection
image to show.

However, you can make a cube map that truly does reflect dynamic objects in the
scene, by rendering a :ref:`dynamic cube map <dynamic-cube-maps>`. This will be
discussed in the next section.

.. |The cube map on a teapot.| image:: cubemap-teapot.jpg
