.. _texture-management:

Texture Management
==================

Different graphics cards provide different amounts of texture memory. If you're
loading a lot of different textures, especially if they're large, you can easily
consume all of your available texture memory. In principle, this shouldn't cause
problems, as long as you don't have all of your textures onscreen at once: both
OpenGL and DirectX are supposed to automatically evict textures from graphics
memory as needed.

In practice, it doesn't always work this cleanly. In some integrated graphics
cards, the "graphics memory" is actually your system memory, so the graphics
driver never needs to evict textures--but if you load too many textures, there
may not be enough memory left for your application. Furthermore, some graphics
drivers have major bugs that manifest as you start to approach the limit of your
graphics memory, causing strange rendering artifacts or even crashes.

For these reasons, it may be useful to limit the amount of graphics memory your
application uses. Panda provides several tools to help with this.

Automatically reducing textures
-------------------------------

You can reduce textures automatically as they are loaded. The easiest way to do
this is to put a line like: ``texture-scale 0.5`` in your Config.prc file. The
above example will scale all textures by a factor of 0.5 in each dimension (for
an overall reduction to 1/4 of the total memory requirement). If there are
certain textures that should not be scaled, for instance GUI textures, you can
exclude them with lines like::

   exclude-texture-scale digits_*.png
   exclude-texture-scale gui*.jpg


Enabling texture compression
----------------------------

Another possibility is to enable and use :ref:`texture-compression`, as
described on the next page. If supported by your graphics card, this will reduce
texture memory requirements dramatically, to 1/4 or 1/8 of the original. There
is some reduction of quality, but not as much as the quality reduction you'd get
from downscaling the textures by the equivalent amount. It is also possible to
enable texture compression in conjunction with texture scaling.

Limiting graphics memory usage overall
--------------------------------------

Finally, it may be prudent to limit the amount of graphics memory that Panda
attempts to use, with a line like::

   graphics-memory-limit 67108864``

The above example imposes a limit of 64MB (64 \* 1024 \* 1024) on the graphics
memory that Panda will attempt to use. This can be a good idea to avoid
allocating runaway textures on integrated graphics cards with no fixed texture
limit, or to work around buggy graphics drivers that crash when you use too
much. Panda will automatically start to unload textures when the specified limit
is exceeded, even if the graphics driver would allow allocating more.

Ideally, it would be great to query the amount of useful graphics memory
provided by the card, and set this as the graphics-memory-limit; unfortunately,
this is impractical for several reasons, including the reasons given above.
Typically, if you wish your application to work on a variety of hardware, you
will need to come up with a handful of default settings and allow the user to
select between them, according to his own knowledge of his hardware
capabilities.

Monitoring memory usage
-----------------------

You can see how much graphics memory you are actually consuming with the
:ref:`PStats <measuring-performance-with-pstats>` tool. Select the "Graphics
memory" option. This graph will show the amount of memory required for active
(onscreen), and inactive (offscreen) textures. It also includes memory required
for vertex and index buffers, though these are typically much smaller than your
texture memory requirements.
