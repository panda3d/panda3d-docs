.. _render-attributes:

Render Attributes
=================

Render Attributes Basics
------------------------

After loading a model, you can alter its appearance by altering its attributes.
For example, you can apply a color to the model, you can illuminate it with
lights, you can cause it to be obscured by fog, you can make it partially
transparent, and so forth. All of these are called render attributes.

Collectively, all the attributes of an object are called the object's render
state, or sometimes just the object's state.

Propagation of Attributes
-------------------------

Attributes can be stored on any node of the scene graph; setting an attribute on
a node automatically applies it to that node as well as to all of the children
of the node (unless an override is in effect, but that's a more advanced topic).

It is possible to create these attributes and assign them to a node directly:

.. only:: python

   .. code-block:: python

      nodePath.node().setAttrib(attributeObject)

.. only:: cpp

   .. code-block:: cpp

      node_path.node()->set_attrib(attributeObject);

But in many cases, especially with the most commonly-modified attributes, you
don't need to create the attributes directly as there is a convenience function
on NodePath (e.g. :meth:`.NodePath.set_fog()`) that manages the creation of the
attributes for you; there will also be a corresponding clear function on
NodePath to remove the attribute (:meth:`.NodePath.clear_fog()`).

Render Attribute Priorities
---------------------------

Every attribute has a priority. By default, that priority is zero. That priority
value affects the inheritance of attributes.

.. toctree::
   :maxdepth: 2

   list-of-all-attributes
   lighting
   materials
   depth-test-and-depth-write
   fog
   alpha-testing
   color-write-masks
   antialiasing
   clip-planes
   tinting-and-recoloring
   backface-culling-and-frontface-culling
   occlusion-culling/index
   light-ramps
   auxiliary-bitplane-control
   stencil-attribute


