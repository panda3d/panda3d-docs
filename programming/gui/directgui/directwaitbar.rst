.. _directwaitbar:

DirectWaitBar
=============

DirectWaitBars are similar to status bars; use them to indicate a slow process
gradually completing (e.g. a loading screen). It has various options for both
the background bar and the loading bar that fills up as the process progresses.
You can call finish() to automatically fill up the bar, or use the following to
set the value (it ranges from 0 to 100 by default):

.. code-block:: python

   myWaitBar['value'] = number

============== ============================================================================================= ================================
Keyword        Definition                                                                                    Value
============== ============================================================================================= ================================
value          Initial value of the loading bar (from 0 to 100)                                              Number
range          The maximum value of the loading bar                                                          Number
barColor       The color of the loading bar                                                                  (R,G,B,A)
barTexture     An image to be display on the loading bar                                                     image filename or Texture object
barRelief      The relief appearance of the loading bar                                                      SUNKEN or RAISED
barBorderWidth If barRelief is SUNKEN, RAISED, GROOVE, or RIDGE, changes the size of the loading bar's bevel (Width, Height)
relief         The relief appearance of the background bar                                                   SUNKEN or RAISED
============== ============================================================================================= ================================

Example
-------

.. code-block:: python

   import direct.directbase.DirectStart
   from direct.gui.OnscreenText import OnscreenText
   from direct.gui.DirectGui import *
   from panda3d.core import *

   # Add some text
   bk_text = "This is my Demo"
   textObject = OnscreenText(text=bk_text, pos=(0.95, -0.95), scale=0.07,
                             fg=(1, 0.5, 0.5, 1), align=TextNode.ACenter,
                             mayChange=1)

   # Callback function to set text
   def incBar(arg):
       bar['value'] += arg
       text = "Progress is:" + str(bar['value']) + '%'
       textObject.setText(text)

   # Create a frame
   frame = DirectFrame(text="main", scale=0.001)
   # Add button
   bar = DirectWaitBar(text="", value=50, pos=(0, .4, .4))

   # Create 4 buttons
   button_1 = DirectButton(text="+1", scale=0.05, pos=(-.3, .6, 0),
                           command=incBar, extraArgs=[1])
   button_10 = DirectButton(text="+10", scale=0.05, pos=(0, .6, 0),
                            command=incBar, extraArgs=[10])
   button_m1 = DirectButton(text="-1", scale=0.05, pos=(0.3, .6, 0),
                            command=incBar, extraArgs=[-1])
   button_m10 = DirectButton(text="-10", scale=0.05, pos=(0.6, .6, 0),
                             command=incBar, extraArgs=[-10])

   # Run the tutorial
   base.run()
