.. _clearing-display-regions:

Clearing Display Regions
========================

When you have more than one DisplayRegion in a particular window, it is
important to consider which of them, if any, you want to perform an explicit
clear operation before drawing.

Clearing means to erase the contents of the window or DisplayRegion, and set it
all to the background color. Normally, you should perform a clear at the
beginning of every frame, or you will be drawing the new frame on top of the
contents of the previous frame.

The default is for clear to be performed by the GraphicsOutput (the window or
buffer), before any DisplayRegions are drawn at all. This is usually the best
way to clear the window, because it is slightly faster to perform one big clear
operation that resets the whole window at once, rather than clearing each
DisplayRegion individually. This particularly makes sense when your
DisplayRegions don't overlap, and they all want to have the same background
color, like this:

.. image:: quaddr.jpg

However, when your DisplayRegions overlap, or when they each need to have a
different background color, you may need to clear the DisplayRegions
individually. Consider the following example:

.. image:: displayregion-3.jpg

Panda must draw this scene by first clearing the window to a gray background,
then drawing the contents of the larger display region (with the panda), then
clearing the smaller, nested display region to a black background, and then
finally drawing the contents of the smaller display region.

You can control the clear operations per DisplayRegion, as well as on the
overall GraphicsOutput. The following methods are defined for both
DisplayRegions and GraphicsOutputs:

.. only:: python

   .. code-block:: python

      win.setClearColorActive(flag)
      win.setClearColor((r, g, b, a))

.. only:: cpp

   .. code-block:: cpp

      win->set_clear_color_active(flag);
      win->set_clear_color(LVecBase4(r, g, b, a));

In the above, flag is a boolean flag--True or False, indicating whether this
window or DisplayRegion should perform a clear to the background color. If
False, no clear will be performed. If True, the color will be cleared before
drawing, and the specific background color used will be specified by r, g, b,
a.

In addition to clearing the color, you will also need to clear the depth or Z
buffer. This buffer is used to determine which objects are in front of other
objects, and if you fail to clear it, some objects may not draw. It has a
similar interface:

.. only:: python

   .. code-block:: python

      win.setClearDepthActive(flag)
      win.setClearDepth(depthValue)

.. only:: cpp

   .. code-block:: cpp

      win->set_clear_depth_active(flag);
      win->set_clear_depth(depthValue);

The depthValue should almost always be 1.0, which is the default.

It is also possible to selectively clear the stencil buffer, and other auxiliary
buffers, in a similar way. See the generated API docs for
:class:`.DrawableRegion` for more information.

Sorting
-------

Note that when you are overlapping DisplayRegions, it becomes very important to
specify the order in which the DisplayRegions should be drawn. To do this, use
:meth:`~.DisplayRegion.set_sort()`:

.. only:: python

   .. code-block:: python

      dr.setSort(sortValue)

.. only:: cpp

   .. code-block:: cpp

      dr->set_sort(sortValue);

The sortValue can be any integer number; the default is zero. All DisplayRegions
for a particular window will be drawn in order from smallest sort first to
largest sort last. If two DisplayRegions have the same sort value, the order in
which they are drawn is undefined.
