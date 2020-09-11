.. _3d-audio:

3D Audio
========

A wrapper :py:mod:`~direct.showbase.Audio3DManager` class has been implemented
to help do positional audio. :py:mod:`~direct.showbase.Audio3DManager` takes as
input an :class:`.AudioManager` and a listener for the sound. A listener is the
point of reference from where the sound should be heard. For a player in a
Panda3D session, this will most likely be the camera. Sounds further away from
the camera will not be loud. Objects nearer to the camera will be loud. Make
sure to use a mono sound source for your 3D audio as stereo sound sources will
not be able to be spatialized and hence can't be used for 3D audio.

.. code-block:: python

   from direct.showbase import Audio3DManager
   audio3d = Audio3DManager.Audio3DManager(base.sfxManagerList[0], camera)

To create a sound that is positional, you need to use the
:py:meth:`~direct.showbase.Audio3DManager.Audio3DManager.loadSfx()` function on
the :py:mod:`~direct.showbase.Audio3DManager` rather than the normal
:py:meth:`loader.loadSfx() <direct.showbase.Loader.Loader.loadSfx>` which is for
non-positional sounds. e.g.

.. code-block:: python

   mySound = audio3d.loadSfx('blue.wav')

Sounds can be attached to objects such that when they move, the sound source
will move along with them.

.. code-block:: python

   audio3d.attachSoundToObject(mySound, teapot)

You can use the manager's
:py:meth:`~direct.showbase.Audio3DManager.Audio3DManager.setSoundVelocity()` and
:py:meth:`~direct.showbase.Audio3DManager.Audio3DManager.setListenerVelocity()`
to set the velocity of sounds or the listener to get the doppler pitch shifting
of moving objects. If you would like the
:py:mod:`~direct.showbase.Audio3DManager` to help you adjust the velocity of
moving objects automatically like it does with their position, you can call
:py:meth:`~direct.showbase.Audio3DManager.Audio3DManager.setSoundVelocityAuto()`
or
:py:meth:`~direct.showbase.Audio3DManager.Audio3DManager.setListenerVelocityAuto()`
like this:

.. code-block:: python

   audio3d.setSoundVelocity(sound, velocityVector)
   audio3d.setListenerVelocity(velocityVector)

   base.cTrav = CollisionTraverser()
   audio3d.setSoundVelocityAuto(sound)
   audio3d.setListenerVelocityAuto()

Currently, for the latter to work, a :class:`.CollisionTraverser` must be attached to
base.cTrav as you see in the example. If you already have one assigned to do
collision detection that will be sufficient.
Read more about :ref:`collision-traversers`.

The attenuation of moving sounds by distance and the doppler shift are based
the way sound works in the real world. By default it assumes a scale of 1
panda unit equal to 1 foot (or 1 meter in Panda3D 1.10 and above). If you use
another scale you'll need to use
:py:meth:`~direct.showbase.Audio3DManager.Audio3DManager.setDistanceFactor()` to
adjust the scale.

.. code-block:: python

   audio3d.setDistanceFactor(scale)

You can adjust the rate that sounds attenuate by distance. If you want to
position the sounds but don't want the volume to be effected by their
distance, you can set the drop off factor to 0.

.. code-block:: python

   audio3d.setDropOffFactor(scale)
