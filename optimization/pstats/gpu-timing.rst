.. _pstats-gpu-timing:

GPU Timing
==========

OpenGL is asynchronous, which means that function calls aren't guaranteed to
execute right away. This can make performance analysis of OpenGL operations
difficult, as the graphs may not accurately reflect the actual time that the GPU
spends doing a certain operation. However, if you wish to more accurately track
down rendering bottlenecks, you may set the following configuration variable:

.. code-block:: text

   pstats-gpu-timing 1

This will enable a new set of graphs that use timer queries to measure how much
time each task is actually taking on the GPU. The GPU process is represented in
PStats as though it were a separate thread.

.. note::

   Please make sure you are at least using Panda3D 1.10.12 when trying to use
   this feature. Older versions had a bug that made GPU timing not work
   correctly with some graphics cards. Panda3D 1.11.0 has even more improvements
   for this feature, so you will get the best results by updating to the very
   latest version.

If your card does not support it or does not give reliable timer query
information, a crude way of working around this and getting more accurate timing
breakdown, you can set this:

.. code-block:: text

   gl-finish 1

Setting this option forces Panda to call glFinish() after every major graphics
operation, which blocks until all graphics commands sent to the graphics
processor have finished executing. This is likely to slow down rendering
performance substantially, but it will make PStats graphs more accurately
reflect where the graphics bottlenecks are.
