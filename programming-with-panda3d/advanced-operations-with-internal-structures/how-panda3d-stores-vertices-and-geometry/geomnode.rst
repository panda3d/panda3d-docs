.. _geomnode:

GeomNode
========

Finally, GeomNode is the glue that connects :ref:`Geoms <geom>` into the scene
graph. A GeomNode contains a list of one or more Geoms.

+-----------------------------------------------------------------------------+
| GeomNode                                                                    |
| +------------------------------------------------------------------------+  |
| | ==== ===========                                                       |  |
| | Geom RenderState                                                       |  |
| | ==== ===========                                                       |  |
| +------------------------------------------------------------------------+  |
| | ==== ===========                                                       |  |
| | Geom RenderState                                                       |  |
| | ==== ===========                                                       |  |
| +------------------------------------------------------------------------+  |
| | ==== ===========                                                       |  |
| | Geom RenderState                                                       |  |
| | ==== ===========                                                       |  |
| +------------------------------------------------------------------------+  |
+-----------------------------------------------------------------------------+


The GeomNode class inherits from :ref:`PandaNode <the-scene-graph>`, so a
GeomNode can be attached directly to the scene graph like any other node; and
like any node, it inherits a transform and a render state from its parents in
the scene graph. This transform and state is then applied to each of the
node's Geoms.

Furthermore, the GeomNode stores an additional render state definition for
each Geom. This allows each Geom within a given GeomNode to have its own
unique state; for instance, each Geom may have a different texture applied.

When a model is loaded from an egg file, normally all the state definitions
required to render the geometry will be stored on these per-Geom state
definitions, rather than at the GeomNode level. These per-Geom states will
override any state that is inherited from the scene graph, unless that scene
graph state has a priority higher than the default priority of zero. (This is
why it is necessary to specify a second parameter of 1 to the
nodePath.setTexture() call, if you want to replace a texture that was applied
to a model in the egg file.)
