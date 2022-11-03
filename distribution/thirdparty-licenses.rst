.. _thirdparty-licenses:

Third-party dependencies and license info
=========================================

License Info
------------

While Panda3D itself uses the Modified BSD license, it brings together many
third-party libraries released under different licenses. This page provides
information on the different libraries and their licenses. Panda3D builds with
some of these libraries by default, however, some of them are linked only into
plug-ins that can be easily removed from the distribution.

Disclaimer
----------

Panda3D takes no responsibility for any act committed using the information
presented here. For legal advice, it is recommended to consult a lawyer.

Building Panda3D
----------------

When building Panda3D yourself on your computer you'll notice that
makepanda.py looks up if you have some libraries installed. On operating
systems with a packaging system, like most GNU/Linux distros have, you'll most
likely find all dependencies as packages in the official repositories.
Otherwise you have to take care of the libraries yourself.

Here you have a list of all third party libraries Panda3D must or can be
compiled against. All of them are optional, but some features of Panda3D
depend on certain libraries being available; omitting certain libraries will
omit the corresponding features from Panda3D.

Recommended Libraries
---------------------

Python
~~~~~~

https://www.python.org/

Panda3D is way easier and faster to code with when using Python bindings.

License: `PSF license <https://docs.python.org/license.html>`__

ZLib
~~~~

https://www.zlib.net/

Used for a range of compression and decompression tasks, particularly .pz files.

License: `zlib license <https://www.zlib.net/zlib_license.html>`__

libjpeg
~~~~~~~

https://www.ijg.org/

JPEG library. Required to read and save JPEG files. As of Panda 1.10, Panda3D
will fall back to stb_image for loading .jpg files when building without
libjpeg, but this may not support all JPEG features.

License: libjpeg license

libpng
~~~~~~

http://www.libpng.org

Portable Network Graphics library. Required to read and save PNG files. As of
Panda 1.10, Panda will fall back to stb_image for loading .png files when
building without libpng, but this may not support all PNG features.

License: `libpng
license <http://www.libpng.org/pub/png/src/libpng-LICENSE.txt>`__

OpenSSL
~~~~~~~

https://www.openssl.org/

Provides some networking and encryption support. Required for HTTPClient, and
for pencrypt/pdecrypt and related functionality, as well as SSL networking.
License: `OpenSSL license <https://www.openssl.org/source/license.html>`__

License note:

Must include this acknowledgement with distribution:

.. code-block:: text

   This product includes software written by Tim Hudson (tjh@cryptsoft.com)

`Some governments <http://www.cryptolaw.org/>`__ place restrictions on
cryptography.

libvorbis
~~~~~~~~~

https://xiph.org/vorbis/

Used to load .ogg files encoded with Vorbis encoding.

License: `BSD <https://raw.githubusercontent.com/xiph/vorbis/master/COPYING>`__

Freetype
~~~~~~~~

http://freetype.sourceforge.net

Font library. Required to use dynamic fonts such as TTF files. Even without this
library, however, Panda can use static fonts stored in egg files, as generated
by the tool egg-mkfont (however, the tool egg-mkfont itself requires Freetype).

License: `FreeType License <http://freetype.sourceforge.net/FTL.TXT>`__ or
`GPL <http://freetype.sourceforge.net/GPL.TXT>`__

License note: To distribute under a proprietary license, FreeType License must
be chosen instead of GPLv2. Use of FreeType must be acknowledged in product
documentation.

GTK2
~~~~

https://www.gtk.org/

The Gimp ToolKit is used by only by the PStats server on non-Windows platforms.
This is a separate utility that can easily be deleted and is only used when
profiling applications.

License: `GNU LGPL <https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html>`__

OpenAL Soft
~~~~~~~~~~~

https://openal-soft.org

The Open Audio Library is a free alternative to FMOD and supports nearly the
same features, including 3D surround sound. We ship the OpenAL Soft
implementation by default on Windows. It can be easily removed from the
distribution.

License: LGPL

Cg Toolkit
~~~~~~~~~~

https://developer.nvidia.com/cg-toolkit

Nvidia's Cg Toolkit is required for Panda's Cg support. At the moment, it cannot
be removed without recompiling Panda3D from source code.

License:
`Proprietary <https://developer.download.nvidia.com/cg/Cg_2.2/license.pdf>`__

License note: Required to use the Panda3D Shader Generator, which utilizes
Nvidia Cg.

Eigen
~~~~~

http://eigen.tuxfamily.org/

Optimized linear algebra library. Optional, but improves performance of matrix
operations significantly.

License: `MPL2 <https://www.mozilla.org/en-US/MPL/2.0/>`__

libsquish
~~~~~~~~~

https://code.google.com/archive/p/libsquish/

Libsquish gives DXT support. This improves Panda's support for pre-compressed
texture images such as dds files, and it allows Panda to streamline compression
of textures images at load time. However, even without this library, Panda can
still compress and use compressed textures, by relying on the interfaces built
into your graphics driver.

License: `MIT License <https://opensource.org/licenses/mit-license.php>`__

libtiff
~~~~~~~

http://libtiff.org/

Tiff image format support.

License: `libtiff license <https://spdx.org/licenses/libtiff.html>`__

OpenEXR
~~~~~~~

https://www.openexr.com/

OpenEXR image format support. New in 1.10.

License: `Modified BSD license <https://www.openexr.com/license.html>`__

DirectX (Windows only)
~~~~~~~~~~~~~~~~~~~~~~

http://msdn.microsoft.com/en-us/directx/default.aspx

Windows DirectX libraries.

License: Proprietary

X libraries (Linux/FreeBSD only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

https://www.x.org/wiki/

X libraries: X11 (display system), Xrandr (support for changing resolution),
Xxf86dga (provides relative mouse mode), Xcursor (provides custom cursor image
support).

License: `MIT License <https://opensource.org/licenses/mit-license.php>`__

Optional
--------

Assimp
~~~~~~

http://www.assimp.org/

As of Panda3D 1.10.0, Panda3D can make use of the Open Asset Importer library
to read in additional 3D file formats (see :ref:`supported-model-formats`).
A list of file formats supported by Assimp can be found
`here <https://github.com/assimp/assimp#supported-file-formats>`__.

License: BSD license

Opus
~~~~

https://opus-codec.org

As of Panda3D 1.10.0, Panda3D can make use of the libopusfile library to read
.opus audio files. This is a higher-quality alternative to lossy formats such
as .ogg and .mp3 that is not restricted by patents.

License: `3-clause BSD <https://github.com/xiph/opusfile/blob/master/COPYING>`__

Patent note: Must agree not to litigate against other Opus users.

FFMPEG
~~~~~~

http://ffmpeg.org

Library for video and audio. Required to load and play video textures. As of
Panda3D 1.9.0, libp3ffmpeg.dll is an optional module that can be easily
removed, and is no longer required for .ogg and .wav files.

License: `LGPL <http://www.ffmpeg.org/legal.html>`__

License note: Must link dynamically.

Patent note: using MP3 files and other formats may require you to pay royalty
fees. Please use .ogg or .opus instead.

FMOD Ex
~~~~~~~

https://www.fmod.com/

FMOD Ex is a proprietary audio library that supports various effects and
surround sound. You must have one of FMOD or OpenAL to build support for
Panda's sound interfaces. (However, you can use external sound libraries such
as pygame, even without these two.)

License: `Proprietary <https://www.fmod.com/index.php/sales>`__

License note: Non-commercial distribution costs nothing. Commercial
distribution costs between US$100 and US$6000 depending on FMOD licensing
option.

Bullet Physics
~~~~~~~~~~~~~~

https://pybullet.org

Physics Library.

License: `zlib license <http://www.zlib.net/zlib_license.html>`__

Open Dynamics Engine (ODE)
~~~~~~~~~~~~~~~~~~~~~~~~~~

https://www.ode.org

One of the most versatile, free physics engines.

License: `LGPL or Modified BSD License <https://www.ode.org/index.html#3.>`__

OpenGL ES
~~~~~~~~~

https://www.khronos.org/opengles/

OpenGL for embedded systems:
GLES (https://www.khronos.org/registry/OpenGL/index_es.php),
EGL (https://www.khronos.org/registry/EGL/) libraries.

3ds Max SDK
~~~~~~~~~~~

https://www.autodesk.com/products/3ds-max/overview

Used to create exporters for Autodesk 3ds Max.

License: Proprietary.

Maya SDK
~~~~~~~~

https://www.autodesk.com/products/maya/overview

The necessary libraries are part of the Maya installation. From Maya 2016.5
onward, the headers are also part of the Maya installation; before, they were
provided separately as part of a "devkit".

Used to create exporters for Maya.

License: Proprietary.

speedtree
~~~~~~~~~

https://store.speedtree.com/

Library for rendering trees.

License: Proprietary.

libRocket
~~~~~~~~~

https://github.com/libRocket/libRocket

C++ user interface middleware package based on the HTML and CSS standards.
Panda3D's libRocket bindings are deprecated.

License: `MIT License <https://opensource.org/licenses/mit-license.php>`__

OpenCV
~~~~~~

https://opencv.org/

An alternate library that provides support for video textures and webcam,
similar to FFMPEG. This is only really useful on macOS, where this is the only
way to get support for webcam input.

License: BSD license

FCollada
~~~~~~~~

https://www.khronos.org/collada/wiki/FCollada

FCollada is an open-source C++ library which offers support for COLLADA
interoperability. It is used by the dae2egg utility, which converts COLLADA
files into Egg files. See :ref:`converting-to-egg`.

The FCollada library is discontinued and no longer being maintained. Support
will likely be removed in a future version of Panda3D.

License: `MIT License <https://opensource.org/licenses/mit-license.php>`__

FFTW2
~~~~~

http://www.fftw.org

Fast Fourier Transforms library for lossy animation compression in bam files.
Compressed animation files may be as small as 10% of the uncompressed animation,
but this is only an on-disk and/or download savings.

Use of fftw in Panda is deprecated. We do not recommend using it in new projects
and we recommend converting existing compressed animations to lossless format.

License: `GPL2 or Proprietary <http://www.fftw.org/fftw2_doc/fftw_8.html>`__

License note: To distribute under a proprietary license, GPL must not be used,
and FFTW proprietary license must be purchased.

ARToolKit
~~~~~~~~~

http://www.hitl.washington.edu/artoolkit/

A library for augmented reality. It makes possible detecting 3D planes in live
webcam video streams and applying 3D geometry to those, for integrating 3D
graphics with a live video feed.

License: `GPL or
Proprietary <http://www.hitl.washington.edu/artoolkit/license.html>`__

License note: To distribute under a proprietary license, GPL must not be used,
and ARToolKit proprietary license must be purchased.

VRPN
~~~~

https://github.com/vrpn/vrpn/wiki

Virtual-Reality Peripheral Network, for using a range of different types of
trackers and controllers with Panda3D.

License: as of July 22, 2010, future versions of VRPN (versions 7.27 and higher)
are being released under the
`Boost Software License 1.0 <https://github.com/vrpn/vrpn/wiki/License>`__

Prior versions were released into the public domain.

Build Tools (for compilation only)
----------------------------------

Bison
~~~~~

http://www.gnu.org/software/bison/

General-purpose parser generator.

Flex
~~~~

http://flex.sourceforge.net/

The Fast Lexical Analyzer.

Patent Restriction Issues
-------------------------

MP3
~~~

MPEG-1 Audio Layer 3 (MP3), while commonly used and since 2017 with expired
patent and licensing, is recommended against. More modern and better suited
audio encodings have been developed and should be used instead.

MPEG
~~~~

Other MPEG related formats are restricted by
`patents <https://www.mpegla.com/>`__ as well. Finding the
prices of licenses for these formats is not even as easy as it was with MP3.

Recommended Alternatives
~~~~~~~~~~~~~~~~~~~~~~~~

Free alternatives exist and are highly encouraged. These formats include
`Ogg Vorbis <https://xiph.org/vorbis/>`__ (lossy),
`Opus <https://opus-codec.org>`__ (lossy) and
`Ogg FLAC <https://xiph.org/flac/>`__ (lossless) for audio, and
`Ogg Theora <https://www.theora.org/>`__ for video.
