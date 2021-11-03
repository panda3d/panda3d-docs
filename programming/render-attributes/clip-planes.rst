.. _clip-planes:

Clip Planes
===========

A clip plane fundamentally divides space into two halves: one half which is
clipped (hidden from rendering), and one half which is rendered.

A common use case is when rendering reflections of flat mirror surfaces (such as
water), to ensure that a camera that is rendering the reflected scene will only
render the part of the scene that is above the surface of the mirror.

It is possible to have multiple clip planes enabled at the same time. This will
cause multiple areas to be culled away. There is an implementation-specific
limit on the number of clip planes that can be active at any one time.

A plane is defined by four coordinates. The first three represent the X, Y, Z
of the plane's surface normal. The last parameter is used to determine the
origin point of the plane. You can create a plane either using three points,
or by using a normal vector and an origin point:

.. only:: python

   .. code-block:: python

      # Create a plane going through these three points
      plane = Plane((100, 0, 2), (100, 100, 2), (0, 100, 2))

      # Create an identical plane pointing upward with a height of 2
      plane = Plane((0, 0, 1), (0, 0, 2))

      # Create the same plane by directly specifying its parameters
      plane = Plane(0, 0, 1, -2)

.. only:: cpp

   .. code-block:: cpp

      // Create a plane going through these three points
      LPlane plane((100, 0, 2), (100, 100, 2), (0, 100, 2));

      // Create an identical plane pointing upward with a height of 2
      LPlane plane((0, 0, 1), (0, 0, 2));

      // Create the same plane by directly specifying its parameters
      LPlane plane(0, 0, 1, -2);

Before we can use it as a clip plane, we need to place it in the scene graph.
This is done by creating a :class:`.PlaneNode`:

.. only:: python

   .. code-block:: python

      plane = Plane(0, 0, 1, -2)
      plane_node = PlaneNode("plane", plane)
      plane_np = render.attach_new_node(plane_node)

.. only:: cpp

   .. code-block:: cpp

      LPlane plane(0, 0, 1, -2);
      PT(PlaneNode) plane_node = new PlaneNode("plane", plane);
      NodePath plane_np = render.attach_new_node(plane_node);

To see a debug representation of the plane, call :meth:`~.NodePath.show()` on
the resulting node path.

Finally, we can use :meth:`~.NodePath.set_clip_plane()` in order to apply it to
any node on which the clipping should take effect:

.. only:: python

   .. code-block:: python

      render.setClipPlane(plane_np)

.. only:: cpp

   .. code-block:: cpp

      render.set_clip_plane(plane_np);

Internally, this will create a :class:`.ClipPlaneAttrib` and assign it to the
node's render state.

.. only:: python

   This is a complete sample program showing a teapot that is being affected by
   two clip planes:

   .. code-block:: python

      from direct.showbase.ShowBase import ShowBase
      from panda3d.core import *

      base = ShowBase()

      teapot = loader.loadModel("models/teapot")
      teapot.setScale(10)
      teapot.reparentTo(render)

      plane1 = Plane((0, 0, 1), (0, 0, 5))
      plane1_np = render.attachNewNode(PlaneNode("plane1", plane1))
      plane1_np.show()
      teapot.setClipPlane(plane1_np)

      plane2 = Plane((1, 0, 0), (-10, 0, 0))
      plane2_np = render.attachNewNode(PlaneNode("plane2", plane2))
      plane2_np.show()
      teapot.setClipPlane(plane2_np)

      base.cam.setPos(10, -200, 30)
      base.run()

.. note::

   Clip planes work normally in the fixed-function pipeline and with the shader
   generator, but if you are using a custom shader, it is your responsibility to
   implement the effect of the clip planes. In GLSL shaders, you can use the
   built-in ``p3d_ClipPlane[]`` input, which contains the view-space coordinates
   of each active plane. One way to implement it is to put something like this
   in the fragment shader:

   .. code-block:: glsl

      uniform vec4 p3d_ClipPlane[2];

      // View-space vertex position passed in from vertex shader
      in vec4 vpos;

      void main() {
        if (dot(p3d_ClipPlane[0], vpos) < 0) {
          discard;
        }
        if (dot(p3d_ClipPlane[1], vpos) < 0) {
          discard;
        }

        // Rest of fragment shader
      }
