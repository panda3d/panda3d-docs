.. _list-of-all-attributes:

List of All Attributes
======================

List of All Attributes
----------------------

The following is a concise list of all the RenderAttribs supported by Panda3D.
Additional documentation can be found by clicking on the name of the
RenderAttrib.

-  :ref:`AlphaTestAttrib <alpha-testing>`: Hides part of the model, based on
   the texture's alpha channel.

-  :ref:`AntialiasAttrib <antialiasing>`: Controls full-screen antialiasing
   and polygon-edge antialiasing.

-  AudioVolumeAttrib: Applies a scale to audio volume for positional sounds.

-  :ref:`AuxBitplaneAttrib <auxiliary-bitplane-control>`: Causes shader
   generator to produce extra data.

-  :ref:`ClipPlaneAttrib <clip-planes>`: Slices off a piece of the model,
   using a clipping plane.

-  :ref:`ColorAttrib <tinting-and-recoloring>`: Tints the model. Only works if
   the model is not illuminated.

-  :ref:`ColorBlendAttrib <transparency-and-blending>`: This specifies how
   colors are blended into the frame buffer, for special effects.

-  :ref:`ColorScaleAttrib <tinting-and-recoloring>`: Modulates vertex colors
   with a flat color.

-  :ref:`ColorWriteAttrib <color-write-masks>`: Causes the model to not affect
   the R, G, B, or A channel of the framebuffer.

-  CullBinAttrib: Controls the order in which Panda renders geometry.

-  :ref:`CullFaceAttrib <backface-culling-and-frontface-culling>`: Causes
   backfaces or frontfaces of the model to be visible.

-  DepthOffsetAttrib: Causes the Z-buffer to treat the object as if it were
   closer or farther.

-  :ref:`DepthTestAttrib <depth-test-and-depth-write>`: Alters the way the
   Z-buffer affects the model.

-  :ref:`DepthWriteAttrib <depth-test-and-depth-write>`: Controls whether or
   not the model affects the Z-buffer.

-  :ref:`FogAttrib <fog>`: Causes the model to be obscured by fog if it is far
   from the camera.

-  :ref:`LightAttrib <lighting>`: Causes the model to be illuminated by
   certain lights.

-  :ref:`LightRampAttrib <light-ramps>`: Enables HDR tone mapping or cartoon
   shading.

-  :ref:`MaterialAttrib <materials>`: Changes the way the model reflects
   light.

-  RenderModeAttrib: Used to enable wireframe rendering.

-  RescaleNormalAttrib: Can disable the automatic correction of non-unit
   normals.

-  ShadeModelAttrib: Can cause the model to appear faceted instead of smooth.

-  :ref:`ShaderAttrib <shaders>`: Gives almost unlimited control, but
   difficult to use.

-  :ref:`StencilAttrib <stencil-attribute>`: Causes the model to affect the
   stencil buffer, or be affected by the stencil buffer.

-  :ref:`TexGenAttrib <automatic-texture-coordinates>`: Causes the system to
   synthesize texture coordinates for the model.

-  :ref:`TexMatrixAttrib <texture-transforms>`: Alters the existing texture
   coordinates.

-  :ref:`TextureAttrib <texturing>`: Applies a texture map to the model.

-  :ref:`TransparencyAttrib <transparency-and-blending>`: Causes the model to
   be partially transparent.

Undocumented
------------

Unfortunately, the Panda3D manual is still a work in progress: there are many
aspects of it that are not fully documented yet. These attributes are not yet
documented:

AudioVolumeAttrib, CullBinAttrib, DepthOffsetAttrib, RenderModeAttrib,
RescaleNormalAttrib, ShadeModelAttrib

However, although the manual does not document these classes, the
:ref:`reference` documentation does.


