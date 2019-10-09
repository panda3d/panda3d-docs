.. _basic-performance-diagnostics:

Basic Performance Diagnostics
=============================

Introductory Performance Diagnostics
------------------------------------

In Panda3D, the "big gun" of performance analysis is called pstats. This program
gives you real-time diagnostic analysis of a running Panda3D virtual world
broken down into hundreds of different categories.

But sometimes, when you've just encountered a problem, you don't want that much
information. Sometimes, you just want a simple question answered, like "how many
meshes do I have," or "is this a fill-rate problem?" For simple questions like
that, there are lots of things you can do to get a quick-and-dirty answer.

The Frame-Rate Meter
--------------------

The frame-rate meter doesn't tell you why your program is running slow, but it
does have one important purpose: it's a lightweight and unobtrusive utility that
you can leave on throughout the entire development process. This is valuable in
that it gives you immediate feedback when you do something inefficient. To turn
on the frame-rate meter, put this in your config file::

   show-frame-rate-meter #t

Or, if you want to have it set at run-time:

.. code-block:: python

   base.setFrameRateMeter(True)

The Scene Analyzer
------------------

If a scene needs to be rendered and has multiple nodes, Panda has to send each
node to the graphics hardware as a separate batch of polygons (because the nodes
might move independently, or have different state changes on them). Modern
graphics hardware hasn't made any improvements recently in handling large
numbers of batches, just in handling large numbers of polygons per batch. So if
a scene is composed of a large number of nodes with a small number of polygons
per node, the frame rate will suffer. This problem is not specific to Panda; any
graphics engine will have the same problem. The problem is due to the nature of
the PC and the AGP bus.

For example, though your graphics card may claim it can easily handle 100,000
polygons, this may be true in practice only if all of those polygons are sent in
one batch--that is, just a single :ref:`geom`. If, however, your scene consists
of 1,000 nodes with 100 polygons each, it may not have nearly as good a frame
rate.

To inspect performance the NodePath.analyze() method is extremely useful. For
example:

.. code-block:: python

   render.analyze()

The response is printed to the command window. It may look something like this::

   371 total nodes (including 43 instances).
   21 transforms; 16% of nodes have some render attribute.
   205 Geoms, with 94 GeomVertexDatas, appear on 133 GeomNodes.
   21665 vertices, 21573 normals, 21557 texture coordinates.
   35183 triangles:
      3316 of these are on 662 tristrips (5.00906 average tris per strip).
      0 of these are on 0 trifans.
      31867 of these are independent triangles.
   0 lines, 0 points.
   99 textures, estimated minimum 326929K texture memory required.

For a scene with many static nodes there exists a workaround.

If a scene is composed of many static objects, for example boxes, and the intent
of all of these boxes to just sit around and be part of the background, or to
move as a single unit, they can flattened together into a handful of nodes (or
even one node). To do this, parent them all to the same node, and use:

.. code-block:: python

   node.flattenStrong()

One thing that flattenStrong() won't touch is geometry under a ModelRoot or
ModelNode node. Since each egg or bam file loads itself up under a ModelRoot
node, the proper way to handle this is to get rid of that node first to make the
geometry from multiple different egg files to be flattened together. This can be
done with the following:

.. code-block:: python

   modelRoot = loader.loadModel('myModel.egg')
   newModel = NodePath('model')
   modelRoot.getChildren().reparentTo(newModel)
