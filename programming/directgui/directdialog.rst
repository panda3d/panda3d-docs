.. _directdialog:

DirectDialog
============

DirectDialog objects are popup windows to alert or interact with the user. It
is invoked just like the other DirectGUI objects, but it also has some unique
keywords. Integral to DirectDialog are dialogName, buttonTextList,
buttonImageList, and buttonValueList. The dialogName should ideally be the
name of the NodePath created to hold the object. The button lists contain the
various properties of the buttons within the dialog box. No maximum number of
buttons needs to be declared.

Panda3D contains a number of shortcuts for common dialog options. For example,
rather than specifying the rather common text list ("Yes","No"), there is a
YesNoDialog that functions exactly like a normal dialog but has buttonTextList
already defined. The other similar dialogs are OkCancelDialog, OkDialog,
RetryCancelDialog, and YesNoCancelDialog.

================ ============================================================================================================================== =======================
Keyword          Definition                                                                                                                     Value
================ ============================================================================================================================== =======================
dialogName       Name of the dialog                                                                                                             String
buttonTextList   List of text to show on each button                                                                                            [Strings]
buttonGeomList   List of geometry to show on each button                                                                                        [NodePaths]
buttonImageList  List of images to show on each button                                                                                          [Image Paths]
buttonValueList  List of values sent to dialog command for each button. If value is [] then the ordinal rank of the button is used as its value [Numbers]
buttonHotKeyList Shortcut key for each button (the button must have focus)                                                                      [Characters]
buttonSize       4-tuple used to specify custom size for each button (to make bigger then geom/text for example)                                (Left,Right,Bottom,Top)
topPad           Extra space added above text/geom/image                                                                                        Number
midPad           Extra space added between text/buttons                                                                                         Number
sidePad          Extra space added to either side of text/buttons                                                                               Number
buttonPadSF      Scale factor used to expand/contract button horizontal spacing                                                                 Number
command          Callback command used when a button is pressed. Value supplied to command depends on values in buttonValueList                 Function
extraArgs        Extra arguments to the function specified in command                                                                           [Extra Arguments]
fadeScreen       If 1, fades screen to black when the dialog appears                                                                            0 or 1
================ ============================================================================================================================== =======================

YesNo Dialog Example
--------------------

.. code-block:: python

   import direct.directbase.DirectStart
   from direct.gui.OnscreenText import OnscreenText
   from direct.gui.DirectGui import *
   from direct.task import Task
   from direct.actor import Actor
   from direct.interval.IntervalGlobal import *
   from panda3d.core import *

   # Add some text
   bk_text = "DirectDialog- YesNoDialog Demo"
   textObject = OnscreenText(text=bk_text, pos=(0.85,0.85),
       scale=0.07, fg=(1, 0.5, 0.5, 1), align=TextNode.ACenter, mayChange=1)

   # Add some text
   output = ""
   textObject = OnscreenText(text=output, pos=(0.95,-0.95),
       scale=0.07, fg=(1, 0.5, 0.5, 1), align=TextNode.ACenter, mayChange=1)

   # Callback function to set text
   def itemSel(arg):
       if arg:
           output = "Button Selected is: Yes"
       else:
           output = "Button Selected is: No"
       textObject.setText(output)

   # Create a frame
   dialog = YesNoDialog(dialogName="YesNoCancelDialog", text="Please choose:",
                        command=itemSel)

   base.camera.setPos(0, -20, 0)
   base.run()

.. note::
   The OkDialog causes an error if being created a second time after destroying
   it with ``myOkDialog.destroy()``. To solve this you can use:

   .. code-block:: python

      myOkDialog.cleanup()
