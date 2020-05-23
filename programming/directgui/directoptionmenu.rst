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
popupMarker_pos    Set the poition of the popupMarker relative to the parent optionMenu            pos=(x,y,z)
popupMarker_relief Set the relief value of the popupMarker, the depth of the beveled edge          relief=x (for int value) or relief=None (for no relief)
================== =============================================================================== =======================================================

Example
-------

.. code-block:: python

   from direct.showbase.ShowBase import ShowBase
   from direct.gui.DirectGui import DirectOptionMenu, OnscreenText
   from panda3d.core import TextNode


   class MyApp(ShowBase):

       def __init__(self):
           ShowBase.__init__(self)

           # Add some text
           self.textObject = OnscreenText(
               text="", pos=(0.95, -0.95),
               scale=0.07, fg=(1, 0.5, 0.5, 1),
               align=TextNode.ACenter, mayChange=1)

           # Create a frame
           menu = DirectOptionMenu(
               text="options",
               scale=0.1,
               command=self.itemSel,
               items=[
                   "item1",
                   "item2",
                   "item3"],
               initialitem=2,
               highlightColor=(
                   0.65,
                   0.65,
                   0.65,
                   1))

       # Callback function to set text
       def itemSel(self, arg):
           self.textObject.setText("Item Selected is: " + arg)


   app = MyApp()
   app.run()

This is a simple demonstration of the DirectOptionMenu.

Dynamic Updating of a Menu
--------------------------

.. code-block:: python

   from direct.showbase.ShowBase import ShowBase
   from direct.gui.DirectGui import DirectOptionMenu, OnscreenText
   from panda3d.core import TextNode


   class MyApp(ShowBase):

       def __init__(self):
           ShowBase.__init__(self)

           # Add some text
           self.textObject = OnscreenText(
               text="", pos=(0.95, -0.95),
               scale=0.07, fg=(1, 0.5, 0.5, 1),
               align=TextNode.ACenter, mayChange=1)

           # Create a frame
           self.menu = DirectOptionMenu(
               text="options", scale=0.1, initialitem=2,
               items=["item1", "item2", "item3", "Add"],
               highlightColor=(0.65, 0.65, 0.65, 1),
               command=self.itemSel, textMayChange=1)

           # Procedurally select a item
           self.menu.set(0)

       # Callback function to set text
       def itemSel(self, arg):
           if arg != "Add":
               # No need to add an element
               output = "Item Selected is: " + arg
               self.textObject.setText(output)
           else:
               # Add an element
               tmp_menu = self.menu['items']
               new_item = "item" + str(len(tmp_menu))
               tmp_menu.insert(-1, new_item)  # add the element before add
               self.menu['items'] = tmp_menu
               # Set the status message
               output = "Item Added is: " + new_item
               self.textObject.setText(output)


   app = MyApp()
   app.run()

In this example we add an item to the menu whenever the Add item is selected.
