.. _optimization:

Performance Optimization
========================

Modern Performance Tuning Introduction
--------------------------------------

Inexperienced game programmers, when they see that their programs are running
slow, often react by trying to reduce the number of polygons. This almost never
makes any difference whatsoever. Back in the mid-90's, reducing polygon counts
was a reasonable strategy to make games faster. That strategy just doesn't work
any more. The reason for this is that video card manufacturers have been
increasing the polygon limits of their video cards by leaps and bounds. In fact,
they've raised the polygon limit so high that you almost never hit that limit
any more: you usually hit some other limit first.

That's the key to modern performance tuning: knowing all the limits of the
machine other than the polygon limit, and figuring out which of those
limitations you've run into. In other words, the key to modern performance
tuning is diagnosis.

Most Common Problem: Silly Little Bugs
--------------------------------------

When people start performance tuning, they often start with the assumption that
there's something serious wrong with the engine, or the design of the game. In
my experience, however, 90% of the time the problem is that the game contains a
silly (but destructive) bug. Here are some examples of bugs that I have seen:

-  A game had a text readout in the corner of the screen, which got updated
   every frame. But they updated the text by creating a new text object, and
   forgot to remove the old text object. So the corner of the screen contained
   thousands of layers of accumulated messages.

-  A shooter allowed you to fire bullets from your gun. But they forgot to
   remove the bullet after it collided with a wall. As a result, the bullets
   just kept going through the wall, and into outer space. Every bullet you or
   anyone else had ever fired was still flying through space, and the animation
   system was working like crazy to animate tens of thousands of bullets.

-  Think of another example here.

I cannot emphasize this too much: do not redesign your game, until you are sure
that the problem isn't a typo! Imagine how irritated you would be if you wrote
an MMO, and then spent six months re-engineering it to make it faster, only to
discover that the entire performance problem was an off-by-one error in a minor
subroutine.

Catching performance problems that are bugs can be tricky. The place to begin is
using the same performance diagnostics that you would use for any other problem.
However, you will usually find a red flag somewhere: if the performance
monitoring tools say that you're rendering 50,000 models, but you only count 50
models on the screen, you're dealing with a bug. You need to be alert enough not
to discount such red flags. If you see a stat that looks suspicious, don't
assume that the performance monitoring tool is telling you the wrong thing ---
assume that there's a bug in the code.

How Fast Should it Run?
-----------------------

One of the things that makes performance tuning difficult is that you need to
find things that are running slower than they "should" - but how do you know how
fast something "should" run? Experienced game programmers have a gut feel for
what their video card should be capable of, but inexperienced ones often don't
really know what to expect. This makes performance tuning that much harder.

However, you have an advantage. We have a collection of
:ref:`sample programs <samples>` demonstrating Panda3D features. It is easy to
turn on the frame-rate meter to see how fast these samples run. The screenshots
in the manual contain frame-rates, taken with a Radeon x700. That should give
you a baseline. It is even more informative to turn on the frame-rate meter to
see what your video card can deliver.

Video Synchronisation
~~~~~~~~~~~~~~~~~~~~~

Panda3D sometimes caps the framerate to not exceed the monitor's refresh rate:
this is called video synchronization. Panda3D knows that since the monitor can't
refresh faster (the monitor refresh rate is most commonly 60 Hz, but higher end
monitors often range between 120 and 240 Hz), everything above that rate is wasted, 
so Panda3D will not refresh faster than the monitor's refresh rate. To disable this 
and be able to see the 'true' framerate, set the config variable ``sync-video``
to ``#f`` in your :ref:`Config.prc <configuring-panda3d>`.

List of Common Performance Issues
---------------------------------

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

   :ref:`memory-full`. A floating point-number takes four bytes. Just one
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
   :ssociate with speed, but these chips are an order of magnitude slower than
   real video cards. Programming for these chips requires special consideration.

   :ref:`too-many-polygons`. This is at the bottom of the likelihood list, but
   it can still happen. Usually this happens in combination with something else,
   e.g. if you have a large vertex shader, performance can be drastically
   reduced for each vertex you add.

   :ref:`miscellaneous`. There are a lot of small things that have a
   surprisingly large impact on performance. For instance, printing messages on
   the console can be very slow in Windows. This section lists a number of
   miscellaneous things that can bog you down.

A recommended read about performance tuning is also chapter 28 of the book GPU
Gems:

http://developer.download.nvidia.com/books/HTML/gpugems/gpugems_ch28.html

.. toctree::
   :maxdepth: 1

   basic-performance-diagnostics
   using-pstats
   rigid-body-combiner
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
