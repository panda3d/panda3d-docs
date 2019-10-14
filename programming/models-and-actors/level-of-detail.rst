.. _level-of-detail:

Level of Detail
===============

Using multiple levels of detail for a part of your scene can help improve
performance. For example you could use LOD to simplify an Actor that is far
away, saving on costly vertex skinning operations. Another use would be to
combine several small objects into a simplified single object, or to apply a
cheaper shader. LOD can also be used to hide objects when they are far away.

.. only:: cpp

    Include file:

    .. code-block:: cpp

        #include "lodNode.h"

To create an LODNode and NodePath:

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
lowest level of LOD the far distance will be where the model will disappear.
If you would prefer it to stay visible even when very far away then use a
sufficiently large number for the far distance.

Note that the order in which the switches are added must be the same as the
order in which the LODs are reparented to the LODNode's NodePath. This is
important to remember if you are not reparenting the LOD immediately after
adding the switch.
