.. _scene-graph-manipulations:

Scene Graph Manipulations
=========================

The default scene graphs
------------------------

By default, there are two different scene graphs created automatically when you
start up Panda3D. These graphs are referred to by their top nodes: render and
render2d.

You use render most often; this is the top of the ordinary 3-D scene. In order
to put an object in the world, you will need to parent it to render (or to some
node that is in turn parented to render).

You will use render2d to render 2-D GUI elements, such as text or buttons, that
you want to display onscreen; for instance, a heads-up display. Anything
parented to render2d will be rendered on top of the 3-D scene, as if it were
painted on the screen glass.

The coordinate system of render2d is set up to match that of the mouse inputs:
the lower-left corner of the screen is (-1, 0, -1), and the upper-right corner
is (1, 0, 1). Since this is a square coordinate system, but the screen is
usually non-square, objects parented directly to render2d may appear squashed.
For this reason, Panda3D also defines a child of render2d, called aspect2d,
which has a scale applied to it to correct the non-square aspect ratio of
render2d. Most often, you will parent GUI elements to aspect2d rather than
render2d.

Specifically, the coordinate system of aspect2d is by default scaled such that x
ranges over [-ratio,ratio], and y ranges over [-1,1] where ratio is
screen_size_x/screen_size_y (in the normal case of a window wider than it is
tall).

There is one more child of render2d to take note of, called pixel2d.
This is scaled in such a way that one Panda unit represents one pixel in the
window. The origin, (0, 0, 0) is in the upper left corner of the window. The
lower right corner has x and z values equal to the width and -height of the
window respectively. As Panda3D uses a Z-Up Right coordinate system, the Y
coordinate in the window will actually be the inverted Z coordinate in Panda.
This node is especially helpful when you want to do pixel-perfect positioning
and scaling.

Finally, you may see references to one other top-level node called
:obj:`~builtins.hidden`. This is simply an ordinary node that has no rendering
properties set up for it, so that things parented to hidden will not be
rendered. Older Panda3D code needed to use hidden to remove a node from the
render scene graph. However, this is no longer necessary, and its use is not
recommended for new programs; the best way to remove a node from render is to
call :meth:`.NodePath.detach_node()`.

Loading models
--------------

You can load up a model with a filename path, in the
:ref:`Panda Filename Syntax <loading-models>`, to the model's egg or bam file.
In many examples, the filename extension is omitted; in this case, Panda will
look for a file with either the .egg or .bam extension.

.. only:: python

   .. code-block:: python

      myNodePath = loader.loadModel("path/to/models/myModel.egg")

.. only:: cpp

   .. code-block:: cpp

      NodePath myNodePath =
        window->load_model(framework.get_models(),"path/to/models/myModel.egg");

The first time you call ``loadModel()`` for a particular model, that model is
read and saved in a table in memory; on each subsequent call, the model is
simply copied from the table, instead of reading the file.

The above call is appropriate for loading static models; for animated models,
see :ref:`loading-actors-and-animations`.

Reparenting nodes and models
----------------------------

One of the most fundamental scene graph manipulations is changing a node's
parent. You need to do this at least once after you load a model, to put it
under render for viewing:

.. only:: python

   .. code-block:: python

      myModel.reparentTo(render)

.. only:: cpp

   .. code-block:: cpp

      myModel.reparent_to(window->get_render());

And to remove it again:

.. only:: python

   .. code-block:: python

      myModel.detachNode()

.. only:: cpp

   .. code-block:: cpp

      myModel.detach_node();

To completely remove a NodePath from the scene graph and memory call the
following, which has the effect of emptying the node and releasing the memory
taken up by the node. Use it only when you have no further use for the node:

.. only:: python

   .. code-block:: python

      myModel.removeNode()

.. only:: cpp

   .. code-block:: cpp

      myModel.remove_node();

As you become more comfortable with scene graph operations, you may find
yourself taking more and more advantage of a deeply nested scene graph, and you
may start to parent your models to other nodes than just render. Sometimes it is
convenient to create an empty node for this purpose, for instance, to group
several models together:

.. only:: python

   .. code-block:: python

      dummyNode = render.attachNewNode("Dummy Node Name")
      myModel.reparentTo(dummyNode)
      myOtherModel.reparentTo(dummyNode)

.. only:: cpp

   .. code-block:: cpp

      NodePath dummyNode = window->get_render().attach_new_node("Dummy Node Name");
      myModel.reparent_to(dummyNode);
      myOtherModel.reparent_to(dummyNode);

Since a node inherits its position information from its parent node, when you
reparent a node in the scene graph you might inadvertently change its position
in the world. If you need to avoid this, you can use a special variant on
:meth:`~.NodePath.reparent_to()`:

.. only:: python

   .. code-block:: python

      myModel.wrtReparentTo(newParent)

.. only:: cpp

   .. code-block:: cpp

      myModel.wrt_reparent_to(newParent);

The "wrt" prefix stands for "with respect to". This special method works like
:meth:`~.NodePath.reparent_to()`, except that it automatically recomputes the
local transform on myModel to compensate for the change in transform under the
new parent, so that the node ends up in the same position relative to the world.

Note that the computation required to perform
:meth:`~.NodePath.wrt_reparent_to()` is a floating-point matrix computation and
is therefore inherently imprecise. This means that if you use
:meth:`~.NodePath.wrt_reparent_to()` repeatedly, thousands of times on the same
node, it may eventually accumulate enough numerical inaccuracies to introduce a
slight scale on the object (for instance, a scale of 1, 1, 0.99999); if left
unchecked, this scale could eventually become noticeable.

Beginners tend to overuse this method; you should not use
:meth:`~.NodePath.wrt_reparent_to()` unless there is a real reason to use it.
