.. _bullet-faq:

Bullet FAQ
==========

This page contains answers to often asked question and elaborations on
different topics related to the Bullet Panda3D module.

Bullet and Scale
----------------

When using physics it is always better to avoid scale wherever possible.
However, the Bullet module does it's best to support setting scale on
RigidBodyNode, GhostNode etc. Shear is not supported at all.

If you know the dimensions of a Bullet collision shape at the time of creation
then create it with those dimensions, and don't use scale to adjust the
dimensions afterwards. For example, if you need a box with extents 5x3x1 then
create it with these extents, and not with extents 1x1x1 and then scale it
with ``Vec3(5, 3, 1)``.

If you have convex meshes or triangle meshes then it is better to "bake" the
scale before creating the collision shape. Baking means to apply the scale to
all vertices first, and then pass the scaled vertex positions to the convex or
triangle mesh shape. This can be done before exporting your model from your
modelling application, or in code after loading the model.

Please note that the effective scale applied to a Bullet collision shape is
the global scale of the node, that is the scale component of the global
transform of this node. So if you have the scene graph "A" --> "B" --> "C",
then the effective scale of the node "C" is the scale set on "A" times the
scale set on "B" times the scale set on "C".
