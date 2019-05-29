.. _auxiliary-bitplane-control:

Auxiliary Bitplane Control
==========================

Auxiliary Bitplane Control
--------------------------

The framebuffer always contains a color bitplane and a depth bitplane. It may
also have a stencil bitplane or accumulation bitplane. In addition, if it is a
render-to-texture framebuffer, it may have auxiliary bitplanes. These
auxiliary bitplanes can be used to store more or less arbitrary user-defined
data.

When per-pixel lighting is enabled via
:ref:`the shader generator <the-shader-generator>`, the shader generator can
be asked to produce extra data into the auxiliary bitplanes. This is done by
setting an AuxBitplaneAttrib:



.. code-block:: python

    np.setAttrib(AuxBitplaneAttrib.make(bits))



Where ``bits`` is a set of bits
indicating what should be written into the auxiliary bitplanes.

Although the framebuffer's alpha channel is not technically an auxiliary
bitplane. However, since it is not generally used to store any data of value,
it can also be thought of as an auxiliary bitplane: a place to store
user-defined data.

When the shader generator is not enabled, this attrib has no effect.

Values That Can be Requested
----------------------------


The following is a list of bits that can be passed to AuxBitplaneAttrib.make:

AuxBitplaneAttrib.ABOGlow
   Copy the glow map (aka self-illumination map) into the alpha channel of the
   framebuffer. Usually this is a prelude to running a bloom filter over the
   scene.
AuxBitplaneAttrib.ABOAuxNormal
   Store the camera-space normal of the polygon surface in the RGB channels of
   the first auxiliary bitplane. This is often used to help detect edges in a
   cartoon inking filter.
AuxBitplaneAttrib.ABOAuxGlow
   Copy the glow map (aka self-illumination map) into the alpha channel of the
   first auxiliary bitplane.
