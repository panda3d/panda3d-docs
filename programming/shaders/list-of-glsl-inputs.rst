.. _list-of-glsl-shader-inputs:

List of GLSL Shader Inputs
==========================

In general, the majority of GLSL shader input types can be specified from a
Panda3D application using a call to :meth:`.NodePath.set_shader_input()`.
However, it is often desirable to let Panda3D automatically fill in the values
of shader inputs, especially for inputs that derive their values from the render
state or 3-D transformation of the currently rendered model.

This page demonstrates which shader input names have a special meaning and will
be automatically filled in by Panda3D when the shader is used. Note that the
names and types have to be copied verbatim.

Vertex shader attributes
------------------------

The following attributes are only permissible in vertex shaders.

These inputs use GLSL 1.40 syntax and above. In versions below that, it may be
necessary to replace the "in" keyword with "attribute".

.. code-block:: glsl

   // The position, normal vector and color of the currently processed vertex.
   in vec4 p3d_Vertex;
   in vec3 p3d_Normal;
   in vec4 p3d_Color;

   // The texture coordinates associated with the Nth texture.
   in vec2 p3d_MultiTexCoord0;
   in vec2 p3d_MultiTexCoord1;
   in vec2 p3d_MultiTexCoord2;

   // These are the tangent and binormal vectors, if present.  If an index is appended,
   // it will use the set of binormals and tangents associated with the Nth texture.
   in vec3 p3d_Binormal;
   in vec3 p3d_Binormal0;
   in vec3 p3d_Binormal1;
   in vec3 p3d_Tangent;
   in vec3 p3d_Tangent0;
   in vec3 p3d_Tangent1;

   // Some models, such as those loaded from glTF, only have a 4-component tangent
   // vector and no binormal.  In this case, the binormal is derived as follows:
   //   binormal = cross(p3d_Normal, p3d_Tangent.xyz) * p3d_Tangent.w
   in vec4 p3d_Tangent;

   // A vertex column named "anything".  The number of components should match up with
   // that of the vertex array.  "uvec" and "ivec" variants are allowed for integer
   // vertex arrays to access un-normalized data.
   in vec4 anything;

   // These two attributes will be present when hardware skinning is enabled.
   // transform_index contains indices into the p3d_TransformTable array for the four
   // most influential joints, and transform_weight the corresponding weights.
   in vec4 transform_weight;
   in uvec4 transform_index;

A special note about vertex colors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before Panda3D 1.10, if p3d_Color was used but no vertex color information was
present on the model, the values would be undefined (but usually (0, 0, 0, 0)).
This means that you could not use the same shader on objects with and without
vertex colors, since objects without vertex colors would appear black instead of
white.

In 1.10, p3d_Color respects the ColorAttrib rules that also applied to the
fixed-function pipeline: p3d_Color will contain a white color if the vertex
colors are absent or if colors are disabled using
:meth:`~.NodePath.set_color_off()`, and a flat color if one is applied using
:meth:`~.NodePath.set_color()`, even if vertex colors are present.

If you are absolutely certain that the model does not have vertex colors, you
may also declare p3d_Color as a uniform instead of a vertex attribute.

If you would like to treat the color column as a generic vertex attribute with
no special handling, you should use the name "color" instead of "p3d_Color",
which will bind it without any special handling.

Uniform shader inputs
---------------------

The following shader inputs are *uniform*, which means that they are constant
across the entire piece of geometry, rather than changing from vertex to vertex.
They have to be declared with the ``uniform`` qualifier, and may be accessed in
any shader stage.

.. code-block:: glsl

   // This is probably the most important uniform, transforming a model-space
   // coordinate into a clip-space (ie. relative to the window) coordinate.  This
   // is usually used in the vertex shader to transform p3d_Vertex and store the
   // result in gl_Position.
   uniform mat4 p3d_ModelViewProjectionMatrix;

   // These are parts of the above matrix.
   uniform mat4 p3d_ModelViewMatrix;
   uniform mat4 p3d_ProjectionMatrix;
   uniform mat4 p3d_ModelMatrix;
   uniform mat4 p3d_ViewMatrix;
   uniform mat4 p3d_ViewProjectionMatrix;

   // This is the upper 3x3 of the inverse transpose of the ModelViewMatrix.  It is
   // used to transform the normal vector into view-space coordinates.
   uniform mat3 p3d_NormalMatrix;

   // It's possible to append Inverse, Transpose, or InverseTranspose to any of the
   // above matrix names to get an inverse and/or transpose version of that matrix:
   uniform mat4 p3d_ProjectionMatrixInverse;
   uniform mat4 p3d_ProjectionMatrixTranspose;
   uniform mat4 p3d_ModelViewMatrixInverseTranspose;

   // These access the Nth texture applied to the model.  The index matches up with
   // the index used by p3d_MultiTexCoordN, p3d_TangentN, and p3d_BinormalN.
   // The sampler type should be adjusted to match the type of the texture.
   uniform sampler2D p3d_Texture0;
   uniform sampler2DArray p3d_Texture1;
   uniform sampler3D p3d_Texture2;
   uniform samplerCube p3d_Texture3;

   // As above, but "Shadow" should be appended if the texture has a shadow filter.
   uniform sampler2DShadow p3d_Texture0;

   // Experimental inputs, new in 1.10.8, containing textures assigned using a
   // particular TextureStage mode.  If no such texture has been assigned, a dummy
   // texture is instead provided containing an appropriate default color.
   uniform sampler2D p3d_TextureModulate[]; // default color: (1, 1, 1, 1)
   uniform sampler2D p3d_TextureAdd[];      // default color: (0, 0, 0, 1)
   uniform sampler2D p3d_TextureNormal[];   // default color: (0.5, 0.5, 1, 0)
   uniform sampler2D p3d_TextureHeight[];   // default color: (0.5, 0.5, 1, 0)
   uniform sampler2D p3d_TextureGloss[];    // default color: (1, 1, 1, 1)

   // New in 1.10.0.  Contains the matrix generated from texture pos and scale.
   uniform mat4 p3d_TextureMatrix[];

   // Access the color scale applied to the node.
   uniform vec4 p3d_ColorScale;

   // Access the material attributes assigned via a Material object.
   // Unused struct parameters may be omitted without consequence.
   uniform struct p3d_MaterialParameters {
     vec4 ambient;
     vec4 diffuse;
     vec4 emission;
     vec3 specular;
     float shininess;

     // These properties are new in 1.10.
     vec4 baseColor;
     float roughness;
     float metallic;
     float refractiveIndex;
   } p3d_Material;

   // The sum of all active ambient light colors.
   uniform struct p3d_LightModelParameters {
     vec4 ambient;
   } p3d_LightModel;

   // Active clip planes, in apiview space.  If there is no clip plane for a given
   // index, it is guaranteed to contain vec4(0, 0, 0, 0).
   uniform vec4 p3d_ClipPlane[...];

   // Reports the frame time of the current frame, for animations.
   uniform float osg_FrameTime;
   // The time elapsed since the previous frame.
   uniform float osg_DeltaFrameTime;
   // New in 1.10.0. Contains the number of frames elapsed since program start.
   uniform int osg_FrameNumber;

   // If hardware skinning is enabled, this contains the transform of each joint.
   // Superfluous array entries will contain the identity matrix.
   uniform mat4 p3d_TransformTable[...];

   // New in 1.10.  Contains information for each non-ambient light.
   // May also be used to access a light passed as a shader input.
   uniform struct p3d_LightSourceParameters {
     // Primary light color.
     vec4 color;

     // Light color broken up into components, for compatibility with legacy
     // shaders.  These are now deprecated.
     vec4 ambient;
     vec4 diffuse;
     vec4 specular;

     // View-space position.  If w=0, this is a directional light, with the xyz
     // being -direction.
     vec4 position;

     // Spotlight-only settings
     vec3 spotDirection;
     float spotExponent;
     float spotCutoff;
     float spotCosCutoff;

     // Individual attenuation constants
     float constantAttenuation;
     float linearAttenuation;
     float quadraticAttenuation;

     // constant, linear, quadratic attenuation in one vector
     vec3 attenuation;

     // Shadow map for this light source
     sampler2DShadow shadowMap;

     // Transforms view-space coordinates to shadow map coordinates
     mat4 shadowViewMatrix;
   } p3d_LightSource[...];

   // New in 1.10.  Contains fog state.
   uniform struct p3d_FogParameters {
     vec4 color;
     float density;
     float start;
     float end;
     float scale; // 1.0 / (end - start)
   } p3d_Fog;

Besides these predefined uniform inputs, it is possible to use most of the types
available in GLSL in conjunction with :meth:`~.NodePath.set_shader_input()` to
pass custom data, including arrays and structs, to a certain named shader input.
You may not use :meth:`~.NodePath.set_shader_input()` to override any of the
inputs with the ``p3d_`` prefix.
