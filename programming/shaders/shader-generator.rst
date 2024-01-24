.. _the-shader-generator:

The Shader Generator
====================

As of version 1.5.0, panda supports several new features:

-  per-pixel lighting
-  normal mapping
-  gloss mapping
-  glow mapping
-  high-dynamic range rendering
-  cartoon shading

It's not that these things weren't possible before: they were. But previously,
you had to write shaders to accomplish these things. This is no longer
necessary. As of version 1.5.0, all that has to happen is for the artist to
apply a normal map, gloss map, or glow map in the 3D modeling program. Then, the
programmer gives permission for shader generation, and Panda3D handles the rest.

A few of these features do require minimal involvement from the programmer:
for instance, high-dynamic range rendering requires the programmer to choose a
tone-mapping operator from a small set of options. But that's it: the amount of
work required of the programmer is vastly less than before.

Many of these features are complementary with
:ref:`image postprocessing operations <common-image-filters>`, some of which are
now nearly-automatic as well. For example, HDR combines very nicely with the
bloom filter, and cartoon shading goes very well with cartoon inking.

Individually, these features are not documented in this chapter of the manual.
Instead, they're documented in the portion of the manual where they make the
most sense. For example, normal mapping, gloss mapping, and glow mapping are all
documented in the section on :ref:`texturing`. HDR and cartoon shading are
documented under Render Attributes in the subsection on :ref:`light-ramps`.

However, to enable any of these features, you need to tell Panda3D that it's OK
to automatically generate shaders and send them to the video card. The call to
do this is:

.. only:: python

   .. code-block:: python

      nodepath.setShaderAuto()

.. only:: cpp

   .. code-block:: cpp

      nodepath.set_shader_auto();

If you don't do this, none of the features listed above will have any effect.
Panda will simply ignore normal maps, HDR, and so forth if shader generation is
not enabled. It would be reasonable to enable shader generation for the entire
game, using this call:

.. only:: python

   .. code-block:: python

      render.setShaderAuto()

.. only:: cpp

   .. code-block:: cpp

      window->get_render().set_shader_auto();

Sample Programs
---------------

Four of the sample programs demonstrate the shader generator in action:

-  :ref:`cartoon-shader`
-  :ref:`glow-filter`
-  :ref:`bump-mapping`
-  :ref:`shadows`

In each case, the sample program provides two versions: Basic and Advanced. The
Basic version relies on the shader generator to make everything automatic. The
Advanced version involves writing shaders explicitly.

Per-Pixel Lighting
------------------

Simply turning on :meth:`~.NodePath.set_shader_auto()` causes one immediate
change: all lighting calculations are done per-pixel instead of per-vertex. This
means that models do not have to be highly tessellated in order to get
nice-looking spotlights or specular highlights.

Of course, the real magic of :meth:`~.NodePath.set_shader_auto()` is that it
enables you to use powerful features like normal maps and the like.

Hardware Skinning
-----------------

The shader generator is additionally able to improve performance of vertex
animation by performing the vertex transformation in the shader, so that it does
not need to happen on the CPU. There are some limitations on this feature, so it
is disabled by default. To enable it, you will need to set the following
variables in the :ref:`Config.prc <configuring-panda3d>` file::

   hardware-animated-vertices true
   basic-shaders-only false

It should be noted that only the four most-weighted joints are considered when
animating each vertex. There is furthermore a limit of 120 joints that may be
active at any given time. This limit may be raised in the future.

Known Limitations
-----------------

The shader generator replaces the fixed-function pipeline with a shader. To make
this work, we have to duplicate the functionality of the entire fixed function
pipeline. That's a lot of stuff. We haven't implemented all of it yet. Here's
what's supported:

-  flat colors, vertex colors and color scales
-  lighting
-  normal maps
-  gloss maps
-  glow maps
-  materials
-  1D, 2D, 3D, cube textures
-  most texture stage and combine modes
-  light ramps (for cartoon shading)
-  most texgen modes (sphere / cube map modes require Panda3D 1.10.14)
-  texmatrix
-  fog

Note that although vertex colors are supported by the ShaderGenerator, in order
to render vertex colors you need to apply a :meth:`.ColorAttrib.make_vertex()`
attrib to the render state. One easy way to do this is to call
:meth:`.NodePath.set_color_off()` (that is, turn off scene graph color, and let
vertex color be visible). In the fixed-function renderer, vertex colors will
render with or without this attrib, so you might not notice if you fail to apply
it. Models that come in via the egg loader should have this attribute applied
already. However, if you are using your own model loader or generating models
procedurally you will need to set it yourself.

How the Shader Generator Works
------------------------------

When panda goes to render something marked :meth:`~.NodePath.set_shader_auto()`,
it synthesizes a shader to render that object. In order to generate the shader,
it examines all the attributes of the object: the lights, the material, the fog
setting, the color, the vertex colors... almost everything. It takes into
account all of these factors when generating the shader. For instance, if the
object has a material attrib, then material color support is inserted into the
shader. If the object has lights, then lighting calculations are inserted into
the shader. If the object has vertex colors, then the shader is made to use
those.

Caching and the Shader Generator
--------------------------------

If two objects are rendered using the same :class:`.RenderState` (ie, the exact
same attributes), then the shader is only generated once. But certain changes to
to the RenderState will the shader to be regenerated. This is not entirely
cheap. Making changes to the RenderState of an object should be avoided when
shader generation is enabled, because this necessitates regeneration of the
shader.

A few alterations don't count as RenderState modifications: in particular,
changing the positions and colors of the lights doesn't count as a change to the
RenderState, and therefore, does not require shader regeneration. This can be
useful: if you just want to tint an object, apply a light to it then change the
color of the light.

There is a second level of caching. If the system generates a shader, it will
then compare that shader to the other shaders it has generated previously. If it
matches a previously-generated shader, it will not need to compile the shader
again.

So, to save the full cost, use the same RenderState. To save most of the cost,
use two RenderStates that are similar. By "similar," I mean having the same
general structure: ie, two models that both have a texture and a normal map, and
both have no vertex colors and neither has a material applied.

Combining Automatic Shaders with Manual Shaders
-----------------------------------------------

Sometimes, you will want to write most of a game using panda's automatic shader
generation abilities, but you'll want to use a few of your own shaders. A
typical example would be a scene with some houses, trees, and a pond. You can
probably do the houses and trees using panda's built-in abilities. However,
Panda doesn't contain anything that particularly looks like pond-water: for
that, you'll probably need to write your own shader.

When you use :meth:`render.set_shader_auto() <.NodePath.set_shader_auto()>`,
that propagates down the scene graph just like any other render attribute. If
you assign a specific shader to a node using
:meth:`render.set_shader(myshader) <.NodePath.set_shader()>`, that overrides any
shader assignment propagated down from above, including an Auto shader
assignment from above. So that means it is easy, in the example above, to enable
auto shader generation for the scene as a whole, and then override that at the
pond-nodepath.

Creating your own Shader Generator
----------------------------------

We anticipate that people who are writing full-fledged commercial games using
Panda3D might want to write their own shader generators. In this way, you can
get any effect you imagine without having to give up the convenience and
elegance of being able to simply apply a normal map or a gloss map to a model,
and having it "just work."

To create your own shader generator, you will need to delve into Panda3D's C++
code. Class ShaderGenerator is meant to be subclassed, and a hook function is
provided to enable you to turn on your own generator.
