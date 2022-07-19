.. _low-level-render-to-texture:

Low-Level Render to Texture
===========================

Render to Texture Basics
------------------------

In Panda3D, rendering to a texture consists of three basic steps:

-  Create a hidden window (class :class:`.GraphicsBuffer`).
-  Render into the hidden window.
-  Transfer the contents of the hidden window into a texture.

When I say "transfer" the contents of a window into a texture, I don't
necessarily mean "copy." There are other ways to transfer the contents of a
window into a texture that may be faster. For example, if the OpenGL
implementation supports the ARB_pbuffers extension, then the transfer might be
achieved using wglBindTexImageARB. The Panda user does not need to worry about
how the transfer is done. It is only important that you know that Panda will use
the fastest means available to transfer the contents of the window into the
texture.

To generalize that a bit, although render-to-texture is usually done with a
hidden window (class :class:`.GraphicsBuffer`), it can also be done with a
visible window (class :class:`.GraphicsWindow`). You can transfer the contents
of any window, hidden or not, into a texture. That's potentially useful - for
example, you can transfer the contents of the main window into a texture, which
you can then use when rendering the next frame. This can be used to create
accumulation-buffer-like effects without an accumulation buffer.

The Simple API
--------------

Here is a short snippet of code that creates a hidden window, creates a camera
that renders into that window, and creates a scene graph for that camera:

.. only:: python

   .. code-block:: python

      mybuffer = base.win.makeTextureBuffer("My Buffer", 512, 512)
      mytexture = mybuffer.getTexture()
      mybuffer.setSort(-100)
      mycamera = base.makeCamera(mybuffer)
      myscene = NodePath("My Scene")
      mycamera.reparentTo(myscene)

.. only:: cpp

   .. code-block:: cpp

      PT(GraphicsOutput) mybuffer;
      PT(Texture) mytexture;
      PT(Camera) mycamera;
      PT(DisplayRegion) region;
      NodePath mycameraNP;
      NodePath myscene;

      mybuffer = window->get_graphics_output()->make_texture_buffer("My Buffer", 512, 512);
      mytexture = mybuffer->get_texture();
      mybuffer->set_sort(-100);
      mycamera = new Camera("my camera");
      mycameraNP = window->get_render().attach_new_node(mycamera);
      region = mybuffer->make_display_region();
      region->set_camera(mycameraNP);
      myscene = NodePath("My Scene");
      mycameraNP.reparent_to(myscene)

The :meth:`~.GraphicsOutput.make_texture_buffer()` is the simple interface to
the render-to-texture functionality. It creates a new hidden window (usually a
:class:`.GraphicsBuffer`), creates a texture to render into, and connects the
texture to the hidden window. The (512, 512) in the function call specifies the
size of the hidden window and texture. Of course, you need to use a power-of-two
size. You can specify (0, 0) to automatically inherit the size of the parent
window. The :meth:`~.GraphicsOutput.get_texture()` method retrieves the texture,
which will be rendered into every frame.

The :meth:`~.GraphicsOutput.set_sort()` method sets a window's sort order. This
controls the order in which panda renders the various windows. The main window's
sort order is zero. By setting the sort order of mybuffer to a negative number,
we ensure that mybuffer will be rendered first. That, in turn, ensures that
mytexture will be ready to use by the time that the main window is rendered.

The new hidden window is not automatically connected to the scene graph. In this
example, we create a separate scene graph rooted at myscene, create a camera to
view that scene graph, and connect the camera to mybuffer.

The function :meth:`~.GraphicsOutput.make_texture_buffer()` usually creates a
GraphicsBuffer (hidden window), but if the video card is not powerful enough to
create an offscreen window, it may not be able to do so. In that case,
:meth:`~.GraphicsOutput.make_texture_buffer()` will create a *parasite buffer*
instead. A parasite buffer is primarily a trick to emulate a GraphicsBuffer on
video cards that are less powerful. The trick is this: instead of rendering to
an offscreen window and then transferring the data into a texture, panda renders
into the main window and then copies the data into the texture. The limitations
of this trick are self-evident. First, it garbles the contents of the main
window. This is usually no big deal, since the main window is usually cleared
and rendered from scratch every frame anyway. The other problem with this trick
is that it fails if the main window is smaller than the desired texture. Since
neither of these problems is common in practice,
:meth:`~.GraphicsOutput.make_texture_buffer()` will use parasite buffers
transparently if GraphicsBuffers are not available.

.. only:: python

   There is a debugging mode in which
   :meth:`~.GraphicsOutput.make_texture_buffer()` will create a visible window
   (class :class:`.GraphicsWindow`) instead of a hidden one (class
   :class:`.GraphicsBuffer`). To enable this debugging mode, set the boolean
   variable "show-buffers #t" in your panda configuration file.

The Advanced API
----------------

The simple API is convenient, but there are a few things it can not do. For
instance, it can not:

-  Copy the main window into a texture.
-  Copy the Z-buffer into a depth texture.
-  Copy the window into a texture, but not every frame.
-  Limit or force the use of Parasite buffers.

If you need this level of control, you need to use a lower-level API. The
low-level function that is called for the creation of all buffers and windows
is :meth:`~.GraphicsEngine.make_output()` on the :class:`.GraphicsEngine` class.

.. only:: python

   .. code-block:: python

      # Request 8 RGB bits, no alpha bits, and a depth buffer.
      fb_prop = FrameBufferProperties()
      fb_prop.setRgbColor(True)
      fb_prop.setRgbaBits(8, 8, 8, 0)
      fb_prop.setDepthBits(16)

      # Create a WindowProperties object set to 512x512 size.
      win_prop = WindowProperties(size=(512, 512))

      # Don't open a window - force it to be an offscreen buffer.
      flags = GraphicsPipe.BF_refuse_window

      base.graphicsEngine.make_output(base.pipe, "My Buffer", -100, fb_prop, win_prop, flags, base.win.getGsg(), base.win)

.. only:: cpp

   .. code-block:: cpp

      // Request 8 RGB bits, no alpha bits, and a depth buffer.
      FrameBufferProperties fb_prop;
      fb_prop.set_rgb_color(true);
      fb_prop.set_rgba_bits(8, 8, 8, 0);
      fb_prop.set_depth_bits(16);

      // Create a WindowProperties object set to 512x512 size.
      WindowProperties win_prop;
      win_prop.set_size(512, 512);

      // Don't open a window - force it to be an offscreen buffer.
      int flags = GraphicsPipe::BF_refuse_window;

      GraphicsEngine *engine = GraphicsEngine::get_global_ptr();
      engine->make_output(pipe, "My Buffer", -100, fb_prop, win_prop, flags, win->get_gsg(), win);

The method takes a :class:`.FrameBufferProperties` object describing the
requested amount of bits that are available in GPU memory, as well as a
WindowProperties object describing the properties of the window to be opened. In
the case of an offscreen buffer, which is acquired by passing BF_refuse_window
as a flag, only the size setting of the WindowProperties object is used.

Offscreen buffers may require passing in a host window and a host GSG, since the
graphics API may require an existing graphics context in order to create an
offscreen buffer. When creating a window, the last two parameters may be
omitted.

For the meaning of the various flags, consult the GraphicsPipe API
documentation.

Several of the :ref:`Sample Programs <samples>` use the lower-level API.
