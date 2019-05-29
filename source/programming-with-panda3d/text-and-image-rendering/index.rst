.. _text-and-image-rendering:

Text and Image Rendering
========================

Panda includes support for easily rendering dynamic text onscreen or in the
3-d world. It supports full use of the Unicode character set, so it can easily
render international languages (including Asian languages, when used with an
appropriate font).

There are three interfaces for creating text, depending on your requirements:
the :ref:`TextNode <text-node>`, which is the fundamental text-rendering class
and serves as the implementation for the other two, :ref:`onscreentext`, a
simple high-level wrapper around TextNode, :ref:`onscreenimage`, the same as
:ref:`onscreentext` but now for images, and :ref:`directlabel`, which
integrates with the rest of the :ref:`directgui` system.


.. toctree::
   :maxdepth: 2

   text-fonts
   text-node
   onscreentext
   onscreenimage
   embedded-text-properties
