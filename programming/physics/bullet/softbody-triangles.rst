.. _softbody-triangles:

Bullet Softbody Triangles
=========================

Soft bodies made from triangular meshes are similar to soft body patches. just
that they are not restricted to rectangular meshes; any two-dimensional triangle
mesh will do. An interesting use case for such a soft body is a triangular mesh
which is closed. Bullet supports simulation of a pressure for the volume
captured inside such a soft body.

Setup
-----

The following code snippet shows how to setup an gas-filled soft body. Instead
of defining the triangle mesh ourselves we use the convenience method
``makeEllipsoid``, which returns a ready-to-use soft body with the shape of an
ellipsoid. The last parameter to this convenience method is the "resolution" of
the ellipsoid. The soft body will have more faces if raising this value.
Increasing the value will make the soft body more realistic, but it also
requires more performance to simulate the soft body.

.. only:: python

   .. code-block:: python

      # Soft body world information
      info = world.getWorldInfo()
      info.setAirDensity(1.2)
      info.setWaterDensity(0)
      info.setWaterOffset(0)
      info.setWaterNormal(Vec3(0, 0, 0))

      # Softbody
      center = Point3(0, 0, 0)
      radius = Vec3(1, 1, 1) * 1.5

      bodyNode = BulletSoftBodyNode.makeEllipsoid(info, center, radius, 128)
      bodyNode.setName('Ellipsoid')
      bodyNode.getMaterial(0).setLinearStiffness(0.1)
      bodyNode.getCfg().setDynamicFrictionCoefficient(1)
      bodyNode.getCfg().setDampingCoefficient(0.001)
      bodyNode.getCfg().setPressureCoefficient(1500)
      bodyNode.setTotalMass(30, True)
      bodyNode.setPose(True, False)

      bodyNP = render.attachNewNode(bodyNode)
      bodyNP.setPos(15, 0, 12)
      bodyNP.setH(90.0)
      world.attachSoftBody(bodyNP.node())

.. only:: cpp

   .. code-block:: cpp

      TODO

When comparing the soft body setup with the previous page, the soft body patch
setup, we will find that there are two differences:

-  First, there are three lines which get the configuration objects for this
   soft body (``getCfg``), and then set different parameters on this
   configuration object, in particular the "pressure coefficient". For more
   detailed information on what these parameters do it is best to fall back to
   the original Bullet documentation. A mapping between the original Bullet
   members of the btSoftBodyConfig class and the Panda3D BulletSoftBodyConfig
   object returned by ``getCfg`` is given on the manual page
   :ref:`softbody-config`.

-  Second, the method ``setPose`` is called. This method sets the current state
   of the soft body as a "default pose" or "lowest energy state". The soft body
   will try to return to this state if possible. The first parameter to this
   method is the volume flag, and the second parameter the frame flag. It is
   usually the best thing to set both flags to ``True``.

Visualisation
-------------

Again, in order to have a visual representation of the soft body we need a
``GeomNode``. We can use almost the same code as we have been using for soft
body patches. The only difference is that we don't need to make the created
geometry two-sided, since the inside of the closed mesh is usually not visible.

.. only:: python

   .. code-block:: python

      from panda3d.core import GeomVertexFormat
      from panda3d.bullet import BulletHelper

      fmt = GeomVertexFormat.getV3n3t2()
      geom = BulletHelper.makeGeomFromFaces(bodyNode, fmt)
      bodyNode.linkGeom(geom)
      visNode = GeomNode('EllipsoidVisual')
      visNode.addGeom(geom)
      visNP = bodyNP.attachNewNode(visNode)

.. only:: cpp

   .. code-block:: cpp

      TODO
