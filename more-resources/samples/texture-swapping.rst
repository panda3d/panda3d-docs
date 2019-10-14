.. _texture-swapping:

Sample Programs: Texture Swapping
=================================

The Texture Swapping Sample Program

To run a sample program, you need to install Panda3D. If you're a Windows
user, you'll find the sample programs in your start menu. If you're a Linux
user, you'll find the sample programs in /usr/share/panda3d.

Screenshots

|Screenshot-Sample-Programs-Texture-Swapping.jpg|

Explanation

This tutorial will show how to use a sequence of textures on an object to
achieve a specific effect. Popular uses of this technique are:

-  Animated sprites
-  Moving shadows

The basic principle of this tutorial is that even though a model file contains
a reference to a texture file, the actual texture applied to a model can be
changed in panda. Textures are just image files and they can be loaded in
panda via loader.loadTexture. Each model loaded into Panda has a texture
attribute that can be changed. Not only can this feature be used to change the
texture on a model from one to another but it can also be used play an
animated sequence on the model by using a sequence of textures and swapping
them at regular intervals.

This tutorial will also demonstrate the billboard function which orients an
object to always face the the camera. This is useful for 2D sprites in a 3D
world.

Above is a screenshot of the tutorial running with two animated sprites. One
is a flying duck and the other is an explosion. Only the explosion has the
billboard effect applied to it. As the camera moves, the explosion will turn
to face the camera while the duck will not.

Back to the List of Sample Programs:

:ref:`samples`

.. |Screenshot-Sample-Programs-Texture-Swapping.jpg| image:: screenshot-sample-programs-texture-swapping.jpg
