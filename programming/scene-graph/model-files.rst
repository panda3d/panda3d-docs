.. _model-files:

Model Files
===========

The most common way to put geometry in the scene is by loading it from a file.
A model file contains a tree of nodes, similar to a scene graph, under which
the actual geometry is stored that Panda3D can render to the screen.

Model files can contain static geometry, but they can also contain information
for animating the model, as well as information about the model's material, ie.
what color the material has, and how this color changes under the influence of
lighting.

Panda does not distinguish between big stuff and small stuff. For example, if a
virtual world contains a coffee cup on a table, and the table is in the middle
of a small island, then the coffee cup, the table, and the island are all
models: each is a piece of static non-animated geometry. A model file could
also contain the entire island with all the smaller models included within it.

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

File Formats
------------

Models can be stored in one of a number of file formats. Panda3D's own native
format for storing models is EGG. This is a human-readable format containing
a textual description of the geometry and its animations and materials.
Panda3D provides various tools that can convert model files from other formats
to the EGG format, and manipulate EGG files in various ways.

The other native format of Panda3D is the BAM format, which is a binary
representation of the internal object structure of Panda3D. As such, it is very
efficient to load. Therefore, it is also the format of choice when shipping the
game to an end-user. Panda3D will automatically convert your models to BAM for
caching purposes, or when packaging a finished game for distribution.

There are a range of plug-ins available to load models in other formats, such
as the :ref:`glTF format <gltf-files>`, which is a widely-used format in the
industry. See :ref:`supported-model-formats` for more information about
supported formats.

Loading a Model File
--------------------

You can load a model file using the following code:

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

The Model Cache
---------------

The first time you load an EGG file, it loads slowly. However, the second time
you use that same EGG file, it loads fast. This is possible because Panda3D is
quietly translating the EGG file into a performance-optimized BAM file. It
stores these BAM files in a directory called the *model cache*. The next time
you try to load the EGG file, if it has not been modified on disk, Panda3D will
load the corresponding optimized BAM file from the model cache instead.

Where this cache is stored depends on your operating system. On Windows, it is
usually in C:\\Users\\YourUser\\AppData\\Local\\Panda3D-|version|, whereas on
Linux, it can be found in ~/.cache/panda3d. The location can be controlled
using the ``model-cache-dir`` variable in your
:ref:`Config.prc <configuring-panda3d>` file, or disabled by setting this
variable to an empty string.

.. only:: python

   You can alternatively force a model to bypass the model cache by passing the
   ``noCache=True`` argument to the ``loader.loadModel`` call.

Compressed Models
-----------------

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
