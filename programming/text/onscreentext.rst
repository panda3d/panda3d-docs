.. _onscreentext:

OnscreenText
============

.. only:: cpp

   .. note::

      This convenience class is only available in the Python API.
      See :ref:`text-node` for the underlying class that is available in C++.

The OnscreenText object is a convenience wrapper around
:ref:`TextNode <text-node>`. You can use it as a quick way to put text onscreen
without having to go through the trouble of creating a TextNode and setting
properties on it. However, it doesn't have the full range of rendering options
that you can get with TextNode directly; and it doesn't support the DirectGUI
features of a :ref:`directlabel`. Use an OnscreenText whenever you want a quick
way to display some ordinary text without a lot of fancy requirements.

.. code-block:: python

   from direct.gui.OnscreenText import OnscreenText
   textObject = OnscreenText(text='my text string', pos=(-0.5, 0.02), scale=0.07)

The OnscreenText object inherits from NodePath, so all of the standard NodePath
operations can be used on the text object. When you are ready to take the text
away, use:

.. code-block:: python

   textObject.destroy()

The following keyword parameters may be specified to the constructor:

========= ===============================================================================================================================================================================================================================================================================
text      the actual text to display. This may be omitted and specified later via setText() if you don’t have it available, but it is better to specify it up front.
style     one of the pre-canned style parameters defined at the head of OnscreenText.py. This sets up the default values for many of the remaining parameters if they are unspecified; however, a parameter may still be specified to explicitly set it, overriding the pre-canned style.
pos       the x, y position of the text on the screen.
scale     the size of the text. This may either be a single float (and it will usually be a small number like 0.07) or it may be a 2-tuple of floats, specifying a different x, y scale.
fg        the (r, g, b, a) foreground color of the text. This is normally a 4-tuple of floats or ints.
bg        the (r, g, b, a) background color of the text. If the fourth value, a, is nonzero, a card is created to place behind the text and set to the given color.
shadow    the (r, g, b, a) color of the shadow behind the text. If the fourth value, a, is nonzero, a little drop shadow is created and placed behind the text.
frame     the (r, g, b, a) color of the frame drawn around the text. If the fourth value, a, is nonzero, a frame is created around the text.
align     one of TextNode.ALeft, TextNode.ARight, or TextNode.ACenter.
wordwrap  either the width to wordwrap the text at, or None to specify no automatic word wrapping.
font      the font to use for the text.
parent    the NodePath to parent the text to initially; the default is aspect2d.
mayChange pass true if the text or its properties may need to be changed at runtime, false if it is static once created (which leads to better memory optimization). The default is false.
========= ===============================================================================================================================================================================================================================================================================

:ref:`onscreenimage` works similarly, but it shows an image on the screen
instead of text.
