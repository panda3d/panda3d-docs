.. _modifying-existing-geometry-data:

Modifying existing geometry data
================================

If you want to load a model and operate on its vertices, you can walk through
the vertices as shown in
:ref:`the previous section <reading-existing-geometry-data>`, but you should
substitute :meth:`~.GeomNode.modify_geom()`,
:meth:`~.Geom.modify_vertex_data()`, and :meth:`~.Geom.modify_primitive()` for
:meth:`~.GeomNode.get_geom()`, :meth:`~.Geom.get_vertex_data()`, and
:meth:`~.Geom.get_primitive()`, respectively. These calls
ensure that, in case the data happens to be shared between multiple different
GeomNodes, you will get your own unique copy to modify, without inadvertently
affecting other nodes.

If you want to modify the vertex data, you have two choices. The simplest
option is to create a new :ref:`geomvertexdata` and fill it up with your new
vertex data (as described in :ref:`creating-and-filling-a-geomvertexdata`),
and then assigning this data to the geom with the call
:meth:`geom.set_vertex_data() <.Geom.set_vertex_data>`.
You must ensure that you add enough vertices to the new GeomVertexData to
satisfy the GeomPrimitives that reference it.

Your second choice is to modify the vertex data in-place, by operating on the
existing vertices. You can do this with a
:ref:`GeomVertexWriter <more-about-geomvertexreader-geomvertexwriter-and-geomvertexrewriter>`.
For instance, if you want to copy the (X, Y) position of each vertex to its
(U, V) texture coordinate, you could do something like this:

.. only:: python

   .. code-block:: python

      texcoord = GeomVertexWriter(vdata, 'texcoord')
      vertex = GeomVertexReader(vdata, 'vertex')

      while not vertex.isAtEnd():
          v = vertex.getData3()
          texcoord.setData2(v[0], v[1])

.. only:: cpp

   .. code-block:: cpp

      GeomVertexWriter texcoord(vdata, "texcoord");
      GeomVertexReader vertex(vdata, "vertex");

      while (!vertex.is_at_end()) {
        LVector3 v = vertex.get_data3();
        texcoord.set_data2(v[0], v[1]);
      }

.. important::

   Important! When you are simultaneously reading from and writing to the same
   GeomVertexData object, you should create all of the GeomVertexWriters you
   need before you create any GeomVertexReader. This is because of Panda's
   internal reference-counting mechanism; creating a GeomVertexWriter may
   automatically (and transparently) force a copy of the data in the
   GeomVertexData, which could invalidate any GeomVertexReaders you have already
   created.

Writing to a column with a GeomVertexWriter does require that the
GeomVertexData's format already has the appropriate columns to handle the data
you are writing (in the above example, for instance, the format must already
have a 'texcoord' column, or the above code will fail). Furthermore, the columns
must have the appropriate format. For instance, if you wanted to upgrade a
model's texture coordinates from 2-D texture coordinates to 3-D texture
coordinates, simply calling
:meth:`texcoord.set_data3(u, v, w) <.GeomVertexWriter.set_data3>` wouldn't
change the fact that the existing texcoord column is a 2-component format; you
would just be trying to stuff a 3-component value into a 2-component column.

If you want to add a new column to a GeomVertexData, or modify the format of an
existing column, you will have to create a new :ref:`geomvertexformat` that
includes the new column (see :ref:`defining-your-own-geomvertexformat`), and
then change the format on the GeomVertexData via
:meth:`vdata.set_format(format) <.GeomVertexData.set_format>`. This
call will internally adjust all of the data to match the new format. (Because of
this internal adjustment, it is important to do this before you create the first
GeomVertexWriter or GeomVertexReader.)
