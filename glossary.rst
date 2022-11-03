.. _glossary:

Glossary
========

.. glossary::

   async
      Common abbreviation of :term:`asynchronous`.

   asynchronous
      Term for an operation that is running in the background, as opposed to
      blocking the flow of the code until it is completed.

   bam
      Binary :term:`model` format native to Panda3D, containing a direct
      representation of the memory structure of a Panda3D scene graph, making
      this format quick to load and ideal for caching and distribution.

   coroutine
      A function that can be suspended and resumed at a later point.
      See :ref:`coroutines`.

   egg
      A :term:`model` file format native to Panda3D which is text-based, meaning
      it can be opened and inspected using a text editor. See :ref:`egg-files`.

   future
      A special handle that represents an :term:`asynchronous` operation that
      will complete at some point in the future. Sometimes called a "promise" in
      other programming languages. Implemented in Panda3D via
      :class:`.AsyncFuture`.

   glb
      A binary form of the :ref:`glTF file format <gltf-files>`.

   glTF
      A standard :term:`model` and scene file format. See :ref:`gltf-files`.

   instancing
      The practice of showing a particular 3D model multiple times without
      duplicating the model in memory, see :ref:`instancing`.

   interrogate
      A tool included with Panda3D that is used to generate Python bindings for
      C++ code.  It is used to make the C++ classes and functions of Panda3D
      accessible to Python code.  See :ref:`interrogate`.

   interval
      A predetermined animation between two states of a particular property
      (usually two positions or rotations of a model), see :ref:`intervals`.
      Multiple intervals can be combined together into compound intervals using
      :ref:`sequences-and-parallels`.

   material
      A description of how 3D geometry should visually appear in the presence of
      a light source.  See :ref:`materials`.

   model
      A model is a tree of nodes, usually loaded from a file on disk, containing
      a collection of pieces of geometry and a description of the materials used
      to render them.

   node
      A particular element in the Panda3D :term:`scene graph`, represented by a
      :class:`.PandaNode` object (or a sub-class thereof).

   node path
      A path describing how to reach a particular :term:`node` from the root of
      the :term:`scene graph`.  In the presence of :ref:`instancing`, there can
      be different paths referring to the same node.  Represented in Panda3D by
      the :class:`.NodePath` class.

   parallel
      A type of :term:`interval` that executes two or more other intervals at
      the same time, see :ref:`sequences-and-parallels`.

   PBR
      Physically-based rendering, a method of defining materials that more
      accurately models the reflection of light on objects, enabling more
      physically accurate rendering results.

   physics
      A system that calculates how objects should move when acted upon by forces
      and collisions with other objects.  See :ref:`physics`.  Note that this is
      separate from the system that *detects* whether two objects collide.
      For that, see :ref:`collision-detection`.

   pstats
      PStats is a tool shipped with Panda3D that is used to display and analyze
      the performance of a Panda3D program.
      See :ref:`measuring-performance-with-pstats`.

   pview
      Model viewer utility that ships with the Panda3D installation, see
      :ref:`pview`.

   pzip
      Refers to the .pz compression format, or the tool used to produce it.

   render
      The default :class:`.NodePath` created to hold the 3D :term:`scene graph`.

   scene graph
      This can be any tree of :term:`nodes <node>` connected together via
      parent-child relationships, but usually refers to the entire collection of
      nodes that make up a 3D scene.  See :ref:`the-scene-graph`.

   sequence
      A type of :term:`interval` that executes two or more other intervals in
      succession (ie. the next one starts after the previous one is finished).
      See :ref:`sequences-and-parallels`.

   texture
      An image that is displayed on a :term:`model` in some manner, see
      :ref:`texturing`.
