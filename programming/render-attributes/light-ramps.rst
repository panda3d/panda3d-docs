.. _light-ramps:

Light Ramps
===========

In standard OpenGL and DirectX lighting, the following calculations are
performed:

-  the lighting value is calculated
-  it is clamped to the range 0-1
-  it is combined with the textures
-  it is clamped to the range 0-1 again
-  it is written to the frame buffer

This process contains two clamps. The :class:`.LightRampAttrib` is a means to
specify that you wish to replace these two clamping operators with something a
little smarter. This is particularly relevant for two major graphics algorithms:
HDR tone mapping, and cartoon shading.

It must be emphasized that light ramps have no effect unless per-pixel lighting
is enabled via :ref:`the shader generator <the-shader-generator>`.

HDR Tone Mapping
----------------

.. note::

   For a more advanced way to apply High Dynamic Range rendering, see the HDR
   postprocessing filter described in :ref:`common-image-filters`.

In HDR tone mapping, the first clamp is removed entirely, and the second one is
replaced with the tone mapping operator. The tone mapping operator maps
brightness values in the range 0-infinity to new brightness values in the range
0-1, however, it does so without clamping. To turn on HDR tone mapping, use one
of the following:

.. only:: python

   .. code-block:: python

      np.setAttrib(LightRampAttrib.makeHdr0())
      np.setAttrib(LightRampAttrib.makeHdr1())
      np.setAttrib(LightRampAttrib.makeHdr2())

.. only:: cpp

   .. code-block:: cpp

      np.set_attrib(LightRampAttrib::make_hdr0());
      np.set_attrib(LightRampAttrib::make_hdr1());
      np.set_attrib(LightRampAttrib::make_hdr2());

The HDR2 tone mapping operator is a familiar operator that is used in many
systems. It has the downside that it tends to reduce contrast a lot:

-  FINAL_RGB = (RGB) / (RGB + 1)

The HDR1 tone mapping operator is similar, but it allocates more of the contrast
range to brightnesses in the range 0-1, and less to brightnesses in the range
1-infinity. This yields a higher-contrast scene, but with more washout:

-  FINAL_RGB = (RGB^2 + RGB) / (RGB^2 + RGB + 1)

The HDR0 tone mapping operator allocates even more of the available contrast
range to brightnesses in the range 0-1. This is even more contrasty, but with
even more washout:

-  FINAL_RGB = (RGB^3 + RGB^2 + RGB) / (RGB^3 + RGB^2 + RGB + 1)

Cartoon Shading (Quantized Lighting)
------------------------------------

In cartoon shading, the first clamp is removed entirely, and the second one is
replaced with a quantization function. This replaces a continuous gradient of
brightness values with a discrete set of light levels. This quantization
function only applies to directional lights, not ambient ones.

To enable quantized lighting, use one of these:

.. only:: python

   .. code-block:: python

      np.setAttrib(LightRampAttrib.makeSingleThreshold(t0, l0))
      np.setAttrib(LightRampAttrib.makeDoubleThreshold(t0, l0, t1, l1))

.. only:: cpp

   .. code-block:: cpp

      np.set_attrib(LightRampAttrib::make_single_threshold(t0, l0));
      np.set_attrib(LightRampAttrib::make_double_threshold(t0, l0, t1, l1));

In a single-threshold system, the brightness of the diffuse lighting
contribution is compared to the threshold ``t0``. If the threshold is not met,
the diffuse light contribution is eliminated. If it is met, the pixel's
brightness is normalized to the specified level ``l0``.

In a double-threshold system, the brightness of the diffuse lighting
contribution is compared to the thresholds ``t0`` and ``t1``. If neither is
attained, the diffuse light contribution is eliminated. If it is met, the
pixel's brightness is normalized to either ``l0`` or ``l1``, depending on which
threshold was passed.

Future Light Ramps
------------------

We are interested in knowing if there are any other light ramps you would like
to see. If so, please notify us on the forums.
