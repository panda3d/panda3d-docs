.. _directoptionmenu:

DirectOptionMenu
================

The DirectOptionMenu class models a popup menu with an arbitrary number of
items. It is composed of the menu bar, the popup marker, and the popup menu
itself. The popup menu appears when the menu is clicked on and disappears when
the user clicks again; if the click was inside the popup, the selection changes.
By default, the text on the menu changes to whatever item is currently selected.
The attributes that affect the appearance of the menu bar don't apply to the
popup. Make sure to specify the items option or it may crash.

================== =============================================================================== =======================================================
Keyword            Definition                                                                      Value
================== =============================================================================== =======================================================
textMayChange      Whether the text on the menu changes with the selection                         0 or 1
initialitem        The index of the item that appears next to the cursor when the popup appears    Number
items              List of items in the popup menu                                                 [Strings]
command            Function called when an item is selected (the item is passed in as a parameter) Function
commandButtons     Which mouse button must be clicked to open the popup                            LMB, MMB, or RMB
extraArgs          Extra arguments to the function specified in command                            [Extra Arguments]
highlightColor     Color of highlighted text                                                       (R,G,B,A)
highlightScale     Scale of highlighted text                                                       (Width,Height)
rolloverSound      The sound made when the cursor rolls over the button                            Sound File Path
clickSound         The sound made when the cursor clicks on the button                             Sound File Path
popupMarkerBorder  Use width to change the size of the border around the popup marker              (Width,Height)
popupMarker_image  Set the state images of the popupMarker                                         (see directButton: image)
popupMarker_scale  Set the scale of the popupMarker                                                scale=x or scale=(x,y,z)
popupMarker_pos    Set the position of the popupMarker relative to the parent optionMenu           pos=(x,y,z)
popupMarker_relief Set the relief value of the popupMarker, the depth of the beveled edge          relief=x (for int value) or relief=None (for no relief)
================== =============================================================================== =======================================================

Example
-------

.. code-block:: python

   import direct.directbase.DirectStart
   from direct.gui.OnscreenText import OnscreenText
   from direct.gui.DirectGui import *
   from panda3d.core import *

   # Add some text
   bk_text = "DirectOptionMenu Demo"
   textObject = OnscreenText(text=bk_text, pos=(0.85, 0.85), scale=0.07,
                             fg=(1, 0.5, 0.5, 1), align=TextNode.ACenter,
                             mayChange=1)

   # Add some text
   output = ""
   textObject = OnscreenText(text=output, pos=(0.95, -0.95), scale=0.07,
                             fg=(1, 0.5, 0.5, 1), align=TextNode.ACenter,
                             mayChange=1)

   # Callback function to set  text
   def itemSel(arg):
       output = "Item Selected is: " + arg
       textObject.setText(output)

   # Create a frame
   menu = DirectOptionMenu(text="options", scale=0.1, command=itemSel,
                           items=["item1", "item2", "item3"], initialitem=2,
                           highlightColor=(0.65, 0.65, 0.65, 1))

   # Run the tutorial
   base.run()

This is a simple demonstration of the DirectOptionMenu.

Dynamic Updating of a Menu
--------------------------

.. code-block:: python

   import direct.directbase.DirectStart
   from direct.gui.OnscreenText import OnscreenText
   from direct.gui.DirectGui import *
   from panda3d.core import *

   # Add some text
   bk_text = "DirectOptionMenu Demo"
   textObject = OnscreenText(text=bk_text, pos=(0.85, 0.85), scale=0.07,
                             fg=(1, 0.5, 0.5, 1), align=TextNode.ACenter,
                             mayChange=1)

   # Add some text
   output = ""
   textObject = OnscreenText(text=output, pos=(0.95, -0.95), scale=0.07,
                             fg=(1, 0.5, 0.5, 1), align=TextNode.ACenter,
                             mayChange=1)

   # Callback function to set text
   def itemSel(arg):
       if arg != "Add":
           # No need to add an element
           output = "Item Selected is: " + arg
           textObject.setText(output)
       else:
           # Add an element
           tmp_menu = menu['items']
           new_item = "item" + str(len(tmp_menu))
           tmp_menu.insert(-1, new_item) #add the element before add
           menu['items'] = tmp_menu
           # Set the status message
           output = "Item Added is: " + new_item
           textObject.setText(output)

   # Create a frame
   menu = DirectOptionMenu(text="options", scale=0.1, initialitem=2,
                           items=["item1", "item2", "item3", "Add"],
                           highlightColor=(0.65, 0.65, 0.65, 1),
                           command=itemSel, textMayChange=1)

   # Procedurally select a item
   menu.set(0)

   # Run the tutorial
   base.run()

In this example we add an item to the menu whenever the Add item is selected.
