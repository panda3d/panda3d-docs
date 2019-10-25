.. _sound-intervals:

Sound Intervals
===============

See :ref:`loading-and-playing-sounds-and-music` for basic information on how
to load and play sounds.

Sound intervals play sounds from inside an interval. Like actor intervals,
sound intervals have a loop parameter and the ability to be paused. Sound
intervals also have volume and start time parameters.

.. code-block:: python

   mySound = loader.loadSfx("mySound.wav")

   myInterval = SoundInterval(
       mySound,
       loop = 0 or 1,
       duration = myDuration,
       volume = myVolume,
       startTime = myStartTime
   )

The looping provided by the sound interval is not clean. There will be a pause
between loops of roughly a tenth of a second. See :ref:`manipulating-sounds`
for a better way to loop sounds.
