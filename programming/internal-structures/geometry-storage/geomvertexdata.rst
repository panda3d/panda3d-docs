.. _geomvertexdata:

GeomVertexData
==============

The fundamental object used to store vertex information in Panda is the
:class:`.GeomVertexData`. This stores a list of vertices, organized conceptually
as a table, where each row of the table represents a different vertex, and the
columns of the table represent the different kinds of per-vertex data that may
be associated with each vertex. For instance, the following table defines four
vertices, each with its own vertex position, normal vector, color, and texture
coordinate pair:

== ========= ========= ============ ========
\  vertex    normal    color        texcoord
0  (1, 0, 0) (0, 0, 1) (0, 0, 1, 1) (1, 0)
1  (1, 1, 0) (0, 0, 1) (0, 0, 1, 1) (1, 1)
2  (0, 1, 0) (0, 0, 1) (0, 0, 1, 1) (0, 1)
3  (0, 0, 0) (0, 0, 1) (0, 0, 1, 1) (0, 0)
== ========= ========= ============ ========


Vertices are always numbered beginning at 0, and continue to the number of
rows in the table (minus 1).

Not all GeomVertexData objects will use these same four columns; some will
have fewer columns, and some will have more. In fact, all columns, except for
"vertex", which stores the vertex position, are optional.

The order of the columns is not meaningful, but the column names are. There
are certain column names that are reserved for Panda, and instruct Panda what
the meaning of each column is. For instance, the vertex position column is
always named "vertex", and the lighting normal column, if it is present, must
be named "normal". See :ref:`geomvertexformat` for the complete list of
reserved column names.

You can define your own custom columns. If there are any columns that have a
name that Panda does not recognize, Panda will not do anything special with
the column, but it can still send it to the graphics card. Of course, it is
then up to you to write a :ref:`vertex shader <shader-basics>` that
understands what to do with the data in the column.

It is possible to break up a GeomVertexData into more than one array. A
GeomVertexArrayData is a table of vertex data that is stored in one contiguous
block of memory. Typically, each GeomVertexData consists of just one array; but
it is also possible to distribute the data so that some columns are stored in
one array, while other columns are stored in another array:

== ========= ========
\  vertex    texcoord
0  (1, 0, 0) (1, 0)
1  (1, 1, 0) (1, 1)
2  (0, 1, 0) (0, 1)
3  (0, 0, 0) (0, 0)
== ========= ========

== ========= ============
\   normal    color
0  (0, 0, 1) (0, 0, 1, 1)
1  (0, 0, 1) (0, 0, 1, 1)
2  (0, 0, 1) (0, 0, 1, 1)
3  (0, 0, 1) (0, 0, 1, 1)
== ========= ============

You might want to do this, for instance, if you have certain columns of data
that are always the same between different blocks of vertices; you can put
those columns in a separate array, and then use the same array within multiple
different GeomVertexData objects. There is no limit to the number of different
arrays you can have within one GeomVertexData; you can make each column a
separate array if you like. (There may be performance implications to
consider. Some graphics drivers may work better with one block of contiguous
data--one array--while others may prefer many different arrays. This
performance difference is likely to be small, however.)
