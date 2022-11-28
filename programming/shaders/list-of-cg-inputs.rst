.. _list-of-possible-cg-shader-inputs:

List of Possible Cg Shader Inputs
=================================

.. caution::

   Support for Cg shaders will be deprecated in an upcoming version of Panda3D.

In many cases, it is desirable to access information from the render state or
from the 3-D transformation of the node that is currently being rendered.
Instead of having to pass all this information manually, it is possible to name
your variables in a special way that Panda3D will recognize and automatically
populate with the relevant data.

The following table describes the inputs that can be used in Cg shaders.

``uniform sampler2D tex_0 : TEXUNIT0``
   The model's first texture. This requires that the model be textured in the
   normal manner. You may also use tex_1, tex_2, and so forth, if the model is
   multitextured.

``sampler3D`` or ``samplerCUBE``
   If the model uses a 3D texture or a cubemap, use tex3D and texCUBE to access
   the color.

``float3 vtx_position: POSITION``
   Vertex Position. Vertex shader only. You may also use float4, in which case
   ``(w==1)``.

``float3 vtx_normal: NORMAL``
   Vertex Normal. Vertex shader only.

``float4 vtx_color : COLOR``
   Vertex color. Vertex shader only.

``float2 vtx_texcoord0: TEXCOORD0``
   UV(W) coordinate set associated with the model's first texture. This requires
   that the model be textured in the normal manner. You may also use
   vtx_texcoord1, vtx_texcoord2, and so forth if the model is multitextured.
   Vertex shader only.

``float2 vtx_texcoord: TEXCOORD0``
   This refers to the default (unnamed) set of UV(W) coordinates, if present,
   rather than being an alias for vtx_texcoord0. Vertex shader only.

``float2 vtx_texcoord_x: TEXCOORD0``
   This refers to a set of UV(W) coordinates with the given name. Vertex shader
   only.

``float3 vtx_tangent0``
   Tangent vector associated with the model's first texture. This can only be
   used if the model has been textured in the normal manner, and if binormals
   have been precomputed. You may also use vtx_tangent1, vtx_tangent2, and so
   forth if the model is multitextured. Vertex shader only.

``float3 vtx_binormal0``
   Binormal vector associated with vtx_texcoord0. This can only be used if the
   model has been textured in the normal manner, and if binormals have been
   precomputed. You can also use vtx_binormal1, vtx_binormal2, and so forth if
   the model has been multitextured. Vertex shader only.

``floatX vtx_anything``
   Panda makes it possible to store arbitrary columns of user-defined data in
   the vertex table; see :ref:`geomvertexdata`. You can access this data using
   this syntax. For example, vtx_chicken will look for a column named "chicken"
   in the vertex array. Vertex shader only.

``uniform float4x4 trans_x_to_y``
   A matrix that transforms from coordinate system X to coordinate system Y. See
   the section on :ref:`shaders-and-coordinate-spaces` for more information.

``uniform float4x4 tpose_x_to_y``
   Transpose of trans_x_to_y

``uniform float4 row0_x_to_y``
   Row 0 of trans_x_to_y.

``uniform float4 row1_x_to_y``
   Row 1 of trans_x_to_y.

``uniform float4 row2_x_to_y``
   Row 2 of trans_x_to_y.

``uniform float4 row3_x_to_y``
   Row 3 of trans_x_to_y.

``uniform float4 col0_x_to_y``
   Col 0 of trans_x_to_y.

``uniform float4 col1_x_to_y``
   Col 1 of trans_x_to_y.

``uniform float4 col2_x_to_y``
   Col 2 of trans_x_to_y.

``uniform float4 col3_x_to_y``
   Col 3 of trans_x_to_y.

``uniform float4x4 mstrans_x``
   Model-Space Transform of X, aka trans_x_to_model

``uniform float4x4 cstrans_x``
   Clip-Space Transform of X, aka trans_x_to_clip

``uniform float4x4 wstrans_x``
   World-Space Transform of X, aka trans_x_to_world

``uniform float4x4 vstrans_x``
   View-Space Transform of X, aka trans_x_to_view

``uniform float4 mspos_x``
   Model-Space Position of X, aka row3_x_to_model

``uniform float4 cspos_x``
   Clip-Space Position of X, aka row3_x_to_clip

``uniform float4 wspos_x``
   World-Space Position of X, aka row3_x_to_world

``uniform float4 vspos_x``
   View-Space Position of X, aka row3_x_to_view

``uniform float4x4 mat_modelview``
   Modelview matrix, transforming model-space coordinates to camera-space
   coordinates.

``uniform float4x4 inv_modelview``
   Inverse of the model-view Matrix

``uniform float4x4 tps_modelview``
   Transposed Modelview Matrix

``uniform float4x4 itp_modelview``
   Inverse Transposed Modelview Matrix

``uniform float4x4 mat_projection``
   Projection Matrix

``uniform float4x4 inv_projection``
   Inverse Projection Matrix

``uniform float4x4 tps_projection``
   Transposed Projection Matrix

``uniform float4x4 itp_projection``
   Inverse Transposed Projection Matrix

``uniform float4x4 mat_modelproj``
   Composed Modelview/Projection Matrix

``uniform float4x4 inv_modelproj``
   Inverse ModelProj Matrix

``uniform float4x4 tps_modelproj``
   Transposed ModelProj Matrix

``uniform float4x4 itp_modelproj``
   Inverse Transposed ModelProj Matrix

``uniform float4 anything``
   A constant vector that was stored using ``setShaderInput``. Parameter
   anything would match data supplied by the call ``setShaderInput("anything",
   Vec4(x,y,z,w))``

``uniform sampler2D anything``
   \
``uniform sampler3D anything``
   \
``uniform sampler2DArray anything``
   \
   A constant texture that was stored using ``setShaderInput``. Parameter
   *anything* would match data supplied by the call
   ``setShaderInput("anything", myTex)``

``uniform float4x4 anything``
   A constant matrix that was stored using ``setShaderInput``. Parameter
   anything would match data supplied by the call setShaderInput("anything",
   myNodePath). The matrix supplied is the nodepath's local transform.

``uniform float4 texpad_x``
   X must be the name of a texture specified via shaderInput. Contains the U,V
   coordinates of the center of the texture. This will be (0.5,0.5) if the
   texture is not padded, but it will be less if the texture is padded.

``uniform float4 texpix_x``
   X must be the name of a texture specified via shaderInput. Contains the U,V
   offset of a single pixel in the texture (ie, the reciprocal of the texture
   size).

``uniform float4x4 attr_material``
   The contents of the material attribute. Row 0 is ambient, Row 1 is diffuse,
   Row 2 is emission, Row 3 is specular, with shininess in W.

``uniform float4 attr_color``
   The contents of the color attribute. This is white unless the model has a
   flat color applied.

``uniform float4 attr_colorscale``
   The contents of the color scale attribute. This is white unless the model has
   a color scale applied using nodePath.setColorScale.

``uniform float4 attr_fog``
   The fog parameters, where applicable. The values are in order: density,
   start, end, scale. The density is for exponential fog only, the start, end
   and scale are for linear fog only. The scale is equal to 1 / (end - start).

``uniform float4 attr_fogcolor``
   The fog color, if applicable.

``uniform float4 alight_x``
   X must be an AmbientLight specified via a shaderInput. Contains the color of
   the light.

``uniform float4x4 dlight_x``
   X must be an DirectionalLight specified via a shaderInput. Row 0 is color,
   row 1 is specular, row 2 is model-space direction, row 3 is model-space
   pseudo half-angle.

``uniform float4 plane_x``
   X must be an PlaneNode specified via a shaderInput. Contains the four terms
   of the plane equation.

``uniform float4 clipplane_0``
   Contains the parameters of the first clipplane (also: clipplane_1,
   clipplane_2, etc. for subsequent clip planes) in world-space coordinates.

``uniform float sys_time``
   Contains the frame time in seconds.

``floatX l_position: POSITION``
   Linearly interpolated Position, as supplied by the vertex shader to the
   fragment shader. Declare "out" in the vertex shader, "in" in the fragment
   shader.

``floatX l_color0: COLOR0``
   Linearly interpolated Primary color, as supplied by the vertex shader to the
   fragment shader. Declare "out" in the vertex shader, "in" in the fragment
   shader.

``floatX l_color1: COLOR1``
   Linearly interpolated Secondary color, as supplied by the vertex shader to
   the fragment shader. Declare "out" in the vertex shader, "in" in the fragment
   shader.

``floatX l_texcoord0: TEXCOORD0``
   Linearly interpolated Texture Coordinate 0, as supplied by the vertex shader
   to the fragment shader. You may also use l_texcoord1, l_texcoord2, and so
   forth. Declare "out" in the vertex shader, "in" in the fragment shader.

``out floatX o_color: COLOR``
   Output Color, as supplied by the fragment shader to the blending units.
   Fragment shader only. (COLOR0 is also accepted.)

``out floatX o_aux: COLOR1``
   Output auxiliary color. Only available if an auxiliary was obtained for the
   shaders target buffer/window. Fragment shader only.

Using Custom Shader Inputs
--------------------------

As of Panda3D 1.8.0, the capabilities for passing numeric shader inputs have
been greatly enhanced. The available input types are as follows::

   - Vec4
   - Vec3
   - Vec2
   - Point4
   - Point3
   - Point2
   - Mat4
   - Mat3
   - PTALMatrix4f
   - PTALMatrix3f
   - PTALVecBase4f
   - PTALVecBase3f
   - PTALVecBase2f
   - PTAFloat
   - PTADouble

For definition let us consider the shader parameter float3. It's type is float
and format is Vec3 (meaning it can hold 3 elements) and a float3x3 input is of
type float and format Mat3 (meaning it can hold 9 elements)

The main concept of the shader inputs is that the Cg input format and type is
independent to the Panda3D input. The only condition is that the number of
elements passed by the user through the setShaderInput() function of Panda3D
and the number of elements expected by the shader input should be the same.
For example, a parameter uniform float4x4 mat[4] (total of 16*4 elements) could
be set with: (the below list is just a sample and there are more ways to
represent it)

.. code-block:: python

   setShaderInput("input_name",PTALMat4f[4])
   setShaderInput(PTALVecBase4f[16])
   setShaderInput(PTAFloat[16*4])
   setShaderInput(PTADouble[16*4])

But for some Cg input types there is no corresponding Panda3D type such as
float3x2(Panda3D does not have a corresponding Mat3x2 class) Hence these input
types can be initiated row-wise as

1 2 3

4 5 6

This row wise input can be sent to the Cg shader in any of the following
ways: (Note that the below list is just a sample and there are more ways to
represent it)

.. code-block:: python

   setShaderInput(PTAFloat[6])
   setShaderInput(PTADouble[6])
   setShaderInput(PTALVecBase3f[2])
   setShaderInput(PTALVecBase2f[3])

Now, the issue of common input types such as float, double, int, long. The GPU
registers generally can handle only floats. Hence even if we do send a double
it will be automatically type casted into float. Hence for such type of inputs
we can use above types.

For example, input types such as

.. code-block:: python

   float3 var
   bool3 var
   half3 var
   double3 var
   fixed3 var
   int3 var

Can be sent to your Cg shader program by (the below list is just a sample and
there are more ways to represent it)

.. code-block:: python

   setShaderInput(PTAFloat[3])
   setShaderInput(PTADouble[3])

Below is a sample code snippet that shows how you can use the new shader inputs.

.. code-block:: python

   from panda3d.core import Vec4
   vec4 = Vec4(0.0,1.0,0.0,1.0)
   myModel.setShaderInput("Inputs.vec4",vec4)

First import the necessary header to use the type of input. In our case it's
:class:`.Vec4`. The next statement shows a Vec4 input type. Then set the Vec4 as
a shader input to your model.
