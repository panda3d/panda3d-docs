.. _texture-transforms:

Texture Transforms
==================

It is possible to apply a matrix to transform the (u, v) texture coordinates of
a model before rendering. In this way, you can adjust the position, rotation, or
scale of a texture, sliding the texture around to suit your particular needs.

Use the following :class:`.NodePath` methods to do this:

.. code-block:: python

   nodePath.setTexOffset(TextureStage, uOffset, vOffset)
   nodePath.setTexScale(TextureStage, uScale, vScale)
   nodePath.setTexRotate(TextureStage, degrees)

If you don't have a particular TextureStage, use
:meth:`.TextureStage.get_default()` as the first parameter.

Note that the operation in each case is applied to the (u, v) texture
coordinates, not to the texture; so it will have the opposite effect on the
texture. For instance, the call :meth:`nodePath.set_tex_scale(ts, 2, 2)
<.NodePath.set_tex_scale>` will effectively double the values of the texture
coordinates on the model, which doubles the space over which the texture is
applied, and thus makes the texture appear half as large.

The above methods apply a 2-d transform to your texture coordinates, which is
appropriate, since texture coordinates are usually two-dimensional. However,
sometimes you are working with :ref:`3-d texture coordinates <3d-textures>`, and
you really do want to apply a 3-d transform. For those cases, there are the
following methods:

.. code-block:: python

   nodePath.setTexPos(TextureStage, uOffset, vOffset, wOffset)
   nodePath.setTexScale(TextureStage, uScale, vScale, wScale)
   nodePath.setTexHpr(TextureStage, h, p, r)

And there is also one generic form:

.. code-block:: python

   nodePath.setTexTransform(TextureStage, transform);

This last method sets a generic TransformState object. This is the same kind of
4x4 transform matrix object that you can get from a NodePath via e.g.,
:meth:`.NodePath.get_transform()`. You can also construct a new TransformState
via a number of methods like :meth:`TransformState::make_pos(VBase3(0, 1, 0))
<.TransformState.make_pos>`. If you intend to apply a 2-d transform only, you
should restrict yourself to methods like
:meth:`TransformState::make_pos2d(VBase2(0, 1)) <.TransformState.make_pos2d>`;
using only 2-d operations may allow the graphics backend to use a slightly
simpler calculation.

Note that the texture transform is associated with a particular TextureStage; it
is not a fixed property of the model or its texture coordinates. You can
therefore apply a different texture transform to each different TextureStage, so
that if you have multiple textures in effect on a particular node, they need not
all be in the same place, even if they all use the same texture coordinates. For
instance, this technique was used to generate the sample images in the
:ref:`Texture Blend Modes <texture-modes>` section. In fact, the following code
was used to place this sample texture (excerpted):

.. code-block:: python

   smiley = loader.loadModel('smiley.egg')
   ts = TextureStage('ts')
   pattern = loader.loadTexture('color_pattern.png')
   smiley.setTexture(ts, pattern)
   smiley.setTexScale(ts, 8, 4)
   smiley.setTexOffset(ts, -4, -2)

and the resulting texture:

|Multitexture sample|

In the above example, we have applied a scale of (8, 4) to reduce the size of
the decal image substantially, and then we specified an offset of (-4, -2) to
slide it around in the positive (u, v) direction to smiley's face (since the (0,
0) coordinate happens to be on smiley's backside). However, these operations
affect only the decal image; the original smiley texture is unchanged from its
normal position, even though both textures are using the same texture
coordinates.

.. |Multitexture sample| image:: smiley-multitex-decal-1.png
