.. _texture-order:

Texture Order
=============

When there are multiple textures in effect, depending on the
:ref:`Texture Blend Mode <texture-modes>` in use, it may be important to
control the order in which the textures apply. For instance, although Modulate
mode and Add mode are order-independent, texture order makes a big difference
to Decal mode, Replace mode, and Blend mode.

To specify the texture order, use :meth:`.TextureStage.set_sort()` on one or
more of your TextureStages. If you do not specify a sort value, the default sort
value is 0. When the geometry is rendered, all of the textures are rendered in
increasing order of sort value, such that the largest sort value is rendered on
top. Thus, if you want to use Decal mode, for instance, to apply a texture on
top of a lower texture, it would be a good idea to use
:meth:`~.TextureStage.set_sort()` to give a higher sort value to your decal
texture.

Also, since some hardware might not be able to render all of the TextureStages
that you have defined on a particular node, Panda provides a way for you to
specify which texture(s) are the most important. Use
:meth:`.TextureStage.set_priority()` for this.

The priority value is only consulted when you have applied more TextureStages
to a particular node than your current hardware can render. In this case,
Panda will select the n textures with the highest priority value (and then
sort them in order by the :meth:`~.TextureStage.set_sort()` value). Between two
textures with the same priority, Panda will prefer the one with the lower sort
value. The default priority is 0.
