.. _optimization:

Performance Optimization
========================

At some point in the development process, as developers add more and more code
and content to their games, they will notice that the game runs more and more
slowly, with movements starting to appear jittery instead of smooth. At this
stage, it becomes necessary to consider performance optimization.

Even if the game is running fast on the developer's machine, it is usually still
worth it to perform performance analysis before releasing the product publicly.
Some players may be using older hardware that is not as powerful as the
developers' machines, and optimizing the game will maximize the amount of
players that can enjoy the game.

However, be careful not to optimize prematurely. Some developers spend a lot of
time early in the development process optimizing parts of the game that end up
being changed or removed later on in the process anyway. To avoid wasting time
optimizing things unnecessarily, it is mainly useful to perform optimization at
the end of the development cycle, or at the point when testing the game becomes
more difficult due to excessively low framerate.

How Fast Should it Run?
-----------------------

One of the things that makes performance tuning difficult is that you need to
find things that are running slower than they "should" - but how do you know how
fast something "should" run? Experienced game programmers have a gut feel for
what their video card should be capable of, but inexperienced ones often don't
really know what to expect. This makes performance tuning that much harder.

The most commonly used metric for performance by gamers is the *frame rate*,
an average of the number of frames that are rendered in a single second (FPS).
You can enable a display showing this number in Panda3D by enabling the
``show-frame-rate-meter`` setting in the :ref:`Config.prc <configuring-panda3d>`
file. However, developers prefer to talk about the reciprocal of this number,
the *frame time*, usually measured in milliseconds. This is because FPS is not
a linear scale and therefore gives a distorted view: I have seen developers
panic because their frame rate decreased from 1000 FPS to 500 FPS, which seems
like a lot, but it represents only a difference of 1 millisecond, which is about
the same as reducing your frame rate from 30 to 29 FPS.

Usually, games budget between 17 and 33 ms (resulting in 30 and 60 FPS
respectively) on mid-range computer hardware, and add settings to decrease the
quality of the game so that this frame rate can be attained on lower-end
hardware as well. Increasing the frame rate to a number higher than 60 is not
very useful, since most computer monitors refresh at this speed, and rendering
faster than this would be a waste.

In fact, by default, Panda3D limits the frame rate to not exceed the monitor's
refresh rate: this is called video synchronization, and besides ensuring that no
processing power is wasted rendering frames that the monitor will not display,
it also has the benefit of reduring some artifacts that can occur when the
monitor refreshes halfway during a frame. This limit can be disabled to see the
true frame rate by setting the config variable ``sync-video`` to ``false`` in
the :ref:`Config.prc <configuring-panda3d>` file, although note that some
drivers will override this setting.

Finding Performance Issues
--------------------------

It is not a good idea to immediately start optimizing various parts of a slow
application without first understanding what is causing the slowdown.
Performance optimization is not a matter of "every little bit helps". You may
spend a lot of time reducing the run time of a function you think is slow, when
it turns out that it is taking only a few microseconds, and has a negligible
effect on your frame rate. Or, you may optimize a function that does take a long
time, only to find out that it doesn't help at all because the engine had to
wait for some unrelated process to finish anyway.

Some game developers, when they see that their programs are running slow, often
react by trying to reduce the number of polygons. This almost never makes any
difference whatsoever. Back in the mid-90's, reducing polygon counts was a
reasonable strategy to make games faster. That strategy just doesn't work
anymore. The reason for this is that video card manufacturers have been
increasing the polygon limits of their video cards by leaps and bounds. In fact,
they've raised the polygon limit so high that you almost never hit that limit
anymore: you usually hit some other limit first.

That's the key to modern performance tuning: knowing all the limits of the
machine other than the polygon limit, and figuring out which of those
limitations you've run into. In other words, the key to modern performance
tuning is diagnosis. The methodology for performance optimization therefore
looks like this:

1. **Diagnose** the problem: isolate the cause of the slowdown. This can be done
   by disabling parts of the game until you find one that has a significant
   effect on the frame rate, but a more sophisticated method is to use the
   :ref:`PStats <measuring-performance-with-pstats>` performance analysis tool,
   which will tell you exactly how much time the different parts of the game are
   contributing to your frame time.
2. **Optimize** the bottleneck: once you have isolated the part of your
   application that is making it slow, you can take steps to mitigate it.
   The page :ref:`common-performance-issues` contains a list of commonly
   occurring bottlenecks, each with an associated page explaining each issue in
   more detail together with possible solutions.
3. **Repeat** these steps as long as your frame time is exceeding your budget.

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

Table of Contents
-----------------

.. toctree::
   :titlesonly:

   basic-performance-diagnostics
   using-pstats
   performance-issues/index
   rigid-body-combiner

Further Reading
---------------

For more information about performance analysis and optimization in 3D
rendering, a recommended read is the following chapter from the free "GPU Gems"
book:

https://developer.nvidia.com/gpugems/gpugems/part-v-performance-and-practicalities/chapter-28-graphics-pipeline-performance
