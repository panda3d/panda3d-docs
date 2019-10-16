.. _converting-from-blender:

Converting from Blender
=======================

Currently, there are two ways to get data from Blender into Panda3D. The most
popular is almost certainly the YABEE exporter.

Option 1: The Egg export Plugins for Blender
--------------------------------------------


There are several Blender plugins contributed by Panda3D users.

YABEE is an exporter for Blender 2.5, 2.6, 2.7 and should work with most
recent versions of blender (2.73a at moment of writing). It's documented and
feature complete. YABEE can export:

| ``   Meshes``
| ``   UV layers``
| ``   Materials and textures (Partially)``
| ``   Armature (skeleton) animation``
| ``   ShapeKeys (morph) animation``
| ``   <Tag> and Collision options export through Blender's "Game logic" -> "properties"``
| ``   Non cyclic NURBS Curves``

https://github.com/09th/YABEE

If you observe any problem, or find a bug, you can report it on official
thread that can be found here:
https://discourse.panda3d.org/t/yet-another-blender-egg-exporter-yabee/10702

----

Chicken is the old and no longer updated, but documented and feature complete
exporter for Blender 2.4. It supports static meshes and armature animation,
materials, vertex colors, alpha textures, tags, object types, etc. It also has
advanced features such as automatic invocation of Panda tools (egg2bam,
egg-optchar and pview) and Motion Extraction. You can find it at
http://sourceforge.net/projects/chicken-export/

--------------

Another exporter for Blender 2.4 that only supports static meshes can be found
at http://xoomer.virgilio.it/glabro1/panda.html

Option 2: The "X" File format
-----------------------------


There exists a free plugin for Blender that can export "X" (DirectX native)
file format. Save the file from blender as an X file, then load it directly
into Panda3D, which can read X file format. Alternately, if you're concerned
about long load times (panda has to translate the file at load time), then
pre-convert the model from X to Egg to Bam using the conversion programs
supplied with Panda3D (x2egg, egg2bam).

Whenever you save a model in a non-native file format, you need to ask
yourself: "does this file format support everything I need?" For example, when
you save out a model in 3DS file format, you automatically lose all bone and
animation data, because the 3DS file format doesn't contain bone and animation
data. In the case of the X file format, you're in good shape: it's a fairly
powerful file format, supporting vertices and triangles, bones and animation.

Note however, when an animated X file is converted to egg, the resulting egg
file only plays the keyframes, but not whats supposed to be in between. For
example, an animation could exist that should spawn 200 frames, gets sized
down to about 40, and playback looks shakey. This shakeyness happens because
the X file format supports the concept of keyframes, with implicit frames
interpolated between them. The egg file format is explicit. An egg file must
give all of the frames of an animation, even the frames that appear between
"keyframes".

Therefore, a run of x2egg with an X file that omits a lot of frames between
keyframes, will product a shapekey animation. The only solution is to ensure
your X files are generated with all frames. Testing of different X file
exporters may be required.

Further, panda's native egg file format supports some esoteric things. For
example, it supports blend targets (morph animations) and motion path curves,
which are not supported by the X file format.

.. caution::

   At one time, it was discovered that there were two bugs in panda's X-file
   importer. One, it was case-sensitive and it should not be. Two, it did not
   handle hyphens in identifiers correctly. It is unknown whether or not these
   bugs have been fixed.
