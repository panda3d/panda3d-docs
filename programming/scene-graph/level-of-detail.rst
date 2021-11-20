.. _level-of-detail:

Level of Detail
===============

To make a scene look as good as possible, modellers often like to make them very
intricately detailed, which requires a model to consist of a high amount of
polygons. However, if every model in a scene were so highly detailed, Panda3D
would spend a lot of time animating and rendering the scene every frame, causing
the performance to drop.

A common technique to prevent this is to create multiple levels of detail for a
model. A highly detailed version of the model is used when it is close to the
camera, whereas if the model is far away, a lower resolution version is used,
since the detail is not discernable at a great distance anyway.

Another use would be to combine several small objects into a simplified single
object, or to apply a shader that is less costly to render at a greater
distance. LOD can also be used to hide objects when they are far away.

.. only:: cpp

   Include file:

   .. code-block:: cpp

      #include "lodNode.h"

To create an :class:`.LODNode` and :class:`.NodePath`:

.. only:: python

   .. code-block:: python

      lod = LODNode('my LOD node')
      lod_np = NodePath(lod)
      lod_np.reparentTo(render)

.. only:: cpp

   .. code-block:: cpp

      PT(LODNode) lod = new LODNode("my LOD node");
      NodePath lod_np (lod);
      lod_np.reparent_to(render);

To add a level of detail to the LODNode:

.. only:: python

   .. code-block:: python

      lod.addSwitch(50.0, 0.0)
      my_model.reparentTo(lod_np)

.. only:: cpp

   .. code-block:: cpp

      lod->add_switch(50.0, 0.0);
      my_model.reparent_to(lod_np);

my_model can be any NodePath you like.

Note that the first argument is the "far" distance after which this LOD will
disappear, and the second argument is the "near" distance at which it will
appear.

Continue this pattern to add as many levels of detail as you like. For your
lowest level of detail the far distance will be where the model will disappear.
If you would prefer it to stay visible even when very far away then use a
sufficiently large number for the far distance.

Note that the order in which the switches are added must be the same as the
order in which the LODs are reparented to the LODNode's NodePath. This is
important to remember if you are not reparenting the LOD immediately after
adding the switch.
