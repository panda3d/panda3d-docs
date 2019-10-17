.. _depth-test-and-depth-write:

Depth Test and Depth Write
==========================

Enabling or Disabling the Depth Buffer
--------------------------------------

By default, depth buffer is enabled and functions normally. It is possible to
turn off the use of the depth buffer. It is also possible to alter the behavior
of the depth buffer.

The most common thing to want to do is to disable the depth-write. This means
that geometry will still be tested against the depth buffer, but it will not
affect the depth buffer. This is often used when rendering objects such as
particles that are transparent. To disable or enable the depth-write, use:

.. code-block:: python

   nodePath.setDepthWrite(False)  # Disable
   nodePath.setDepthWrite(True)   # Enable

It may also be desirable to disable the depth-test. This means that the geometry
pays no attention whatsoever to the contents of the depth-buffer. This is often
used for rendering things like heads-up displays, which have no relation to the
3D depth of the scene. To disable or enable the depth-test, use:

.. code-block:: python

   nodePath.setDepthTest(False)  # Disable
   nodePath.setDepthTest(True)   # Enable

One can remove these settings using ``clearDepthTest`` and ``clearDepthWrite``.

Altering the Depth Buffer
-------------------------

Occasionally, it is desirable to alter the functionality of the depth buffer.
Normally, the depth buffer only renders things that are in front, but it can be
made to render things that are in back, or equal. This is rarely used, but it
can be important for certain unusual algorithms like shadow volumes.

To do this, you need to use the DepthTestAttrib directly, in one of the
following variants:

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

Depth Sorting
-------------

When turning depth test off, it is sometimes desirable to use depth sorting
instead. Depth sorting is controlled by the culling system, which can be
controlled by the CullBinAttrib.

Transparency
------------

Certain settings of the TransparencyAttrib can also affect the depth-test.
