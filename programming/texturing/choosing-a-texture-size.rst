.. _choosing-a-texture-size:

Choosing a Texture Size
=======================

Standard Texture Sizes
----------------------

Most graphics hardware requires that your texture images always be a size that
is a power of two in each dimension. That means you can use any of the following
choices for a texture size: 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048,
or so on (but unless you have a really high-end card, you'll probably need to
stop there).

The textures don't usually have to be square: they don't have to have the same
size in both dimensions. But each dimension does usually have to be a power of
two. So 64 × 128 is all right, for instance, or 512 × 32, or 256 × 256. But you
can't make a texture image that is 200 × 200 pixels, since 200 isn't a power of
two.

By default, Panda3D will automatically rescale any texture image down to the
nearest smaller power of two when you read it from disk, so you usually don't
have to think about this--but your application will load faster if you scale
your textures properly in the first place.

If you would like Panda3D to rescale your images up to the next larger power of
two instead of down to the next smaller power of two, use:

.. code-block:: text

   textures-power-2 up

in your config file. The default is:

.. code-block:: text

   textures-power-2 down

As of version 1.8.0, another mode was added which adds black borders as needed
to frame the texture within a larger power-two texture. To enable this mode
instead, use:

.. code-block:: text

   textures-power-2 pad

in your config file.

It will then be up to your code to apply ``texture.getTexScale()`` where needed.
This mode does, of course, prevent using repeated textures.

Although you usually shouldn't use non power-of-two textures, for some things
like GUI graphics it is not very uncommon to have them like that and let the
game engine scale or pad them automatically.

Note that the size you choose for the texture image has nothing to do with the
size or shape of the texture image onscreen--that's controlled by the size and
shape of the polygon you apply it to. Making a texture image larger won't make
it appear larger onscreen, but it will tend to make it crisper and more
detailed. Similarly, making a texture smaller will tend to make it fuzzier.

Padded Textures
---------------

Sometimes, you need to load data into a texture every frame. The most common
example is when you're playing a movie. Let's say, for example, that the movie
is encoded at 640x480 at 30fps. Neither of those dimensions is a power-of-two.
It would theoretically be possible for Panda3D to rescale the image to 512x512,
but it would have to do it 30 times per second, which is too expensive to be
practical.

Instead, panda pads the data. Panda creates a 1024x512 texture, which is the
smallest power-of-two size that can hold a 640x480 movie. It sticks the 640x480
movie into the lower-left corner of the texture. Then, it adds a black border to
the right edge and top edge of the movie, padding it out to 1024x512.

From that point forward, it's just a texture with a movie in the lower-left
corner, and black bars on the upper and right sides. However, if you use UV
coordinates carefully, you can cause just the movie to be displayed. To do this,
you need to know how big those black bars are:

.. code-block:: python

   padx = texture.getPadXSize()
   pady = texture.getPadYSize()

Panda3D only uses padded textures in a few very special cases: 1. When playing
a non-power-of-two movie. 2. When using render-to-texture, and a
non-power-of-two buffer.

Nonstandard Texture Sizes
-------------------------

Some newer graphics cards can render textures that are not a power of two.
This is generally not very useful for loading art from disk: after all, game art
is usually created in power-of-two sizes no matter what. However, it is useful
to avoid wasteful movie padding of the kind described above. If you have one of
these cards and you want to enable the use of non-power-of-two textures, you can
put the following line in your Config.prc:

.. code-block:: text

   textures-power-2 none

You can also attempt to have panda detect your video card's capabilities
automatically, using this command:

.. code-block:: text

   textures-auto-power-2 #t

If this variable is true, then panda will wait until you open a window, and then
ask the window's driver if the driver supports non-power-of-two textures. If so,
then the config variable ``textures-power-2`` will automatically be adjusted. In
this way, you can configure Panda3D to use non-power-of-two textures if they are
available.

.. caution::

   There is a potential pitfall when using ``textures-auto-power-2``. If you
   open a window that supports non-power-of-two textures, panda will switch into
   ``textures-power-2 none`` mode. If you then open a second window using a
   different video card which doesn't support non-power-of-two textures, then
   panda will have no choice but to print an error message.

.. note::

   Note that some cards appear to be able to render non-power-of-two textures,
   but the driver is really just scaling the textures at load time. With cards
   like these, you're better off letting Panda do the scaling, or dynamic
   textures may render very slowly.
