.. _the-rigid-body-combiner:

The Rigid Body Combiner
=======================

When you are developing a complex game, you will most likely run into the
problem that you will have :ref:`too many meshes <too-many-meshes>` in your
scene. Panda3D's flattening methods can help you reducing the number of nodes,
but often when you have hundreds of moving bodies this is not always an option.
Therefore, Panda3D has a feature to help you reduce the number of nodes, even if
they are moving: the :class:`.RigidBodyCombiner`.

The RigidBodyCombiner is designed to reduce the number of nodes actually sent to
the graphics card, just like the flattening functions. But instead of flattening
everything into one node immediately, the RigidBodyCombiner keeps your original
node structure intact, still allowing you to apply transforms (e.g. moving
around, rotating or scaling) sub-nodes. But what's actually sent to the graphics
cards is just one node, a combined version of all these sub-nodes. If you want
to see the combined version of these nodes (not likely), you can call
:meth:`~.RigidBodyCombiner.get_internal_scene()`, this function will return the
NodePath that is actually sent to the graphics card.

The RigidBodyCombiner class is just another kind of :class:`.PandaNode`. All of
the standard node interfaces apply. Thus, the easiest way to add nodes to a
RigidBodyCombiner is to wrap a :class:`.NodePath` around it, and then use the
standard :meth:`~.NodePath.reparent_to()` interfaces to parent the nodes you
want to combine to this NodePath.

When you are done with reparenting the nodes, you need to call
:meth:`~.RigidBodyCombiner.collect()` on the original
:class:`.RigidBodyCombiner` instance. This is a fairly expensive call and you
should normally only call this once -- but after you called
:meth:`~.RigidBodyCombiner.collect()` you may freely transform all nodes below
without having to call this again. If you later add more children to the RBC,
though, you will need to call :meth:`~.RigidBodyCombiner.collect()` again.

The vertices of the objects you attach to the RigidBodyCombiner must be
transformed each frame on the CPU. For this reason, you may find a performance
advantage in limiting the number of vertices in the models you use. Also, be
sure you do not have normals on your models unless you are actually using
lighting.

.. only:: python

   Here is a small example showing a random cloud of boxes:

   .. code-block:: python

      from direct.directbase.DirectStart import *
      from panda3d.core import RigidBodyCombiner, NodePath, Vec3
      import random

      rbc = RigidBodyCombiner("rbc")
      rbcnp = NodePath(rbc)
      rbcnp.reparentTo(render)

      for i in range(200):
          pos = Vec3(random.uniform(-100, 100),
                     random.uniform(-100, 100),
                     random.uniform(-100, 100))

          f = loader.loadModel("box.egg")
          f.setPos(pos)
          f.reparentTo(rbcnp)

      rbc.collect()
      base.run()

.. note::

   :ref:`RenderEffects <render-effects>` such as
   :ref:`Billboards <billboard-effects>` are not supported below this node.

For more information and a complete list of RigidBodyCombiner methods please see
the :class:`~panda3d.core.RigidBodyCombiner` page in the API Reference.
