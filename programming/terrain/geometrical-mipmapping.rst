.. _geometrical-mipmapping:

Geometrical MipMapping
======================

The GeoMipTerrain generates terrain geometry from a heightfield image, but it
does more than any bruteforce terrain generator: the GeoMipTerrain divides the
terrain into multiple chunks, where each of them can have a different level of
detail. The advantage of this approach is that, when the focal point (the place
where the terrain has the highest quality, probably the camera) moves, not the
entire terrain has to be regenerated to match the correct detail level, like the
:ref:`HeightfieldTesselator <heightfield-tesselator>`, but only the chunks that
have a different LOD can be regenerated. Also, it improves culling and collision
detection.

Basic Usage
~~~~~~~~~~~

Using the GeoMipTerrain is quite easy, it does not require to write many
complicated calculations:

.. only:: python

   .. code-block:: python

      terrain = GeoMipTerrain("mySimpleTerrain")
      terrain.setHeightfield("yourHeightField.png")
      #terrain.setBruteforce(True)
      terrain.getRoot().reparentTo(render)
      terrain.generate()

.. only:: cpp

   .. code-block:: cpp

      GeoMipTerrain terrain("mySimpleTerrain");
      terrain.set_heightfield(Filename("maps/yourHeightField.png"));
      terrain.set_bruteforce(true);
      terrain.get_root().reparent_to(window->get_render());
      terrain.generate();

First, the code creates a GeoMipTerrain instance. The
:meth:`~.GeoMipTerrain.set_heightfield()` call loads in a heightfield image.
Preferably this is a size of a power of two plus one (like 129, 257, 513, 1025,
etc.), but if it is not, the GeoMipTerrain will automatically scale it up to the
nearest correct size (which is quite slow).
:meth:`~.GeoMipTerrain.set_heightfield()` can take a
:ref:`PNMImage <creating-new-textures-from-scratch>`, Texture or a path
according to the :ref:`filename-syntax`.

The :meth:`set_bruteforce(True) <.GeoMipTerrain.set_bruteforce>` call sets the
terrain to bruteforce rendering -- this means that the terrain is created at the
highest quality (the lowest detail level), and LOD is not applied.
In the next section we will explain how to set a LOD level and a Focal Point.
The :meth:`~.GeoMipTerrain.get_root()` call returns the NodePath of the terrain.
It is then reparented to ``render`` to be a part of the scene graph. You can
apply :ref:`common-state-changes` to this NodePath.
Finally, the :meth:`~.GeoMipTerrain.generate()` call generates the terrain
geometry. Note that if the terrain is still quite flat, you will have to scale
the terrain NodePath in the Z direction, because by default, the Z positions are
between 0 and 1. To fix this, scale the terrain up in the Z direction (before
generating it, otherwise it might require you to regenerate it):

.. only:: python

   .. code-block:: python

      terrain.getRoot().setSz(100)

.. only:: cpp

   .. code-block:: cpp

      terrain.get_root().set_sz(100);

Dynamic Terrains
~~~~~~~~~~~~~~~~

This code shows a dynamically updated terrain with LOD:

.. only:: python

   .. code-block:: python

      # Set up the GeoMipTerrain
      terrain = GeoMipTerrain("myDynamicTerrain")
      terrain.setHeightfield("yourHeightField.png")

      # Set terrain properties
      terrain.setBlockSize(32)
      terrain.setNear(40)
      terrain.setFar(100)
      terrain.setFocalPoint(base.camera)

      # Store the root NodePath for convenience
      root = terrain.getRoot()
      root.reparentTo(render)
      root.setSz(100)

      # Generate it.
      terrain.generate()

      # Add a task to keep updating the terrain
      def updateTask(task):
          terrain.update()
          return task.cont

      taskMgr.add(updateTask, "update")

.. only:: cpp

   .. code-block:: cpp

      // Set up the GeoMipTerrain
      GeoMipTerrain terrain("myDynamicTerrain");
      terrain.set_heightfield(Filename("maps/yourHeightField.png"));

      // Set terrain properties
      terrain.set_block_size(32);
      terrain.set_near(40);
      terrain.set_far(100);
      terrain.set_focal_point(camera);

      // Store the root NodePath for convenience
      NodePath root = terrain.get_root();
      root.reparent_to(window->get_render());
      root.set_sz(100);

      // Generate it.
      terrain.generate();

      // Add a task to keep updating the terrain
      taskMgr->add(new GenericAsyncTask("Updates terrain", &UpdateTerrain, nullptr));

      // And the task, outside main:
      AsyncTask::DoneStatus UpdateTerrain(GenericAsyncTask *task, void *data) {
        terrain.update();
        return AsyncTask::DS_cont;
      }

This code shows a dynamically updated terrain, which is updated every frame with
the camera as focal point. You see that a few functions are called: The
blocksize is set to 32. This means that GeoMipTerrain has to divide the terrain
in chunks of 32x32 quads. Then, the near and far distances are set. The Near
distance is the distance from the focal point to where the terrain starts to
decrease in quality. The far clip is the distance where the terrain is lowest
quality. Also, the focal point is set to the Camera's NodePath; you can specify
any NodePath you want, but also a Point2 or Point3. If you specify the latter,
please note that only the X and Y positions are used to calculate the distance;
the Z position is disregarded. Note that you need to experiment with those
values to get a good quality terrain while still maintaining a good performance.

Next, for convenience, the terrain root is stored in a separate variable, which
is scaled and placed in the scene graph. The terrain is then initially
generated, and a task is created which calls
:meth:`terrain.update() <.GeoMipTerrain.update>` every frame. This function
calculates the new LOD levels based on the movement of the focal point and
updates the chunks which have got a new LOD level.

Advanced Control
~~~~~~~~~~~~~~~~

The GeoMipTerrain provides some advanced features over the terrain:

Minimum Level
-------------

You can specify a minimum LOD level to GeoMipTerrain. You can do this if you
find the terrain a bit too high quality near the focal point, and this could
waste your performance. If you set a minimum LOD level, you can prevent this and
force the chunks to have a minimum level of detail:


.. only:: python

   .. code-block:: python

      terrain.setMinLevel(2)

.. only:: cpp

   .. code-block:: cpp

      terrain.set_min_level(2);

If you make the value higher, it will decrease the quality level near the focal
point.

Automatic Flattening
--------------------

Since flattening the terrain root might interfere with the updating system,
GeoMipTerrain provides an auto-flattening function, which can be really useful
if you have :ref:`too many meshes <too-many-meshes>` in your scene. This
function calls one of NodePath's flattening functions every time the terrain is
regenerated, and each time before the chunks are modified the terrain is
restored from a backup node:

.. only:: python

   .. code-block:: python

      terrain.setAutoFlatten(GeoMipTerrain.AFMStrong)

.. only:: cpp

   .. code-block:: cpp

      terrain.set_auto_flatten(GeoMipTerrain::AFM_strong);

There are multiple options: AFM_strong for :meth:`~.NodePath.flatten_strong()`,
AFM_medium for :meth:`~.NodePath.flatten_medium()`, AFM_light for
:meth:`~.NodePath.flatten_light()`, and AFM_off for no flattening at all.
After setting the AutoFlattenMode, GeoMipTerrain will automatically take care of
it at the next :meth:`~.GeoMipTerrain.update()` call.

Notes
~~~~~

-  For a full function overview, see the :class:`~panda3d.core.GeoMipTerrain`
   page in the API Reference.

-  The GeoMipTerrain generates texture coordinates between 0 and 1, making the
   texture stretched over the entire terrain. If you are using a shader, please
   do not directly base the coordinates on the ``vtx_position``, because since
   the terrain can have multiple chunks the vertex position is relative to the
   chunk. Instead, base your shader calculations on the ``vtx_texcoord0``
   generated by the GeoMipTerrain.

-  The GeoMipTerrain class implements part of the GeoMipMapping algorithm,
   described in
   `this paper <https://www.flipcode.com/archives/article_geomipmaps.pdf>`__ by
   Willem H. de Boer.
