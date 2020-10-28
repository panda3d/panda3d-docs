.. _geomvertexformat:

GeomVertexFormat
================

The :class:`.GeomVertexFormat` object describes how the columns of a
GeomVertexData are ordered and named, and exactly what kind of numeric data is
stored in each column. Every GeomVertexData has an associated GeomVertexFormat,
which describes how the data in that object is stored.

Just as a GeomVertexData object is really a list of one or more
GeomVertexArrayData objects, a GeomVertexFormat object is a list of one or
more GeomVertexArrayFormat objects, each of which defines the structure of the
corresponding array. There will be one GeomVertexArrayFormat object for each
array in the format. Each GeomVertexArrayFormat, in turn, consists of a list
of GeomVertexColumn objects, one for each column in the array. For instance,
the format for a GeomVertexData with six columns, distributed over three
different arrays, might look like this:

.. raw:: html

   <center>
   <table>
   <tr>
   <td style="border: 1px solid black; background: #c1beea; padding: 5pt">
   <p>GeomVertexFormat</p>
   <table>
   <tr>
   <td style="border: 1px solid black; background: #acb1ed; padding: 5pt">
   <p>GeomVertexArrayFormat</p>
   <table>
   <tr>
   <td style="border: 1px solid black; background: #9197d8; padding: 5pt">
   <p>GeomVertexColumn</p>
   </td>
   </tr>
   <tr>
   <td style="border: 1px solid black; background: #9197d8; padding: 5pt">
   <p>GeomVertexColumn</p>
   </td>
   </tr>
   <tr>
   <td style="border: 1px solid black; background: #9197d8; padding: 5pt">
   <p>GeomVertexColumn</p>
   </td>
   </tr>
   </table>
   </td>
   </tr>
   </table>
   <table>
   <tr>
   <td style="border: 1px solid black; background: #acb1ed; padding: 5pt">
   <p>GeomVertexArrayFormat</p>
   <table>
   <tr>
   <td style="border: 1px solid black; background: #9197d8; padding: 5pt">
   <p>GeomVertexColumn</p>
   </td>
   </tr>
   </table>
   </td>
   </tr>
   </table>
   <table>
   <tr>
   <td style="border: 1px solid black; background: #acb1ed; padding: 5pt">
   <p>GeomVertexArrayFormat</p>
   <table>
   <tr>
   <td style="border: 1px solid black; background: #9197d8; padding: 5pt">
   <p>GeomVertexColumn</p>
   </td>
   </tr>
   <tr>
   <td style="border: 1px solid black; background: #9197d8; padding: 5pt">
   <p>GeomVertexColumn</p>
   </td>
   </tr>
   </table>
   </td>
   </tr>
   </table>
   </td>
   </tr>
   </table>
   </center>

Each GeomVertexColumn has a number of properties:

getNumComponents()
   This defines the number of numeric components of the data in the column. For
   instance, the vertex position, which is typically an (X, Y, Z) triple, has
   three components: X, Y, and Z. A texture coordinate usually has two components
   (U, V), but sometimes has three components (U, V, W).

getNumericType()
   This defines the kind of numeric data that is stored in each component. It
   must be one of the following symbols:

   Geom.NT_float32
      Each component is a 32-bit floating-point number. This is by far the
      most common type.

   Geom.NT_uint8
      Each component is a single 8-bit integer, in the range 0 - 255. OpenGL
      encodes an RGBA color value as a four-component array of 8-bit integers
      of this type, in R, G, B, A order.

   Geom.NT_uint16
      Each component is a single 16-bit integer, in the range 0 - 65535.

   Geom.NT_uint32
      Each component is a single 32-bit integer, in the range 0 - 4294967295.

   Geom.NT_packed_dcba
      Each component is a 32-bit word, with four 8-bit integer index values
      packed into it in little-endian order (D, C, B, A), DirectX-style. This
      is usually used with a 1-component column (since each component already
      has four values). DirectX uses this format to store up to four indexes
      into a transform table for encoding vertex animation. (The
      GeomVertexReader and GeomVertexWriter classes will automatically reorder
      the A, B, C, D parameters you supply into DirectX's D, C, B, A order.)

   Geom.NT_packed_dabc
      Each component is a 32-bit word, with four 8-bit integer index values
      packed into it in ARGB order (D, A, B, C). As above, this is normally
      used with a 1-component column. DirectX uses this format to represent an
      RGBA color value. (The GeomVertexReader and GeomVertexWriter classes
      will automatically reorder the R, G, B, A parameters you supply into
      DirectX's A, R, G, B order.) This should only be used with a C_color
      contents value.

   Geom.NT_packed_ufloat
      Each component is a 32-bit word, containing two packed unsigned 11-bit
      floats and one 10-bit float. Only supported in newer OpenGL versions
      from Panda3D 1.10 onward. Can only encode values between 0 and 64512.

getContents()
   This defines, in a general way, the semantic meaning of the data in the
   column. It is used by Panda to decide how the data should be modified when
   a transform matrix or texture matrix is applied; it also controls the
   default value for the column data, as well as the way data is stored and
   fetched from the column. The contents specification must be one of the
   following symbols:

   Geom.C_point
      The data represents a point in object coordinates, either in 3-D space
      (if it is a 3-component value) or in 4-D homogenous space (if it is a
      4-component value). When a transform matrix is applied to the vertex
      data, the data in this column is transformed as a point. If a
      4-component value is stored into a 3-component column, the fourth
      component is understood to be a homogenous coordinate, and it implicitly
      scales the first three. Similarly, if a 4-component value is read from a
      3-component column, the fourth value is implicitly 1.0.

   Geom.C_clip_point
      The data represents a point already transformed into clip coordinates;
      that is, these points have already been transformed for rendering
      directly. Panda will not transform the vertices again during rendering.
      Points in clip coordinates should be in 4-D homogeneous space, and thus
      usually have four components.

   Geom.C_normal
      The data represents a 3-D normal vector, perpendicular to the surface.
      This is different from C_vector in that it preserves this orthogonality
      when non-uniform scales are applied. It also makes sure that a unit
      length vector stays normalized when a scale is applied. New in 1.9.1;
      C_vector is used in earlier releases.

   Geom.C_vector
      The data represents a generic 3-D vector, such as a tangent, or
      binormal, in object coordinates. When a transform matrix is applied to
      the vertex data, the data in this column is transformed as a vector
      (that is, ignoring the matrix's translation component).

   Geom.C_texcoord
      The data represents a texture coordinate, either 2-D or 3-D. When a
      texture matrix (not a transform matrix) is applied to the vertex data,
      it transforms the data in this column, as a point.

   Geom.C_color
      The data represents an RGBA color value. If a floating-point value is
      used to read or write into an integer color component, it is
      automatically scaled from 0.0 .. 1.0 into the full integer range. Also,
      the default value of a color column is (1, 1, 1, 1), as opposed to any
      other columns, whose default value is 0. Must have 3 or 4 components.

   Geom.C_index
      The data represents an integer index into some table.

   Geom.C_morph_delta
      The data represents an offset value that will be applied to some other
      column during animation.

   Geom.C_other
      The data has some other, custom meaning; do not attempt to transform it.

getName()
   The column name is the most important single piece of information to Panda.
   The column name tells Panda the specific meaning of the data in the column.
   The name is also a unique handle to the column; within a given format,
   there may not be two different columns with the same name. There are a
   number of column names that have special meaning to Panda:

   vertex
      The position in space of each vertex, usually given as an (x, y, z)
      triple in 3-D coordinates. This is the only mandatory column for
      rendering geometry; all other columns are optional. The vertex is
      usually Geom.NTFloat32, Geom.CPoint, 3 components.

   normal
      The surface normal at each vertex. This is used to compute the visible
      effects of lighting; it is not related to the collision system, which
      has its own mechanism for determining the surface normal. You should
      have a normal column if you intend to enable lighting; if this column is
      not present, the object may look strange in the presence of lighting.
      The normal should always be Geom.NTFloat32, Geom.C_vertex, 3 components.

   texcoord
      The U, V texture coordinate pair at each vertex, for the default
      coordinate set. This column is necessary in order to apply a texture to
      the geometry (unless you use a TexGenAttrib). It is usually a 2-D
      coordinate pair, but sometimes, when you are using 3-d textures or cube
      maps, you will need a 3-D U, V, W coordinate triple. The texcoord should
      be Geom.NTFloat32, Geom.C_texcoord, 2 or 3 components.

   texcoord.\ *foo*
      This is the U, V texture coordinate pair for the texture coordinate set
      with the name *"foo"* (where *foo* is any arbitrary name). It is only
      necessary if you need to have multiple different texture coordinate sets
      on a piece of geometry, in order to apply multitexturing. As with
      texcoord, above, it may be a 2-d or a 3-d value.

   tangent
      \
   binormal
      These two columns work together, along with the normal column, to
      implement normal maps (bump maps). They define the normal map space at
      each vertex. Like a normal, these should be Geom.NTFloat32,
      Geom.C_vector, 3 components.

   tangent.\ *foo*
      \
   binormal.\ *foo*
      These column names define a tangent and binormal for the texture
      coordinate set with the name *"foo"*.

   color
      This defines an RGBA color value. If this column is not present, the
      default vertex color is white (unless it is overridden with a
      :meth:`nodePath.setColor() <.NodePath.setColor>` call).
      Internally, OpenGL expects the color format to be Geom.NTUint8 (or
      Geom.NTFloat32), Geom.C_color, 4 components, while DirectX expects the
      color to be Geom.NTPackedDabc, Geom.C_color, 1 component.
      In fact, you may use either format regardless of your current rendering
      backend, and Panda will automatically convert the column as necessary.

   rotate
      \
   size
      \
   aspect_ratio
      These three columns are used when rendering sprites (that is, GeomPoints
      with :meth:`nodePath.setRenderModeThickness() <.NodePath.setRenderModeThickness>`
      in effect).
      If present, they control the rotation counterclockwise in degrees, the
      per-vertex thickness, and the aspect ratio of the square, respectively.
      Each of these should be Geom.NTFloat32, Geom.C_other, 1 component.
      The remaining column names have meaning only to define vertex animation,
      for instance to implement Actors. Although these column names are
      documented below, vertex animation is an advanced feature of the Panda
      vertex representation; we recommend you let Panda take care of setting up
      the vertex animation tables, rather than attempting to create them
      yourself.

   transform_blend
      This is used to control vertex assignment to one or more animated
      transform spaces. The value in this column is an integer index into the
      TransformBlendTable that is associated with the GeomVertexData; each
      entry in the TransformBlendTable defines a different weighted
      combination of transform spaces, so by indexing into this table, you can
      associate each vertex with a different weighted combination of transform
      spaces.

   transform_weight
      \
   transform_index
      These two columns work together, in a manner similar to transform_blend,
      but they index into the TransformTable associated with the
      GeomVertexData, instead of the TransformBlendTable. This is particularly
      suited for sending vertices to OpenGL or DirectX to do the animation,
      rather than performing the animation on the CPU.

   column.morph.\ *slider*
      Columns with names of this form define a floating-point morph offset
      that should be scaled by the value of the morph slider named *"slider"*,
      and then added to the column named *"column"* (where *slider* and
      *column* are arbitrary names). This is used during vertex animation on
      the CPU.

A column may have any name (though each name must be unique within a given
GeomVertexFormat). If there are additional columns with names other than those
in the above table, Panda will not do anything special with the columns, but
it will send the vertex data to any vertex shader that requests that data by
name, using the vtx\_columnname parameter name. See
:ref:`List of Possible Shader Inputs <list-of-possible-cg-shader-inputs>`.

There are also additional properties associated with each GeomVertexColumn
that determine its exact offset and byte-alignment within each row of the
array, but normally you do not need to worry about these, unless you are
designing a GeomVertexFormat that matches some already-existing block of data.
See the auto-generated API specification for more details.
