.. _lighting:

Lighting
========

Lighting Basics
---------------

In the real world, if you put a light in a room, objects in that room are
illuminated. For example, if you put a table lamp in your living room, that lamp
automatically illuminates your sofa and your chair. In a 3D engine like Panda3D,
lights don't illuminate things automatically. Instead, you must tell the chair
and the sofa to *be illuminated* by the lamp.

So to reiterate, lighting a scene in Panda3D consists of two steps:

1. Creating lights, and positioning them within the scene.

2. Telling the other objects to *be illuminated* by the lights.

Panda3D defines four different kinds of light objects: point, directional,
ambient, and spotlight. Each of these is a node that should be attached
somewhere within the scene graph. Like anything you put into the scene, lights
have a position and orientation, which is determined by the basic scene graph
operations like :meth:`~.NodePath.set_pos()`, :meth:`~.NodePath.set_hpr()`, etc.
The :meth:`~.NodePath.look_at()` method is particularly useful for pointing
spotlights and directional lights at a particular object.

.. only:: cpp

   Note that you will need to include the following headers according to the
   type of lights you are going to use:

   .. code-block:: cpp

      #include "ambientLight.h"
      #include "directionalLight.h"
      #include "pointLight.h"
      #include "spotlight.h"

The following code inserts a directional light into the scene:

.. only:: python

   .. code-block:: python

      dlight = DirectionalLight('my dlight')
      dlnp = render.attachNewNode(dlight)

.. only:: cpp

   .. code-block:: cpp

      PT(DirectionalLight) d_light;
      d_light = new DirectionalLight("my d_light");
      NodePath dlnp = window->get_render().attach_new_node(d_light);

Note that, unlike a real, physical light bulb, the light objects are not
themselves directly visible. Although you can't see a Panda light itself, you
*can* see the effect it has on the geometry around it. If you want to make a
light visible, one simple trick is to load a simple model (like a sphere) and
parent it directly to the light itself.

Creating the light and putting it in the scene graph doesn't, by itself, have
any visible effect. Your next step is to tell some object to be illuminated by
the light. To do this, use the :meth:`.NodePath.set_light()` method, which
turns on the light for the indicated NodePath and everything below it in the
scene graph.

In the simplest case, you want all of your lights to illuminate everything they
can, so you turn them on at render, the top of the scene graph:

.. only:: python

   .. code-block:: python

      render.setLight(plnp)

.. only:: cpp

   .. code-block:: cpp

      window->get_render().set_light(pnlp);

You can remove the light setting from render:

.. only:: python

   .. code-block:: python

      render.clearLight(plnp)

.. only:: cpp

   .. code-block:: cpp

      window->get_render().clear_light(pnlp);

You could also apply the :meth:`~.NodePath.set_light()` call to a sub-node in
the scene graph, so that a given light only affects a particular object or group
of objects:

.. only:: python

   .. code-block:: python

      sofa.setLight(plnp)

.. only:: cpp

   .. code-block:: cpp

      sofa.set_light(plnp)

Note that there are two (or more) different NodePaths involved here: the
NodePath of the light itself, which defines the position and/or orientation of
the light, and the NodePath(s) on which you call :meth:`~.NodePath.set_light()`,
which determines what subset of the scene graph the light illuminates. There's
no requirement for these two NodePaths to be related in any way.

Lots of Lights: Performance Implications
----------------------------------------

Each light slows down rendering a little. Using a half-dozen lights to
illuminate an object is no problem at all. However, if you were to use a hundred
lights to illuminate an object, that object would render slowly.

Because of this, when you create a big virtual world, you need to pick and
choose which lights affect which objects. For example, if you had a dungeon
containing a hundred torches, it would not be practical to tell every object to
be illuminated by every torch. Instead, for each object in the dungeon, you
would want to search for the three or four nearest torches, and tell the object
to be illuminated only by those three or four torches.

When per-pixel lighting is enabled, lights are considerably more costly.

Colored Lights
--------------

.. only:: python

   All lights have a color, which is specified by
   :meth:`light.color = (r, g, b, a) <.Light.color>`.
   The default color is full white:
   :meth:`light.color = (1, 1, 1, 1) <.Light.color>`.
   The alpha component is largely irrelevant.

.. only:: cpp

   All lights have a color, which is specified by
   :meth:`light.set_color(LColor(r, g, b, a)) <.Light.set_color>`.
   The default color is full white:
   :meth:`light.set_color(LColor(1, 1, 1, 1)) <.Light.set_color>`.
   The alpha component is largely irrelevant.

If you are trying to simulate a natural light, it may be easier to set the color
temperature instead, by calling :meth:`.Light.set_color_temperature()` with a
value in Kelvin. Use a value of 6500 for pure white, a lower value to get a
warmer white color and a higher value to get a cooler white.

.. only:: python

   The color of the specular highlight can be set individually using
   :meth:`light.setSpecularColor((r, g, b, a)) <.Light.set_specular_color>`,
   however, this should not be done as this will produce an unnatural effect.
   This method is deprecated and may be removed in a future version of Panda3D.
   By default, the specular color of a light is automatically set from its
   regular color.

.. only:: cpp

   The color of the specular highlight can be set individually using
   :meth:`light.set_specular_color(LColor(r, g, b, a)) <.Light.set_specular_color>`,
   however, this should not be done as this will produce an unnatural effect.
   This method is deprecated and may be removed in a future version of Panda3D.
   By default, the specular color of a light is automatically set from its
   regular color.

.. note::
   The R, G, B values can be larger than 1, if you want brighter lights!
   In fact, to achieve a realistic look, you may need to set your light colors
   many orders of magnitude higher than "full white", and use HDR rendering
   techniques (described in :ref:`common-image-filters`) to make sure that the
   full dynamic range of your lights can be adequately represented and
   compressed down to the range that the user's monitor can display.

Point Lights
------------

Point lights are the easiest kind of light to understand: a point light
simulates a light originating from a single point in space and shining in all
directions, like a very tiny light bulb. A point light's position is
important, but its orientation doesn't matter.

.. only:: python

   .. code-block:: python

      plight = PointLight('plight')
      plight.setColor((0.2, 0.2, 0.2, 1))
      plnp = render.attachNewNode(plight)
      plnp.setPos(10, 20, 0)
      render.setLight(plnp)

.. only:: cpp

   .. code-block:: cpp

      PT(PointLight) plight = new PointLight("sun");
      plight->set_color(LColor(.7, .7, .7, 1));
      NodePath plnp = render.attach_new_node(plight);
      plnp.set_pos(500, 500, 500);
      render.set_light(plnp);

Attenuation
-----------

You can set the attenuation coefficients, which causes the light to drop off
gradually with distance. There are three attenuation coefficients: constant,
linear, and quadratic.

.. only:: python

   .. code-block:: python

      plight.attenuation = (c, l, q)

.. only:: cpp

   .. code-block:: python

      plight->set_attenuation(LVecBase3(c, l, q));

The default values for these constants are (1, 0, 0), respectively. This means
that the intensity of a light is by default not dependent on the distance to the
light source.

In real-life, lighting conforms to what is known as the inverse-square law. This
means that the light falls off proportional to the inverse of the square of the
distance. To achieve this effect, you need to set the quadratic coefficient to
1:

.. only:: python

   .. code-block:: python

      plight.attenuation = (0, 0, 1)

.. only:: cpp

   .. code-block:: python

      plight->set_attenuation(LVecBase3(0, 0, 1));

One disadvantage of this is that the light intensity will approach infinity as
the distance approaches zero. A common way to avoid this in real-time rendering
is to set the constant coefficient to 1.

.. only:: python

   .. code-block:: python

      plight.attenuation = (1, 0, 1)

.. only:: cpp

   .. code-block:: cpp

      plight->set_attenuation(LVecBase3(1, 0, 1));

This will make the light intensity smoothly reach 1 as the distance to the light
source approaches zero.

Directional Lights
------------------

A directional light is an infinite wave of light, always in the same direction,
like sunlight. A directional light's position doesn't matter, but its
orientation is important. The default directional light is shining down the
forward (+Y) axis; you can use :meth:`.NodePath.set_hpr()` or
:meth:`~.NodePath.set_light()` to rotate it to face in a different direction.

.. only:: python

   .. code-block:: python

      dlight = DirectionalLight('dlight')
      dlight.setColor((0.8, 0.8, 0.5, 1))
      dlnp = render.attachNewNode(dlight)
      dlnp.setHpr(0, -60, 0)
      render.setLight(dlnp)

.. only:: cpp

   .. code-block:: cpp

      PT(DirectionalLight) d_light;
      d_light = new DirectionalLight("my d_light");
      d_light->set_color(LColor(0.8, 0.8, 0.5, 1));
      NodePath dlnp = window->get_render().attach_new_node(d_light);
      dlnp.set_hpr(-30, -60, 0);
      window->get_render().set_light(dlnp);

Ambient Lights
--------------

An ambient light is used to fill in the shadows on the dark side of an object,
so it doesn't look completely black. The light from an ambient light is
uniformly distributed everywhere in the world, so the ambient light's position
and orientation are irrelevant.

Usually you don't want to create an ambient light without also creating one of
the other kinds of lights, since an object illuminated solely by ambient light
will be completely flat shaded and you won't be able to see any of its details.
Typically, ambient lights are given a fairly dark gray color, so they don't
overpower the other lights in the scene.

.. code-block:: python

   alight = AmbientLight('alight')
   alight.setColor((0.2, 0.2, 0.2, 1))
   alnp = render.attachNewNode(alight)
   render.setLight(alnp)

Spotlights
----------

Spotlights represent the most sophisticated kind of light. A spotlight has both
a point and a direction, and a field-of-view. In fact, a spotlight contains a
lens, just like a camera does; the lens should be a PerspectiveLens and is used
to define the area of effect of the light (the light illuminates everything
within the field of view of the lens).

Note that the English word "spotlight" is one word, as opposed to the other
kinds of lights, which are two words. Thus, the class name is correctly spelled
"Spotlight", not "SpotLight".

.. code-block:: python

   slight = Spotlight('slight')
   slight.setColor((1, 1, 1, 1))
   lens = PerspectiveLens()
   slight.setLens(lens)
   slnp = render.attachNewNode(slight)
   slnp.setPos(10, 20, 0)
   slnp.lookAt(myObject)
   render.setLight(slnp)

Putting it all Together
-----------------------

Here is an example of lighting. There are an ambient light and two directional
lights lighting the scene, and a green ambient light that only affects one of
the pandas.

.. code-block:: python

   import direct.directbase.DirectStart
   from panda3d.core import *

   # Put two pandas in the scene, panda x and panda y.
   x = loader.loadModel('panda')
   x.reparentTo(render)
   x.setPos(10,0,-6)

   y = loader.loadModel('panda')
   y.reparentTo(render)
   y.setPos(-10,0,-6)

   # Position the camera to view the two pandas.
   base.trackball.node().setPos(0, 60, 0)

   # Now create some lights to apply to everything in the scene.

   # Create Ambient Light
   ambientLight = AmbientLight('ambientLight')
   ambientLight.setColor((0.1, 0.1, 0.1, 1))
   ambientLightNP = render.attachNewNode(ambientLight)
   render.setLight(ambientLightNP)

   # Directional light 01
   directionalLight = DirectionalLight('directionalLight')
   directionalLight.setColor((0.8, 0.2, 0.2, 1))
   directionalLightNP = render.attachNewNode(directionalLight)
   # This light is facing backwards, towards the camera.
   directionalLightNP.setHpr(180, -20, 0)
   render.setLight(directionalLightNP)

   # Directional light 02
   directionalLight = DirectionalLight('directionalLight')
   directionalLight.setColor((0.2, 0.2, 0.8, 1))
   directionalLightNP = render.attachNewNode(directionalLight)
   # This light is facing forwards, away from the camera.
   directionalLightNP.setHpr(0, -20, 0)
   render.setLight(directionalLightNP)

   # Now attach a green light only to object x.
   ambient = AmbientLight('ambient')
   ambient.setColor((0.5, 1, 0.5, 1))
   ambientNP = x.attachNewNode(ambient)

   # If we did not call setLightOff() first, the green light would add to
   # the total set of lights on this object. Since we do call
   # setLightOff(), we are turning off all the other lights on this
   # object first, and then turning on only the green light.
   x.setLightOff()
   x.setLight(ambientNP)

   base.run()

Shadow Mapping
--------------

Panda3D offers fully automatic shadow mapping support for spotlights,
directional lights and point lights. You can enable shadows by calling
:meth:`~.LightLensNode.set_shadow_caster()`. The nodes that receive shadows will
need to have :ref:`the Shader Generator <the-shader-generator>` enabled,
otherwise no shadows will appear.

.. only:: python

   .. code-block:: python

      # Use a 512x512 resolution shadow map
      light.setShadowCaster(True, 512, 512)
      # Enable the shader generator for the receiving nodes
      render.setShaderAuto()

.. only:: cpp

   .. code-block:: cpp

      // Use a 512x512 resolution shadow map
      light->set_shadow_caster(true, 512, 512);
      // Enable the shader generator for the receiving nodes
      window->get_render().set_shader_auto();

Note that, even though in general shadowing is easy to set-up, you will want to
tweak the light's lens settings to get the best depth buffer precision. Use the
:meth:`~.Lens.set_near_far()` method on the Lens to get a perfect fit of what is
being rendered. Also, for directional lights, you will need to call
:meth:`~.Lens.set_film_size()` on the Lens and position the light properly so
that the light camera will get an optimal view of the scene.

Also note that every Light is in fact also a Camera, so you can easily exclude
objects from being shadowed (e.g. for performance reasons) by use of camera
masks.

If you have very thin objects, you may run into self-shadowing issues if the
backside of the object casts shadows on its frontside. You can easily fix this
by applying a depth offset to the object in question. A depth offset of 1 means
to use an offset as small as possible, but big enough to make a difference. This
should generally be enough. You can call :meth:`~.NodePath.set_depth_offset()`
on the NodePath or use the ``depth-offset`` scalar in the .egg file.

.. only:: python

   .. code-block:: python

      leaves.setDepthOffset(1)

.. only:: cpp

   .. code-block:: cpp

      leaves.set_depth_offset(1);
