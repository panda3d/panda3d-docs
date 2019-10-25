.. _creating-and-filling-a-geomvertexdata:

Creating and filling a GeomVertexData
=====================================

Once you have a :ref:`geomvertexformat`, registered and ready to use, you can
use it to create a :ref:`geomvertexdata`.

.. only:: python

   .. code-block:: python

      vdata = GeomVertexData('name', format, Geom.UHStatic)

.. only:: cpp

   Using a :ref:`custom vertex format <defining-your-own-geomvertexformat>`.

   .. code-block:: cpp

      PT(GeomVertexData) vdata;
      vdata = new GeomVertexData("name", format, Geom::UH_static);

   Or using a
   :ref:`Pre-defined vertex format <pre-defined-vertex-formats>`.

   .. code-block:: cpp

      PT(GeomVertexData) vdata;
      vdata = new GeomVertexData("name", GeomVertexFormat::get_????(), Geom::UH_static);

The first parameter to the GeomVertexData constructor is the name of the data,
which is any arbitrary name you like. This name is mainly for documentation
purposes; it may help you identify this vertex data later. You can leave it
empty if you like.

The second parameter is the :ref:`geomvertexformat` to use for this
GeomVertexData. The format specifies the number of arrays that will be created
for the data, the names and formats of the columns in each array, and the number
of bytes that need to be allocated for each row.

The third parameter is a usage hint, which tells Panda how often (if ever) you
expect to be modifying these vertices, once you have filled them in the first
time. If you will be filling in the vertices once (or only once in a while) and
using them to render many frames without changing them, you should use
Geom.UHStatic. The vast majority of vertex datas are of this form. Even
GeomVertexDatas that include vertex animation tables should usually be declared
Geom.UHStatic, since the vertex data itself will not be changing (even though
the vertices might be animating).

However, occasionally you might create a GeomVertexData whose vertices you
intend to adjust in-place every frame, or every few frames; in this case, you
can specify Geom.UHDynamic, to tell Panda not to make too much effort to cache
the vertex data. This is just a performance hint; you're not required to adhere
to the usage you specify, though you may get better render performance if you
do.

If you are unsure about this third parameter, you should probably use
Geom.UHStatic.

Next, it is **highly recommended** that you set the number of rows you're going
to write. This is an optional step; Panda will resize the underlying table
appropriately as you are adding new data, but this will cause every
``add_dataXX()`` call to be *much slower* than if you had specified a number of
rows.

.. only:: python

   .. code-block:: python

      vdata.setNumRows(4)

.. only:: cpp

   .. code-block:: cpp

      vdata->set_num_rows(4);

Now that you have created a GeomVertexData, you should create a number of
:ref:`GeomVertexWriters <more-about-geomvertexreader-geomvertexwriter-and-geomvertexrewriter>`,
one for each column, to fill in the data.

.. only:: python

   .. code-block:: python

      vertex = GeomVertexWriter(vdata, 'vertex')
      normal = GeomVertexWriter(vdata, 'normal')
      color = GeomVertexWriter(vdata, 'color')
      texcoord = GeomVertexWriter(vdata, 'texcoord')

.. only:: cpp

   .. code-block:: cpp

      GeomVertexWriter vertex(vdata, "vertex");
      GeomVertexWriter normal(vdata, "normal");
      GeomVertexWriter color(vdata, "color");
      GeomVertexWriter texcoord(vdata, "texcoord");

It is your responsibility to know which columns exist in the GeomVertexFormat
you have used. It is legal to create a GeomVertexWriter for a column that
doesn't exist, but it will be an error if you later attempt to use it to add
data.

To add data, you can now iterate through your vertices and call one of the
addData methods on each GeomVertexWriter.

.. only:: python

   .. code-block:: python

      vertex.addData3(1, 0, 0)
      normal.addData3(0, 0, 1)
      color.addData4(0, 0, 1, 1)
      texcoord.addData2(1, 0)

      vertex.addData3(1, 1, 0)
      normal.addData3(0, 0, 1)
      color.addData4(0, 0, 1, 1)
      texcoord.addData2(1, 1)

      vertex.addData3(0, 1, 0)
      normal.addData3(0, 0, 1)
      color.addData4(0, 0, 1, 1)
      texcoord.addData2(0, 1)

      vertex.addData3(0, 0, 0)
      normal.addData3(0, 0, 1)
      color.addData4(0, 0, 1, 1)
      texcoord.addData2(0, 0)

.. only:: cpp

   .. code-block:: cpp

      vertex.add_data3(1, 0, 0);
      normal.add_data3(0, 0, 1);
      color.add_data4(0, 0, 1, 1);
      texcoord.add_data2(1, 0);

      vertex.add_data3(1, 1, 0);
      normal.add_data3(0, 0, 1);
      color.add_data4(0, 0, 1, 1);
      texcoord.add_data2(1, 1);

      vertex.add_data3(0, 1, 0);
      normal.add_data3(0, 0, 1);
      color.add_data4(0, 0, 1, 1);
      texcoord.add_data2(0, 1);

      vertex.add_data3(0, 0, 0);
      normal.add_data3(0, 0, 1);
      color.add_data4(0, 0, 1, 1);
      texcoord.add_data2(0, 0);

Each call to addData() adds a new row (vertex) to the vertex data, if there is
not already one there. The above sample code creates the following data table:

== ========= ========= ============ ========
\  vertex    normal    color        texcoord
0  (1, 0, 0) (0, 0, 1) (0, 0, 1, 1) (1, 0)
1  (1, 1, 0) (0, 0, 1) (0, 0, 1, 1) (1, 1)
2  (0, 1, 0) (0, 0, 1) (0, 0, 1, 1) (0, 1)
3  (0, 0, 0) (0, 0, 1) (0, 0, 1, 1) (0, 0)
== ========= ========= ============ ========

Note that there is no relationship between the different GeomVertexWriters,
other than the fact that they are operating on the same table. Each
GeomVertexWriter maintains its own counter of its current row. This means you
must fill in the data for every row of each column, even if you don't care about
writing the data for some particular column on certain rows. For instance, even
if you want to allow the default color for vertex 1 and 2, you must still call
color.addData4() four times, in order to fill in the color value for vertex 3.
