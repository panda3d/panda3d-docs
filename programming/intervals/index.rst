.. _intervals:

Intervals
=========

Panda3D's Interval system is a sophisticated mechanism for playback of scripted
actions. With the use of Intervals, you can build up a complex interplay of
animations, sound effects, or any other actions, and play the script on demand.

The core of system is the :py:class:`~direct.interval.Interval.Interval` class.
There are several different kinds of Intervals, which will be discussed in
detail in the following pages, but all of them have in common the following
property: each Interval represents an action (or a series of actions) that
occurs over a specific, finite interval of time (hence the name).

The real power of the Interval system comes from :ref:`sequences-and-parallels`,
which are a special kind of Interval that can contain nested Intervals of any
kind (including additional Sequences and/or Parallels). By using these grouping
Intervals, you can easily assemble complex scripts from the basic atoms.

Using Intervals
---------------

In any Panda3D module that uses Intervals, you should first import the interval
module:

.. code-block:: python

   from direct.interval.IntervalGlobal import *

There are a handful of methods that all Intervals have in common.

To start an Interval playing, use one of the following:

.. code-block:: python

   interval.start()
   interval.start(startT, endT, playRate)
   interval.loop()
   interval.loop(startT, endT, playRate)

The three parameters are optional. The startTime and endTime parameters define
the subset of the interval to play; these should be given as times in seconds,
measured from the start of the interval. The playRate, if specified, allows you
play the interval slower or faster than real time; the default is 1.0, to play
at real time.

Normally, an Interval will play to the end and stop by itself, but you can stop
a playing Interval prematurely:

.. code-block:: python

   interval.finish()

This will stop the interval and move its state to its final state, as if it had
played to the end. This is a very important point, and it allows you to define
critical cleanup actions within the interval itself, which are guaranteed to
have been performed by the time the interval is finished.

You can also temporarily pause and resume an interval:

.. code-block:: python

   interval.pause()
   interval.resume()

If you pause an interval and never resume or finish it, the remaining actions in
the interval will not be performed.

And you can jump around in time within an interval:

.. code-block:: python

   interval.setT(time)

This causes the interval to move to the given time, in seconds since the
beginning of the interval. The interval will perform all of the actions between
its current time and the new time; there is no way to skip in time without
performing the intervening actions.

It is legal to set the time to an earlier time; the interval will do its best to
reset its state to the previous state. In some cases this may not be possible
(particularly if a :ref:`Function Interval <function-intervals>` is involved).

.. code-block:: python

   interval.setPlayRate(playRate)

With this you can change the play rate of the interval when it is already
running.

Finally, there are a handful of handy query methods:

.. code-block:: python

   interval.getDuration()

Returns the length of the interval in seconds.

.. code-block:: python

   interval.getT()

Returns the current elapsed time within the interval, since the beginning of the
interval.

.. code-block:: python

   interval.isPlaying()

Returns true if the interval is currently playing, or false if it was not
started, has already finished, or has been explicitly paused or finished.

.. code-block:: python

   interval.isStopped()

Returns true if the interval has not been started, has already played to its
completion, or has been explicitly stopped via finish(). This is not quite the
same this as ``(not interval.isPlaying())``, since it does not return true for a
paused interval.

.. toctree::
   :maxdepth: 2

   lerp-intervals
   function-intervals
   actor-intervals
   sound-intervals
   motion-path-and-particle-intervals
   sequences-and-parallels
   position-rotation-and-scale-intervals
   projectile-intervals
