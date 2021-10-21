.. _softbody-tetrahedron:

Bullet Softbody Tetrahedron
===========================

The last kind of soft bodies are those made up from tetrahedral meshes. A
tetrahedral mesh is a mesh where the single elements are not triangles, but
tetrahedrons, that is "pyramids" with four corners. Tetrahedral meshes are
sometimes called "volume" meshes, since they fill out a volume and not just
the surface of the mesh.

Setup
-----

Setup for tetrahedral soft bodies is more complicated than the previously
shown soft body types, since we first have to get the data which describes a
tetrahedral mesh. Common 3D modelling packages usually don't support for
modelling tetrahedral meshes.

If we somehow have assumed the tetrahedral data we can set up the soft body
directly from the vertices and indices. Let's assume we have the vertices as a
list of triples (three times a floating point coordinate), and we have the
tetrahedron indices as a list of four-tuples (four indices make up one
tetrahedron).

.. only:: python

   .. code-block:: python

      points = [(x1, y1, z1), (x2, y2, z2), ...]
      elements = [(i0, i1, i2, i3), (i4, i5, i6, i7), ...]

      points = [Point3(x,y,z) * 3 for x,y,z in nodes]
      indices = sum([list(x) for x in elements], [])

      bodyNode = BulletSoftBodyNode.makeTetMesh(info, points, indices, True)

.. only:: cpp

   .. code-block:: cpp

      TODO

The third line just transform the list of coordinates into a list of Panda3D
points, and the fourth line transforms the list of four-tuples into a flat list
of indices.

Assuming we don't have the tetrahedral data prepared for us; in this case we
need to create it ourselves. A good tool for this purpose is "tetgen", which is
a tetrahedral mesh generator and Delaunay triangulator. The tetgen homepage is
https://www.berlios.de/software/tetgen/ . Panda3D Bullet module has support for
setting up soft bodies directly from tetgen mesh files:

.. only:: python

   .. code-block:: python

      ele = file('models/tetra.1.ele', 'r').read()
      face = file('models/tetra.1.face', 'r').read()
      node = file('models/tetra.1.node', 'r').read()

      bodyNode = BulletSoftBodyNode.makeTetMesh(info, ele, face, node)

.. only:: cpp

   .. code-block:: cpp

      TODO

Once the soft body is created we still have to set it up properly. The following
code snippet shows how to do so:

.. only:: python

   .. code-block:: python

      bodyNode.setName('Tetra')
      bodyNode.setVolumeMass(300)
      bodyNode.getShape(0).setMargin(0.01)
      bodyNode.getMaterial(0).setLinearStiffness(0.1)
      bodyNode.getCfg().setPositionsSolverIterations(1)
      bodyNode.getCfg().clearAllCollisionFlags()
      bodyNode.getCfg().setCollisionFlag(BulletSoftBodyConfig.CFClusterSoftSoft, True)
      bodyNode.getCfg().setCollisionFlag(BulletSoftBodyConfig.CFClusterRigidSoft, True)
      bodyNode.generateClusters(6)

      bodyNP = self.worldNP.attachNewNode(bodyNode)
      bodyNP.setPos(0, 0, 8)
      bodyNP.setHpr(45, 0, 0)
      world.attachSoftBody(bodyNode)

.. only:: cpp

   .. code-block:: cpp

      TODO

The method ``generateClusters`` is new. We didn't use this method so far when
setting up non-volume soft bodies. It splits the soft body volume up into the
given number of small, convex clusters, which consecutively will be used for
collision detection with other soft bodies or rigid bodies.

Visualisation
-------------

There are two different ways to visualise a tetrahedral soft body. First you can
let Panda3D generate a ``Geom`` for you, like in the previous two soft body
manual pages. The following code shows how to do this:

.. only:: python

   .. code-block:: python

      geom = BulletHelper.makeGeomFromFaces(node)
      visNode = GeomNode('TetraVisual')
      visNode.addGeom(geom)
      visNP = softNP.attachNewNode(visNode)
      bodyNode.linkGeom(geom)

.. only:: cpp

   .. code-block:: cpp

      TODO

The second way is to use an already existing model - maybe the model which has
been used to calculate the tetrahedron mesh - and link it to the soft body,
like the following code snippet shows. Panda3D will compare the vertices of the
model with the nodes of the soft body, and link each vertex to the closest soft
body node.

.. only:: python

   .. code-block:: python

      visNP = loader.loadModel('models/cube.egg')
      visNP.reparentTo(softNP)

      geom = visNP \
          .findAllMatches('**/+GeomNode').getPath(0).node() \
          .modifyGeom(0)
      bodyNode.linkGeom(geom)

.. only:: cpp

   .. code-block:: cpp

      TODO
