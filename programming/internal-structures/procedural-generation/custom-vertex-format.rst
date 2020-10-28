.. _defining-your-own-geomvertexformat:

Defining your own GeomVertexFormat
==================================

Before you can create any geometry in Panda3D, you must have a valid
:ref:`geomvertexformat`. You can decide exactly which columns you want to have
in your format, by building the format up one column at a time. (But you might
be able to avoid this effort by taking advantage of one of the
:ref:`pre-defined formats <pre-defined-vertex-formats>` listed on the next
page.)

To build up your custom format, you need to first create an empty
:class:`.GeomVertexArrayFormat`, and add columns one at a time by calling
:meth:`~.GeomVertexArrayFormat.add_column()`:

.. only:: python

   .. code-block:: python

      array = GeomVertexArrayFormat()
      array.addColumn("vertex", 3, Geom.NTFloat32, Geom.CPoint)

.. only:: cpp

   .. code-block:: cpp

      PT(GeomVertexArrayFormat) array;
      array = new GeomVertexArrayFormat();
      array->add_column(InternalName::make("vertex"), 3,
                        Geom::NT_float32, Geom::C_point);

The parameters to :meth:`~.GeomVertexArrayFormat.add_column()` are, in order,
the column name, the number of components, the numeric type, and the contents
specification. See :ref:`geomvertexformat` for a detailed description of each of
these parameters and their appropriate values. You may also supply an optional
fifth parameter, which specifies the byte offset within the row at which the
column's data begins; but normally you should omit this to indicate that the
column's data immediately follows the previous column's data.

.. only:: cpp

   Note that the column name should be an :class:`.InternalName` object, as
   returned by a call to :meth:`.InternalName.make()`. This is Panda's mechanism
   for tokenizing a string name, to allow for fast name lookups during
   rendering. Other than this detail, the column name is really just an
   arbitrary string.

It is your responsibility to ensure that all of the parameters passed to
:meth:`~.GeomVertexArrayFormat.add_column()` are appropriate for the column you
are defining. The column data will be stored exactly as you specify. When
rendering, Panda will attempt to convert the column data as it is stored to
whatever format your graphics API (e.g. OpenGL or DirectX) expects to receive.

For instance, to define a vertex format that includes a vertex position and a
(U, V) texture coordinate:

.. only:: python

   .. code-block:: python

      array = GeomVertexArrayFormat()
      array.addColumn("vertex", 3, Geom.NTFloat32, Geom.CPoint)
      array.addColumn("texcoord", 2, Geom.NTFloat32, Geom.CTexcoord)

.. only:: cpp

   .. code-block:: cpp

      PT(GeomVertexArrayFormat) array;
      array = new GeomVertexArrayFormat();
      array->add_column(InternalName::make("vertex"), 3,
                        Geom::NT_float32, Geom::C_point);
      array->add_column(InternalName::make("texcoord"), 2,
                        Geom::NT_float32, Geom::C_texcoord);

Once you have defined the columns of your array, you should create a
:class:`.GeomVertexFormat` to hold the array:

.. only:: python

   .. code-block:: python

      format = GeomVertexFormat()
      format.addArray(array)

.. only:: cpp

   .. code-block:: cpp

      PT(GeomVertexFormat) unregistered_format;
      unregistered_format = new GeomVertexFormat();
      unregistered_format->add_array(array);

If you want your format to consist of multiple different arrays, you can
create additional arrays and add them at this point as well.

Finally, before you can use your new format, you must register it. Registering
a format builds up the internal tables necessary to use the vertex format for
rendering. However, once you have registered a format, you can no longer add
or remove columns, or modify it in any way; if you want to make changes to the
format after this point, you'll have to start over with a new
:class:`.GeomVertexFormat` object.

.. only:: python

   .. code-block:: python

      format = GeomVertexFormat.registerFormat(format)

.. only:: cpp

   .. code-block:: cpp

      CPT(GeomVertexFormat) format;
      format = GeomVertexFormat::register_format(unregistered_format);

You should always register a format with a syntax similar to the above: that
is, you should use the return value of registerFormat as your new, registered
format object, and discard the original format object. (The returned format
object may be the same format object you started with, or it may be a
different object with an equivalent meaning. Either way, the format object you
started with should be discarded.)
