.. _too-many-text-updates:

Too Many Text Updates
=====================

If you are using the :ref:`TextNode <text-node>` or :ref:`onscreentext` (or
similar) interfaces, and you have large chunks of text changing every frame, you
might find it to be a big performance hit. Panda3D does a lot of work to
assemble the text, so you will want to minimize unnecessary calls to
:meth:`~.TextNode.set_text()` or related functions that force the text to be
recomputed.

On the other hand, if you really want to change your text frequently, you can
try putting this in your :ref:`Config.prc <configuring-panda3d>` file::

   text-flatten 0

This will remove the call to :meth:`~.NodePath.flatten_strong()` within the text
generation process.
Changing the text may be a bit faster, but rendering the resulting text might be
slower, since you will be dealing with :ref:`more meshes <too-many-meshes>` in
your scene graph.

If you have a lot of different glyphs, Panda may spend more effort garbage
collecting used glyphs in order to conserve texture memory. You can increase
the default texture size to improve the performance of this, for example::

   text-page-size 512 512
