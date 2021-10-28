.. _geom:

Geom
====

The :class:`.Geom` object collects together a :ref:`geomvertexdata` and one or
more :ref:`geomprimitive` objects, to make a single renderable piece of
geometry. In fact, an individual Geom is the smallest piece into which Panda
will subdivide the scene for rendering; in any given frame, either an entire
Geom is rendered, or none of it is.

Fundamentally, a :class:`.Geom` is very simple; it contains a pointer to a
single GeomVertexData, and a list of one or more GeomPrimitives, of various
types, as needed. All the associated GeomPrimitives index into the same
GeomVertexData.

.. raw:: html

   <center><table>
   <tr><td style="border: 1px solid black; background: #c1beea; padding: 5pt">
   <p>Geom</p>
   <table>
   <tr><td style="border: 1px solid black; background: #9197d8; padding: 5pt">
   <p>GeomVertexData</p>
   </td></tr>
   </table>
   <table>
   <tr><td style="border: 1px solid black; background: #acb1ed; padding: 5pt">
   <p>GeomTriangles</p>
   </td></tr>
   <tr><td style="border: 1px solid black; background: #acb1ed; padding: 5pt">
   <p>GeomTriangles</p>
   </td></tr>
   <tr><td style="border: 1px solid black; background: #acb1ed; padding: 5pt">
   <p>GeomTristrips</p>
   </td></tr>
   </table>
   </td></tr>
   </table></center>

The GeomVertexData pointer may be unique to each Geom, or one GeomVertexData
may be shared among many different Geoms (each of which might use a different
subset of its vertices). Also, although the GeomPrimitive objects are usually
unique to each Geom, they may also be shared between different Geoms.

Although a Geom can have any number of GeomPrimitives associated with it, all
of the GeomPrimitives must be of the same fundamental primitive type:
triangles, lines, or points. A particular Geom might have GeomTriangles,
GeomTristrips, and GeomTrifans; or it might have GeomLines and GeomLinestrips;
or it might have GeomPoints. But no one Geom can have primitives from two
different fundamental types. You can call
:meth:`geom.get_primitive_type() <.Geom.get_primitive_type>` to determine the
fundamental primitive type stored within a particular Geom.
