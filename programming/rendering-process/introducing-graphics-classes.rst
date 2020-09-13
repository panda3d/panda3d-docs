.. _introducing-graphics-classes:

Introducing Graphics Classes
============================

GraphicsEngine
--------------

The :class:`.GraphicsEngine` is where it all begins. There is only one, global,
GraphicsEngine in an application, and its job is to keep all of the pointers to
your open windows and buffers, and also to manage the task of doing the
rendering, for all of the open windows and buffers. Panda normally creates a
GraphicsEngine for you at startup, which is available as
``base.graphicsEngine``. There is usually no reason to create a second
GraphicsEngine.

GraphicsPipe
------------

Each application will also need at least one :class:`.GraphicsPipe`. The
GraphicsPipe encapsulates the particular API used to do rendering. For instance,
there is one GraphicsPipe class for OpenGL rendering, and a different
GraphicsPipe for DirectX. Although it is possible to create a GraphicsPipe of a
specific type directly, normally Panda will create a default GraphicsPipe for
you at startup, which is available in ``base.pipe``.

The GraphicsPipe object isn't often used directly, except to create the
individual GraphicsWindow and GraphicsBuffer objects.

GraphicsWindow and GraphicsBuffer
---------------------------------

The :class:`.GraphicsWindow` class is the class that represents a single
onscreen window for rendering. Panda normally opens a default window for you at
startup, which is available in ``base.win``. You can create as many additional
windows as you like. (Note, however, that some graphics drivers incur a
performance penalty when multiple windows are open simultaneously.)

Similarly, :class:`.GraphicsBuffer` is the class that represents a hidden,
offscreen buffer for rendering special offscreen effects, such as
render-to-texture. It is common for an application to have many offscreen
buffers open at once.

Both classes inherit from the base class :class:`.GraphicsOutput`, which
contains all of the code common to rendering to a window or offscreen buffer.

GraphicsStateGuardian
---------------------

The :class:`.GraphicsStateGuardian`, or GSG for short, represents the actual
graphics context. This class manages the actual nuts-and-bolts of drawing to a
window; it manages the loading of textures and vertex buffers into graphics
memory, and has the functions for actually drawing triangles to the screen.
(During the process of rendering the frame, the "graphics state" changes several
times; the GSG gets its name from the fact that most of its time is spent
managing this graphics state.)

You would normally never call any methods on the GSG directly; Panda handles all
of this for you, via the GraphicsEngine. This is important, because in some
modes, the GSG may operate almost entirely in a separate thread from all of your
application code, and it is important not to interrupt that thread while it
might be in the middle of drawing.

Each :class:`.GraphicsOutput` object keeps a pointer to the GSG that will be
used to render that window or buffer. It is possible for each GraphicsOutput to
have its own GSG, or it is possible to share the same GSG between multiple
different GraphicsOutputs. Normally, it is preferable to share GSG's, because
this tends to be more efficient for managing graphics resources.

Consider the following diagram to illustrate the relationship between these
classes. This shows a typical application with one window and two offscreen
buffers:

.. digraph:: inheritance

   rankdir=TB
   node [shape=box];

   subgraph cluster {
      style=solid;
      pipe [label="GraphicsPipe"];
      output1 [label="GraphicsOutput\n(window)"];
      output2 [label="GraphicsOutput\n(buffer)"];
      output3 [label="GraphicsOutput\n(buffer)"];
      gsg1 [label="GSG"];
      gsg2 [label="GSG"];
      gsg3 [label="GSG"];
      label="GraphicsEngine";
   }

   pipe -> output1;
   pipe -> output2;
   pipe -> output3;

   output1 -> gsg1;
   output2 -> gsg2;
   output3 -> gsg3;

The GraphicsPipe was used to create each of the three GraphicsOutputs, of which
one is a GraphicsWindow, and the remaining two are GraphicsBuffers. Each
GraphicsOutput has a pointer to the GSG that will be used for rendering.
Finally, the GraphicsEngine is responsible for managing all of these objects.

In the above illustration, each window and buffer has its own GSG, which is
legal, although it's usually better to share the same GSG across all open
windows and buffers.
