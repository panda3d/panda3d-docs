.. _materials:

Materials
=========

Materials
---------

Materials affect how the surfaces of models appear when lights are enabled in
Panda. These have various effects such as how shiny an object appears, the
brightness of its colors etc. Material properties are combined with textures
and lighting to get the final look of an object.

It must be emphasized that materials only work when lights are applied to an
object. Otherwise, materials have no effect.

Explanation of Lighting
-----------------------

When light strikes a 3D model, light reflects off the model. If there were no
light reflecting off the model, the model would appear pitch black. The light
reflecting off the model is what causes it to have a non-black color onscreen.
In the real world, light is incredibly complicated --- so complicated, that it
is infeasible to do realistic calculations. Instead, Panda3D leaves it in your
hands, giving you some basic tools to express how much light you want
reflecting from each surface.

The tools provided are lights and materials. Lights are used to express how
much light is striking the model. Materials are used to express how much of
the light striking the model is reflected.

Panda3D separates the light striking the model into two general categories:
nondirectional, and directional. Directional light is light that comes straight
from a particular lamp. Because we know where it's coming from, we also know
what direction it is coming from. Nondirectional light is light that maybe came
from somewhere, bounced around a bit, and then eventually hit the model.
Because we don't know exactly where it came from, we don't know what direction
it is coming from. Panda3D handles nondirectional and directional light
separately.

There are four kinds of lights in Panda3D: ambient, point, diffuse, and
directional. The ambient light only creates nondirectional light. The other
three create directional light.

When light strikes the surface of the model, it is the Material that governs
how much of it reflects. The Material consists of four values:

Ambient Scattering
   Governs how much of the nondirectional light is reflected. Nondirectional
   light is always assumed to come from all directions, and it always reflects
   in all directions equally.
Diffuse Scattering
   Governs how much of the directional light is scattered. Scattering means
   that the light may have arrived from a particular direction, but it bounces
   off the model in all directions. Scattering looks like light hitting a
   painted white wall.
Specular Reflection
   Governs how much of the directional light is reflected. Specular reflection
   looks like light hitting a shiny piece of plastic: you can vaguely see a
   reflection of the lamp in the plastic, though the reflection just looks
   like a bright spot.
Emissivity
   Governs how much light the surface produces itself, for glowing surfaces
   like neon or glow sticks.

Default Behavior and Explicit Behavior
--------------------------------------

If the model does not have an explicit material, does not have a flat color,
and does not have vertex colors, the behavior is this:

#. All nondirectional light is reflected without being tinted.
#. All directional light is scattered without being tinted.
#. No specular reflection occurs.
#. No emissivity occurs.

If the model does not have an explicit material, but it does have a flat color
or a vertex color, the behavior is this:

#. All nondirectional light is reflected after being modulated by the model's
   color.
#. All directional light is scattered after being modulated by the model's
   color.
#. No specular reflection occurs.
#. No emissivity occurs.

When you set an explicit material on an object, the behavior is as follows:

#. All nondirectional light is reflected after being modulated by the explicit
   ambient color.
#. All directional light is scattered after being modulated by the explicit
   diffuse color.
#. All directional light is reflected specularly after being modulated by the
   explicit specular color.
#. The explicit emissive color is added to the light.

It is possible to mix-and-match explicit with default behavior. For example,
you can specify an explicit specular color, but not specify an explicit
ambient, diffuse, or emissive color. If you do that, the behavior would be:

#. All nondirectional light is reflected after being modulated by the model's
   color.
#. All directional light is scattered after being modulated by the model's
   color.
#. All directional light is reflected specularly after being modulated by the
   explicit specular color.
#. No emissivity occurs.

Creating and Using Materials
----------------------------

To use explicit materials, import the Materials module when you first begin
your script. Then creating Materials is a matter of creating instances of the
:class:`.Material` class and setting the relevant properties:

.. only:: python

   .. code-block:: python

      import direct.directbase.DirectStart
      from panda3d.core import Material

      myMaterial = Material()
      myMaterial.setShininess(5.0) # Make this material shiny
      myMaterial.setAmbient((0, 0, 1, 1)) # Make this material blue

      myNode = loader.loadModel("panda") # Load the model to apply the material to
      myNode.setMaterial(myMaterial) # Apply the material to this nodePath

.. only:: cpp

   .. code-block:: cpp

      PT(Material) mat = new Material;
      mat->set_shininess(5.0); // Make this material shiny
      mat->set_ambient(LColor(0, 0, 1, 1)); // Make this material blue

      NodePath model = window->load_model(window->get_render(), "panda"); // Load the model to apply the material to
      model.set_material(mat); // Apply the material to this nodePath

Material Properties
-------------------

The following table details the properties available in a material, its effects
as well as the relevant setter method. Most of these properties have additional
get and clear methods as well.

========= =================================================================================================================================================================================================================================================================== ================================
Property  Effects                                                                                                                                                                                                                                                             Setter Method
========= =================================================================================================================================================================================================================================================================== ================================
Ambient   This is the color of the object as it appears in the absence of direct light. This will be multiplied by any ambient lights in effect on the material to set its base color.                                                                                        :meth:`material.set_ambient((R,G,B,A)) <.Material.set_ambient>`
Diffuse   This is the primary color of an object; the color of the object as it appears in direct light, in the absence of highlights. This will be multiplied by any lights in effect on the material to get the color in the parts of the object illuminated by the lights. :meth:`material.set_diffuse((R,G,B,A)) <.Material.set_diffuse>`
Emission  This is the color of the object as it appears in the absence of any light whatsoever, including ambient light. It is as if the object is glowing by this color (although of course it will not illuminate neighboring objects)                                      :meth:`material.set_emission((R,G,B,A)) <.Material.set_emission>`
Shininess This controls the size of the specular highlight spot. In general, larger numbers produce a smaller specular highlight, which makes the object appear shinier. Smaller numbers produce a larger highlight, which makes the object appear less shiny.                :meth:`material.set_shininess(0..128) <.Material.set_shininess>`
Specular  This is the highlight color of an object: the color of small highlight reflections.                                                                                                                                                                                 :meth:`material.set_specular((R,G,B,A)) <.Material.set_specular>`
========= =================================================================================================================================================================================================================================================================== ================================

Other Material Methods
----------------------

Besides the setter methods covered above, you can also get material properties
using their get methods, such as :meth:`~.Material.get_shininess()`,
:meth:`~.Material.get_diffuse()`, etc.

Properties can also be reset by using the clear methods:
:meth:`~.Material.clear_ambient()`, :meth:`~.Material.clear_specular()`, etc.
Shininess does not have a clear method.

Additionally you can check if a material has a property with the has methods:
:meth:`~.Material.has_ambient()`, :meth:`~.Material.has_emission()`, etc.

Materials have two other methods that have not been covered yet,
:meth:`set_local(bool) <.Material.set_local>` and
:meth:`set_twoside(bool) <.Material.set_twoside>`. The former controls whether
to use camera-relative specular highlights or orthogonal specular highlights.
This should be set to True unless an orthogonal projection camera is in use.
The latter controls if lighting should appear on both sides of a polygon.
Both these methods have equivalent get methods.

Inspecting and Replacing Materials
----------------------------------

When loading a model from a file, it may be useful to dynamically inspect which
materials are present. This is possible using methods provided on the NodePath
object that represents the model to which the materials are applied.

.. only:: python

   .. code-block:: python

      # Find all materials
      mats = car.findAllMaterials()

      # Find a specific material by name (wildcards allowed)
      blue = car.findMaterial("blueMetal")

      # Find all materials whose name end in Metal
      coloredMetals = car.findAllMaterials("*Metal")

.. only:: cpp

   .. code-block:: cpp

      // Find all materials
      MaterialCollection mats = car.find_all_materials();

      // Find a specific material by name (wildcards allowed)
      PT(Material) blue = car.find_material("blueMetal");

      // Find all materials whose name end in Metal
      MaterialCollection colored_metals = car.find_all_materials("*Metal");

In some cases, you may want to replace a material with a different one. An easy
way to set the material for a node is just to apply it with an override value,
meaning it takes precedence over a material applied to any node below it:

.. only:: python

   .. code-block:: python

      red = Material()
      #...set up red material
      car.setMaterial(red, 1)

.. only:: cpp

   .. code-block:: cpp

      PT(Material) red = new Material;
      //...set up red material
      car.set_material(red, 1);

However, this will set the material on all parts of the model. In this case, it
will also give the wheels the same red metal look! As of Panda3D 1.10, there is
an easy way to replace all instances of a specific material only:

.. only:: python

   .. code-block:: python

      blue = car.findMaterial("blueMetal")
      red = Material()
      #...set up red material

      car.replaceMaterial(blue, red)

.. only:: cpp

   .. code-block:: cpp

      PT(Material) blue = car.find_material("blueMetal");
      PT(Material) red = new Material;
      //...set up red material

      car.replace_material(blue, red);

Related Classes
~~~~~~~~~~~~~~~

-  :class:`panda3d.core.Material`
-  :class:`panda3d.core.MaterialCollection`
