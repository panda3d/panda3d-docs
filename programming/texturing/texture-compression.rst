.. _texture-compression:

Texture Compression
===================

You may be familiar with image file formats like JPEG, which can compress image
data dramatically and make image files much smaller than they would be
otherwise, in return for sacrificing a tiny bit of the original image quality.

JPEG compression only applies to the image size on disk, however. Once you
load a texture image into memory, whether it came from a JPEG, PNG, or TGA file,
it always takes up the same amount of texture memory on your graphics card
(based on the size of the texture).

There is a different option, however, for compressing texture images in-memory.
Most modern graphics cards can use a handful of run-time compression algorithms
to render directly from a texture that has been compressed in-memory. This is
called block compression. It's not really very much like JPEG compression
internally, but you can think of it in the same way. It does have some things in
common: it reduces the size of the image dramatically (4 times or even 8 times
smaller), and it sacrifices a tiny bit of image quality.

Most block compression methods (such as DXT and 3Dc) operate on blocks of 4 by 4
pixels. Therefore, it is recommended that your texture size is a multiple of 4
in both dimensions, or extra padding will have to be applied.

Runtime texture compression
---------------------------

The easiest way to enable compressed texture images is to put the following in
your Config.prc file::

   compressed-textures 1

This will ask your graphics driver to compress each texture as it loads. This
means it takes a tiny bit longer to load each texture, but the resulting texture
will take up much less space in texture memory.

There's one important advantage to compressing the textures at runtime this way:
the graphics driver will be able to compress all the textures using whatever
texture compression algorithm it understands, DXT or otherwise. Not all graphics
cards support all compression algorithms, so using this option allows the driver
to choose the best algorithm it supports. If the graphics driver doesn't support
any compression algorithms at all, it will simply load the textures
uncompressed. Either way, your application will still run and all of your
textures will be visible.

TXO file format
---------------

Panda has a native file format for storing texture images, called TXO (the
abbreviation is for "texture object"). This is similar to BAM files. A TXO file
contains all of the texture image data in a format very similar to Panda's
internal representation, so it loads into memory very quickly.

More importantly, perhaps, TXO files can optionally store pre-compressed
texture images. You can use the command:
``egg2bam -txo -ctex model.egg -o model.bam`` to convert your model to a BAM
file, and all of its textures to TXO files, with the image data pre-compressed
within the TXO file so that it will not need to be compressed at runtime later.
(You may need to specify "pandagl" instead of "pandadx9" as your rendering
engine while you run the egg2bam command--at the time of this writing, there
were issues with using Panda's DirectX driver in an offline mode like this.
However, the resulting TXO files will load on either OpenGL or DirectX at
runtime.)

TXO files have the same drawbacks as BAM files: they are tied to a particular
version of Panda, so you may need to regenerate them when you next upgrade your
Panda version.

A bigger drawback to storing pre-compressed texture images this way is that not
all graphics cards support all kinds of DXT compression, and if you try to load
a TXO file that a graphics card doesn't understand, Panda3D will decompress the
texture on the CPU before uploading it to the graphics card. Thus,
pre-compressing all of your textures may cause a loss of texture quality on
older cards.

Note that decompression is only available if Panda3D has been compiled with
support for the libsquish library; if not, the texture will fail to load
entirely if the driver does not support the requested compression mode.

DDS file format
---------------

In addition to Panda's native TXO file format, there is a fairly standard format
called DDS, which has some of the same properties of TXO. Like TXO, you can
store pre-compressed images in a DDS file. The biggest advantage of the DDS file
format is that there are already several tools available on the internet to
generate DDS files, including GIMP and Photoshop plugins.

Generating your own DDS files has several advantages; chief among them is that
you have complete control over the compression artifacts of your texture and can
result in less loss of quality since slower compression techniques may be used.
However, it has the same issues as storing pre-compressed texture images in TXO
files: there is a possibility some graphics cards don't support the texture
compression you have used, in which case the texture will have to be
decompressed before it can be loaded.

Texture cache
-------------

There is a compromise between dynamic compression and pre-compressed textures:
you can ask Panda to compress textures on the fly, and then save the resulting
compressed image to a TXO file on disk. The next time you load that particular
texture, it will load quickly from its TXO file. Since the TXO file was
generated by the user's graphics driver, it will presumably use a supported
compression algorithm.

To enable this feature, simply insert the following lines in your Config.prc
file::

   compressed-textures 1
   model-cache-dir /c/temp/panda-cache
   model-cache-compressed-textures 1

Where ``model-cache-dir`` specifies any folder on the disk (it will be created
if it doesn't already exist). Note that the ``model-cache-dir`` may already be
specified; the default distribution of Panda specifies a model-cache to speed
up loading bam files.
