.. _directscrollbar:

DirectScrollBar
===============

.. only:: python

   A DirectScrollBar is similar to the "scroll bar" widget commonly used by the
   user to page through a large document.
   It consists of a long trough, a thumb that slides along the trough, and a
   pair of buttons on either side of the trough to scroll one line at a time.
   A DirectScrollBar can be oriented either vertically or horizontally.

   The DirectScrollBar is similar in function to :ref:`directslider`, but it is
   specifically designed for scrolling through a large window. In fact, a pair
   of DirectScrollBars is used to implement the :ref:`directscrolledframe`,
   which manages this scrolling functionality automatically. (Because
   DirectScrolledFrame exists, you will probably not need to create a
   DirectScrollBar directly, unless you have some custom purpose that requires a
   scroll bar.)

   DirectScrollBar has many things in common with :ref:`directslider`. Like
   :ref:`directslider`, the normal DirectGui parameters such as frameSize, geom,
   and relief control the look of the trough. You can control the look of the
   thumb by prefixing each of these parameters with the prefix "thumb\_", e.g.
   ``thumb_frameSize``; similarly, you can control the look of the two scroll
   buttons by prefixing these with "incButton\_" and "decButton\_". You can
   retrieve or set the current position of the thumb with
   ``myScrollBar['value']``.

   =========================================================================== ============================================================================================================================================================================================ =================================================
   Keyword                                                                     Definition                                                                                                                                                                                   Value
   =========================================================================== ============================================================================================================================================================================================ =================================================
   value                                                                       Initial position of the thumb                                                                                                                                                                Default is 0
   range                                                                       The (min, max) range of the thumb                                                                                                                                                            Default is (0, 1)
   pageSize                                                                    The amount to jump the thumb when the user clicks left or right, (up or down if the scrollbar is vertical), of the thumb; this also controls the width of the thumb when resizeThumb is True Default is 0.1
   scrollSize                                                                  The amount to move the thumb when the user clicks once on either scroll button                                                                                                               Default is 0.01
   orientation                                                                 The orientation of the scroll bar                                                                                                                                                            DGG.HORIZONTAL or DGG.VERTICAL
   manageButtons                                                               Whether to automatically adjust the buttons when the scroll bar’s frame is changed                                                                                                           True or False
   resizeThumb                                                                 Whether to adjust the width of the thumb to reflect the ratio of pageSize to the overall range; requires manageButtons to be True as well                                                    True or False
   command                                                                     Function called when the position of the thumb changes (takes no arguments)                                                                                                                  Function
   extraArgs                                                                   Extra arguments to the function specified in command                                                                                                                                         [Extra Arguments]
   thumb_geom, thumb_relief, thumb_text, thumb_frameSize, etc.                 Parameters to control the look of the thumb                                                                                                                                                  Any parameters appropriate to :ref:`directbutton`
   incButton_geom, incButton_relief, incButton_text, incButton_frameSize, etc. Parameters to control the look of the lower or right scroll button                                                                                                                           Any parameters appropriate to :ref:`directbutton`
   decButton_geom, decButton_relief, decButton_text, decButton_frameSize, etc. Parameters to control the look of the upper or left scroll button                                                                                                                            Any parameters appropriate to :ref:`directbutton`
   =========================================================================== ============================================================================================================================================================================================ =================================================

   Here is a small example on how to create the scrollbar:

   .. code-block:: python

      from direct.gui.DirectGui import DirectScrollBar

      mybar = DirectScrollBar(range=(0, 100), value=50, pageSize=3, orientation= DGG.VERTICAL)
      mybar.setPos(-1, 0, -0.5)

   This will give you a scrollbar at the lower left side of the screen. If you
   want to parent the scrollbar to a determined frame, you add the keyword
   **parent** to the set of keyboards like so:

   .. code-block:: python

      mybar = DirectScrollBar(parent=myframe, range=(0,100), value=50, pageSize=3, orientation= DGG.VERTICAL)
      mybar.setPos(-1, 0, -0.5)
