.. _loading-and-playing-sounds-and-music:

Loading and Playing Sounds and Music
====================================

Architecture
------------

The implementation of the sound system in Panda3D allows for a division of
audio into two categories - Sound Effects and Music. This division is only a
convenience for programmers as Panda3D allows these two audio groups to be
treated individually. These differences are explained on the next page.

Basics
------

Loading a Sound
~~~~~~~~~~~~~~~

.. only:: python

   Loading sound is done through the :py:mod:`~direct.showbase.Loader` class by
   supplying the path to the sound file as a parameter for
   :py:meth:`~direct.showbase.Loader.Loader.loadSfx()`. Here's an example:

   .. code-block:: python

      base = ShowBase()
      mySound = base.loader.loadSfx("path/to/sound_file.ogg")

.. only:: cpp

   Loading sound is done through the :class:`AudioManager` class by supplying
   the path to the sound file as a parameter for
   :meth:`~AudioManager.get_sound()`. Here's an example:

   .. code-block:: cpp

      PT(AudioManager) AM = AudioManager::create_AudioManager();
      PT(AudioSound) mySound = AM->get_sound("path/to/sound_file.ogg") ;

These will return an object of the type :class:`.AudioSound`. It is necessary to
put the extension in the sound filename.

Playing/Stopping a Sound
~~~~~~~~~~~~~~~~~~~~~~~~

To play sounds you can do the following:

.. only:: python

   .. code-block:: python

      mySound.play()

.. only:: cpp

   .. code-block:: cpp

      mySound->play();

To stop a sound:

.. only:: python

   .. code-block:: python

      mySound.stop()

.. only:: cpp

   .. code-block:: cpp

      mySound->stop();

Querying Sound Status
~~~~~~~~~~~~~~~~~~~~~

To check the status of a sound, call :meth:`~.AudioSound.status()`:

.. only:: python

   .. code-block:: python

      status = mySound.status()

.. only:: cpp

   .. code-block:: cpp

      mySound->status();

:meth:`~.AudioSound.status()` returns a constant depending on the status of the
sound:

================== ========================================================================
Constant           Status
================== ========================================================================
AudioSound.BAD     The sound is not working properly.
AudioSound.READY   The sound is not currently playing and is ready to be played on command.
AudioSound.PLAYING The sound is currently playing.
================== ========================================================================

.. only:: python

   Example usage of this would be to stop a sound from playing only if it's
   currently playing.

   .. code-block:: python

      if mySound.status() == mySound.PLAYING:
          mySound.stop()

Setting Volume
~~~~~~~~~~~~~~

The volume can be set between 0 and 1 and will linearly scale between these.

.. only:: python

   .. code-block:: python

      mySound.setVolume(0.5)

.. only:: cpp

   .. code-block:: cpp

      mySound->set_volume(0.5);

Panning a Sound
~~~~~~~~~~~~~~~

You can change the balance of a sound. The range is between -1.0 to 1.0. Hard
left is -1.0 and hard right is 1.0.

.. only:: python

   .. code-block:: python

      mySound.setBalance(-0.5)

.. only:: cpp

   .. code-block:: cpp

      mySound->set_balance(-0.5);

.. only:: python

   .. note::

      If Panda3D is running from an interactive prompt, call
      :meth:`~.AudioManager.update()` after you play a sound.

      .. code-block:: python

         base.sfxManagerList[n].update()

      This is because the :meth:`~.AudioManager.update()` command is called
      every frame to reset a sound's channel. In interactive mode, however,
      Panda3D's frame update is suspended and does not run automatically.
