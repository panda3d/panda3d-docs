.. _collision-shapes:

Bullet Collision Shapes
=======================

On the previous page we have been introduced to Bullet basics. Two simple
collision shapes - a box and a plane - have been used in this simple script.
This page will now introduce more collision shapes provided by Bullet, starting
with primitive shapes and then moving on to more complex ones.

Primitive shapes:

-  Sphere Shape
-  Plane Shape
-  Box Shape
-  Cylinder Shape
-  Capsule Shape
-  Cone Shape

Complex shapes:

-  Compound Shape
-  Convex Hull Shape
-  Triangle Mesh Shape
-  Heightfield Shape
-  Soft Body Shape
-  Multi Sphere Shape
-  Convex Point Cloud Shape

Sphere Shape
------------

The most basic collision shape, a sphere with radius radius. The sphere is
centered around its origin.

.. only:: python

   .. code-block:: python

      from panda3d.bullet import BulletSphereShape
      radius = 0.5
      shape = BulletSphereShape(radius)

.. only:: cpp

   .. code-block:: cpp

      #include "bulletSphereShape.h"
      ...
      double radius = 0.5;
      PT(BulletSphereShape) sphere_shape = new BulletSphereShape(radius);

Plane Shape
-----------

Another primitive collision shape, an infinite plane. To create a plane you
have to pass both the plane's normal vector (Vec3(nx, ny, nz)) and the plane
constant (d, which is the distance of the plane's origin. Planes can only be
used for static objects.

.. only:: python

   .. code-block:: python

      from panda3d.bullet import BulletPlaneShape
      normal = Vec3(0, 0, 1)
      d = 0
      shape = BulletPlaneShape(normal, d)

.. only:: cpp

   .. code-block:: cpp

      #include "bulletPlaneShape.h"
      ...
      LVecBase3 normal(0, 0, 1);
      double d = 1;
      PT(BulletPlaneShape) floor_shape = new BulletPlaneShape(normal, d);
      ...

Box Shape
---------

A box-shaped primitive collision shape. To create a box you have to pass a
vector with the half-extents (Vec3(dx, dx, dx)). The full extents of the box
will be twice the half extents, e. g. from -dx to +dx on the local x-axis.

.. only:: python

   .. code-block:: python

      from panda3d.bullet import BulletBoxShape
      dx = 0.5
      dy = 0.5
      dz = 1.0
      shape = BulletBoxShape(Vec3(dx, dy, dz))

.. only:: cpp

   .. code-block:: cpp

      #include "bulletBoxShape.h"
      ...
      double dx = 0.5;
      double dy = 0.5;
      double dz = 0.5;
      PT(BulletBoxShape) box_shape = new BulletBoxShape(LVecBase3(dx, dy, dz));

Cylinder Shape
--------------

A primitive collision shape which is represents a cylinder. We can create a
cylinder shape by either passing it's radius, height and cylinder axis, or by
passing a vector with half extents and the cylinder axis. The following
example creates two cylinder shapes, both with radius 0.5 and height 1.4.

.. only:: python

   .. code-block:: python

      from panda3d.bullet import BulletCylinderShape
      radius = 0.5
      height = 1.4
      shape1 = BulletCylinderShape(radius, height, ZUp)
      shape2 = BulletCylinderShape(Vec3(radius, 0, 0.5 * height), ZUp)

.. only:: cpp

   .. code-block:: cpp

      #include "bulletCylinderShape.h"
      ...
      double radius = 0.5;
      double height = 1.4;
      PT(BulletCylinderShape) cylinder_shape_one = new BulletCylinderShape(radius, height);

Capsule Shape
-------------

A primitive collision shape which is a "capped" cylinder. "Capped" means that
there are half-spheres at both ends, unlike the real cylinder which has flat
ends. Capsule shapes are a good choice for character controllers, since they
are fast, symmetrical, and allow smooth movement over steps.

To create a capsule shape we have to pass the capsule's radius, the height of
the cylindrical part, and the up-axis. The total height of the capsule will be
the height of the cylindrical part, plus twice the radius.

.. only:: python

   .. code-block:: python

      from panda3d.bullet import BulletCapsuleShape
      radius = 0.5
      height = 1.0
      shape = BulletCapsuleShape(radius, height, ZUp)

.. only:: cpp

   .. code-block:: cpp

      #include "bulletCapsuleShape.h"
      ...
      double radius = 0.5;
      double height = 1.0;
      PT(BulletCapsuleShape) capsule_shape = new BulletCapsuleShape(radius, height);

Cone Shape
----------

Again a primitive collision shape, which represents a cone. We have to pass
the radius of the circular base of the cone, and it's height.

.. only:: python

   .. code-block:: python

      from panda3d.bullet import BulletConeShape
      radius = 0.6
      height = 1.0
      shape = BulletConeShape(radius, height, ZUp)

.. only:: cpp

   .. code-block:: cpp

      #include "bulletConeShape.h"
      ...
      double radius = 0.6;
      double height = 1.0;
      PT(BulletConeShape) cone_shape = new BulletConeShape(radius, height);

Compound Shape
--------------

Compound shapes are assemblies made up from two or more individual shapes. For
example you could create a collision shape for a table from five box shapes.
One "flat" box for the table plate, and four "thin" ones for the table legs.

The Panda3D Bullet module has no specialized class for compound shapes. It
automatically creates a compound shape if more than one shape is added to a
body node.

The following code snippet will create such a compound shape, resembling the
before mentioned table.

.. only:: python

   .. code-block:: python

      shape1 = BulletBoxShape((1.3, 1.3, 0.2))
      shape2 = BulletBoxShape((0.1, 0.1, 0.5))
      shape3 = BulletBoxShape((0.1, 0.1, 0.5))
      shape4 = BulletBoxShape((0.1, 0.1, 0.5))
      shape5 = BulletBoxShape((0.1, 0.1, 0.5))

      bodyNP.node().addShape(shape1, TransformState.makePos(Point3(0, 0, 0.1)))
      bodyNP.node().addShape(shape2, TransformState.makePos(Point3(-1, -1, -0.5)))
      bodyNP.node().addShape(shape3, TransformState.makePos(Point3(-1, 1, -0.5)))
      bodyNP.node().addShape(shape4, TransformState.makePos(Point3(1, -1, -0.5)))
      bodyNP.node().addShape(shape5, TransformState.makePos(Point3(1, 1, -0.5)))

.. only:: cpp

   .. code-block:: cpp

      PT(BulletBoxShape) shape1 = new BulletBoxShape(LVecBase3(0.1, 0.1, 0.5));
      PT(BulletBoxShape) shape2 = new BulletBoxShape(LVecBase3(0.1, 0.1, 0.5));
      PT(BulletBoxShape) shape3 = new BulletBoxShape(LVecBase3(0.1, 0.1, 0.5));
      PT(BulletBoxShape) shape4 = new BulletBoxShape(LVecBase3(0.1, 0.1, 0.5));
      PT(BulletBoxShape) shape5 = new BulletBoxShape(LVecBase3(0.1, 0.1, 0.5));

      np_body.node().add_shape(shape1, TransformState::make_pos(LPoint3(0, 0, 0.1)));
      np_body.node().add_shape(shape2, TransformState::make_pos(LPoint3(-1, -1 ,-0.5)));
      np_body.node().add_shape(shape3, TransformState::make_pos(LPoint3(-1, 1, -0.5)));
      np_body.node().add_shape(shape4, TransformState::make_pos(LPoint3(1, -1 ,-0.5)));
      np_body.node().add_shape(shape5, TransformState::make_pos(LPoint3(1, 1, -0.5)));

Convex Hull Shape
-----------------

The first of the non-primitive collision shapes. A good analogy for a convex
hull is an elastic membrane or balloon under pressure which is placed around a
given set of vertices. When released the membrane will assume the shape of the
convex hull. Convex hull shapes should be used for dynamic objects, if it is
not possible to find a good approximation of the objects shape using collision
primitives.

Convex hull shapes can be created is several ways:

.. only:: python

   .. code-block:: python

      from panda3d.bullet import BulletConvexHullShape

      # Add each vertex separately
      shape1 = BulletConvexHullShape()
      shape1.addPoint(Point3(1, 1, 2))
      shape1.addPoint(Point3(0, 0, 0))
      shape1.addPoint(Point3(2, 0, 0))
      shape1.addPoint(Point3(0, 2, 0))
      shape1.addPoint(Point3(2, 2, 0))

      # Add several vertices with a single call
      shape2 = BulletConvexHullShape()
      shape2.addArray([
         Point3(1, 1, 2),
         Point3(0, 0, 0),
         Point3(2, 0, 0),
         Point3(0, 2, 0),
         Point3(2, 2, 0),
      ])

      # Add all vertices which can be found in a Geom object
      geomNodes = loader.loadModel(path).findAllMatches('**/+GeomNode')
      geomNode = geomNodes.getPath(0).node()
      geom = geomNode.getGeom(0)
      shape3 = BulletConvexHullShape()
      shape3.addGeom(geom)

.. only:: cpp

   .. code-block:: cpp

      #include "bulletConvexHullShape.h"
      ...

      // Add each vertex separately
      PT(BulletConvexHullShape) convex_hull_shape = new BulletConvexHullShape();
      convex_hull_shape->add_point(LPoint3(1, 1, 2));
      convex_hull_shape->add_point(LPoint3(0, 0, 0));
      convex_hull_shape->add_point(LPoint3(2, 0, 0));
      convex_hull_shape->add_point(LPoint3(0, 2, 0));
      convex_hull_shape->add_point(LPoint3(2, 2, 0));

Triangle Mesh Shape
-------------------

Another non-primitive collision shape. A triangle mesh shape is similar to the
convex hull shape, except that it is not restricted to convex geometry; it can
contain concave parts. A typical use case for triangle mesh shapes is the
static geometry of a game level. However, it is possible to use triangle mesh
shapes for dynamic objects too. We have to explicitly tell Bullet if we want a
static or dynamic triangle mesh shape at the time the shape is created.

To create a triangle mesh shape, we first have to create a triangle mesh
object. The following example will create a simple quad composed of two
triangles.

.. only:: python

   .. code-block:: python

      from panda3d.bullet import BulletTriangleMeshShape
      p0 = Point3(-10, -10, 0)
      p1 = Point3(-10, 10, 0)
      p2 = Point3(10, -10, 0)
      p3 = Point3(10, 10, 0)
      mesh = BulletTriangleMesh()
      mesh.addTriangle(p0, p1, p2)
      mesh.addTriangle(p1, p2, p3)
      shape = BulletTriangleMeshShape(mesh, dynamic=False)

.. only:: cpp

   .. code-block:: cpp

      #include "bulletTriangleMesh.h"
      ...
      LPoint3 points_array[4] = {
          LPoint3(-10, -10, 0),
          LPoint3(-10, 10, 0),
          LPoint3(10, -10, 0),
          LPoint3(10, 10, 0),
      };

      PT(BulletTriangleMesh) triangle_mesh = new BulletTriangleMesh;
      triangle_mesh->add_triangle(points_array[0], points_array[1], points_array[2]);
      triangle_mesh->add_triangle(points_array[1], points_array[2], points_array[3]);

      PT(BulletTriangleMeshShape) triangle_mesh_shape = new BulletTriangleMeshShape(triangle_mesh, false);

We can use a convenience method to add all triangles from a Geom object with
one method call. The geom will be decomposed first, so it does not have to
contain only triangles; for example, it can contain triangle strips too.

.. only:: python

   .. code-block:: python

      from panda3d.bullet import BulletTriangleMesh
      mesh = BulletTriangleMesh()
      mesh.addGeom(geom)

.. only:: cpp

   .. code-block:: cpp

      #include "bulletTriangleMesh.h"
      ...
      PT(BulletTriangleMesh) triangle_mesh = new BulletTriangleMesh();
      triangle_mesh->add_geom(geom);

Heightfield Shape
-----------------

A special non-primitive collision shape. Give a heightfield image we can
construct a terrain mesh with only a few lines of code.

.. only:: python

   .. code-block:: python

      from panda3d.core import Filename
      from panda3d.core import PNMImage
      from panda3d.bullet import BulletHeightfieldShape
      from panda3d.bullet import ZUp
      height = 10.0
      img = PNMImage(Filename('elevation.png'))
      shape = BulletHeightfieldShape(img, height, ZUp)

.. only:: cpp

   .. code-block:: cpp

      #include "pnmImage.h"
      #include "bulletHeightfieldShape.h"

      PNMImage pnm_image;
      pnm_image.read(Filename("models/elevation.png"));

      PT(BulletHeightfieldShape) heightfield_shape = new BulletHeightfieldShape(*pnm_image, height);

The heightfield shape will be oriented the same way as a GeoMipTerrain created
from the same image, but GeoMipTerrain and BulletHeightfieldShape have
different origins. The BulletHeightfieldShape is centered around the origin,
while the GeoMipTerrain uses the lower left corner as its origin. However,
this can be easily corrected by positioning the GeoMipTerrain with an offset
relative to the static rigid body node.

If you are using ShaderTerrainMesh, then you need to use a Texture object as a
height map. This will ensure that the shape of the physical body corresponds to
the visible geometry.

.. only:: python

   .. code-block:: python

      from panda3d.core import Filename
      offset = img.getXSize() / 2.0 - 0.5
      terrain = GeoMipTerrain('terrain')
      terrain.setHeightfield(img)
      terrainNP = terrain.getRoot()
      terrainNP.setSz(height)
      terrainNP.setPos(-offset, -offset, -height / 2.0)

.. only:: cpp

   .. code-block:: cpp

      GeoMipTerrain *terrain = get_geomip_terrain();
      terrain->set_heightfield(*pnm_image);
      terrain->set_block_size(32);
      terrain->set_near(50);
      terrain->set_far(100);
      terrain->set_focal_point(window->get_camera_group());

      NodePath terrain_root = terrain->get_root();

      float offset = pnm_image->get_x_size() / 2.0 - 0.5;
      terrain_root.set_pos(-offset, -offset, -height / 2.0);

      terrain_root.set_scale(terrain_root.get_scale().get_x(), terrain_root.get_scale().get_y(), height);
      terrain_root.reparent_to(window->get_render());

Soft Body Shape
---------------

This special collision shape is used in connection with soft bodies. It can
not be created directly. Soft bodies will be discussed later within this
manual.
