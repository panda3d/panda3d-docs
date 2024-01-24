.. _cg-tutorial-part-3:

Cg Tutorial Part 3
==================

.. caution::

   Support for Cg shaders will be deprecated in an upcoming version of Panda3D.

Cg Tutorial Part 3: The Simplest Useful Shader
----------------------------------------------

Here our shader will actually have useful output. It won't be anything fancy,
just the silhouettes of the boxes since we're not doing anything with the
lighting just yet. To recap, there are two types of shaders. Vertex shaders
and fragment shaders. In DirectX these are called vertex shaders and pixel
shaders. Fragment shader is a more accurate name for it but for the moment
think of fragments as the equivalent of pixels.

The Shader
----------

.. code-block:: glsl

   void vshader(
       uniform float4x4 mat_modelproj,
       in float4 vtx_position : POSITION,
       out float4 l_position : POSITION)
   {
       l_position = mul(mat_modelproj, vtx_position);
   }

   void fshader(
       out float4 o_color : COLOR)
   {
       o_color = float4(1.0, 0.0, 1.0, 1.0);
   }

The vshader function is called once for every processed vertex while fshader
is called for every drawn pixel. Because our cube has 24 vertices, vshader is
called 24 times per cube in this example. fshader is called for every visible
pixel of this cube. The larger the cube on the screen, the more often fshader
needs to be called. We cannot say if it is called 100 times or 1000 times per
cube. If the cube is far away and we only see one pixel on the screen then
vshader is still called 24 times while fshader may only be called once. The
vertex shader is always called before the fragment shader. As mentioned in the
previous tutorial, a vertex that is being processed knows nothing about the
other vertices and this allows shader processing to be parallelized, that is
the GPU can process multiple shader calls at the same time.

Given a 800x600 screen, the GPU needs to process 480,000 fragment shader
calls. As even the highest end GPU right now doesn't have that many
processors, each processor will run the fragment shader multiple times. If
your fragment or vertex shader is too complex, the GPU would not be able to
process it in a timely manner and the FPS would drop. Today shaders can be
complex but you should not expect a single shader to be able to do everything.
Often you would need to write many specialized shaders which you then
carefully apply to your scene. The Auto Shader generator in Panda3D is an
example of this. A normal mapped node would have a different shader from a
node that has a glow map applied to it but you do not see this as the Auto
Shader Generator creates the necessary specialized shader for you.

Now, lets look at the shader that we have in this tutorial. As previously
mentioned, the vshader function handles vertices. The only thing a vertex
shader can do is calculate properties for vertices. One such property is the
position. A vertex shader can move vertices around. In this tutorial we only
move around the vertices but in the next tutorial we will calculate more
properties for the vertex. A vertex shader cannot create new vertices nor can
it delete vertices. This is a limitation that geometry shaders try to solve.

If we take a closer look at the vertex shader, we can see a new line with the
keyword "uniform" and a line with the "in" keyword. The "in" keyword means
that there is some input from somewhere, in this case the input is named
vtx_position. Referencing the
:ref:`List of Possible Shader Inputs <list-of-possible-cg-shader-inputs>`, you
can see that vtx_position is a reserved name. The input vtx_position gives us
is the vertex coordinates for the vertex as it appears in the egg file.
