.. _directscrolledframe:

DirectScrolledFrame
===================

The DirectScrolledFrame is a special variant of DirectFrame that allows the
user to page through a larger frame than would otherwise fit onscreen. The
DirectScrolledFrame consists of a small onscreen frame which is actually a
window onto a potentially much larger virtual canvas; the user can scroll
through this canvas through the use of one or two
:ref:`DirectScrollBars <directscrollbar>` on the right and bottom of the
frame.

The ``frameSize`` parameter controls the size and placement of the visible,
onscreen frame; use the ``canvasSize`` parameter to control the size of the
larger virtual canvas.

You can then parent any widgets you like to the NodePath returned by
:meth:`myFrame.getCanvas() <direct.gui.DirectScrolledFrame.DirectScrolledFrame.getCanvas>`
The DirectGui items you attach to this canvas NodePath will be visible through
the small window; you should position them within the virtual canvas using
values within the coordinate range you established via the ``canvasSize``
parameter.

By default, the scroll bars are automatically created with the
DirectScrolledFrame and will be hidden automatically when they are not needed
(that is, if the virtual frame size is equal to or smaller than the onscreen
frame size). You can adjust either frame size at runtime and the scroll bars
will automatically adjust as needed. If you would prefer to manage the scroll
bars yourself, you can set one or both of ``manageScrollBars`` and
``autoHideScrollBars`` to False.

========================================================= ========================================================================================================== ====================================================
Keyword                                                   Definition                                                                                                 Value
========================================================= ========================================================================================================== ====================================================
canvasSize                                                Extents of the virtual canvas                                                                              (Left, right, bottom, top)
frameSize                                                 Extents of the actual visible frame                                                                        (Left, right, bottom, top)
manageScrollBars                                          Whether to automatically position and scale the scroll bars to fit along the right and bottom of the frame True or False
autoHideScrollBars                                        Whether to automatically hide one or both scroll bars when not needed                                      True or False
scrollBarWidth                                            Specifies the width of both scroll bars at construction time                                               Default is 0.08
verticalScroll_relief, verticalScroll_frameSize, etc.     Parameters to control the look of the vertical scroll bar                                                  Any parameters appropriate to :ref:`directscrollbar`
horizontalScroll_relief, horizontalScroll_frameSize, etc. Parameters to control the look of the horizontal scroll bar                                                Any parameters appropriate to :ref:`directscrollbar`
========================================================= ========================================================================================================== ====================================================

As a very small and simple example on how to use this element we have a simple
scrolled frame on the middle of the screen:

.. code-block:: python

   from direct.gui.DirectGui import *
   import direct.directbase.DirectStart

   myframe = DirectScrolledFrame(canvasSize=(-2, 2, -2, 2), frameSize=(-.5, .5, -.5, .5))
   myframe.setPos(0, 0, 0)

   run()
