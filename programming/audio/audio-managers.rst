.. _audio-managers:

Audio Managers
==============

Sound effects and music in code are implemented as :class:`.AudioManager`
objects. You can access these audio managers with the following code:

.. code-block:: python

   sfxMgr = base.sfxManagerList[0]
   musicMgr = base.musicManager

In :py:obj:`~builtins.base`, :py:obj:`sfxManagerList
<direct.showbase.ShowBase.ShowBase.sfxManagerList>` is a list of
:class:`.AudioManager` objects intended to be used for sound effects, and
:py:obj:`musicManager <direct.showbase.ShowBase.ShowBase.musicManager>` is an
:class:`.AudioManager` object intended to be used for music.

Each :class:`.AudioManager` object can have 16 different sounds cached at a
given time. This value is actually set as the ``audio-cache-limit`` in the panda
config.prc (found in your install directory) and can be changed.

.. only:: python

   By default, :py:obj:`base.musicManager
   <direct.showbase.ShowBase.ShowBase.musicManager>` has a limit of 1 concurrent
   sound, however. This limit can be explicitly increased using the following
   code:

   .. code-block:: python

      # Allow playing two music files at the same time.
      base.musicManager.setConcurrentSoundLimit(2)

   There are times where either sound effects, music, or both should be disabled
   and later enabled. These commands affect entire categories of sounds. Passing
   True or False in the last 2 functions will disable or enable the respective
   groups.

   .. code-block:: python

      base.disableAllAudio()
      base.enableAllAudio()
      base.enableMusic(True)
      base.enableSoundEffects(True)

Positional audio is implemented through a wrapper of these objects and is
covered in the next section, :ref:`3d-audio`.
