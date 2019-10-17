.. _creating-new-mousewatchers-for-display-regions:

Creating New MouseWatchers for Display Regions
==============================================

When working with multiple display regions in a single window, it can be
difficult to get accurate mouse interaction. base.mouseWatcherNode, the default
MouseWatcher in Panda3D, reports the mouse coordinates for the entire window. To
get mouse coordinates relative to a specific display region the MouseWatcher
needs to be restricted to that region with the setDisplayRegion() method.

.. code-block:: python

   myDR = base.win.makeDisplayRegion(0, 1, 0, 1)
   base.mouseWatcherNode.setDisplayRegion(myDR)

However, restricting the default MouseWatcher to a display region will prevent
the mouse from being used outside of that region. For example, the image below
shows two display regions, a 3D view in the top portion, and a menu in the
bottom portion.

.. image:: displayregionmousewatcher.png

If base.mouseWatcherNode is restricted to the 3D view display region, the mouse
won't interact with the menu buttons.

One way to get around this problem is to create a new MouseWatcher to handle the
3D view display region. By doing so, the mouse can interact with other display
regions, such as the one containing the menu, and the program can still get
accurate mouse coordinates for the 3D view display region for things like
:ref:`clicking-on-3d-objects` which is discussed later in the manual.

Creating a new MouseWatcher and tying it to a display region is a three step
process. First, the new MouseWatcher has to be created.

.. code-block:: python

   myMouseWatcher = MouseWatcher()
   # Creates a new mouse watcher

In order for the new MouseWatcher to do its job, it needs to receive information
about the mouse from the system. This information comes from the
MouseAndKeyboard object. To get the information, our new MouseWatcher needs to
be a child of MouseAndKeyboard. We know that base.mouseWatcherNode is already a
child of MouseAndKeyboard, so we can use that to our advantage to make our new
MouseWatcher a child of it as well.

.. code-block:: python

   base.mouseWatcher.getParent().attachNewNode(myMouseWatcher)
   # Gets MouseAndKeyboard, the parent of base.mouseWatcherNode
   # that passes mouse data into MouseWatchers,
   # and attaches myMouseWatcher to it.

Now that our MouseWatcher is getting mouse information from the system, we just
need to set it to the display region we want it to monitor.

.. code-block:: python

   myMouseWatcher.setDisplayRegion(myDisplayRegion)
   # Restricts my MouseWatcher to my intended display region.

With that done, we can get accurate mouse coordinates within the display
region from our new MouseWatcher.

.. code-block:: python

   if myMouseWatcher.hasMouse():
       mpos = myMouseWatcher.getMouse()
