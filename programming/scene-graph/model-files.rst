.. _model-files:

Model Files
===========

The most common way to put geometry in the scene is by loading it from a file.
A model file contains a tree of nodes, similar to a scene graph. Most models
will contain one or more :class:`.GeomNode` nodes, which contain the actual
geometry that Panda3D can render to the screen.

Panda does not distinguish between big stuff and small stuff. For example, if a
virtual world contains a coffee cup on a table, and the table is in the middle
of a small island, then the coffee cup, the table, and the island are all
models: each is a piece of static non-animated geometry.

Panda3D does distinguish between animated and non-animated geometry, however.
"Animated" in this sense means that the geometry changes shape; a flying ball
wouldn't be considered animated, because it stays a sphere. Animated models are
explained further in the :ref:`animated-models` section; this section just
explains how to load non-animated geometry.

Loading a model from a file isn't the only way to put geometry on the screen.
Many engines provide tools to create terrain, and store that terrain into
heightmap images. Panda3D can generate geometry for a kind of heightmap terrain;
refer to the :ref:`terrain` section for more information. For many simple
scenes, though, it is simpler to use a static model loaded from a file rather
than a dynamically generated heightmap terrain.

Loading a Model File
--------------------

You can load a model using the following code:

.. only:: python

   .. code-block:: python

      myNodePath = loader.loadModel("path/to/models/myModel.egg")

   This call can take an absolute or relative path, although it is strongly
   recommended to use relative paths only. These relative paths are resolved
   using the "model path", which is set by default to the path of the main
   Python file. Do note that the path always uses forward slashes, even on
   Windows. See :ref:`filename-syntax` for more information about filenames.

.. only:: cpp

   .. code-block:: cpp

      NodePath myNodePath =
        window->load_model(framework.get_models(), "path/to/models/myModel.egg");

   This call can take an absolute or relative path, although it is strongly
   recommended to use relative paths only. These relative paths are resolved
   using the "model path", which is set by default to the path of the compiled
   executable file. Do note that the path always uses forward slashes, even on
   Windows. See :ref:`filename-syntax` for more information about filenames.

The first time you make this call for a particular model, that model is read and
saved in a table in memory; on each subsequent call, the model is simply copied
from the table, instead of reading the file.

This call returns a :class:`.NodePath` object representing the root of the
model's tree of nodes. This object is used to manipulate the model further and
place it into the scene graph.

.. note::

   In many examples, you will see that the extension is omitted. In this case,
   Panda3D will automatically look for a file with the .egg extension.

Placing the Model in the Scene Graph
------------------------------------

The most important manipulation is to change the parent of a node. A model is by
default loaded without a parent, but it needs to be placed into an active scene
graph so that Panda3D will be able to find the model's geometry and render it to
the screen.

The default 3D scene graph is called :obj:`~builtins.render`, and this is how to
reparent the model to this scene graph:

.. only:: python

   .. code-block:: python

      myModel.reparentTo(render)

.. only:: cpp

   .. code-block:: cpp

      myModel.reparent_to(window->get_render());

It is possible to reparent the model to any node (even to another model, or to
a sub-part of a different model), not just to :obj:`~builtins.render`!
What's important is that it is parented to a node that is itself parented to a
scene graph, so that Panda3D can find it. Otherwise, the model will remain
invisible.

The converse is to remove a model from the scene graph, which can be done as
follows:

.. only:: python

   .. code-block:: python

      myModel.detachNode()

.. only:: cpp

   .. code-block:: cpp

      myModel.detach_node();

Panda's Primary File Format
---------------------------

In Panda3D, geometry is generally stored in EGG files. An EGG file can contain
static geometry, but it can also contain information for animating the model,
as well as information about the model's material, ie. what color the material
has, and how this color changes under the influence of lighting).

EGG files are created by exporting models from 3D modeling programs like Maya,
Max, or Blender. Currently, the support for Maya is very strong, since the
developers of Panda3D mostly use Maya. The Max exporter is not very reliable
right now. There is a third-party exporter for Blender, which is said to be
quite good.

The EGG format is a human-readable format. You can open an EGG file in a text
editor and see what it contains. See :ref:`egg-syntax` for more detailed
information about the contents of EGG files.

Panda's Optimized File Format
-----------------------------

The EGG file is optimized for debugging, not speed. The first time you load an
EGG file, it loads slowly. However, the second time you use that same EGG file,
it loads fast.

This is possible because Panda3D is quietly translating the EGG file into a
performance-optimized form: the BAM file. It stores these BAM files in a
directory called the model cache. When developing a game, this works great: the
only time you notice a delay is if you just created the EGG file for the first
time. Otherwise, it runs blazing fast.

However, there is one situation where this doesn't work so well: if you are
shipping your game to a customer. You don't want your customer's first
experience with your game to have delays caused by file loading. In that case,
it may make sense to ship BAM files instead of EGG files to the user. To do
this, you would use a tool like ``egg2bam`` to convert your EGG files into BAM
files manually. The distribution tools that ship with Panda3D automatically
convert your models to .bam.

.. caution::

   Whereas .egg files are considered to be stable across many versions of
   Panda3D, .bam files are a reflection of the internal memory structure of
   Panda3D.  Therefore, it's theoretically possible for a .bam file created
   using one version of Panda3D to no longer work in a different version of
   Panda3D in the future.  Therefore, if you choose to work directly with .bam
   files, you should make sure to always preserve the source assets and
   information about the pipeline so that you can reconvert them as needed.

Other File Formats
------------------

An increasingly commonly used format for 3D models is the glTF format. This is a
standard format that is very widely supported by many modelling suites. There
are also many models available on the internet in this format.

In the future, Panda3D will contain native support for loading glTF models.
Until then, there is a high quality third party plug-in that can be installed
that can be used to load glTF models:

https://github.com/Moguri/panda3d-gltf

.. only:: python

   After installing this plug-in using the "pip" package manager, no extra steps
   are needed. You can simply give Panda a path to a file with a .gltf extension
   and it will load via the panda3d-gltf plug-in.

Compressing Models
------------------

Because EGG files are text-based, they can get rather large in size. It is often
desirable to store them in a compressed fashion so that they take up less space.
This can be done using the pzip utility that ships with Panda3D::

   pzip model.egg

That will turn it into a file called "model.egg.pz", which will be considerably
smaller. Panda3D will be able to load this model without any extra steps.

To undo this step and return it to its original form, just run it through the
"punzip" utility.

Loading Models Asynchronously
-----------------------------

When loading very large models, it can sometimes take some time before the model
has finished loading. If this is done while the user is interacting with the
program, it generates an undesirable lag. To alleviate this, Panda3D can load
models in the background, without disrupting the user experience.

See :ref:`async-loading` for more information about these techniques. However,
they are advanced techniques and if you are still learning Panda3D it is
recommended to revisit this later, when optimizing your program.
