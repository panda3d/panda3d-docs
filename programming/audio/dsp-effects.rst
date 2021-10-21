.. _dsp-effects:

DSP Effects
===========

DSP, or Digital Signal Processing, allows you to apply effect filters to your
in-game audio. As of now, DSP effects are only available in Panda if you use the
FMOD audio library. By default, Panda ships using the OpenAL audio library but
FMOD can be enabled simply by editing :ref:`Config.prc <configuring-panda3d>`.
Please keep in mind that using FMOD in a commercial application will require
purchasing a license.

You will need to change this line in your Config.prc: (some versions of Panda3D
might already be set to FMOD)

::

   audio-library-name p3openal_audio

To this::

   audio-library-name p3fmod_audio

The FilterProperties Object
---------------------------

Any DSP you add to your sound will require the use of
:class:`.FilterProperties`, which is a list of filters and their coefficients.
Start with this import:

.. code-block:: python

   from panda3d.core import FilterProperties

This will allow you to create lists of filters, like this one:

.. code-block:: python

   fp = FilterProperties()

This just adds a blank filter list. From here we can add whatever filter we'd
like. To stay consistent with the example below, we'll add a reverb effect.

.. code-block:: python

   fp.addReverb(0.6, 0.5, 0.1, 0.1, 0.1)

All this really does is add this particular reverb to our filter list - sound is
not yet affected. To apply these filters to our audio output, use:

.. code-block:: python

   audioMgr.configureFilters(fp)

where ``audioMgr`` is an :class:`.AudioManager` object, most likely
:py:obj:`base.sfxManagerList <direct.showbase.ShowBase.ShowBase.sfxManagerList>`
or :py:obj:`base.musicManager <direct.showbase.ShowBase.ShowBase.musicManager>`.

Depending on the sound you use, reverb may be very or only slightly noticeable;
try using a quick sound at first, like a clap.

You can add more than just reverb to your sound. The full list of available
filters is here:

:class:`panda3d.core.FilterProperties`

Below is a sample program for adding a reverb effect:

.. code-block:: python

   # This is just to ensure that we are using FMOD. In your application,
   # please edit the Config.prc file that you distribute
   from panda3d.core import loadPrcFileData
   loadPrcFileData("", "audio-library-name p3fmod_audio")

   from direct.showbase.ShowBase import ShowBase
   from panda3d.core import FilterProperties

   base = ShowBase()

   mySound = loader.loadSfx("models/audio/sfx/GUI_rollover.wav")
   mySound.setLoop(True)
   mySound.play()

   fp = FilterProperties()
   fp.addReverb(0.6, 0.5, 0.1, 0.1, 0.1)
   base.sfxManagerList[0].configureFilters(fp)

   base.run()
