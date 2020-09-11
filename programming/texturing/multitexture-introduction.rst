.. _multitexture-introduction:

Multitexture Introduction
=========================

Panda3D provides the ability to apply more than one texture image at a time to
the polygons of a model. The textures are applied on top of each other, like
coats of paint; very much like the "layers" in a popular photo-paint program.

To layer a second texture on a model, you will have to understand Panda's
concept of a :class:`.TextureStage`. Think of a TextureStage as a slot to hold a
single texture image. You can have as many different TextureStages as you want
in your scene, and each TextureStage might be used on one, several, or all
models.

When you apply a texture to a model, for instance with the
:meth:`~.NodePath.set_texture()` call, you are actually binding the texture to a
particular TextureStage. If you do not specify a TextureStage to use, Panda
assumes you mean the "default" TextureStage object, which is a global pointer
which you can access as :meth:`.TextureStage.get_default()`.

Each :class:`.TextureStage` can hold one texture image for a particular model.
If you assign a texture to a particular TextureStage, and then later (or at a
lower node) assign a different texture to the same TextureStage, the new texture
completely replaces the old one. (Within the overall scene, a given TextureStage
can be used to hold any number of different textures for different nodes; but it
only holds one texture for any one particular node.)

However, you can have as many different TextureStages as you want. If you create
a new TextureStage and use it to assign a second texture to a node, then the
node now has both textures assigned to it.

Although there is no limit to the number of TextureStages you assign this way,
your graphics card will impose some limit on the number it can render on any one
node. Modern graphics cards will typically have a limit of 4 or 8 textures at
once; some older cards can only do 2, and some very old cards have a limit of 1
(only one texture at a time). You can find out the multitexture limit on your
particular card with the call :meth:`base.win.getGsg().get_max_texture_stages()
<.GraphicsStateGuardian.get_max_texture_stages>`.

Remember, however, that this limit only restricts the number of different
TextureStages you can have on any one particular node; you can still have as
many different TextureStages as you like as long as they are all on different
nodes.

Let's revisit the example from :ref:`simple-texture-replacement`, where we
replaced the normal texture on smiley.egg with a new texture image that contains
a random color pattern. This time, instead of assigning the new texture to the
default TextureStage, we'll create a new TextureStage for it, so that both
textures will still be in effect:

.. code-block:: python

   smiley = loader.loadModel('smiley.egg')
   smiley.reparentTo(render)
   tex = loader.loadTexture('maps/noise.rgb')
   ts = TextureStage('ts')
   smiley.setTexture(ts, tex)

Note that we can create a new TextureStage object on the fly; the only parameter
required to the TextureStage parameter is a name, which is significant only to
us. When we pass the TextureStage as the first parameter to
:meth:`~.NodePath.set_texture()`, it means to assign the indicated texture to
that TextureStage. Also note that we no longer need to specify an override to
the :meth:`~.NodePath.set_texture()` call, since we are not overriding the
texture specified at the Geom level, but rather we are adding to it.

And the result is this:

.. image:: multitex-smiley-noise.png

To undo a previous call to add a texture, use:

.. only:: python

   .. code-block:: python

      smiley.clearTexture(ts)

.. only:: cpp

   .. code-block:: cpp

      smiley.clear_texture(ts);

passing in the same TextureStage that you used before. Or, alternatively, you
may simply use:

.. only:: python

   .. code-block:: python

      smiley.clearTexture()

.. only:: cpp

   .. code-block:: cpp

      smiley.clear_texture();

to remove all texture specifications that you previously added to the node
smiley. This does not remove the original textures that were on the model when
you loaded it; those textures are assigned at a different node level, on the
Geom objects that make up the model.
