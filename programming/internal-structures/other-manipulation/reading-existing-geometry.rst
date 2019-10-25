.. _reading-existing-geometry-data:

Reading existing geometry data
==============================

You can fairly easily extract and examine or operate on the vertices for an
existing model, although you should be aware that the order in which the
vertices appear in a model is undefined. There is no correlation between the
order in which vertices are listed in an egg file, and the order in which they
will appear in the resulting loaded model. Panda may rearrange the vertices,
or even add or remove vertices, as needed to optimize the model for rendering
performance. Even from one session to the next, the vertices might come out in
a different order.

This does make certain kinds of vertex operations difficult; if you plan to
write code that expects to encounter the vertices of a model in a particular
order, we recommend you build up those vertices yourself using a
:ref:`GeomVertexWriter <more-about-geomvertexreader-geomvertexwriter-and-geomvertexrewriter>`
(as described in :ref:`creating-and-filling-a-geomvertexdata`), so that you
have explicit control over the vertex order.

However, if you have no need to operate on the vertices in any particular order,
or if you just want to casually browse the vertices in a model, feel free to use
the following instructions to read the data.

When you load a model, you have a handle to the root node of the model, which
is usually a ModelRoot node. The geometry itself will be stored in a series of
:ref:`GeomNodes <geomnode>`, which will be children of the root node. In order
to examine the vertex data, you must visit the GeomNodes in the model. One way
to do this is to walk through all the GeomNodes like this:

.. only:: python

   .. code-block:: python

      geomNodeCollection = model.findAllMatches('**/+GeomNode')
      for nodePath in geomNodeCollection:
          geomNode = nodePath.node()
          processGeomNode(geomNode)

.. only:: cpp

   .. code-block:: cpp

      NodePathCollection geomNodeCollection = model.find_all_matches("**/+GeomNode");

      for (size_t i = 0; i < geomNodeCollection.get_num_paths(); ++i) {
        PT(GeomNode) g = DCAST(GeomNode, geomNodeCollection.get_path(i).node());
        processGeomNode(g);
      }

Once you have a particular GeomNode, you must walk through the list of
:ref:`Geoms <geom>` stored on that node. Each Geom also has an associated
RenderState, which controls the visible appearance of that Geom (e.g. texture,
backfacing, etc.).

.. only:: python

   .. code-block:: python

      def processGeomNode(geomNode):
          for i in range(geomNode.getNumGeoms()):
              geom = geomNode.getGeom(i)
              state = geomNode.getGeomState(i)
              print(geom)
              print(state)
              processGeom(geom)

.. only:: cpp

   .. code-block:: cpp

      void processGeomNode(GeomNode *geomnode) {
        for (size_t j = 0; j < geomnode->get_num_geoms(); ++j) {
          PT(Geom) geom = geomnode->get_geom(j);
          geom->write(nout); // Outputs basic info on the geom
          geomnode->get_geom_state(j)->write(nout); // Basic renderstate info
          processGeom(geom);
        }
      }

Note that geomNode.getGeom() is only appropriate if you will be reading, but not
modifying, the data. If you intend to modify the geom data in any way (including
any nested data like vertices or primitives), you should use
geomNode.modifyGeom() instead.

Each Geom has an associated :ref:`geomvertexdata`, and one or more
:ref:`GeomPrimitives <geomprimitive>`. Some GeomVertexData objects may be shared
by more than one Geom, especially if you have used flattenStrong() to optimize a
model.

.. only:: python

   .. code-block:: python

      def processGeom(geom):
          vdata = geom.getVertexData()
          print(vdata)
          processVertexData(vdata)
          for i in range(geom.getNumPrimitives()):
              prim = geom.getPrimitive(i)
              print(prim)
              processPrimitive(prim, vdata)

.. only:: cpp

   .. code-block:: cpp

      void processGeom(Geom *geom) {
        PT(GeomVertexData) vdata = geom->get_vertex_data();
        vdata->write(nout);
        processVertexData(vdata);
        for (size_t i = 0; i < geom.get_num_primitives(); ++i) {
          PT(GeomPrimitive) prim = geom->get_primitive(i);
          prim->write(nout,0);
          processPrimitive(prim, vdata);
        }
      }

As above, get_vertex_data() is only appropriate if you will only be reading,
but not modifying, the vertex data. Similarly, getPrimitive() is appropriate
only if you will not be modifying the primitive index array. If you intend to
modify either one, use modifyVertexData() or modifyPrimitive(), respectively.

You can use the
:ref:`GeomVertexReader <more-about-geomvertexreader-geomvertexwriter-and-geomvertexrewriter>`
class to examine the vertex data. You should create a GeomVertexReader for
each column of the data you intend to read. It is up to you to ensure that a
given column exists in the vertex data before you attempt to read it (you can
use vdata.hasColumn() to test this).

.. only:: python

   .. code-block:: python

      def processVertexData(vdata):
          vertex = GeomVertexReader(vdata, 'vertex')
          texcoord = GeomVertexReader(vdata, 'texcoord')
          while not vertex.isAtEnd():
              v = vertex.getData3()
              t = texcoord.getData2()
              print("v = %s, t = %s" % (repr(v), repr(t)))

.. only:: cpp

   .. code-block:: cpp

      void processVertexData(const GeomVertexData *vdata) {
        GeomVertexReader vertex(vdata, "vertex");
        GeomVertexReader texcoord(vdata, "texcoord");
        while (!vertex.is_at_end()) {
          LVector3 v = vertex.get_data3();
          LVector3 t = texcoord.get_data2();
          nout << "V = " << v << "T = " << t << endl;
        }
      }

Each GeomPrimitive may be any of a handful of different classes, according to
the primitive type it is; but all GeomPrimitive classes have the same common
interface to walk through the list of vertices referenced by the primitives
stored within the class.

You can use the setRow() method of GeomVertexReader to set the reader to a
particular vertex. This affects the next call to getData(). In this way, you
can extract the vertex data for the vertices in the order that the primitive
references them (instead of in order from the beginning to the end of the
vertex table, as above).

.. only:: python

   .. code-block:: python

      def processPrimitive(prim, vdata):
          vertex = GeomVertexReader(vdata, 'vertex')

          prim = prim.decompose()

          for p in range(prim.getNumPrimitives()):
              s = prim.getPrimitiveStart(p)
              e = prim.getPrimitiveEnd(p)
              for i in range(s, e):
                  vi = prim.getVertex(i)
                  vertex.setRow(vi)
                  v = vertex.getData3()
                  print("prim %s has vertex %s: %s" % (p, vi, repr(v)))

.. only:: cpp

   .. code-block:: cpp

      void processPrimitive(const GeomPrimitive *orig_prim, const GeomVertexData *vdata) {
        GeomVertexReader vertex(vdata, "vertex");

        CPT(GeomPrimitive) prim = orig_prim->decompose();

        for (size_t k = 0; k < prim->get_num_primitives(); ++k) {
          int s = prim->get_primitive_start(k);
          int e = prim->get_primitive_end(k);
          for (int i = s; i < e; ++i) {
            int vi = prim->get_vertex(b);
            vertex.set_row(vi);
            LVector3 v = vertex.get_data3();
            nout << "prim " << k << " has vertex " << vi <<": " << v << endl;
          }
        }
      }

You may find the call to prim.decompose() useful (as shown in the above
example). This call automatically decomposes higher-order primitive types,
like GeomTristrips and GeomTrifans, into the equivalent component primitive
types, like GeomTriangles; but when called on a GeomTriangles, it returns the
GeomTriangles object unchanged. Similarly, GeomLinestrips will be decomposed
into GeomLines. This way you can write code that doesn't have to know anything
about GeomTristrips and GeomTrifans, which are fairly complex; it can assume
it will only get the much simpler GeomTriangles (or, in the case of lines or
points, GeomLines and GeomPoints, respectively).
