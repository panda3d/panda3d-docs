.. _putting-your-new-geometry-in-the-scene-graph:

Putting your new geometry in the scene graph
============================================

Finally, now that you have a :ref:`geomvertexdata` and one or more
:ref:`geomprimitive` objects, you can create a :ref:`geom` object and a
:ref:`geomnode` to put the new geometry in the scene graph, so that it will be
rendered.

.. only:: python

   .. code-block:: python

      geom = Geom(vdata)
      geom.addPrimitive(prim)

      node = GeomNode('gnode')
      node.addGeom(geom)

      nodePath = render.attachNewNode(node)

.. only:: cpp

   .. code-block:: cpp

      PT(Geom) geom;
      geom = new Geom(vdata);
      geom->add_primitive(prim);

      PT(GeomNode) node;
      node = new GeomNode("gnode");
      node->add_geom(geom);

      NodePath nodePath = window->get_render().attach_new_node(node);

The Geom constructor requires a pointer to the GeomVertexData object you will
be using. There is only one GeomVertexData associated with any particular
Geom. You can reset the Geom to use a different GeomVertexData later, if you
like, by calling :meth:`geom.setVertexData() <.Geom.set_vertex_data>`.

The GeomNode constructor requires a name, which is the name of the node and
will be visible in the scene graph. It can be any name you like that means
something to you.

In the above example, we have created only one Geom, and added only one
GeomPrimitive to the Geom. This is the most common case when you are creating
geometry at runtime, although in fact a GeomNode may include multiple Geoms,
and each Geom may include multiple GeomPrimitives. (However, all of the
primitives added to a Geom must have the same fundamental primitive type:
triangles, lines, or points. You can add GeomTriangles and GeomTristrips to
the same Geom, or you can add GeomLines and GeomLinestrips, but if you have
GeomTriangles and GeomLinestrips, you must use two different Geoms.)

It is important that the range of vertex index numbers used by your
GeomPrimitives is consistent with the number of vertices in your
GeomVertexData (for instance, if you have 100 vertices in your GeomVertexData,
your GeomPrimitives must only reference vertices numbered 0 through 99). If
this is not the case, you will get an exception when you call addPrimitive().
