.. _creating-windows-and-buffers:

Creating Windows and Buffers
============================

Although Panda does provide the convenience function ``base.openWindow()`` to
create a new window, this function does a lot of things automatically for you
and therefore takes away a lot of control. The following discussion will focus
instead on creating a window using the low-level interface, in order provide a
clearer understanding of the actual class relationships.

In order to create a window, you will first need a GraphicsEngine and a
GraphicsPipe object. Both of these were discussed in more detail in previous
pages. Panda will typically create both of these for you at startup, and store
them in ``base.graphicsEngine`` and ``base.pipe``, respectively.

You will also need to create a FrameBufferProperties object. This defines
important properties such as the number of bits you wish to allocate for red,
green, and blue channels; as well as the number of bits for depth buffer; and
whether you require a stencil buffer or special multisampling bits for
antialiasing. Your graphics card may be able to switch itself into one of
several different configurations, and you can use the FrameBufferProperties to
request certain properties that are more important to you. Note, however, that
there is no guarantee that the graphics card you are running on will be able to
provide everything you ask for (but you can later ask what properties you
actually got). You can get a default FrameBufferProperties object using
``FrameBufferProperties.getDefault()``. The default FrameBufferProperties has
its settings already filled according to the Config.prc file variables; it is
usually a good choice to use.

You will need to create a WindowProperties object as well. At a minimum, this
defines the X, Y size of the window or buffer you want to create. For an
offscreen buffer, this is all it defines; but if you are creating a window, it
also allows you to specify things like the window title, the placement onscreen,
whether it should be user-resizable, and so on. You can get a default
WindowProperties object using ``WindowProperties.getDefault()``. The default
WindowProperties object has its settings filled in according to Config.prc file
variables. If you are creating an offscreen buffer, you may wish to use
``WindowProperties.size(x, y)`` which creates a simple WindowProperties object
that simply requests a buffer of size x y.

Once you have all of these objects, you can create a new window or buffer using
the call graphicsEngine.makeOutput(). This is the fundamental method for
creating a new GraphicsOutput; all of the other convenience functions like
base.makeWindow() or win.makeTextureBuffer() eventually funnel down into this
call. This method accepts several parameters:

.. code-block:: python

   base.graphicsEngine.makeOutput(pipe, name, sort, fb_prop, win_prop, flags, gsg, host)


pipe
   The GraphicsPipe to use to create this output, usually ``base.pipe``.

name
   A string name to assign to this output. Each window and buffer should have a
   name, which makes it easier for you to identify the object in a list. This is
   an internal name only, and has nothing to do with the window title displayed
   above the window.

sort
   The sort order of this output. This determines the order in which the windows
   will be rendered, which is particularly important for offscreen buffers that
   are used to render to textures, which are in turn used in other windows or
   buffers.

fb_prop
   The FrameBufferProperties for this output. If you intend to be sharing GSG’s
   between multiple windows or buffers, it is usually important that they also
   share the same FrameBufferProperties.

win_prop
   The WindowProperties for this output.

flags
   An integer value, a union of several possible bitmask options defined by the
   GraphicsPipe class. This controls the type of GraphicsOutput we are
   requesting, for instance whether we want a window or buffer, or other exotic
   requirements. Set this to ``GraphicsPipe.BFRequireWindow`` if you want to
   create a GraphicsWindow, or to ``GraphicsPipe.BFRefuseWindow`` if you want to
   create a GraphicsBuffer. For more options, see the source code.

gsg
   This parameter is optional, but if provided, it is a GSG to share with other
   windows or buffers. You can get the GSG from an existing window or buffer
   with win.getGsg(). If you omit this parameter, a new GSG will be created.

host
   This parameter is optional, but if provided, it is an already-existing host
   window or buffer. This is useful when creating an offscreen buffer; it allows
   the creation of a **ParasiteBuffer**, if necessary, instead of a true
   GraphicsBuffer object. If you provide a host window, Panda will be able to
   return either a ParasiteBuffer or a GraphicsBuffer, according to what the
   graphics driver is best able to provide.

The return value of ``makeOutput()`` is either the new GraphicsWindow or
GraphicsBuffer object, or None if it failed for some reason.
