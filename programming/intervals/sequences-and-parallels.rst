.. _sequences-and-parallels:

Sequences and Parallels
=======================

You will need to have this import statement to use Sequences and Parallels.

.. code-block:: python

   from direct.interval.IntervalGlobal import *

Sequences and Parallels can control when intervals are played. Sequences play
intervals one after the other, effectively a “do in order” command. Parallels
are a “do together,” playing all intervals at the same time. Both have simple
formats, and every kind of interval may be used.

.. code-block:: python

   mySequence = Sequence(myInterval1, ..., myIntervaln, name="Sequence Name")
   myParallel = Parallel(myInterval1, ..., myIntervaln, name="Parallel Name")

To add to sequences or parallels after creating them, use the ``append`` method.

.. code-block:: python

   mySequence.append(myInterval)
   myParallel.append(myInterval)

Sequences and Parallels may also be combined for even greater control. Also,
there is a wait interval that can add a delay to Sequences. While it can be
defined beforehand, it does not have to be.

.. code-block:: python

   delay = Wait(2.5)
   pandaWalkSeq =
       Sequence(
           Parallel(pandaWalk, pandaWalkAnim),
           delay,
           Parallel(pandaWalkBack, pandaWalkAnim),
           Wait(1.0),
           Func(myFunction, arg1)
       )

In the above example, a wait interval is generated. After that, a Sequence is
made that uses a Parallel, the defined wait interval, another Parallel, and a
wait interval, and a call to the function function myFunction is generated in
the Sequence. Such Sequences can get very long very quick, so it may be prudent
to define the internal Parallels and Sequences before creating the master
Sequence.

One can do very powerful things with Sequences and Parallels. Examine this
Sequence:

.. code-block:: python

   s = OnscreenImage('wav_is_playing.png')
   s.reparentTo(aspect2d)
   s.setTransparency(1)
   fadeIn = s.colorScaleInterval(3, (1, 1, 1, 1), (1, 1, 1, 0))
   fadeOut = s.colorScaleInterval(3, (1, 1, 1, 0))
   sound = loader.loadSfx('sound.wav')

   Sequence(
       fadeIn,
       SoundInterval(sound),
       fadeOut
   ).start()

   base.run()

It fades an image in, plays a sound, waits till sounds stops and then fades the
image out. Doing this conventional way would require a class to store state, a
task to check timings, and produce messy code.
