.. _too-many-text-updates:

Performance Issue: Too Many Text Updates
========================================

If you are using the :ref:`TextNode <text-node>` or :ref:`onscreentext` (or
similar) interfaces, and you have large chunks of text changing every frame, you
might find it to be a big performance hit. Panda3D does a lot of work to
assemble the text, so you will want to minimize unnecessary calls to
``setText()`` or related functions that force the text to be recomputed.

On the other hand, if you really want to change your text frequently, you can
try putting this in your :ref:`Config.prc <configuring-panda3d>` file::

   text-flatten 0

This will remove the call to flattenStrong() within the text generation process.
Changing the text will be much faster, but rendering the resulting text might be
slower, since you will be dealing with :ref:`more meshes <too-many-meshes>` in
your scene graph.

Panda3D 1.6.0 and later contain a performance optimization that speeds up the
text generation. If you have this version, you will also need the following line
in your Config.prc, in addition to the text-flatten line, to achieve the same
effect (though this is not recommended, for the reason stated above)::

   text-dynamic-merge 0

This setting is no longer recommended for Panda3D 1.10.0, which actually
performs significantly better with text-dynamic-merge set to 1.

If you have a lot of different glyphs, Panda may spend more effort garbage
collecting used glyphs in order to conserve texture memory. You can increase
the default texture size to improve the performance of this, for example::

   text-page-size 512 512
