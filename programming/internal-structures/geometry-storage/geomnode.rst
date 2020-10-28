.. _geomnode:

GeomNode
========

Finally, :class:`.GeomNode` is the glue that connects :ref:`Geoms <geom>` into
the scene graph. A :class:`.GeomNode` contains a list of one or more Geoms.

.. raw:: html

   <center><table>
   <tr><td style="border: 1px solid black; background: #c1beea; padding: 5pt">
   <p>GeomNode</p>
   <table>
   <tr><td><table style="border: 1px solid black; background: #acb1ed; padding: 5pt">
   <tr><td style="border: 1px solid black; background: #9197d8; padding: 5pt">
   <p>Geom</p>
   </td><td style="border: 1px solid black; background: #9197d8; padding: 5pt">
   <p>RenderState</p>
   </td></tr>
   </table></td></tr>
   <tr><td><table style="border: 1px solid black; background: #acb1ed; padding: 5pt">
   <tr><td style="border: 1px solid black; background: #9197d8; padding: 5pt">
   <p>Geom</p>
   </td><td style="border: 1px solid black; background: #9197d8; padding: 5pt">
   <p>RenderState</p>
   </td></tr>
   </table></td></tr>
   <tr><td><table style="border: 1px solid black; background: #acb1ed; padding: 5pt">
   <tr><td style="border: 1px solid black; background: #9197d8; padding: 5pt">
   <p>Geom</p>
   </td><td style="border: 1px solid black; background: #9197d8; padding: 5pt">
   <p>RenderState</p>
   </td></tr>
   </table></td></tr>
   </table>
   </td></tr>
   </table></center>

The :class:`.GeomNode` class inherits from :ref:`PandaNode <the-scene-graph>`,
so a GeomNode can be attached directly to the scene graph like any other node;
and like any node, it inherits a transform and a render state from its parents
in the scene graph. This transform and state is then applied to each of the
node's Geoms.

Furthermore, the GeomNode stores an additional render state definition for
each Geom. This allows each Geom within a given GeomNode to have its own
unique state; for instance, each Geom may have a different texture applied.

When a model is loaded from an egg file, normally all the state definitions
required to render the geometry will be stored on these per-Geom state
definitions, rather than at the GeomNode level. These per-Geom states will
override any state that is inherited from the scene graph, unless that scene
graph state has a priority higher than the default priority of zero.
(This is why it is necessary to specify a second parameter of 1 to the
:meth:`nodePath.setTexture() <.NodePath.setTexture>` call, if you want to
replace a texture that was applied to a model in the egg file.)
