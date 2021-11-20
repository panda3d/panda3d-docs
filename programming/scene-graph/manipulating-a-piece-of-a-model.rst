.. _manipulating-a-piece-of-a-model:

Manipulating a Piece of a Model
===============================

Every model, when loaded, becomes a :class:`~.ModelNode` in the scene graph.
Beneath the :class:`~.ModelNode` are one or more :class:`GeomNodes <.GeomNode>`
containing the actual polygons. If you want to manipulate a piece of a model,
for instance, if you want to change the texture of just part of a model, you
need a pointer to the relevant GeomNode.

In order to obtain such a pointer, you must first ensure that the relevant
geometry is in a :class:`~.GeomNode` of its own (and not merged with all the
other geometry). In other words, you must ensure that panda's optimization
mechanisms do not cause the geometry to be merged with the geometry of the rest
of the model. While normally this optimization is a good thing, if you want to
change textures on a specific part of the model (for example, just a character's
face) you will need this geometry to be separate.

There are two different ways that you should do this, according to the type of
model it is.

Animated (skeleton animation) models
------------------------------------

If your model is animated via keyframe animation in a package such as 3DSMax
or Maya--that is, the sort of model you expect to load in via the
:ref:`Actor <animated-models>` interface--then Panda will be aggressive in
combining all of the geometry into as few nodes as possible. In order to mark
particular geometry to be kept separate, you should use the ``egg-optchar``
program.

The name "optchar" is short for "optimize character", since the egg-optchar
program is designed to optimize an animated character for runtime performance by
removing unused and unneeded joints. However, in addition to this optimization,
it also allows you to label a section of a model for later manipulation. Once
you have labeled a piece of geometry, Panda's optimization mechanisms will not
fold it in to the rest of the model.

Your first step is to note the name of the object in your modeling program. For
example, suppose you want to control the texture of a model's head, and suppose
(hypothetically) the head is labeled "Sphere01" in your modeling program. Use
egg-optchar to tell panda that "Sphere01" deserves to be kept separate and
labeled:

.. code-block:: bash

   egg-optchar -d outputDir -flag Sphere01=theHead modelFile.egg anim1.egg anim2.egg

Note that you must always supply the model file(s) and all of its animation
files to egg-optchar at the same time. This is so it can examine all of the
joints and determine which joints are actually animated; and it can remove
joints by operating on all the files at once. The output of egg-optchar is
written into the directory named by the "-d" parameter.

The "-flag" switch will ensure that panda does not rearrange the geometry for
the named polyset, folding it into the model as a whole. It also assigns the
polyset a meaningful name. Once you have labeled the relevant piece of geometry,
you can obtain a pointer to it using the :meth:`~.NodePath.find()` method:

.. only:: python

   .. code-block:: python

      myModelsHead = myModel.find("**/theHead")

.. only:: cpp

   .. code-block:: cpp

      NodePath myModelsHead = myModel.find("**/theHead");

With this NodePath, you can manipulate the head separately from the rest of the
model. For example, you can move the piece using :meth:`~.NodePath.set_pos()`,
or change its texture using :meth:`~.NodePath.set_texture()`, or for that
matter, do anything that you would do to any other scene graph node.

Unanimated (environment) models
-------------------------------

Other kinds of models, those that do not contain any skeleton or animations, are
not optimized as aggressively by the Panda loader, on the assumption that the
model's hierarchy was structured the way it is intentionally, to maximize
culling (see :ref:`pipeline-tips`). Thus, only certain nodes are combined with
others, so it's quite likely that an object that you modeled as a separate node
in your modeling package will still be available under the same name when you
load it in Panda. But Panda doesn't promise that it will never collapse together
nodes that it thinks need to be combined for optimization purposes, unless you
tell it not to.

In the case of an unanimated model, the way to protect a particular node is to
insert the ``<Model>`` flag into the egg file within the particular group. The
way to do this depends on your modeling package (and this documentation still
needs to be written).
