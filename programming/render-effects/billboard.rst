.. _billboard-effects:

Billboard Effects
=================

A billboard is a special effect that causes a node to rotate automatically to
face the camera, regardless of the direction from which the camera is looking.
It is usually applied to a single textured polygon representing a complex object
such as a tree. Judicious use of billboards can be an effective way to create a
rich background environment using very few polygons.

Panda indicates that a node should be billboarded to the camera by storing a
BillboardEffect on that node. Normally, you do not need to create a
BillboardEffect explicitly, since there are a handful of high-level methods on
NodePath that will create one for you:

.. only:: python

   .. code-block:: python

      myNodePath.setBillboardAxis()
      myNodePath.setBillboardPointWorld()
      myNodePath.setBillboardPointEye()

.. only:: cpp

   .. code-block:: cpp

      myNodePath.set_billboard_axis();
      myNodePath.set_billboard_point_world();
      myNodePath.set_billboard_point_eye();

Each of the above calls is mutually exclusive; there can be only one kind of
billboard effect on a node at any given time. To undo a billboard effect, use:

.. only:: python

   .. code-block:: python

      myNodePath.clearBillboard()

.. only:: cpp

   .. code-block:: cpp

      myNodePath.clear_billboard();

The most common billboard type is an axial billboard, created by the
``setBillboardAxis()`` method. This kind of billboard is constrained to rotate
around its vertical axis, so is usually used to represent objects that are
radially symmetric about the vertical axis (like trees).

Less often, you may need to use a point billboard, which is free to rotate about
any axis. There are two varieties of point billboard. The world-relative point
billboard always keeps its up vector facing up, i.e. along the Z axis, and is
appropriate for objects that are generally spherical and have no particular axis
of symmetry, like clouds. The eye-relative point billboard, on the other hand,
always keeps its up vector towards the top of the screen, no matter which way
the camera tilts, and is usually used for text labels that float over objects in
the world.

There are several more options available on a BillboardEffect, but these are
rarely used. If you need to take advantage of any of these more esoteric
options, you must create a BillboardEffect and apply it to the node yourself:

.. code-block:: python

   myEffect = BillboardEffect.make(
       upVector=vec3,
       eyeRelative=bool,
       axialRotate=bool,
       offset=float,
       lookAt=nodepath,
       lookAtPoint=point3
   )
   myNodePath.node().setEffect(myEffect)
