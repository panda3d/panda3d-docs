.. _sound:

Sound
=====

Sound System Options
--------------------

To play audio in your game, Panda3D can offer you the following three choices
of audio libraries:

-  `OpenAL <http://connect.creativelabs.com/openal/default.aspx>`__ is a
   well-known and popular open-source audio library. Panda3D uses the `OpenAL
   Soft <http://openal-soft.org/>`__ implementation.
-  `FMOD <http://www.fmod.org/>`__ is a powerful proprietary cross-platform
   sound engine that supports various types of sound files - MP3, WAV, AIFF,
   MIDI, MOD, WMA, and OGG Vorbis. However, its license restricts you from
   using it for commercial purposes unless you actually purchase a special
   license. Non-commercial use of FMOD is free of charge. (For more
   information on this, visit the `FMOD
   Licenses <http://www.fmod.org/index.php/sales>`__ page.)
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
the variable ``audio-library-name`` and change
the value to one of ``p3openal_audio``,
``p3fmod_audio``, or
``miles_audio``. (The names of the
libraries may differ with the way Panda3D was built.)

Extra Notes
-----------

If you don't want to use one or both of the libraries shipped by default with
the SDK, then you can remove the associated library files after installation
or compile Panda3D from source with the appropriate settings to keep them out
of the build.

**Note for users of Panda3D 1.5.4 and under:** If you are using FMOD and a
64-bit operating system, you might run into a strange assertion error or even
a crash if the memory address of the sound exceeds 4 billion. This is because
of an issue in FMOD. To avoid being affected by this issue, you must make sure
your memory usage doesn't exceed 4 GiB (which is not likely, and even
impossible on 32-bit systems).


.. toctree::
   :maxdepth: 2

   loading-and-playing-sounds-and-music
   manipulating-sounds
   audio-managers
   dsp-effects
   3d-audio
   multi-channel
