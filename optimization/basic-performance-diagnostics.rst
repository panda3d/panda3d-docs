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

   show-frame-rate-meter true

Or, if you want to have it set at run-time:

.. only:: python

   .. code-block:: python

      base.setFrameRateMeter(True)

.. only:: cpp

   .. code-block:: cpp

      PT(FrameRateMeter) meter;
      meter = new FrameRateMeter("frame_rate_meter");
      meter->setup_window(graphics_window);

However, keep in mind that measuring the frame rate in FPS gives a distorted
view of the application performance. This is because FPS is not a linear scale:
improving your frame rate from 500 to 1000 FPS sounds like a lot, but it
represents a difference of only 1 millisecond, which is about the same as
improving your frame rate from 29 to 30 FPS, and does therefore not actually
represent a very significant optimization.

It is more meaningful to look at the reciprocal of this number, the
*frame time*, usually measured in milliseconds. To see the frame rate in ms,
put this in your config file::

   frame-rate-meter-milliseconds true

The Scene Graph Analyzer
------------------------

To inspect the complexity of a scene or object, the :meth:`.NodePath.analyze()`
method is extremely useful. This will quickly tell you if your scene has
:ref:`too many meshes <too-many-meshes>`, for example.

.. only:: python

   .. code-block:: python

      render.analyze()

.. only:: cpp

   .. code-block:: cpp

      SceneGraphAnalyzer sga;
      sga.add_node(render.node());
      sga.write(std::cerr);

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

To optimize a scene with too many static nodes, see :ref:`too-many-meshes` for
possible solutions.
