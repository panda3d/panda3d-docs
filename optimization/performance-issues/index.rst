.. _common-performance-issues:

Common Performance Issues
=========================

Here is a list of things that can go wrong, roughly in order from most likely
to least likely. Each of these has a section to explain it in greater detail.

   :ref:`too-many-meshes`. A well-made typical 3D model contains one mesh. Huge
   3D models, such as the model of an entire dungeon or an entire island, might
   contain multiple meshes. 3D models created by inexperienced modelers can
   contain dozens of meshes. Most video cards can render about 300 meshes total
   for the entire scene. Panda3D contains tools to coalesce multiple meshes into
   one, but they aren't fully automatic.

   :ref:`too-many-state-changes`. The state of an object is the sum of its
   color, material, light, fog, and other attributes. It can be expensive, for a
   variety of reasons, to have too many different states in your scene. It is
   better if many objects share the same state.

   :ref:`too-many-text-updates`. If you have lots of text in your game that
   gets updated every frame, it will often take a long time for Panda to keep
   regenerating the text. You need to minimize the amount of text to
   regenerate per frame.

   :ref:`Performance Issue: Too Many Pixel Shader Instructions <too-many-shader-instructions>`.
   If you are using per-pixel lighting, or hand-written shaders, you need to
   be conscious of how long your shaders are. Adding one pixel shader
   instruction can slow the video card a lot. Adding a texture lookup can slow
   it even more. Professional pixel shaders contain 20-30 assembly-level
   instructions.

   :ref:`excessive-fill`. The fill rate of the video card is number of pixels
   it can render per second. Objects that are occluded (behind other objects)
   still consume fill rate. The total fill-consumption of
   the scene is the total screen real estate of all objects, including the
   occluded ones. Particles, in particular, can consume fill-rate like crazy,
   especially if the camera gets close to the particles.

   :ref:`memory-full`. A floating-point number takes four bytes. Just one
   vertex contains (X,Y,Z), and a normal, and a texture coordinate. An RGBA
   color takes four bytes, so a 1024x1024 texture is four megabytes. Do the
   math, and you'll see how fast it all adds up.

   :ref:`python-calculation`. Python is a very slow language. Most Panda3D
   programs only run a few thousand lines of python per frame, since all the
   real work is done in C++. Sometimes, though, you need to do some complex
   calculation, and Panda3D just doesn't contain any C++ code to do it for you.
   In that case, trying to write the calculation in python can cause problems.
   You may need a C++ plug-in.

   :ref:`failure-to-garbage-collect`. It's easy to get used to the fact that
   Python's garbage collector can automatically clean up Panda3D data
   structures. Unfortunately, there are a few structures that can't be cleaned
   up automatically. You need to know what they are, or you may end up with a
   leak.

   :ref:`collision-system-misuse`. The collision system can detect most types of
   collisions very rapidly. However, it is possible to construct situations that
   the collision detection system just can't handle. Know what it's good at, and
   what it's not.

   :ref:`motherboard-integrated-video`. Motherboard video is very misleading.
   The chips have names like "Radeon" and "GeForce" that we have come to
   associate with speed, but these chips are an order of magnitude slower than
   real video cards. Programming for these chips requires special consideration.

   :ref:`too-many-polygons`. This is at the bottom of the likelihood list, but
   it can still happen. Usually this happens in combination with something else,
   e.g. if you have a large vertex shader, performance can be drastically
   reduced for each vertex you add.

   :ref:`miscellaneous`. There are a lot of small things that have a
   surprisingly large impact on performance. For instance, printing messages on
   the console can be very slow in Windows. This section lists a number of
   miscellaneous things that can bog you down.

.. toctree::
   :hidden:

   too-many-meshes
   too-many-state-changes
   too-many-text-updates
   too-many-shader-instructions
   excessive-fill
   memory-full
   python-calculation
   failure-to-garbage-collect
   collision-system-misuse
   motherboard-integrated-video
   too-many-polygons
   miscellaneous
