.. _texture-combine-modes:

Texture Combine Modes
=====================

In addition to the several :ref:`Texture Blend Modes <texture-modes>` described
previously, there is a more advanced interface on TextureStage that allows for a
larger vocabulary of texture blending options.

Although several of the following options (CMReplace, CMModulate, CMAdd) have
obvious parallels with the simpler blend modes described previously, they are in
fact more powerful, because with each of the following you may specify the
particular source or sources to be used for the operation; you are not limited
to simply applying the operation to the top texture and the texture below.

RGB modes
---------

The following specify the effect of the RGB (color) channels. A separate set of
methods, below, specifies the effect of the alpha channel.

.. only:: python

   .. code-block:: python

      ts.setCombineRgb(TextureStage.CMReplace, source, operand)

.. only:: cpp

   .. code-block:: cpp

      ts->set_combine_rgb(TextureStage::CM_replace, source, operand);

This mode is similar to "replace mode". Whatever color is specified by source
and operand becomes the new color.

.. only:: python

   .. code-block:: python

      ts.setCombineRgb(TextureStage.CMModulate, source0, operand0, source1, operand1)

.. only:: cpp

   .. code-block:: cpp

      ts->set_combine_rgb(TextureStage::CM_modulate, source0, operand0, source1, operand1);

This mode is similar to "modulate mode". The color from source0/operand0 is
multiplied by the color from source1/operand1.

.. only:: python

   .. code-block:: python

      ts.setCombineRgb(TextureStage.CMAdd, source0, operand0, source1, operand1)

.. only:: cpp

   .. code-block:: cpp

      ts->set_combine_rgb(TextureStage::CM_add, source0, operand0, source1, operand1);

This mode is similar to "add mode". The color from source0/operand0 is added to
the color from source1/operand1, and the result is clamped to 1 (white).

.. only:: python

   .. code-block:: python

      ts.setCombineRgb(TextureStage.CMAddSigned, source0, operand0, source1, operand1)

.. only:: cpp

   .. code-block:: cpp

      ts->set_combine_rgb(TextureStage::CM_add_signed, source0, operand0, source1, operand1);

In this mode, the colors are added as signed numbers, and the result wraps.

.. only:: python

   .. code-block:: python

      ts.setCombineRgb(TextureStage.CMSubtract, source0, operand0, source1, operand1)

.. only:: cpp

   .. code-block:: cpp

      ts->set_combine_rgb(TextureStage::CM_modulate, source0, operand0, source1, operand1);

In this mode, source1/operand1 is subtracted from source0/operand0.

.. only:: python

   .. code-block:: python

      ts.setCombineRgb(TextureStage.CMInterpolate,
                       source0, operand0, source1, operand1, source2, operand2)


.. only:: cpp

   .. code-block:: cpp

      ts->set_combine_rgb(TextureStage::CM_interpolate,
                          source0, operand0, source1, operand1, source2, operand2);

This is the only mode that uses three sources. The color value of source2/operand2
is used to select between source0/operand0 and source1/operand1. When source2
is 0, source1 is selected, and when source2 is 1, source0 is selected. When
source2 is between 0 and 1, the color is smoothly blended between source0 and
source1.

Alpha modes
-----------

The following methods more-or-less duplicate the functionality of the above,
but they control what happens to the alpha channel. Thus, you have explicit
control over whether an alpha cutout in the top texture should produce an
alpha cutout in the resulting object.

.. only:: python

   .. code-block:: python

      ts.setCombineAlpha(TextureStage.CMReplace, source, operand)
      ts.setCombineAlpha(TextureStage.CMModulate, source0, operand0, source1, operand1)
      ts.setCombineAlpha(TextureStage.CMAdd, source0, operand0, source1, operand1)
      ts.setCombineAlpha(TextureStage.CMAddSigned, source0, operand0, source1, operand1)
      ts.setCombineAlpha(TextureStage.CMSubtract, source0, operand0, source1, operand1)
      ts.setCombineAlpha(TextureStage.CMInterpolate, source0, operand0, source1, operand1,
                         source2, operand2)

.. only:: cpp

   .. code-block:: cpp

      ts->set_combine_alpha(TextureStage::CM_replace, source, operand);
      ts->set_combine_alpha(TextureStage::CM_modulate, source0, operand0, source1, operand1);
      ts->set_combine_alpha(TextureStage::CM_add, source0, operand0, source1, operand1);
      ts->set_combine_alpha(TextureStage::CM_add_signed, source0, operand0, source1, operand1);
      ts->set_combine_alpha(TextureStage::CM_subtract, source0, operand0, source1, operand1);
      ts->set_combine_alpha(TextureStage::CM_interpolate, source0, operand0, source1, operand1,
                            source2, operand2);

Source values
-------------

This table lists the legal values for any of source, source0, source1, or
source2, in the above calls. This broadly gives you control over which two (or
three) textures are used as inputs to the above combine modes.

.. only:: python

   TextureStage.CSTexture
      The current, or “top” texture image.

   TextureStage.CSConstant
      A constant color, specified via :meth:`.TextureStage.set_color()`.

   TextureStage.CSConstantColorScale
      The same as CSConstant, but the color will be modified by
      :meth:`.NodePath.set_color_scale()`.

   TextureStage.CSPrimaryColor
      The “primary” color of the object, before the first texture stage was
      applied, and including any lighting effects.

   TextureStage.CSPrevious
      The result of the previous texture stage; i.e. the texture below.

   TextureStage.CSLastSavedResult
      The result of any of the previous texture stages; specifically, the last
      stage for which :meth:`TextureStage.set_saved_result(True)
      <.TextureStage.set_saved_result>` was called.

.. only:: cpp

   TextureStage::CS_texture
      The current, or “top” texture image.

   TextureStage::CS_constant
      A constant color, specified via :cpp:func:`TextureStage::set_color()`.

   TextureStage::CS_constant_color_scale
      The same as CS_constant, but the color will be modified by
      :cpp:func:`NodePath::set_color_scale()`.

   TextureStage::CS_primary_color
      The “primary” color of the object, before the first texture stage was
      applied, and including any lighting effects.

   TextureStage::CS_previous
      The result of the previous texture stage; i.e. the texture below.

   TextureStage::CS_last_saved_result
      The result of any of the previous texture stages; specifically, the last
      stage for which :cpp:func:`TextureStage::set_saved_result(true)
      <TextureStage::set_saved_result>` was called.

Operands
--------

This table lists the legal values for any of operand, operand0, operand1, or
operand2, in the above calls. This fine-tunes the channel data that is used from
each texture input.

.. only:: python

   TextureStage.COSrcColor
      Use the RGB color. When used in a
      :meth:`~.TextureStage.set_combine_alpha()` call, RGB is automatically
      aggregated into grayscale.

   TextureStage.COOneMinusSrcColor
      The complement of the RGB color.

   TextureStage.COSrcAlpha
      Use the alpha value. When used in a
      :meth:`~.TextureStage.set_combine_rgb()` call, alpha is automatically
      expanded into uniform RGB.

   TextureStage.COOneMinusSrcAlpha
      The complement of the alpha value.

.. only:: cpp

   TextureStage::CO_src_color
      Use the RGB color. When used in a
      :meth:`~.TextureStage.set_combine_alpha()` call, RGB is automatically
      aggregated into grayscale.

   TextureStage::CO_one_minus_src_color
      The complement of the RGB color.

   TextureStage::CO_src_alpha
      Use the alpha value. When used in a
      :meth:`~.TextureStage.set_combine_rgb()` call, alpha is automatically
      expanded into uniform RGB.

   TextureStage::CO_one_minus_src_alpha
      The complement of the alpha value.
