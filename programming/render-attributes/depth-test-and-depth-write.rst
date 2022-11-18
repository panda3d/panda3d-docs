.. _depth-test-and-depth-write:

Depth Test and Depth Write
==========================

Enabling or Disabling the Depth Buffer
--------------------------------------

By default, Panda3D renders the `render` scene graph with Z-buffering enabled.
This technique makes it possible to render overlapping geometry in arbitrary
order without having rear surfaces appear on top of front surfaces. It is
possible to disable the depth buffer or alter its behavior.

In the 2D scene graph `render2d`, the depth buffer is disabled by default,
because it is used for GUI and not for self-overlapping 3D models. But in rare
cases, it is desirable to show 3D models in the 2D scene graph, so it is
possible to enable the depth buffer for those models specifically.

The most common thing to want to do is to disable the depth-write. This means
that geometry will still be tested against the depth buffer, but it will not
affect the depth buffer. This is often used when rendering objects such as
particles that are transparent. To disable or enable the depth-write, use:

.. only:: python

   .. code-block:: python

      nodePath.setDepthWrite(False)  # Disable
      nodePath.setDepthWrite(True)   # Enable

.. only:: cpp

   .. code-block:: cpp

      nodePath.set_depth_write(false);  // Disable
      nodePath.set_depth_write(true);   // Enable

It may also be desirable to disable the depth-test. This means that the geometry
pays no attention whatsoever to the contents of the depth-buffer. This is often
used for rendering things like heads-up displays, which have no relation to the
3D depth of the scene. To disable or enable the depth-test, use:

.. only:: python

   .. code-block:: python

      nodePath.setDepthTest(False)  # Disable
      nodePath.setDepthTest(True)   # Enable

.. only:: cpp

   .. code-block:: cpp

      nodePath.set_depth_test(false);  // Disable
      nodePath.set_depth_test(true);   // Enable

One can remove these settings using :meth:`~.NodePath.clear_depth_test()` and
:meth:`~.NodePath.clear_depth_write()`.

Altering the Depth Buffer
-------------------------

Occasionally, it is desirable to alter the functionality of the depth buffer.
Normally, the depth buffer only renders things that are in front, but it can be
made to render things that are in back, or equal. This is rarely used, but it
can be important for certain unusual algorithms like shadow volumes.

To do this, you need to use the :class:`.DepthTestAttrib` directly, in one of
the following variants:

.. only:: python

   .. code-block:: python

      nodePath.setAttrib(DepthTestAttrib.make(RenderAttrib.MNone))
      nodePath.setAttrib(DepthTestAttrib.make(RenderAttrib.MNever))
      nodePath.setAttrib(DepthTestAttrib.make(RenderAttrib.MLess))
      nodePath.setAttrib(DepthTestAttrib.make(RenderAttrib.MEqual))
      nodePath.setAttrib(DepthTestAttrib.make(RenderAttrib.MLessEqual))
      nodePath.setAttrib(DepthTestAttrib.make(RenderAttrib.MGreater))
      nodePath.setAttrib(DepthTestAttrib.make(RenderAttrib.MGreaterEqual))
      nodePath.setAttrib(DepthTestAttrib.make(RenderAttrib.MNotEqual))
      nodePath.setAttrib(DepthTestAttrib.make(RenderAttrib.MAlways))

.. only:: cpp

   .. code-block:: cpp

      nodePath.set_attrib(DepthTestAttrib::make(RenderAttrib::M_none));
      nodePath.set_attrib(DepthTestAttrib::make(RenderAttrib::M_never));
      nodePath.set_attrib(DepthTestAttrib::make(RenderAttrib::M_less));
      nodePath.set_attrib(DepthTestAttrib::make(RenderAttrib::M_equal));
      nodePath.set_attrib(DepthTestAttrib::make(RenderAttrib::M_less_equal));
      nodePath.set_attrib(DepthTestAttrib::make(RenderAttrib::M_greater));
      nodePath.set_attrib(DepthTestAttrib::make(RenderAttrib::M_greater_equal));
      nodePath.set_attrib(DepthTestAttrib::make(RenderAttrib::M_not_equal));
      nodePath.set_attrib(DepthTestAttrib::make(RenderAttrib::M_always));

Depth Sorting
-------------

When turning depth test off, it is sometimes desirable to use depth sorting
instead. Depth sorting is controlled by the culling system, which can be
controlled by the :class:`.CullBinAttrib`.

Transparency
------------

Certain settings of the :class:`.TransparencyAttrib` can also affect the
depth-test.
