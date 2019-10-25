.. _softbody-patch:

Bullet Softbody Patch
=====================

Soft body patches are two-dimensional rectangular meshes, which can be used to
simulate for example a flag, a tapestry, or sheets of paper.

Setup
-----

Setting up a soft body patch is similar to soft body ropes, but a few extra
settings have to be done. The following code will create rectangular path with
31 by 31 segments, and thus 32 x 32 nodes.

.. only:: python

   .. code-block:: python

      from panda3d.bullet import BulletSoftBodyNode

      info = self.world.getWorldInfo()
      info.setAirDensity(1.2)
      info.setWaterDensity(0)
      info.setWaterOffset(0)
      info.setWaterNormal(Vec3(0, 0, 0))

      resx = 31
      resy = 31

      p00 = Point3(-8, -8, 0)
      p10 = Point3( 8, -8, 0)
      p01 = Point3(-8,  8, 0)
      p11 = Point3( 8,  8, 0)

      fixeds = 1+2+4+8
      gendiags = True

      bodyNode = BulletSoftBodyNode.makePatch(info, p00, p10, p01, p11, resx, resy, fixeds, gendiags)

      material = bodyNode.appendMaterial()
      material.setLinearStiffness(0.4)
      bodyNode.generateBendingConstraints(2, material)

      bodyNode.setTotalMass(50.0)
      bodyNode.getShape(0).setMargin(0.5)
      bodyNP = self.worldNP.attachNewNode(bodyNode)
      world.attachSoftBody(bodyNode)

.. only:: cpp

   .. code-block:: cpp

      TODO

First we have to configure the soft body world properties, like we did for
soft body ropes too. Next we define variables for the resolution in x- and
y-direction, and for the four corner points of the patch.

The variable fixeds is set to the value 1+2+4+8=15, meaning that the patch
should be attached to the world on all four corners. To attach it to the first
and third corner (diagonal) we would set the value to 1+8=9, and to not attach
it at all we would set it to 0.

Now we can create the soft body node using the factory method
``makePatch``. The following
configuration differs from what we have seen for soft body ropes.

-  First we create an additional material attached to the soft body. Initially
   a soft body has already one material, but for this example we want a second
   one.
-  On the material we set the linear stiffness, and the create bending
   constraints for this material.
-  Finally we choose a value of about the grid spacing for the soft bodies
   margin. Other bodies colliding with the soft body could fall through in
   between the nodes if the value is too small, and if it is too large they
   will already collide with the soft body when still noticeably far away.

Visualisation
-------------

In order to have a visual representation of the soft body patch we need a
``GeomNode``. Panda3D's Bullet
module has a helper method which will do the work for us. The following code
snippet shows how use this helper method.

.. only:: python

   .. code-block:: python

      from panda3d.core import GeomVertexFormat
      from panda3d.bulletimport BulletHelper

      fmt = GeomVertexFormat.getV3n3t2()
      geom = BulletHelper.makeGeomFromFaces(bodyNode, fmt, True)
      bodyNode.linkGeom(geom)
      visNode = GeomNode('')
      visNode.addGeom(geom)
      visNP = bodyNP.attachNewNode(visNode)

.. only:: cpp

   .. code-block:: cpp

      TODO

The third parameter to ``makeGeomFromFaces``
is set to ``True``, making the
created geometry be two-sided. If set to
``False`` we would get a
one-sided geometry, which might be enough, depending on your requirements.

So far the generated geometry has no texture and no texture coordinates. But
the texture has already a column for texcoords, so we just need to write
texcoords using a ``GeomVertexRewriter``. The
following code shows a convenience method which will do this for us.

.. only:: python

   .. code-block:: python

      tex = loader.loadTexture('models/panda.jpg')
      visNP.setTexture(tex)
      BulletHelper.makeTexcoordsForPatch(geom, resx, resy)

.. only:: cpp

   .. code-block:: cpp

      TODO

Note: It is also possible to render soft body patches using a
``NurbsSurfaceEvaluator`` and
``SheetNode``, but results are
usually better when rendering patches directly, that is using linked
``Geom``.
