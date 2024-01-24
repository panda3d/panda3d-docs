.. _gui:

GUI
===

The 2D Scene Graphs
-------------------

By default, there are two different scene graphs created automatically when you
start up Panda3D. These graphs are referred to by their top nodes: render and
render2d.

You use render most often; this is the top of the ordinary 3-D scene. In order
to put an object in the world, you will need to parent it to render (or to some
node that is in turn parented to render).

You will use render2d to render 2-D GUI elements, such as text or buttons, that
you want to display onscreen; for instance, a heads-up display. Anything
parented to render2d will be rendered on top of the 3-D scene, as if it were
painted on the screen glass.

The coordinate system of render2d is set up to match that of the mouse inputs:
the lower-left corner of the screen is (-1, 0, -1), and the upper-right corner
is (1, 0, 1). Since this is a square coordinate system, but the screen is
usually non-square, objects parented directly to render2d may appear squashed.
For this reason, Panda3D also defines a child of render2d, called aspect2d,
which has a scale applied to it to correct the non-square aspect ratio of
render2d. Most often, you will parent GUI elements to aspect2d rather than
render2d.

Specifically, the coordinate system of aspect2d is by default scaled such that x
ranges over [-ratio,ratio], and y ranges over [-1,1] where ratio is
screen_size_x/screen_size_y (in the normal case of a window wider than it is
tall).

There is one more child of render2d to take note of, called pixel2d.
This is scaled in such a way that one Panda unit represents one pixel in the
window. The origin, (0, 0, 0) is in the upper left corner of the window. The
lower right corner has x and z values equal to the width and -height of the
window respectively. As Panda3D uses a Z-Up Right coordinate system, the Y
coordinate in the window will actually be the inverted Z coordinate in Panda.
This node is especially helpful when you want to do pixel-perfect positioning
and scaling.

Rendering Text
--------------

Panda3D includes support for easily rendering dynamic text onscreen or in the
3-d world. It supports full use of the Unicode character set, so it can easily
render international languages (including Asian languages, when used with an
appropriate font).

.. only:: python

   There are three interfaces for creating text, depending on your requirements:
   the :ref:`TextNode <text-node>`, which is the fundamental text-rendering
   class and serves as the implementation for the other two,
   :ref:`onscreentext`, a simple high-level wrapper around TextNode, and
   :ref:`directlabel`, which integrates with the rest of the :ref:`directgui`
   system.

Rendering 3D Models
-------------------

It is possible to render 3D models in the 2D scene graph. However, because the
depth buffer is disabled by default on the 2D scene graph, self-overlapping
models may not render correctly. It is necessary to turn on the depth buffer for
these models. This is explained on the page :ref:`depth-test-and-depth-write`.

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2
   :titlesonly:

   rendering-text
   rendering-images
   directgui/index
   text-fonts
   embedded-text-properties
