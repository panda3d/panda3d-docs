.. _texture-filter-types:

Texture Filter Types
====================

It's rare that the pixels of a texture image match one-to-one with actual screen
pixels when a texture is visible onscreen. Usually, it is the case that either a
single pixel of the texture is stretched over multiple screen pixels (texture
magnification--the texture image is stretched bigger), or the opposite, that
multiple pixels of a texture contribute to the color of a single screen pixel
(texture minification--the texture image is squished smaller). Often, a single
polygon will have some texture pixels that need to be magnified, and some pixels
that need to be minified (the graphics card can handle both cases on a single
polygon).

You can control how the texture looks when it is magnified or minified by
setting its filter type.

.. only:: python

   .. code-block:: python

      texture.setMagfilter(type)
      texture.setMinfilter(type)

.. only:: cpp

   .. code-block:: cpp

      texture->set_magfilter(type);
      texture->set_minfilter(type);

The type value is a value from the FilterType enum of :class:`.SamplerState`.
There is a separate filter type setting for magnification and for minification.
For both magnification and minification, the filter type may be one of:

FT_nearest
   Sample the nearest pixel
FT_linear
   Sample the four nearest pixels, and linearly interpolate them

For minification only, in addition to the above two choices, you can also
choose from:

FT_nearest_mipmap_nearest
   Point sample the pixel from the nearest mipmap level
FT_linear_mipmap_nearest
   Bilinear filter the pixel from the nearest mipmap level
FT_nearest_mipmap_linear
   Point sample the pixel from two mipmap levels, and linearly blend
FT_linear_mipmap_linear
   Bilinearly filter the pixel from two mipmap levels, and linearly blend the
   results. This is also called trilinear filtering

The default filter type for both magnification and minification is
``FT_linear``.

Consider the visual effects of the various filter types on magnification and
minification of the following texture:

|A fractal image|

FT_nearest
----------

.. only:: python

   .. code-block:: python

      texture.setMagfilter(SamplerState.FT_nearest)
      texture.setMinfilter(SamplerState.FT_nearest)

.. only:: cpp

   .. code-block:: cpp

      texture->set_magfilter(SamplerState::FT_nearest);
      texture->set_minfilter(SamplerState::FT_nearest);

|Magnification w/FTNearest| |Minification w/FTNearest|

Usually, ``FT_nearest`` is used only to achieve a special pixelly effect.

FT_linear
---------

.. only:: python

   .. code-block:: python

      texture.setMagfilter(SamplerState.FT_linear)
      texture.setMinfilter(SamplerState.FT_linear)

.. only:: cpp

   .. code-block:: cpp

      texture->set_magfilter(SamplerState::FT_linear);
      texture->set_minfilter(SamplerState::FT_linear);

|Magnification w/FTLinear| |Minification w/FTLinear|

``FT_linear`` is a good, general-purpose choice, though it isn't perfect.

Mipmaps
-------

Many graphics tutorials will go on for pages and pages about exactly what
mipmapping means and how it all works inside. We'll spare you those details
here; but you should understand the following things about mipmapping:

1. It requires 33% more texture memory (per mipmapped texture), but it renders
   quickly.

2. It helps the texture look much smoother than filtering alone when it is
   minified.

3. Mipmapping doesn't have anything at all to do with magnification.

4. It has a tendency to blur minified textures out a little too much, especially
   when the texture is applied to a polygon that is very nearly edge-on to the
   camera.

There are four different filter types that involve mipmapping, but you almost
always want to use just the last one, ``FT_linear_mipmap_linear``. The other
modes are for advanced uses, and sometimes can be used to tweak the mipmap
artifacts a bit (especially to reduce point 4, above). If you don't understand
the description in the table above, it's not worth worrying about.

.. only:: python

   .. code-block:: python

      texture.setMinfilter(SamplerState.FT_linear_mipmap_linear)

.. only:: cpp

   .. code-block:: cpp

      texture->set_minfilter(SamplerState::FT_linear_mipmap_linear);

|Minification w/FTLinearMipmapLinear|

Anisotropic Filtering
---------------------

There is one final addition to the texture filtering equation: you can enable
anisotropic filtering on top of any of the above filter modes, which enables a
more expensive, slightly slower rendering mode that generally produces superior
effects. In particular, anisotropic filtering is usually better at handling
texture minification than mipmapping, and doesn't tend to blur out the texture
so much.

To enable anisotropic filtering, you specify the degree:

.. only:: python

   .. code-block:: python

      texture.setAnisotropicDegree(degree)

.. only:: cpp

   .. code-block:: cpp

      texture->set_anisotropic_degree(degree);

The degree should be a power-of-two integer number. The default value is 1,
which indicates no anisotropic filtering; set it to a higher number to indicate
the amount of filtering you require. Larger numbers are more expensive but
produce a better result, up to the capability of your graphics card. Many
graphics cards support up to 16x anisotropic filtering.

.. only:: python

   .. code-block:: python

      texture.setAnisotropicDegree(2)

.. only:: cpp

   .. code-block:: cpp

      texture->set_anisotropic_degree(2);

|Magnification w/anisotropic filtering| |Minification w/anisotropic filtering|

.. |A fractal image| image:: fractal.jpg
.. |Magnification w/FTNearest| image:: texture-mag-nearest.jpg
.. |Minification w/FTNearest| image:: texture-min-nearest.jpg
.. |Magnification w/FTLinear| image:: texture-mag-linear.jpg
.. |Minification w/FTLinear| image:: texture-min-linear-0.jpg
.. |Minification w/FTLinearMipmapLinear| image:: texture-min-mipmap-0.jpg
.. |Magnification w/anisotropic filtering| image:: texture-mag-aniso.jpg
.. |Minification w/anisotropic filtering| image:: texture-min-aniso.jpg
