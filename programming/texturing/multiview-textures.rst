.. _multiview-textures:

Multiview Textures
==================

Any Panda texture, including a cube map or video texture, can also be loaded as
a multiview texture. This means that there are multiple different images, or
views, stored within the texture object.

The most common use for a multiview texture is to implement a stereo texture, or
a texture with two views: one for each of the left and the right eyes. For
instance, you would do this to project a 3-D movie onto a screen in your virtual
space.

In its default configuration, whenever Panda renders to a 3-D stereo window (see
:ref:`stereo-display-regions`), any multiview textures are automatically treated
as stereo textures. View 0 is presented to the left eye, and view 1 is presented
to the right eye. Additional views beyond view 1 are not used.

A multiview texture is loaded as a series of independent texture images (similar
to the way a cube map or 3-D texture is loaded). Each image is numbered, and the
first image (or left image) is image number 0. The right image is image number
1. If there are additional views, they are numbered consecutively from there.
All of the images in the series must have the same filename, except for the
image sequence number.

To load a multiview texture, use:

.. only:: python

   .. code-block:: python

      tex = loader.loadTexture('filename_#.png', multiview=True)

.. only:: cpp

   .. code-block:: cpp

      LoaderOptions options;
      options.set_texture_flags(LoaderOptions::TF_multiview);
      PT(Texture) tex = TexturePool::load_texture("filename_#.png", 0, false, options);

where the hash mark in the filename is replaced with the digit (or digits) that
correspond to the image sequence number. For instance, the above example would
load image files named filename_0.png and filename_1.png.

You can also load cube maps in the same way. A cube map consists of six
independently loaded texture images numbered 0 through 5, which define the six
faces of a cube. With a stereo cube map, there are twelve texture images
numbered 0 through 11. The first six images define the six faces of the cube in
the left view, and the next six images define the six faces of the cube in the
right view.

.. only:: python

   .. code-block:: python

      tex = loader.loadCubeMap('cubemap_##.png', multiview=True)

.. only:: cpp

   .. code-block:: cpp

      LoaderOptions options;
      options.set_texture_flags(LoaderOptions::TF_multiview);
      PT(Texture) tex = TexturePool::load_texture("cubemap_##.png", 0, false, options);

Finally, 3-D textures work this way as well. (Note that here by 3-D texture we
mean one that contains height, width, and depth; this is not to be confused with
a stereo texture, which contains a left and a right view. It is possible to have
a stereo 3-D texture, which contains a left and a right view that both contain
height, width, and depth.) When loading a multiview 3-D texture, you must
specify the number of views explicitly, because Panda won't be able to figure
that out based on the number of image files alone.

.. only:: python

   .. code-block:: python

      tex = loader.load3DTexture('tex3d_#.png', multiview=True, numViews=2)

.. only:: cpp

   .. code-block:: cpp

      LoaderOptions options;
      options.set_texture_flags(LoaderOptions::TF_multiview);
      options.set_texture_num_views(2);
      PT(Texture) tex = TexturePool::load_3d_texture("tex3d_#.png", 0, false, options);
