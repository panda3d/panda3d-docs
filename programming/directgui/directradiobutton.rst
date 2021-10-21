.. _directradiobutton:

DirectRadioButton
=================

DirectRadioButtons are similar to check buttons, except only one button is
selected when it is clicked. Their usage is almost identical to regular buttons,
except that the text area and box area can be modified separately.

============== =========================================================================================================================================================================== ==========================================
Keyword        Definition                                                                                                                                                                  Value
============== =========================================================================================================================================================================== ==========================================
text_scale     Scale of the displayed text                                                                                                                                                 (sx,sz)
indicatorValue The initial boolean state of the radiobutton                                                                                                                                0 or 1
variable       The variable whose value will be set by radiobutton. Since we can not use call by reference for int or string variables in python, I used a list instead.                   define a list and pass it
value          The value to be set to the variable. Since we are using a list, we can define multiple values. But the length of value list must be same as length of variable list.        a list of values
others         The list of radio button instances sharing same variable. This must be set by using setOthers() after all radiobuttons are created.                                         a list of radioButton instances
boxImage       BG Image of the radio button                                                                                                                                                Image Path
boxImageColor  Color of the BG image                                                                                                                                                       (R,G,B,A)
boxImageScale  Scale of the BG image                                                                                                                                                       Number
boxGeom        FG Image on the radio button                                                                                                                                                Image Path
boxGeomColor   Color of the FG image                                                                                                                                                       (R,G,B,A)
boxGeomScale   Scale of the FG image                                                                                                                                                       Number
boxPlacement   Position of the box relative to the text area                                                                                                                               ‘left’,’right’, ‘above’, ‘below’, ‘center’
boxBorder      Size of the border around the box                                                                                                                                           Number
command        Command the button performs when clicked.    Function
extraArgs      Extra arguments to the function specified in command                                                                                                                        [Extra Arguments]
commandButtons Which mouse button must be clicked to do the command                                                                                                                        LMB, MMB, or RMB
rolloverSound  The sound made when the cursor rolls over the button                                                                                                                        Sound File Path
clickSound     The sound made when the cursor clicks on the button                                                                                                                         Sound File Path
pressEffect    Whether or not the button sinks in when clicked                                                                                                                             <0 or 1>
============== =========================================================================================================================================================================== ==========================================

Example
-------

.. code-block:: python

   import direct.directbase.DirectStart
   from direct.gui.OnscreenText import OnscreenText
   from direct.gui.DirectGui import *
   from panda3d.core import *

   v = [0]
   # Add some text
   bk_text = "This is my Demo"
   textObject = OnscreenText(text=bk_text, pos=(0.95, -0.95), scale=0.07,
                             fg=(1, 0.5, 0.5, 1), align=TextNode.ACenter,
                             mayChange=1)

   # Callback function to set  text
   def setText(status=None):
       bk_text = "CurrentValue : %s"%v
       textObject.setText(bk_text)

   # Add button
   buttons = [
       DirectRadioButton(text='RadioButton0', variable=v, value=[0],
                         scale=0.05, pos=(-0.4, 0, 0), command=setText),
       DirectRadioButton(text='RadioButton1', variable=v, value=[1],
                         scale=0.05, pos=(0, 0, 0), command=setText),
       DirectRadioButton(text='RadioButton2', variable=v, value=[2],
                         scale=0.05, pos=(0.4, 0, 0), command=setText)
   ]

   for button in buttons:
       button.setOthers(buttons)

   # Run the tutorial
   base.run()
