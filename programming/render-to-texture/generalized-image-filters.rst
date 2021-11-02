.. _generalized-image-filters:

Generalized Image Filters
=========================

.. only:: cpp

   .. note::

      Sorry, but the CommonFilters and FilterManager classes are implemented in
      Python and will not be of much use to C++ users.

The Filter Manager
------------------

Class FilterManager is designed to make it easier to apply filters to your
scene. Of course, the easiest way to apply filters to your scene is to use class
:ref:`CommonFilters <common-image-filters>`. But if that utility does not
contain the filters you need, then the FilterManager is your next best choice.
The main function of the FilterManager is to help you set up the offscreen
buffers, the quads, and the textures.

Import the class like this:

.. code-block:: python

   from direct.filter.FilterManager import FilterManager

The Simplest Filter
-------------------

The simplest possible code that uses the FilterManager looks like this:

.. code-block:: python

   manager = FilterManager(base.win, base.cam)
   tex = Texture()
   quad = manager.renderSceneInto(colortex=tex)
   quad.setShader(Shader.load("myfilter.sha"))
   quad.setShaderInput("tex", tex)

The first line creates an object of class FilterManager. We have told it that we
want to apply filtering to the contents of the main window. We have also told it
that we want to filter the stuff that's being rendered by the main camera, and
not, for instance, the 2D camera.

The second line creates a texture - this is the texture that we're going to
render the scene into.

The third line does most of the work. This removes the scene from the window,
and instead, directs the rendering of the scene into 'tex'. It puts a quad into
the window in place of the scene. The quad is returned.

Finally, we apply a shader to the quad, and pass the scene texture to the
shader. Presumably, the shader is rendering the scene onto the quad, which
covers the window. Presto, filtered scene.

There's one tricky aspect of all this. Usually, the window is usually not a
power of two. The texture will end up being bigger than the window: for
instance, if the window is 800x600, then the texture will be 1024x1024. The
scene will be rendered into the lower-left 800x600 pixels of the texture. The
shader needs to compensate for this. If you forget this, you will see an empty
band above and to the right of the texture.

Here is a basic shader code example, it applies a simple black and white effect:

.. code-block:: glsl

   //Cg

   void vshader(
       float4 vtx_position : POSITION,
       float2 vtx_texcoord0 : TEXCOORD0,
       out float4 l_position : POSITION,
       out float2 l_texcoord0 : TEXCOORD0,
       uniform float4 texpad_tex,
       uniform float4x4 mat_modelproj)
   {
       l_position=mul(mat_modelproj, vtx_position);
       l_texcoord0 = vtx_position.xz * texpad_tex.xy + texpad_tex.xy;
   }

   void fshader(float2 l_texcoord0 : TEXCOORD0,
                out float4 o_color : COLOR,
                uniform sampler2D k_tex : TEXUNIT0)
   {
       float4 c = tex2D(k_tex, l_texcoord0);

       // To have a useless filter that outputs the original view
       // without changing anything, just use :
       //o_color  = c;

       // basic black and white effet
       float moyenne = (c.x + c.y + c.z)/3;
       o_color = float4(moyenne, moyenne, moyenne, 1);
   }

Extracting More Information from the Scene
------------------------------------------

In addition to fetching the color buffer of the scene, you can also fetch the
depth buffer:

.. code-block:: python

   manager = FilterManager(base.win, base.cam)
   tex = Texture()
   dtex = Texture()
   quad = manager.renderSceneInto(colortex=tex, depthtex=dtex)

The depth buffer is particularly useful for filters like depth-of-field. You
can pass the depth-texture to the shader too.

Sometimes, scene rendering may generate not just a color buffer and a depth
buffer, but also an auxiliary buffer. If so, you can fetch that too:

.. code-block:: python

   manager = FilterManager(base.win, base.cam)
   tex = Texture()
   atex = Texture()
   quad = manager.renderSceneInto(colortex=tex, auxtex=atex)

Doing this would really only make sense if you've asked the renderer to put
something of interest into the auxiliary buffer. To do this, see
AuxBitplaneAttrib.

Using Intermediate Stages
-------------------------

The setup shown above works for any filter that can be computed in one stage.
However, for certain filters, you want to perform intermediate computations
before putting the output into the window.

The method ``renderQuadInto`` creates a quad, and then causes that quad to be
rendered into a texture. This is the classic intermediate processing step for
image postprocessing. Using ``renderQuadInto``, we can create a simple two-stage
filter:

.. code-block:: python

   manager = FilterManager(base.win, base.cam)
   tex1 = Texture()
   tex2 = Texture()
   finalquad = manager.renderSceneInto(colortex=tex1)
   interquad = manager.renderQuadInto(colortex=tex2)
   interquad.setShader(Shader.load("stage1.sha"))
   interquad.setShaderInput("tex1", tex1)
   finalquad.setShader(Shader.load("stage2.sha"))
   finalquad.setShaderInput("tex2", tex2)

So tex1 will contain the raw, unfitered scene. Tex2 will contain a scene that
has been filtered through stage1.sha. The window will contain a scene that has
been filtered through both stage1.sha and stage2.sha.

The function 'renderQuadInto' accepts the keywords 'colortex', 'auxtex0', and
'auxtex1'. It does not accept 'depthtex,' since no depth buffer is used when
rendering a quad.

Resolution Management
---------------------

Unless you specify otherwise, all textures will be the same resolution as the
window. The FilterManager will preserve this condition - it will automatically
resize the offscreen textures if the window gets resized.

The intermediate stages created by ``renderQuadInto`` can be the same size as
the window, but they can also be larger or smaller by a constant factor. The
function takes the following keyword arguments:

-  mul - The 'mul' option multiplies the size by an integer constant.

-  div - The 'div' option divides the size by an integer constant.

-  align - Relevant only when using the 'div' option - the window size is
   aligned to a specified alignment before dividing. This is useful to
   minimize resampling artifacts.

Cleaning Up
-----------

This function will cause the FilterManager to put everything back the way it
started:

.. code-block:: python

   manager.cleanup()
