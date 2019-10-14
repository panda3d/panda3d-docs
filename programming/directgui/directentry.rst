.. _directentry:

DirectEntry
===========

The DirectEntry creates a field that accepts text entered by the user. It
provides a blinking cursor and support for backspace and the arrow keys. It
can accept either a single line of text, with a fixed width limit (it doesn't
scroll), or it can accept multiple word-wrapped lines.

================= ========================================================================================= =================
Keyword           Definition                                                                                Value
================= ========================================================================================= =================
initialText       Initial text to load in the field                                                         String
entryFont         Font to use for text entry                                                                Font object
width             Width of field in screen units                                                            Number
numLines          Number of lines in the field                                                              Integer
cursorKeys        True to enable the use of cursor keys (arrow keys)                                        0 or 1
obscured          True to hide passwords, etc.                                                              0 or 1
command           Function to call when enter is pressed(the text in the field is passed to the function)   Function
extraArgs         Extra arguments to the function specified in command                                      [Extra Arguments]
rolloverSound     The sound made when the cursor rolls over the field                                       Sound File Path
clickSound        The sound made when the cursor inside the field                                           Sound File Path
focus             Whether or not the field begins with focus (focusInCommand is called if true)             0 or 1
backgroundFocus   If true, field begins with focus but with hidden cursor, and focusInCommand is not called 0 or 1
focusInCommand    Function called when the field gains focus                                                Function
focusInExtraArgs  Extra arguments to the function specified in focusInCommand                               [Extra Arguments]
focusOutCommand   Function called when the field loses focus                                                Function
focusOutExtraArgs Extra arguments to the function specified in focusOutCommand                              [Extra Arguments]
================= ========================================================================================= =================

Example
-------

.. code-block:: python

   import direct.directbase.DirectStart
   from direct.gui.OnscreenText import OnscreenText
   from direct.gui.DirectGui import *
   from panda3d.core import *

   #add some text
   bk_text = "This is my Demo"
   textObject = OnscreenText(text=bk_text, pos=(0.95, -0.95), scale=0.07,
                             fg=(1, 0.5, 0.5, 1), align=TextNode.ACenter,
                             mayChange=1)

   #callback function to set  text
   def setText(textEntered):
       textObject.setText(textEntered)

   #clear the text
   def clearText():
       entry.enterText('')

   #add text entry
   entry = DirectEntry(text = "", scale=.05, command=setText,
   initialText="Type Something", numLines = 2, focus=1, focusInCommand=clearText)

   #run the tutorial
   base.run()

This example implements a text entry widget typically seen in web pages.
