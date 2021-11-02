.. _creating-windows-and-buffers:

Creating Windows and Buffers
============================

Although Panda does provide the convenience function :meth:`base.openWindow()`
to create a new window, this function does a lot of things automatically for you
and therefore takes away a lot of control. The following discussion will focus
instead on creating a window using the low-level interface, in order provide a
clearer understanding of the actual class relationships.

In order to create a window, you will first need a :class:`.GraphicsEngine` and
a :class:`.GraphicsPipe` object. Both of these were discussed in more detail in
previous pages. Panda will typically create both of these for you at startup,
and store them in ``base.graphicsEngine`` and ``base.pipe``, respectively.

You will also need to create a :class:`.FrameBufferProperties` object. This
defines important properties such as the number of bits you wish to allocate for
red, green, and blue channels; as well as the number of bits for depth buffer;
and whether you require a stencil buffer or special multisampling bits for
antialiasing. Your graphics card may be able to switch itself into one of
several different configurations, and you can use the FrameBufferProperties to
request certain properties that are more important to you. Note, however, that
there is no guarantee that the graphics card you are running on will be able to
provide everything you ask for (but you can later ask what properties you
actually got). You can get a default FrameBufferProperties object using
:meth:`.FrameBufferProperties.get_default()`. The default FrameBufferProperties
has its settings already filled according to the Config.prc file variables; it
is usually a good choice to use.

You will need to create a :class:`.WindowProperties` object as well. At a
minimum, this defines the X, Y size of the window or buffer you want to create.
For an offscreen buffer, this is all it defines; but if you are creating a
window, it also allows you to specify things like the window title, the
placement onscreen, whether it should be user-resizable, and so on. You can get
a default WindowProperties object using :meth:`.WindowProperties.get_default()`.
The default WindowProperties object has its settings filled in according to
Config.prc file variables. If you are creating an offscreen buffer, you may wish
to use ``WindowProperties(size=(W, H))`` which creates a simple WindowProperties
object that simply requests a buffer of size W×H.

Once you have all of these objects, you can create a new window or buffer using
the call :meth:`.GraphicsEngine.make_output()`. This is the fundamental method
for creating a new :class:`.GraphicsOutput`; all of the other convenience
functions like :py:meth:`base.openWindow()` or :meth:`win.make_texture_buffer()
<.GraphicsOutput.make_texture_buffer>` eventually funnel down into this call.
This method accepts several parameters:

.. only:: python

   .. code-block:: python

      base.graphicsEngine.makeOutput(pipe, name, sort, fb_prop, win_prop, flags, gsg, host)

.. only:: cpp

   .. code-block:: cpp

      GraphicsEngine *engine = GraphicsEngine::get_global_ptr();
      engine->make_output(pipe, name, sort, fb_prop, win_prop, flags, gsg, host);

pipe
   The :class:`.GraphicsPipe` to use to create this output, usually ``base.pipe``.

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
   The :class:`.FrameBufferProperties` for this output. If you intend to be
   sharing GSG’s between multiple windows or buffers, it is usually important
   that they also share the same :class:`.FrameBufferProperties`.

win_prop
   The :class:`.WindowProperties` for this output.

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

The return value of :meth:`~.GraphicsEngine.make_output()` is either the new
:class:`.GraphicsWindow` or :class:`.GraphicsBuffer` object, or None if it
failed for some reason.
