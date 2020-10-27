.. _more-about-geomvertexreader-geomvertexwriter-and-geomvertexrewriter:

More about GeomVertexReader, GeomVertexWriter, and GeomVertexRewriter
=====================================================================

The classes GeomVertexReader and GeomVertexWriter together represent the core
interface for reading and writing the numeric data stored within a
:ref:`geomvertexdata` object.

These two classes work similarly. Both are designed to get a temporary pointer
to the data for a particular column when they are constructed, and they
increment that pointer as you walk through the vertices. Initially, they start
at row number 0 (the first vertex in the table), and after each setData/getData
operation, they automatically increment to the next row (the next vertex).

You construct a GeomVertexReader or GeomVertexWriter with a pointer to the
:ref:`geomvertexdata` object you are operating on, and the name of the column
you wish to process, e.g.:

.. code-block:: python

   color = GeomVertexReader(vdata, 'color')

Because the GeomVertexReader and GeomVertexWriter classes only store a temporary
pointer, which might become invalid between frames or even between different
tasks within a frame, these objects should not be stored in any persistent
object. Instead, they are designed to be temporary objects that are constructed
locally, used immediately to iterate through a list of vertices, and then
released. If you need to keep a persistent iterator for your vertex data, to be
used over a long period of time (e.g. over several frames), then you should
store just the GeomVertexData pointer (along with the current vertex index
number if you require this), and construct a temporary GeomVertexReader/Writer
each time you need to access it.

The following methods are available to read and write data in a column:

==================== ===================== ============= ===================== ============
**GeomVertexReader** **GeomVertexWriter**
-------------------- ----------------------------------------------------------------------
x = getData1()       setData1(x)                         addData1(x)
-------------------- ----------------------------------- ----------------------------------
v2 = getData2()      setData2(x, y)        setData2(v2)  addData2(x, y)        addData2(v2)
v3 = getData3()      setData3(x, y, z)     setData3(v3)  addData3(x, y, z)     addData3(v3)
v4 = getData4()      setData4(x, y, z, w)  setData4(v4)  addData4(x, y, z, w)  addData4(v4)
x = getData1i()      setData1i(x)                        addData1i(x)
-------------------- ----------------------------------- ----------------------------------
\                    setData2i(x, y)                     addData2i(x, y)
-------------------- ----------------------------------- ----------------------------------
\                    setData3i(x, y, z)                  addData3i(x, y, z)
-------------------- ----------------------------------- ----------------------------------
\                    setData4i(x, y, z, w)               addData4i(x, y, z, w)
==================== =================================== ==================================

Each of the getData family of functions supported by GeomVertexReader returns
the value of the data in the current column, converted to the requested type.
The 'i' suffix indicates an integer value, while the lack of this suffix
indicates a floating-point value; the digit indicates the number of components
you expect to receive.

For instance, getData2() always returns a VBase2, regardless of the type of data
actually stored in the column. If the column contains a 2-component value such
as a 2-D texture coordinate, then the returned value will represent the (U, V)
value in that column. However, if the column type does not match the requested
type, a conversion is quietly made; for instance, if you call getData2() but the
column actually contains a 3-D texture coordinate, the third component will be
omitted from the return value, which will still be a VBase2.

Similarly, the setData and addData family of functions supported by
GeomVertexWriter accept a value in the indicated format, and convert it to
whatever format is required by the column. So if you call setData3(), and the
column has three components, you will set all three components with the x, y, z
parameters of setData3(); but if the column has only two components, only the
x, y parameters will be used to set those two components, and the third
parameter will be ignored.

Certain kinds of numeric conversions are performed automatically, according to
the column's designated contents. For instance, if you store a floating-point
value into an integer column, the fractional part of the value is usually
truncated. However, if the column contents indicates that it represents a color
value, then the floating-point value is automatically scaled from the range 0.0
.. 1.0 into the full numeric range of the column's integer value. This allows
you to store color components in the range 0.0 .. 1.0, and get the expected
result (that is, the value is scaled into the range 0 .. 255). A similar
conversion happens when data is read.

There are no getData2i, 3i, or 4i methods available, simply because Panda does
not currently define a multi-component integer value that can be returned to
Python. Since most multi-component column types are floating-point, or can be
expressed as floating-point, this is not generally a limitation.

Each GeomVertexReader keeps track of the current read row, which is initially 0;
the current value can be retrieved by getReadRow(). Each call to a getData
function returns the value of the column at the current read row, and then
increments the current read row. It is an error to call getData when the read
row has reached the end of the data, but you can call isAtEnd(), which returns
true when the reader has reached the end. Thus, you can iterate through all the
rows of a vertex table by repeatedly calling getData until isAtEnd() returns
true.

Similarly, each GeomVertexWriter keeps track of the current write row, which is
initially 0, and can be retrieved by getWriteRow(). Each call to setData or
addData stores the given value in the current write row, and then increments the
current write row. It is an error to call setData when the write row has reached
the end of the data; but as with the GeomVertexReader, you can call isAtEnd() to
determine when you have reached the end of the data.

The addData family of functions work exactly like the setData functions, except
that addData can be called when the GeomVertexWriter has reached its end.
In this case, addData will add a new row to the table, and then fill in the
specified data in that row (and then increment the current write row). If
addData is called when the current write row already exists, it behaves exactly
the same as setData.

With either GeomVertexReader or GeomVertexWriter, you can set the current read
or write row at any time with the call setRow(). This sets the current read row
(GeomVertexReader) or current write row (GeomVertexWriter) to the indicated
value; the next call to getData or setData/addData will then operate on the
specified row, and increment from there.

GeomVertexRewriter
------------------

The GeomVertexRewriter class exists as a convenience for code that needs to
alternately read and write the data on a column. GeomVertexRewriter multiply
inherits from GeomVertexReader and GeomVertexWriter, so it supports the getData
family of functions, as well as the setData and addData family of functions. It
also has both a current read row and a current write row, which might be
different.

Normally, you would use a GeomVertexRewriter to walk through the list of
vertices from the beginning to end, reading and writing as it goes. For
instance, to set all of the Z components of a piece of geometry to 0.0, while
preserving the X and Y components, you might write a loop such as:

.. code-block:: python

   vertex = GeomVertexRewriter(vdata, 'vertex')
   while not vertex.isAtEnd():
       v = vertex.getData3()
       vertex.setData3(v[0], v[1], 0.0)

Note that this example code calls getData3() and setData3() exactly once
through each iteration, which increments the current read row and current write
row, respectively; so the current read row and current write row are kept in
sync with each other.

Important! When you are simultaneously reading from and writing to the same
GeomVertexData object, you should create all of the GeomVertexWriters and
GeomVertexRewriters you need before you create any GeomVertexReader. This is
because of Panda's internal referencing-counting mechanism; creating a
GeomVertexWriter may automatically (and transparently) force a copy of the data
in the GeomVertexData, which could invalidate any GeomVertexReaders you have
already created.
