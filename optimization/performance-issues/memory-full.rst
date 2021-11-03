.. _memory-full:

Memory Full
===========

A floating-point number takes four bytes. Just one vertex contains (X,Y,Z), and
a normal, and a texture coordinate. An RGBA color takes four bytes, so a
1024x1024 texture is four megabytes. Do the math, and you'll see how fast it all
adds up.

If CPU memory is used excessively, it is possible to use PStats to find out
which Panda3D structures are using the most memory. Click the "System memory"
graph, and then navigate down into the various subcollectors to find out the
cause of the high memory consumption.

Also see the page :ref:`failure-to-garbage-collect` for a possible cause of CPU
memory filling up.
