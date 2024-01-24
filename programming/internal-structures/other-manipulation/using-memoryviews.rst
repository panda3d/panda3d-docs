.. _using-memoryviews:

Using memoryviews
=================

Since :class:`.GeomVertexArrayData` supports the buffer protocol (as of Panda3D
1.9.0; see
`this blog post <https://www.panda3d.org/blog/buffer-protocol-support/>`__), an
alternative to using
:ref:`GeomVertexWriter/Reader/Rewriter <more-about-geomvertexreader-geomvertexwriter-and-geomvertexrewriter>`
(as described in :ref:`creating-and-filling-a-geomvertexdata`) is to use
:py:class:`memoryview` objects to alter the contents of this structure directly.
Other object types that implement the buffer protocol are :py:class:`bytearray`
and :py:class:`array.array` in Python, as well as ``numpy`` arrays, so it's
possible to seamlessly pass data between these and memoryviews.

A memoryview can be used to change the values in a vertex array, but also to add
values right after the creation of the array.

Creating geometry
-----------------

Let's start with a very simple example, where a :class:`.GeomVertexData` is
created with the :ref:`pre-defined format <pre-defined-vertex-formats>`
:meth:`.GeomVertexFormat.get_v3()`, such that the resulting data object will
consist of only a single array, containing the model-space vertex coordinates. A
memoryview of that array can be created as follows:

.. code-block:: python

   v_format = GeomVertexFormat.get_v3()
   v_data = GeomVertexData('name', v_format, GeomEnums.UH_static)
   v_data.unclean_set_num_rows(4)
   v_array = v_data.modify_array(0)
   # create a memoryview that float values can be assigned to
   view = memoryview(v_array).cast('B').cast('f')

One important thing to note is that the size of a memoryview cannot be changed.
So it is necessary to set the size of the vertex array before creating a view of
it.
In the code above, the number of vertex data rows is set to 4. This implicitly
also sets the row count of all of its arrays to that same number.

Filling in the newly created vertex data can be done like this:

.. code-block:: python

   import array

   # all of the coordinates can be put into a Python array...
   coordinates = array.array('f', [
       -1.0, 0.0, -1.0,  # the coordinates of the 1st vertex
       1.0, 2.0, -1.0,   # the coordinates of the 2nd vertex
       1.0, 0.0, 1.0,    # the coordinates of the 3rd vertex
       -1.0, 0.0, 1.0    # the coordinates of the 4th vertex
   ])
   # ...and assigned to the memoryview all at once
   view[:] = coordinates
   # it's also possible to assign a single float value to a particular element
   # of the memoryview:
   view[4] = 0.0  # modify the y-coordinate of the 2nd vertex

Similarly, the GeomPrimitive that combines the vertices into renderable geometry
can be filled using a memoryview as well. After all, the return value of
:meth:`.GeomPrimitive.modify_vertices` is also a :class:`.GeomVertexArrayData`.
Let's assume we want to render a square consisting of two triangles:

.. code-block:: python

   indices = array.array('H', [
       0, 1, 2,  # the vertex indices of the 1st triangle
       0, 2, 3   # the vertex indices of the 2nd triangle
   ])
   tris_prim = GeomTriangles(GeomEnums.UH_static)
   tris_array = tris_prim.modify_vertices()
   # note that `unclean_set_num_rows` fills the primitive with more or fewer
   # random integer values, which can be much larger than the number of vertices
   # in the associated vertex data object; this will cause an error when the
   # primitive is added to the scenegraph, so make sure the correct indices are
   # assigned before doing so, or call `set_num_rows` (slightly slower) instead
   tris_array.unclean_set_num_rows(len(indices))
   view = memoryview(tris_array).cast('B').cast('H')
   view[:] = indices

Note that if the model is intended to contain a large amount of vertices
(whether these are all added to the geometry at creation time or afterwards), an
error will occur if that number exceeds 65535. This is because the index type of
a GeomPrimitive is set to ``GeomEnums.NT_uint16`` by default. To prevent this,
set the index type to ``GeomEnums.NT_uint32`` and cast values to the 'I' format:

.. code-block:: python

   # use the 'I' format if values higher than 65535 are needed
   indices = array.array('I', [
       0, 1, 2,  # the vertex indices of the 1st triangle
       0, 2, 3   # the vertex indices of the 2nd triangle
   ])
   tris_prim = GeomTriangles(GeomEnums.UH_static)
   # prepare the primitive to accept indices bigger than 65535, such that more
   # vertices can be added to the geometry later on
   tris_prim.set_index_type(GeomEnums.NT_uint32)
   tris_array = tris_prim.modify_vertices()
   tris_array.unclean_set_num_rows(len(indices))
   # cast to 'I' instead of 'H' if indices higher than 65535 are needed
   view = memoryview(tris_array).cast('B').cast('I')
   view[:] = indices

Up till now, we've assumed that the vertex data contains only float values.
However, the vertex format might support integer data as well. For instance, a
custom column for storing indices might be required for a shader you want to
apply to your model. More commonly, you will want the vertex format to support
8-bit integer color components.
In this case, it is no longer possible to assign the values directly; they have
to be converted to bytes.

As an example, here is some code that makes use of the
:meth:`.GeomVertexFormat.get_v3n3c4t2()` format:

.. code-block:: python

   import struct

   v_format = GeomVertexFormat.get_v3n3c4t2()
   stride = v_format.arrays[0].stride  # the size of a data row, in bytes
   v_data = GeomVertexData('name', v_format, GeomEnums.UH_static)
   v_data.unclean_set_num_rows(4)
   v_array = v_data.modify_array(0)
   view = memoryview(v_array).cast('B')
   values = bytearray()
   # add the data of the 1st vertex to the bytearray
   values.extend(struct.pack(
       '6f4B2f',  # the format corresponds to the GeomVertexFormat
       -1.0, 0.0, -1.0,    # format: '3f'; the position of the 1st vertex
       0.0, -1.0, 0.0,     # format: '3f'; the normal vector of the 1st vertex
       255, 128, 64, 255,  # format: '4B'; the color of the 1st vertex
       0.0, 0.0            # format: '2f'; the UVs of the 1st vertex
   ))
   # add the data of the remaining vertices to the bytearray
   ...
   # assign all of the values to the memoryview
   view[:] = values

Altering geometry
-----------------

If you require your model geometry to be dynamically altered at runtime, then
the use of memoryviews is very efficient, as it can reduce or even avoid any
unnecessary copy operations.

Adding geometry
^^^^^^^^^^^^^^^

Consider the square from the previous sample code to be a side of a cube. To add
another side to that cube, you could use code like this:

.. code-block:: python

   old_count = v_data.get_num_rows()
   # increase the number of data rows by 4 (since the new side has 4 vertices)
   vertex_data.set_num_rows(old_count + 4)
   v_array = vertex_data.modify_array(0)
   view = memoryview(v_array).cast('B')
   view[old_count * stride:] = values  # bytearray with new side values

   tris_array = tris_prim.modify_vertices()
   old_count = tris_array.get_num_rows()
   # increase the number of index rows by 6 (2 triangles, thus 6 vertex indices)
   tris_array.set_num_rows(old_count + 6)
   view = memoryview(tris_array).cast('B').cast('H')
   view[old_count:] = indices  # array.array filled with 6 new vertex indices

Removing geometry
^^^^^^^^^^^^^^^^^

If part of the geometry needs to be removed, e.g. a side from the cube in the
previous example, this can be accomplished using code like the following:

.. code-block:: python

   old_count = v_data.get_num_rows()
   # the size, in bytes, of the data associated with a cube side
   size = 4 * stride  # 4 (vertices per side) times the size of a data row
   # in this case, the start index of the data to be removed can simply be
   # calculated as the index of the corresponding side (`n` if it was the `nth`
   # side to be added to the cube) multiplied by the size of that side
   start = side_index * size
   v_array = v_data.modify_array(0)
   view = memoryview(v_array).cast('B')
   # instead of actually deleting the data, it is overwritten with the data that
   # follows it;
   # the end index of the data to overwrite equals the maximum index minus the
   # size of the side data, such that the subview (slice) of that data and the
   # subview of the data that follows the data to be overwritten have the exact
   # same size; only then can the latter be copied to the former
   view[start:-size] = view[start+size:]
   # now all that remains to be done is to update the number of data rows by
   # decreasing it by 4 (the number of vertices per side)
   v_data.set_num_rows(old_count - 4)

   old_count = tris_prim.get_num_vertices()
   start = side_index * 6 # (2 triangles, thus 6 vertex indices)
   # just like the vertex data rows, the corresponding indices in the primitive
   # will be overwritten with those following them;
   # the latter additionally need to be offset, otherwise they would reference
   # vertices that are not in the vertex data table (since there are 4 fewer now)
   tris_prim.offset_vertices(-4, start + 6, old_count)
   tris_array = tris_prim.modify_vertices()
   view = memoryview(tris_array).cast('B').cast('H')
   view[start:-6] = view[start+6:]
   tris_array.set_num_rows(old_count - 6)
