.. _common-image-filters:

Common Image Filters
====================

.. only:: cpp

   .. note::

      Sorry, but the CommonFilters and FilterManager classes are implemented in
      Python and will not be of much use to C++ users.

The purpose of the :py:class:`~direct.filter.CommonFilters.CommonFilters` class
is to make it easy to set up a number of common image postprocessing operations.

Import the class like this:

.. code-block:: python

   from direct.filter.CommonFilters import CommonFilters

Currently, the image postprocessing operations supported by CommonFilters are:

#. Bloom Filter - creates a glowing halo around bright objects.
#. Cartoon Inker - draws black lines around 3D objects.
#. Volumetric Lighting - screen-space method for casting god-rays.
#. Inverted Filter - inverts all colors.
#. Blur/Sharpen Filter - applies a generic blur or sharpen filter.
#. Ambient Occlusion - applies a screen-space ambient occlusion filter.
#. Gamma Adjust - applies a gamma adjustment.
#. sRGB Encode - ensures the image is encoded using the sRGB inverse EOTF.
#. High Dynamic Range Filter - enables HDR rendering and tone mapping.
#. Exposure Adjust - applies exposure compensation before tone mapping.
#. MSAA - enables multisample antialiasing.

Basic Setup
-----------

The first step is to create an object of class CommonFilters. Pass in a pointer
to your window, and your 3D camera:

.. code-block:: python

   filters = CommonFilters(base.win, base.cam)

This will have no effect until you enable a filter (instructions below.) Once a
filter is enabled, class CommonFilters will reconfigure the Panda3D rendering as
follows:

-  It will render the scene into an offscreen buffer, using the camera you
   provided.
-  It will remove the scene from the specified window, and replace it with a
   fullscreen quad.
-  The quad will be textured with the scene, plus a shader that implements
   whatever filter you have selected.

If all goes well, the net effect is that your scene will continue to appear in
your window, but it will be filtered as you specify.

What if the Video Card can't handle it?
---------------------------------------

If the video card is not capable of implementing your filters, then all filters
will be removed and the filter-enabling function will return False.
Otherwise, filter-enabling functions will return True.

The Bloom Filter
----------------

The bloom filter causes bright objects to have a glowing halo around them. To
enable a bloom filter, use ``setBloom``. To disable, use ``delBloom``:

.. code-block:: python

   filters.setBloom( ... options ...)
   filters.delBloom()

The bloom filter works as follows. First, it renders the scene into a texture.
It also asks the renderer to render any glow-maps into the alpha channel of the
texture. After rendering the scene, it generates a second copy of the scene
which has been darkened until only the brightest pixels are visible, and all the
others go to black. It then blurs that texture, yielding soft halos where the
bright pixels used to be, and black everywhere else. It then adds the soft halos
back onto the scene in the window.

Note: If you want to use glow maps to indicate which parts of the image should
receive bloom, you should assign a nonzero value to the alpha value of the
blend-weight parameter, and you should enable the
:ref:`shader generator <the-shader-generator>` for the models that have glow maps
applied.

The bloom filter has many keyword parameters:

-  blend - The bloom filter needs to measure the brightness of each pixel. It
   does this by weighting the R,G,B, and A components. Default weights:
   (0.3,0.4,0.3,0.0). You should assign a nonzero weight to the alpha channel
   if you want the glow map to have an effect, or a value like (0, 0, 0, 1) if
   you only want your glow map to indicate which models should glow.

-  mintrigger - Minimum brightness at which a halo is generated. Default: 0.6

-  maxtrigger - Maximum brightness at which the halo reaches peak intensity.
   Default: 1.0

-  desat - Degree to which the halo is desaturated. Setting this to zero means
   the halo is the same color as the bright pixel. Setting it to one means the
   halo is white. Default: 0.6

-  intensity - An adjustment parameter for the brightness of the halos.
   Default: 1.0

-  size - Adjusts the size of the halos. Takes a string value: "small",
   "medium", or "large". The reason that this is a discrete value and not a
   continuous one is that the blur operation involves downsampling the
   original texture by a power of two. Default: "medium"

The Cartoon Inking Filter
-------------------------

The cartoon inking filter causes objects to have black lines around them. To
enable a cartoon inking filter, use ``setCartoonInk``. To disable, use
``delCartoonInk``:

.. code-block:: python

   filters.setCartoonInk( ... options ...)
   filters.delCartoonInk()

The cartoon inking filter works by rendering a camera-space normal into an
texture. Then, a postprocessing filter does an edge-detect algorithm on the
camera-space normal texture.

The filter has the following keyword parameters:

-  separation - Distance in pixels, controls the width of the ink line.
   Default: 1 pixel.

-  color - Color of the outline. Default: (0, 0, 0, 1)

The Volumetric Lighting Filter
------------------------------

The Volumetric Lighting filter makes objects cast visible light rays (also known
as crepuscular rays, god rays or sunbeams) that can be occluded by visible
geometry. This is an easy way to easily create nice-looking light/sun effects.

.. code-block:: python

   filters.setVolumetricLighting( ... options ...)
   filters.delVolumetricLighting()

The filter has the following keyword parameters:

-  caster - NodePath that indicates the origin of the rays. Usually, you would
   pass your light, and create a sun billboard which is reparented to the
   light's NodePath.

-  numsamples - Number of samples. The more samples you use, the slower the
   effect will be, but you will have smoother light rays. Note that using a
   fuzzy billboarded dot instead of a hard-edged sphere as light caster can
   help with smoothing the end result, too. This value does not need to be a
   power-of-two, it can be any positive number. Default: 32

-  density - This defines the length of the rays. The default value of 5.0 is
   probably too high for many purposes, usually a value between 0.5 and 1.0
   works best. This also depends on the number of samples and exposure you've
   chosen, though. Default: 5.0

-  decay - Decay makes rays gradually decrease in brightness. The default
   value of 0.1 is not well chosen and makes the rays very short! Usually,
   this a value close to 1.0, like 0.98. Default: 0.1

-  exposure - Defines the brightness of the rays. Default: 0.1

The Inverted Filter
-------------------

This filter simply inverts the colors of the image.

.. code-block:: python

   filters.setInverted()
   filters.delInverted()

This filter has no parameters.

The Blur / Sharpen Filter
-------------------------

This filter can apply a blur or sharpen effect to the image.

.. code-block:: python

   filters.setBlurSharpen( ... options ...)
   filters.delBlurSharpen()

The filter has the following keyword parameters:

-  amount - The amount of blurring, this is usually a value between 0.0 and
   2.0. You can take values smaller than 0.0 or larger than 2.0, but this
   usually gives ugly artifacts. A value of 0.0 means maximum blur. A value of
   1.0 does nothing, and if you go past 1.0, the image will be sharpened
   instead of blurred. Default: 0.0

The Ambient Occlusion Filter
----------------------------

This filter adds a simple screen-space ambient occlusion effect to the scene.

.. code-block:: python

   filters.setAmbientOcclusion( ... options ...)
   filters.delAmbientOcclusion()

It is important that the viewing frustrum's near and far values fit the scene as
tightly as possible. Note that you need to do lots of tweaking to the parameters
to get this filter to work for your particular situation.

The filter has the following keyword parameters:

-  numsamples - The amount of samples used. Default: 16

-  radius - The sampling radius of the rotating kernel. Default: 0.05

-  amount - Default: 2.0

-  strength - Default: 0.01

-  falloff - Default: 0.000002

The Gamma Adjust Filter
-----------------------

This filter performs a simple gamma adjustment by raising the color values to
the given power.

Do not use this to adjust to the 2.2 gamma of a computer monitor.  For that,
see the below filter.

.. code-block:: python

   filters.setGammaAdjust(1.5)
   filters.delGammaAdjust()

The sRGB Encode Filter
----------------------

This filter applies the inverse sRGB Electro-Optical Transfer Function (EOTF)
to the final rendering result.  This allows the lighting and blending
calculations to be performed in linear space, which results in more accurate
colors and lighting.

The effect of this is similar to applying a gamma adjustment of 1.0/2.2, but
not quite.  The sRGB transfer function has a linear section in the beginning to
better preserve the fidelity of dark values.

When enabling this, it is important to make sure that all color input textures
are properly configured to use the sRGB format, to prevent them from appearing
too bright and washed-out.

If the ``framebuffer-srgb`` setting is active, this filter is unnecessary.
Panda will detect if this is the case and refuse to apply this filter, in order
to prevent double-applying the sRGB transformation.

.. code-block:: python

   filters.setSrgbEncode()
   filters.delSrgbEncode()

This filter is available as of Panda3D 1.10.7.

The High Dynamic Range Filter
-----------------------------

This filter enables High Dynamic Range rendering.  This will enable the use of
a floating-point framebuffer format and disables clamping of the color values
before they are written to the framebuffer.  This allows you to use far greater
brightness values on your lights, which creates a greater dynamic range in your
scene.  A tonemapping filter (ACES) is used to bring the values back into the
appropriate range for display on a monitor.

Depending on the brightness of your lights, it may be necessary to use the
Exposure Adjust filter in order to prevent an oversaturated image.

It is recommended to set your lights to use an inverse square falloff
attenuation (using ``setAttenuation(0, 0, 1)``), enable the sRGB Encode filter,
and use realistically bright values for your light colors to achieve the most
realistic effect.

.. code-block:: python

   filters.setHighDynamicRange()
   filters.delHighDynamicRange()

This filter is available as of Panda3D 1.10.7.

The Exposure Adjust Filter
--------------------------

This filter is meant to be used in conjunction with the HDR filter, above, in
order to adjust the exposure level.  In a game where the player moves between
different parts of the scene with different lighting levels, it will be
necessary to adjust this on the fly depending on the player's location.
This is similar to how our eyes adjust to different light levels as we move
between areas of differing brightness.

The value is in f-stops, meaning that a value of 0 resulting in no adjustment,
and each value above 0 doubles the scene luminance, whereas each value below 0
halves it.

.. code-block:: python

   filters.setExposureAdjust(0)
   filters.delExposureAdjust()

This filter is available as of Panda3D 1.10.7.

The MSAA Filter
---------------

This is not really a "filter" as such, but just a way to enable multisample
antialiasing on the offscreen buffer.  Doing this has a couple of advantages
compared to enabling multisample filtering on the main window, such as the fact
that you can switch this setting based on detected capabilities and user
settings, without having to reopen the window.

When using this setting, it is recommended to leave multisample filtering off
on the main window, otherwise it will be a waste of GPU memory.  So, do *not*
put ``framebuffer-multisample`` in your Config.prc file.

This filter is available as of Panda3D 1.10.13.
