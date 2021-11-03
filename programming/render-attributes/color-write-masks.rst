.. _color-write-masks:

Color Write Masks
=================

Color Write Masks
-----------------

Color write masks enable you to block writes to the Red, Green, Blue, or Alpha
channels of the framebuffer. This is not a frequently-used capability, but it
does have a few applications:

-  When using red-blue 3D glasses, you might want to render the red image, then
   the blue image. (In fact, Panda uses this technique automatically when you
   set red-blue-stereo 1 in your Config.prc file.)

-  Battletech Battle Pods connect 3 black-and-white monitors to a single R,G,B
   video card output (really!) With the help of color write masks, you could
   update an individual monitor.

-  Sometimes, one wants to store data in the alpha-channel of the framebuffer.
   Using a color mask can avoid accidentally overwriting that data.

Using a color write-mask is not free. During normal rendering, each pixel
written to the frame buffer requires a memory write. With a color-mask active, a
memory read-modify-write cycle is needed, which is more expensive.

By default, color write masks are off.

Turning on the Color Mask
-------------------------

To enable writes to all the channels of the framebuffer, use this:

.. only:: python

   .. code-block:: python

      nodePath.setAttrib(ColorWriteAttrib.make(ColorWriteAttrib.CAll))

.. only:: cpp

   .. code-block:: cpp

      nodePath.set_attrib(ColorWriteAttrib::make(ColorWriteAttrib::C_all));

This can also be done by combining separate attributes for individual channels,
like the following:

.. only:: python

   .. code-block:: python

      bits = ColorWriteAttrib.CAlpha
      bits |= ColorWriteAttrib.CRed
      bits |= ColorWriteAttrib.CGreen
      bits |= ColorWriteAttrib.CBlue
      nodePath.setAttrib(ColorWriteAttrib.make(bits))

.. only:: cpp

   .. code-block:: cpp

      int bits = ColorWriteAttrib::C_alpha;
      bits |= ColorWriteAttrib::C_red;
      bits |= ColorWriteAttrib::C_green;
      bits |= ColorWriteAttrib::C_blue;
      nodePath.set_attrib(ColorWriteAttrib::make(bits));

To disable writes to one or more channels, omit that bit in the code above.
