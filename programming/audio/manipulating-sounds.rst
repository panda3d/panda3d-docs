.. _manipulating-sounds:

Manipulating Sounds
===================

Looping a Sound
---------------

To cause a sound to loop (i.e., cause it to repeat once it is finished playing)
do the following:

.. only:: python

   .. code-block:: python

      mySound.setLoop(True)
      mySound.play()

.. only:: cpp

   .. code-block:: cpp

      mySound->set_loop(true);
      mySound->play();

To stop a sound from looping pass False in the :meth:`~.AudioSound.set_loop()`
function.

.. only:: python

   .. code-block:: python

      mySound.setLoop(False)

.. only:: cpp

   .. code-block:: cpp

      mySound->set_loop(false);

Sounds can also be looped for a certain number of times:

.. only:: python

   .. code-block:: python

      mySound.setLoopCount(n)

.. only:: cpp

   .. code-block:: cpp

      mySound->set_loop_count(n);

Where 'n' can be any positive integer. 0 will cause a sound to loop forever. 1
will cause a sound to play only once. >1 will cause a sound to loop that many
times.

.. note::

   Setting a sound's loop count to 0 or >1 will automatically set a sound's loop
   flag to true.

Notes on Looping Sounds Seamlessly
----------------------------------

Looping a sound seamlessly should be as simple as loading the sound, then
calling :meth:`~.AudioSound.set_loop()` and :meth:`~.AudioSound.play()`.
However, occasionally Panda users have had difficulty getting sounds to loop
seamlessly. The problems have been traced to three(!) different causes:

#. Some MP3 encoders contain a bug where they add blank space at the end of the
   sound. This causes a skip during looping. Try using a wav instead.
#. Some have tried using Sound Intervals to create a loop. Unfortunately, sound
   intervals depend on Panda's Thread to restart the sound, and if the CPU is
   is busy, there's a skip. This is not a seamless method, in general. Use
   :meth:`~.AudioSound.set_loop()` instead.
#. There is a bug in Miles sound system, which requires a workaround in Panda3D.
   At one time, the workaround was causing problems with FMOD, until we devised
   a new workaround. This bug no longer exists, you can ignore it.

So the easiest way to get a reliable looping sound is to use wav files, and to
use :meth:`~.AudioSound.set_loop()`, not sound intervals. Of course, when it
comes time to ship your game, you can convert your sounds to mp3, but before you
do, test your mp3 encoder to see if it contains the blank-space bug.

Cueing Time
-----------

There are :meth:`~.AudioSound.get_time()`, :meth:`~.AudioSound.set_time()` and
:meth:`~.AudioSound.length()` functions for sounds. These will respectively,
report the current time position, set the current time position and report the
length. All these are in seconds.

.. only:: python

   .. code-block:: python

      mySound.length()

.. only:: cpp

   .. code-block:: cpp

      mySound->length();

will return the length of a sound file in seconds.

.. only:: python

   .. code-block:: python

      mySound.getTime()

.. only:: cpp

   .. code-block:: cpp

      mySound->get_time();

will get the current time the 'playback head' of a sound is at in seconds.

.. only:: python

   .. code-block:: python

      mySound.setTime(n)

.. only:: cpp

   .. code-block:: cpp

      mySound->set_time(n);

will set the 'playhead head' of a sound to n (where is seconds).

.. caution::

   When using the default OpenAL back-end, setting the time will *not* take
   effect immediately.  You will need to call :meth:`~.AudioSound.play()` to
   restart the sound at the configured position.

Changing Playback Speed
-----------------------

To change a sound's playback speed, use:

.. only:: python

   .. code-block:: python

      mySound.setPlayRate(n)

.. only:: cpp

   .. code-block:: cpp

      mySound->set_play_rate(n);

Where ``n`` is any float.

Negative numbers will play a sound backwards. Passing the value 0 will pause the
sound.

You can also get a sound's play rate with:

.. only:: python

   .. code-block:: python

      mySound.getPlayRate()

.. only:: cpp

   .. code-block:: cpp

      mySound->get_play_rate();
