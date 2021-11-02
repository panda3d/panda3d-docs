.. _models-and-actors:

Models and Actors
=================

Geometry Basics
---------------

There are two classes in Panda3D for 3D Geometry: the 'Model', which is for
non-animated geometry, and the 'Actor', which is for animated geometry.

Note that a geometry is only considered animated if it changes shape. So for
example, a baseball wouldn't be considered animated: it may fly all over the
place, but it stays a sphere. A baseball would be a model, not an actor.

Panda does not distinguish between big stuff and small stuff. For example, if a
virtual world contains a coffee cup on a table, and the table is in the middle
of a small island, then the coffee cup, the table, and the island are all
models: each is a piece of static non-animated geometry.

Many engines provide tools to create terrain, and store that terrain into
heightmap images. Panda3D can generate geometry for a kind of heightmap terrain;
refer to the :ref:`terrain` section for more information. For many simple
terrains, though, many people prefer to use a static model rather than a
heightmap image.

The following sections of the manual assume that you have a valid egg file which
has an animatable model, and some additional egg files containing animations. To
learn how to convert a model into an egg file see the :ref:`model-export`
section.

Panda's Primary File Format
---------------------------

In Panda3D, geometry is generally stored in EGG files. An EGG file can contain:

-  A Model (static geometry)
-  An Actor (dynamic geometry)
-  An Animation (to be applied to an actor)
-  Both an Actor and an Animation.

EGG files are created by exporting models from 3D modeling programs like Maya,
Max, or Blender. Currently, the support for Maya is very strong, since the
developers of Panda3D mostly use Maya. The Max exporter is not very reliable
right now. There is a third-party exporter for Blender, which is said to be
quite good.

It is not recommended to pack both an actor and an animation into an EGG file:
this tends to result in developer confusion.

Panda's Other File Format
-------------------------

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
experience with your game to have delays caused by egg file loading. In that
case, it may make sense to ship BAM files instead of EGG files to the user. To
do this, you would use a tool like ``egg2bam`` or ``packpanda`` to convert your
EGG files into BAM files manually.

.. caution::

   Whereas .egg files are considered to be stable across many versions of
   Panda3D, .bam files are a reflection of the internal memory structure of
   Panda3D.  Therefore, it's theoretically possible for a .bam file created
   using one version of Panda3D to no longer work in a different version of
   Panda3D in the future.  Therefore, if you choose to work directly with .bam
   files, you should make sure to always preserve the source assets and
   information about the pipeline so that you can reconvert them as needed.


.. toctree::
   :maxdepth: 2

   loading-models
   loading-actors-and-animations
   actor-animations
   multi-part-actors
   attaching-objects-to-joints
   controlling-joints
   level-of-detail
