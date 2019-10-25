.. _softbody-rope:

Bullet Softbody Rope
====================

Soft body ropes are best compared to chains of interconnected nodes. This page
deals with setup, visualization and attaching things to soft body ropes.

Setup
-----

The following code will create a soft body rope with 8 segments (variable
``res``), and thus 8 + 2 = 10 nodes. ``p1`` is the initial position of the first
node, and ``p2`` is the initial position of the last node. ``fixeds`` will be
explained later on this page.

.. only:: python

   .. code-block:: python

      from panda3d.bullet import BulletSoftBodyNode

      info = self.world.getWorldInfo()
      info.setAirDensity(1.2)
      info.setWaterDensity(0)
      info.setWaterOffset(0)
      info.setWaterNormal(Vec3(0, 0, 0))

      res = 8
      p1 = Point3(0, 0, 4)
      p2 = Point3(10, 0, 4)
      fixeds = 0

      bodyNode = BulletSoftBodyNode.makeRope(info, p1, p2, res, fixeds)
      bodyNode.setTotalMass(50.0)
      bodyNP = worldNP.attachNewNode(bodyNode)
      world.attachSoftBody(bodyNode)

.. only:: cpp

   .. code-block:: cpp

      TODO

Visualisation
-------------

So far we have a physical object, the soft body rope, but aside from the debug
renderer this object is not shown in our scene. We need something to visualize
the rope.

There are two ways of rendering the rope. First we can make use of a NURBS
curve, or we can simple render the rope using geom lines. First we have a look
at how to render the rope using geom lines.

.. only:: python

   .. code-block:: python

      from panda3d.core import GeomNode

      geom = BulletHelper.makeGeomFromLinks(bodyNode)

      visNode = GeomNode('')
      visNode.addGeom(geom)
      visNP = bodyNP.attachNewNode(visNode)

      bodyNode.linkGeom(geom)

.. only:: cpp

   .. code-block:: cpp

      TODO

The class ``BulletHelper`` has a convenience method which creates a ready-to-use
``Geom`` for us. We only need to wrap the ``Geom`` in a ``GeomNode``, and insert
it into the scene graph. Since we want the visualisation of the rope to be at
the same place as the rope we insert the ``GeomNode`` as a child of the
``BulletSoftBodyNode``.

There is just one thing missing. The ``GeomNode`` doesn't know that it is the
visualization of a soft body rope. When advancing the simulation time the soft
body rope will deform, but the visualization will always stay the way it has
been created. To fix this we can tell the soft body node that this particular
``Geom`` is it's visualization. The soft body node will now update the ``Geom``
each frame. This is done in the last line, by linking the geom to the soft body
node.

The result doesn't look very good. It's just a thin line. But instead of the
above code we can use a NURBS curve for visualization.

.. only:: python

   .. code-block:: python

      from panda3d.core import RopeNode
      from panda3d.core import NurbsCurveEvaluator

      curve = NurbsCurveEvaluator()
      curve.reset(res + 2)

      bodyNode.linkCurve(curve)

      visNode = RopeNode('')
      visNode.setCurve(curve)
      visNode.setRenderMode(RopeNode.RMTube)
      visNode.setUvMode(RopeNode.UVParametric)
      visNode.setNumSubdiv(4)
      visNode.setNumSlices(8)
      visNode.setThickness(0.4)
      visNP = self.worldNP.attachNewNode(visNode)
      visNP.setTexture(loader.loadTexture('some_texture.jpg'))

.. only:: cpp

   .. code-block:: cpp

      TODO

First we create a nurbs curve (``NurbsCurveEvaluator``), and then we link this
nurbs curve to the soft body rope node. The soft body node will update the nurbs
curve every frame from now on.

But we are not done yet. We still need to create something that can be seen in
the scene graph. A ``RopeNode`` can render a ``NurbsCurveEvaluator``. For
details on how to configure the ``RopeNode`` please refer to the Panda3D API
documentation; both the ``RopeNode`` and the ``NurbsCurveEvaluator`` are not
part of the panda3d.bullet, but core Panda3D classes.

Attaching the rope
------------------

Now we have created a rope, and we can render it. Next we want to attach the
rope to something, that is "glue" it either to some other object, usually a
rigid body, or to a specific position of the world.

At the beginning of this page we promised to deal with the ``fixeds`` parameter
later on the page. This is the place. Using the ``fixeds`` parameter we can
attach the rope to a position in the world (global coordinates!). Depending on
the value of this parameter we can attach different nodes/vertices of the rope:

-  0: No node/vertex is attached.
-  1: Only the first node/vertex is attached.
-  2: Only the last node/vertex is attached.
-  3: Both the first and the last node/vertex are attached.

Or we want to attach the soft body rope to a rigid body. In the following code
snippet the last node/vertex of a soft body rope is attached to a rigid body.

.. only:: python

   .. code-block:: python

      # NodePath for some BulletSoftBody "rope"
      softNP = ...

      # NodePath for some BulletRigidBody
      rigidNP = ...

      # Index of the last node of the rope
      idx = softNP.node().getNumNodes() - 1

      # Attach the last node of the rope with the rigid body
      softNP.node().appendAnchor(idx, rigidNP.node())

.. only:: cpp

   .. code-block:: cpp

      TODO
