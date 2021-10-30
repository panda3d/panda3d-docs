.. _sound:

Sound
=====

Sound System Options
--------------------

To play audio in your game, Panda3D can offer you the following three choices
of audio libraries:

-  `OpenAL <https://www.openal.org/>`__ is a well-known and popular open-source
   audio library. Panda3D uses the `OpenAL Soft <https://openal-soft.org/>`__
   implementation.
-  `FMOD <https://www.fmod.com/>`__ is a powerful proprietary cross-platform
   sound engine that supports various types of sound files - MP3, WAV, AIFF,
   MIDI, MOD, WMA, and OGG Vorbis. However, its license restricts you from
   using it for commercial purposes unless you actually purchase a special
   license. Non-commercial use of FMOD is free of charge. (For more
   information on this, visit the
   `FMOD Licenses <https://www.fmod.com/index.php/sales>`__ page.)
-  `Miles <http://www.radgametools.com/miles.htm>`__ is a sound system that is
   not included in the downloadable binaries of Panda3D. In order to use this
   you will need to purchase Miles and compile Panda3D from scratch using the
   ppremake system

If these choices are not enough for you, then you can try other sound
libraries.

Setting the Sound System
------------------------

To configure Panda3D to use a specific sound system, you will need to change
your :ref:`Config.prc <configuring-panda3d>` configuration. You should look up
the variable ``audio-library-name`` and change the value to one of
``p3openal_audio``, ``p3fmod_audio``, or ``miles_audio``. (The names of the
libraries may differ with the way Panda3D was built.)

Extra Notes
-----------

If you don't want to use one or both of the libraries shipped by default with
the SDK, then you can remove the associated library files after installation
or compile Panda3D from source with the appropriate settings to keep them out
of the build.


.. toctree::
   :maxdepth: 2

   loading-playing-sounds-music
   manipulating-sounds
   audio-managers
   dsp-effects
   3d-audio
   multi-channel
