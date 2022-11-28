.. _panda3d-rendering-process:

Panda3D Rendering Process
=========================

The rendering process in Panda is comprised by four classes and their
interactions: :class:`.GraphicsPipe`, :class:`.GraphicsEngine`,
:class:`.GraphicsStateGuardian`, and :class:`.GraphicsOutput`. The following
sections will explain the purpose of each of these classes in detail.

Note that the following interfaces are for the advanced user only. If you are
writing a simple application that only needs to open a window and perform basic
3-D rendering, there is no need to use any of these interfaces, as the
appropriate calls to open a default window are made automatically when you
import :py:mod:`direct.directbase.DirectStart` at the start of your application.

At some point, however, you may wish to understand more deeply how to manage
your windows and buffers, and to do this it will help you to understand how
everything is connected together.


.. toctree::
   :maxdepth: 2

   multithreaded-render-pipeline
   introducing-graphics-classes
   graphics-pipe
   creating-windows-and-buffers
   display-regions
   creating-mouse-watchers
   clearing-display-regions
   2d-display-region
   stereo-display-regions
   multi-pass-rendering
   controlling-render-order
   supported-renderer-features
