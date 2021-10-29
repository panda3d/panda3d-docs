.. _compass-effects:

Compass Effects
===============

A CompassEffect causes a node to inherit its rotation (or pos or scale, if
specified) from some other reference node in the graph, or more often from the
root.

In its purest form, a CompassEffect is used to keep the node's rotation fixed
relative to the top of the scene graph, despite other transforms that may exist
above the node. Hence the name: the node behaves like a magnetic compass, always
pointing in the same direction.

As an couple of generalizing extensions, the CompassEffect may also be set up to
always orient its node according to some other reference node than the root of
the scene graph. Furthermore, it may optionally adjust any of pos, rotation, or
scale, instead of necessarily rotation; and it may adjust individual pos and
scale components. (Rotation may not be adjusted on an individual component
basis, that's just asking for trouble.)

Be careful when using the pos and scale modes. In these modes, it's possible for
the CompassEffect to move its node far from its normal bounding volume, causing
culling to fail. If this is an issue, you may need to explicitly set a large (or
infinite) bounding volume on the effect node.

.. only:: python

   .. code-block:: python

      nodePath.setCompass()

.. only:: cpp

   .. code-block:: cpp

      nodePath.set_compass();

If a :class:`.NodePath` is supplied to the :meth:`~.NodePath.set_compass()`
call, it indicates the node to which the rotation will be kept relative (which
is ``render`` by default).
