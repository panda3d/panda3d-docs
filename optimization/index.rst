.. _optimization:

Performance Optimization
========================

Modern Performance Tuning Introduction
--------------------------------------

Inexperienced game programmers, when they see that their programs are running
slow, often react by trying to reduce the number of polygons. This almost never
makes any difference whatsoever. Back in the mid-90's, reducing polygon counts
was a reasonable strategy to make games faster. That strategy just doesn't work
anymore. The reason for this is that video card manufacturers have been
increasing the polygon limits of their video cards by leaps and bounds. In fact,
they've raised the polygon limit so high that you almost never hit that limit
anymore: you usually hit some other limit first.

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

-  A team had gone through the effort of creating optimized collision geometry
   for their scenes, but they accidentally forgot to disable the collision check
   against the unoptimized visible geometry. Now, Panda3D was spending a lot of
   time checking collisions against both the optimized and the highly detailed,
   unoptimized collision geometry.

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

Finding Common Performance Issues
---------------------------------

The page :ref:`common-performance-issues` contains a list of commonly occurring
performance issues, each with an associated page explaining each issue in more
detail.

A recommended read about performance tuning is also chapter 28 of the book GPU
Gems:

http://developer.download.nvidia.com/books/HTML/gpugems/gpugems_ch28.html

.. toctree::
   :titlesonly:

   basic-performance-diagnostics
   using-pstats
   performance-issues/index
   rigid-body-combiner
