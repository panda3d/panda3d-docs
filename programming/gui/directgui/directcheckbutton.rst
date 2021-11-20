.. _directcheckbutton:

DirectCheckButton
=================

DirectCheckButtons are similar to buttons, except they represent a binary state
that is toggled when it is clicked. Their usage is almost identical to regular
buttons, except that the text area and box area can be modified separately.

============== ================================================================================== ========================
Keyword        Definition                                                                         Value
============== ================================================================================== ========================
text_scale     Scale of the displayed text                                                        (sx,sz)
indicatorValue The initial boolean state of the checkbox                                          0 or 1
boxImage       Image on the checkbox                                                              Image Path
boxImageColor  Color of the image on the box                                                      (R,G,B,A)
boxImageScale  Scale of the displayed image                                                       Number
boxPlacement   Position of the box relative to the text area                                      ‘left’,’right’
boxRelief      Relief appearance of the checkbox                                                  DGG.SUNKEN or DGG.RAISED
boxBorder      Size of the border around the box                                                  Number
command        Command the button performs when clicked(0 or 1 is passed, depending on the state) Function
extraArgs      Extra arguments to the function specified in command                               [Extra Arguments]
commandButtons Which mouse button must be clicked to do the command                               LMB, MMB, or RMB
rolloverSound  The sound made when the cursor rolls over the button                               Sound File Path
clickSound     The sound made when the cursor clicks on the button                                Sound File Path
pressEffect    Whether or not the button sinks in when clicked                                    <0 or 1>
============== ================================================================================== ========================

Example
-------

.. code-block:: python

   import direct.directbase.DirectStart
   from direct.gui.OnscreenText import OnscreenText
   from direct.gui.DirectGui import *
   from panda3d.core import *

   # Add some text
   bk_text = "This is my Demo"
   textObject = OnscreenText(text=bk_text, pos=(0.95,-0.95), scale=0.07,
                             fg=(1, 0.5, 0.5, 1), align=TextNode.ACenter,
                             mayChange=1)

   # Callback function to set  text
   def setText(status):
       if status:
           bk_text = "Checkbox Selected"
       else:
           bk_text = "Checkbox Not Selected"
   textObject.setText(bk_text)

   # Add button
   b = DirectCheckButton(text = "CheckButton" ,scale=.05,command=setText)

   # Run the tutorial
   base.run()

Programmatically changing the indicatorValue
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you programmatically want to change the checkbutton's indicatorValue, you need
to call ``setIndicatorValue`` afterwards to update the checkbutton, like:

.. code-block:: python

   b["indicatorValue"] = True
   b.setIndicatorValue()

boxImage and other box\* keywords
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Just as DirectButton may be passed a 4-tuple of values to be used in the four
button states, the box\* keyword arguments may be supplied with multiple entries
to denote the unchecked and checked state. To supply arguments to be used in the
two states of the checkbox, construct a 3-tuple of values with a 'None' in the
final entry, i.e. (unchecked, checked, None). For example, to set two different
images for the unchecked and checked states:

.. code-block:: python

   boxImage = ("pathToDisabledImage.jpg", "pathToEnabled.jpg", None)
