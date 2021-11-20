.. _text-fonts:

Text Fonts
==========

Loading a Font
~~~~~~~~~~~~~~

Panda3D can render text using a variety of fonts. If your version of Panda3D has
been compiled with support for the FreeType library (the default distribution of
Panda3D has been), then you can load any TTF file, or any other font file type
that is supported by FreeType, directly:

.. only:: python

   .. code-block:: python

      font = loader.loadFont('arial.ttf')

.. only:: cpp

   .. code-block:: cpp

      PT(TextFont) font = FontPool::load_font("arial.ttf");

The named file is searched for along the model-path, just like a regular egg
file. You can also give the full path to the font file if you prefer (but
remember to observe the :ref:`filename-syntax`).

It is also possible to pre-generate a font with the egg-mkfont command-line
utility::

   egg-mkfont -o arial.egg arial.ttf

This will generate an egg file (arial.egg in the above example) and an
associated texture file that can then be loaded as if it were a font:

.. only:: python

   .. code-block:: python

      font = loader.loadFont('arial.egg')

.. only:: cpp

   .. code-block:: cpp

      PT(TextFont) font = FontPool::load_font("arial.egg");

There are several options you can specify to the egg-mkfont utility; use
``egg-mkfont -h`` to give a list.

For example, to generate a font file with foo.png as the texture, instead of the
default foo.rgb do the following::

   egg-mkfont -pp foo.png -o foo.egg foo.ttf

The advantages to pre-generating a font are (a) the resulting egg file can be
used by a version of Panda that does not include support for FreeType, and (b)
you can apply some painterly effects to the generated texture image using
Photoshop or a similar program (note that you'll need to open the egg file in a
text editor and change the ``<Texture>`` entry to replace "alpha" with "rgba",
otherwise the font will appear grayscale). On the other hand, you have to decide
ahead of time which characters you will want to use from the font; the default
is the set of ASCII characters.

There are three default font files supplied with the default distribution of
Panda3D in the models subdirectory; these are "cmr12.egg", a Roman font,
"cmss12.egg", a Sans-Serif font, and "cmtt12.egg", a Teletypewriter-style
fixed-width font. These three fonts were generated from free fonts provided with
the Metafont utility (which is not a part of Panda3D). There is also a default
font image which is compiled into Panda if you do not load any other font.

Font Quality
~~~~~~~~~~~~

Occasionally, i.e. when displaying large characters and irrespective of the font
used, the default font quality won't be enough and the characters will show
noticeable blurring, especially along curving edges. The way to overcome this is
to set appropriately the *pixels per unit* value of the font object. This is
done through the method :meth:`~.DynamicTextFont.set_pixels_per_unit()` of the
class :class:`~panda3d.core.DynamicTextFont`, e.g.:

.. only:: python

   .. code-block:: python

      font.setPixelsPerUnit(60)

.. only:: cpp

   .. code-block:: cpp

      PT(TextFont) font=FontPool::load_font("arial.ttf");
      PT(DynamicTextFont) dfont = DCAST(DynamicTextFont, font);
      dfont->set_pixels_per_unit(60);

Notice that this method is only available with DynamicTextFont objects. These
are the objects created when loading FreeType-compatible fonts such as TTF
files. In these cases the font file is loaded into memory and characters are
rasterized and mapped onto a polygon as the need arises. Changes to the font
object (such as resetting the pixels per unit value) will regenerate the
textures for all characters that have been generated so far, a small price to
pay for the flexibility of a dynamic font. When a font is loaded from an egg
file instead, the returned object is a :class:`~panda3d.core.StaticTextFont`
that provides a much restricted functionality. Effectively these kind of egg
files are "frozen" fonts: their characters have been permanently rendered into a
texture and cannot be easily changed from inside your application.

Panda3D defaults to 40 pixels per unit and this is sufficient for small to
normal sized on screen text. Should you wish to use higher values, you might
need to increase the page size, normally set to 256 pixels in height and width.
To do so you can use the method
:meth:`set_page_size(width, height) <.DynamicTextFont.set_page_size>`, e.g.:

.. only:: python

   .. code-block:: python

      font.setPageSize(512, 512)

.. only:: cpp

   .. code-block:: cpp

      dfont->set_page_size(512, 512);

Beware however that this increases the size of the texture for each character,
hence increasing memory consumption. I.e. all else being equal a page size of
256x256 (the default) will use a quarter of the memory used with a page size of
512x512 and 1/16th of the memory used by a page size of 1024x1024.

Alternative Render Modes
~~~~~~~~~~~~~~~~~~~~~~~~

Fonts loaded through the FreeType library (resulting in a DynamicTextFont
object) are normally rasterized into textures and mapped onto polygons, due to
the default Render Mode being set to ``RM_texture``. The render mode however can
be changed using the method :meth:`~.DynamicTextFont.set_render_mode()`, to
allow for radically different generated characters. For example, the following
statement ensures that generated characters will be fully three-dimensional,
thick, polygonal characters.

.. only:: python

   .. code-block:: python

      font.setRenderMode(TextFont.RMSolid)

.. only:: cpp

   .. code-block:: cpp

      dfont->set_render_mode(TexFont::RM_solid);

.. only:: python

   Other available modes are TextFont.RMWireframe, generating characters as
   polylines, TextFont.RMPolygon, generating characters as flat polygonal
   objects, and TextFont.RMExtruded, generating characters as extruded polygonal
   surfaces.

.. only:: cpp

   Other available modes are TextFont::RM_wireframe, generating characters as
   polylines, TextFont::RM_polygon, generating characters as flat polygonal
   objects, and TextFont::RM_extruded, generating characters as extruded
   polygonal surfaces.

.. warning::

   At the time of the writing and with very few exceptions, nearly all tested
   TTF fonts available on Vista were compatible with the RMTexture render mode.
   However, many of the same fonts would crash the application if set to a
   different render mode such as TextFont.RMSolid. (Bug Report
   `#383251 <https://bugs.launchpad.net/panda3d/+bug/383251>`__)
