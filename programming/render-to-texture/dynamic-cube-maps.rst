.. _dynamic-cube-maps:

Dynamic Cube Maps
=================

.. only:: python

   Since the six faces of a cube map are really just six different views of a
   scene from the same point, it's possible to generate a cube map automatically
   by rendering these six different views at runtime.

   This is really just a form of offscreen rendering to a texture. Instead of
   rendering just one 2-D texture image, though, rendering a dynamic cube map
   means rendering six different 2-D images, one for each face of a cube map
   texture.

   Panda3D makes this easy for you. To start rendering a dynamic cube map,
   simply call:

   .. code-block:: python

      rig = NodePath('rig')
      buffer = base.win.makeCubeMap(name, size, rig)

   This will return an offscreen ``GraphicsBuffer`` that will be used to render
   the cube map. The three required parameters to ``makeCubeMap()`` are:

   name
      An arbitrary name to assign to the cube map and its associated
      ``GraphicsBuffer``. This can be any string.
   size
      The size in pixels of one side of the cube. Many graphics cards require
      this size to be a power of two. Some cards don’t *require* a power of two,
      but will perform very slowly if you give anything else.
   rig
      The camera rig node. This should be a new ``NodePath``. It will be filled
      in with six cameras. See below.

   There are also additional, optional parameters to ``makeCubeMap()``:

   cameraMask
      This specifies the ``DrawMask`` that is associated with the cube map’s
      cameras. This is an advanced Panda3D feature that can be used to hide or
      show certain objects specifically for the cube map cameras.
   toRam
      This is a boolean flag that, when True, indicates the texture image will
      be made available in system RAM, instead of leaving it only in texture
      memory. The default is False. Setting it True is slower, but may be
      necessary if you want to write out the generated cube map image to disk.

   Note that we passed a new ``NodePath``, called ``rig`` in the above example,
   to the ``makeCubeMap()`` call. This ``NodePath`` serves as the "camera rig";
   the ``makeCubeMap()`` method will create six cameras facing in six different
   directions, and attach them all to the camera rig. Thus, you can parent this
   rig into your scene and move it around as if it were a six-eyed camera.
   Normally, for environment maps, you would parent the rig somewhere within
   your shiny object so it can look out of the shiny object and see the things
   that should be reflected in it.

   The actual cube map itself be retrieved with the call:

   .. code-block:: python

      tex = buffer.getTexture()

   You can apply the texture to geometry as in the
   :ref:`previous example <environment-mapping-with-cube-maps>`. You should use
   the ``MWorldCubeMap`` mode to generate texture coordinates for your geometry
   since the camera rig will have a :ref:`CompassEffect <compass-effects>` on it
   to keep it unrotated with respect to ``render``.

   When you are done with the cube map, you should remove its buffer (and stop
   the cube map from continuing to render) by calling:

   .. code-block:: python

      base.graphicsEngine.removeWindow(buffer)

   As a complete example, here is how we might load up a dynamic cube map
   environment on our teapot and move the teapot down the street to show off the
   dynamic reflections:

   .. code-block:: python

      scene = loader.loadModel('bvw-f2004--streetscene/street-scene.egg')
      scene.reparentTo(render)
      scene.setZ(-2)

      teapot = loader.loadModel('teapot.egg')
      teapot.reparentTo(render)

      rig = NodePath('rig')
      buffer = base.win.makeCubeMap('env', 64, rig)
      rig.reparentTo(teapot)

      teapot.setTexGen(TextureStage.getDefault(), TexGenAttrib.MWorldCubeMap)
      teapot.setTexture(buffer.getTexture())

      zoom = teapot.posInterval(5, VBase3(20, 0, 0), startPos=VBase3(-20, 0, 0))
      zoom.loop()

   .. warning::

      When you render a dynamic cube map, don't forget that you are re-rendering
      your scene *six times* every frame in addition to the main frame render.
      If you are not careful, and if you have a complex scene, then you could
      easily end up reducing your frame rate by a factor of seven.

      It is a good idea to limit the amount of geometry that you render in the
      cube map. One simple way to do this is to ensure that the
      :ref:`far plane <lenses-and-field-of-view>` on the cube map cameras is set
      relatively close in. Since all of the cube map cameras share the same
      lens, you can adjust the near and far plane of all of the cameras at once
      like this:

      .. code-block:: python

         lens = rig.find('**/+Camera').node().getLens()
         lens.setNearFar(1, 100)

      It is especially important when you are using cube maps that you structure
      your scene graph hierarchically and divide it up spatially so that Panda3D's
      view-frustum culling can do an effective job of eliminating the parts of the
      scene that are behind each of the six cameras. (Unfortunately, the street-
      scene model used in the above example is not at all well-structured, so the
      example performs very poorly on all but the highest-end hardware.)

      It's also usually a good idea to keep the cube map size (the ``size``
      parameter to ``makeCubeMap()``) no larger than it absolutely has to be to get
      the look you want.

      You can also take advantage of the ``DrawMask`` to hide things from the cube
      cameras that are not likely to be important in the reflections. The
      documentation for this advanced feature of Panda3D will be found in another
      section of the manual (which, as of the time of this writing, has yet to be
      written).

      Finally, you can temporarily disable the cube map rendering from time to time
      if you know the environment won't be changing for a little while. The cube
      map will retain its last-rendered image. You can do this with
      ``buffer.setActive(0)``. Use ``buffer.setActive(1)`` to re-activate it.

.. only:: cpp

