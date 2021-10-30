.. _creating-the-geomprimitive-objects:

Creating the GeomPrimitive objects
==================================

Now that you have a :ref:`geomvertexdata` with a set of vertices, you can
create one or more :ref:`geomprimitive` objects that use the vertices in your
GeomVertexData.

In general, you do this by first creating a GeomPrimitive of the appropriate
type, and then calling :meth:`~.GeomPrimitive.add_vertex()` for each vertex in
your primitive, followed by :meth:`~.GeomPrimitive.close_primitive()` after each
primitive is complete. You can contain as many primitives as you like to the
same GeomPrimitive object; this is more efficient than creating many separate
GeomPrimitive objects.

Different GeomPrimitive types have different requirements for the number of
vertices per primitive. Some always have a fixed amount of vertices, like
GeomTriangles, GeomLines and GeomPoints. You should simply add all of the
vertices for these primitives. Some people call
:meth:`~.GeomPrimitive.close_primitive()` after adding every primitive, but this
is not strictly necessary. Other GeomPrimitive types have a variable number of
vertices, like GeomTristrips, GeomTrifans and GeomLinestrips. Because you need
to tell Panda3D how many vertices are in every primitive, you should call
:meth:`~.GeomPrimitive.close_primitive()` after adding every primitive.

For example:

.. only:: python

   .. code-block:: python

      prim = GeomTriangles(Geom.UHStatic)

      prim.addVertex(0)
      prim.addVertex(1)
      prim.addVertex(2)
      # thats the first triangle

      # you can also add a few at once
      prim.addVertices(2, 1, 3)

      prim.addVertices(0, 5, 6)

.. only:: cpp

   .. code-block:: cpp

      // In order for this to work you need to have included "geomTriangles.h"

      PT(GeomTriangles) prim;
      prim = new GeomTriangles(Geom::UH_static);

      prim->add_vertex(0);
      prim->add_vertex(1);
      prim->add_vertex(2);
      // thats the first triangle

      // you can also add a few at once
      prim->add_vertices(2, 1, 3);

      prim->add_vertices(0, 5, 6);


Note that the GeomPrimitive constructor requires one parameter, which is a
usage hint, similar to the usage hint required for the :ref:`geomvertexdata`
constructor. Like that usage hint, this tells Panda whether you will
frequently adjust the vertex indices on this primitive after it has been
created. Since it is very unusual to adjust the vertex indices on a primitive
(usually, if you intend to animate the vertices, you would operate on the
vertices, not these indices), this is almost always
``Geom.UH_static``, even if the primitive
is associated with a dynamic GeomVertexData. However, there may be special
rendering effects in which you actually do manipulate this vertex index table
in-place every few frames, in which case you should use Geom.UHDynamic. As
with the GeomVertexData, this is only a performance hint; you're not required
to adhere to the usage you specify.

If you are unsure about this parameter, you should use ``Geom.UH_static``.

The above sample code defines a GeomTriangles object that looks like this:

.. raw:: html

   <center><table style="border-collapse: collapse">
   <tr>
   <td style="padding-left: 64pt"></td>
   </tr>
   <tr>
   <td style="border: 1px solid black; background: #c1beea; text-align: center">0</td>
   </tr>
   <tr>
   <td style="border: 1px solid black; background: #c1beea; text-align: center">1</td>
   </tr>
   <tr>
   <td style="border: 1px solid black; background: #c1beea; text-align: center">2</td>
   </tr>
   <tr>
   <td> </td>
   </tr>
   <tr>
   <td style="border: 1px solid black; background: #c1beea; text-align: center">2</td>
   </tr>
   <tr>
   <td style="border: 1px solid black; background: #c1beea; text-align: center">1</td>
   </tr>
   <tr>
   <td style="border: 1px solid black; background: #c1beea; text-align: center">3</td>
   </tr>
   <tr>
   <td> </td>
   </tr>
   <tr>
   <td style="border: 1px solid black; background: #c1beea; text-align: center">0</td>
   </tr>
   <tr>
   <td style="border: 1px solid black; background: #c1beea; text-align: center">5</td>
   </tr>
   <tr>
   <td style="border: 1px solid black; background: #c1beea; text-align: center">6</td>
   </tr>
   </table></center>

The actual positions of the vertices depends on the values of the vertices
numbered 0, 1, 2, 3, and 5 in the associated :ref:`geomvertexdata` (you will
associate your GeomPrimitives with a GeomVertexData
:ref:`in the next step <putting-your-new-geometry-in-the-scene-graph>`, when
you attach the GeomPrimitives to a :ref:`geom`).

Finally, there are a few handy shortcuts for adding multiple vertices at once:

.. code-block:: python

   # Add 2, 3, or 4 vertices in a single call.
   add_vertices(v1, v2)
   add_vertices(v1, v2, v3)
   add_vertices(v1, v2, v3, v4)

   # Add numVertices consecutive vertices, beginning at vertex "start".
   # For instance, add_consecutive_vertices(5, 3) adds vertices 5, 6, 7.
   add_consecutive_vertices(start, numVertices)

   # Adds numVertices consecutive vertices, beginning with the next vertex
   # after the last vertex you added, or beginning at vertex 0 if these are
   # the first vertices.
   add_next_vertices(numVertices)

None of the above shortcut methods calls
:meth:`~.GeomPrimitive.close_primitive()` for you; it is still your
responsibility to call :meth:`~.GeomPrimitive.close_primitive()` each time you
add the appropriate number of vertices to a primitive that requires it.
