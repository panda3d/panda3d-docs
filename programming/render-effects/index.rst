.. _render-effects:

Render Effects
==============

There are a number of special render effects that may be set on scene graph
nodes to change the way they render. This includes BillboardEffect, Compass
Effect, DecalEffect, PolylightEffect, and ShowBoundsEffect.

List of All Render Effects:
---------------------------

:ref:`BillboardEffect <billboard-effects>`
   Dictates that geometry at this node should automatically rotate to face the
   camera, or any other arbitrary node.
CharacterJointEffect
   The effect binds the node back to the character, so that querying the
   relative transform of the affected node will automatically force the
   indicated character to be updated first.
PolylightEffect
   A PolylightEffect can be used on a node to define a LightGroup for that
   node. A LightGroup contains PolylightNodes which are essentially nodes that
   add color to the polygons of a model based on distance. PolylightNode is a
   cheap way to get lighting effects specially for night scenes
:ref:`CompassEffect <compass-effects>`
   In its purest form, a CompassEffect is used to keep the node's rotation
   fixed relative to the top of the scene graph, despite other transforms that
   may exist above the node. Hence the name: the node behaves like a magnetic
   compass, always pointing in the same direction.
ShowBoundsEffect
   Applied to a GeomNode to cause a visible bounding volume to be drawn for
   this node. This is generally used only during development to help identify
   bounding volume issues.
DecalEffect
   Applied to a GeomNode to indicate that the children of this GeomNode are
   coplanar and should be drawn as decals (eliminating Z-fighting).
TexProjectorEffect
   This effect automatically applies a computed texture matrix to the
   specified texture stage, according to the relative position of two
   specified nodes.

RenderEffect represents render properties that must be applied as soon as they
are encountered in the scene graph, rather than propagating down to the leaves.
This is different from RenderAttrib, which represents properties like color and
texture that don't do anything until they propagate down to a GeomNode.

You should not attempt to create or modify a RenderEffect directly; instead,
use the make() method of the appropriate kind of effect you want. This will
allocate and return a new RenderEffect of the appropriate type, and it may
share pointers if possible. Do not modify the new RenderEffect if you wish to
change its properties; instead, create a new one.

Once you have created a RenderEffect, you need to decide what it should affect.
If you have an effect that should affect everything in the scene the NodePath in
the next line of code is "render". If you only want it to affect specific
objects, choose the appropriate place in the scene graph.

.. only:: python

   .. code-block:: python

      nodePath.node().setEffect(<Render Effect>)

.. only:: cpp

   .. code-block:: cpp

      nodePath.node()->set_effect(<Render Effect>);

.. toctree::
   :maxdepth: 2

   billboard
   compass
