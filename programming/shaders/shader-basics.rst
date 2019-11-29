.. _shader-basics:

Shader Basics
=============

Overview of Shaders
-------------------

Panda3D supports two shading languages: **Cg** and **GLSL**.
This section assumes that you have a working knowledge of a shader language.
If not, it would be wise to read about Cg or GLSL before trying to understand
how they fit into Panda3D.

Though Panda3D has used only Cg in the past, it is recommended that you create
new shaders in GLSL unless you want to target DirectX as well, since the NVIDIA
Cg toolkit is no longer being maintained.

There are various types of shaders, each capable of describing a different stage
in the rendering process. In the most simple case, a model simply has a *vertex
shader*, which describes how each vertex is processed, and a *fragment shader*
(also called a *pixel shader* in DirectX parlance), describing how the color of
each visible pixel on the model is determined. A shader pipeline can be composed
of one or more of the following types of shaders:

Vertex shader
   The first stage of the pipeline. It is run for each vertex on the model
   geometry, and is responsible for preparing the vertex data, usually by
   transforming the original vertex position to on-screen X, Y coordinates.
Tessellation control (hull) shader
   Optional. When tessellation is used, this specifies how to subdivide the
   tessellation patch. GLSL only.
Tessellation evaluation (domain) shader
   Optional. When tessellation is used, this determines the position of the
   tessellated vertices. GLSL only.
Geometry shader
   Optional. This is run for each *input primitive* (usually a triangle), and
   determines how the geometry is formed from the input vertices. It may also
   create additional geometry.
Fragment (pixel) shaders
   This is the last stage of the pipeline before the pixel is blended into the
   framebuffer, and usually the most useful one. It determines the color of each
   pixel of the rendered geometry, and therefore performs tasks such as lighting
   and texturing.

There is also another advanced type of shader called a
:ref:`Compute shader <compute-shaders>`, which stands on its own and does not
fit into the pipeline above.

You will often only find a vertex and fragment shader, since geometry and
tessellation shaders are relatively new features that are useful only in more
specific cases.

Cg Shaders
----------

Overview of Cg Shaders
~~~~~~~~~~~~~~~~~~~~~~

A Cg shader must contain procedures named ``vshader()`` and ``fshader()``; the
vertex shader and fragment shader respectively. If a geometry shader is used,
then it must also contain a procedure named ``gshader()``.

Single-File Cg Shaders
~~~~~~~~~~~~~~~~~~~~~~

To write a Cg shader in a single file, you must create a shader program that
looks much like the one shown below. This example preserves position but
switches the red and green channels of everything it is applied to:

.. code-block:: glsl

   //Cg

   void vshader(float4 vtx_position : POSITION,
                float4 vtx_color: COLOR,
                out float4 l_position : POSITION,
                out float4 l_color0 : COLOR0,
                uniform float4x4 mat_modelproj)
   {
     l_position = mul(mat_modelproj, vtx_position);
     l_color0 = vtx_color;
   }

   void fshader(float4 l_color0 : COLOR0,
                out float4 o_color : COLOR)
   {
     o_color = l_color0.grba;
   }

Multi-File Cg Shaders
~~~~~~~~~~~~~~~~~~~~~

Cg shaders can be divided into several files as well; one for the vertex shader,
another for the fragment shader, and a third for the geometry shader. The
procedure names are still required to be ``vshader()``, ``fshader()`` and
``gshader()`` in their respective shader files.

GLSL Shaders
------------

Overview of GLSL Shaders
~~~~~~~~~~~~~~~~~~~~~~~~

To write a GLSL shader, you must write your vertex, pixel and geometry shaders
separately, since GLSL requires the names of the entry point to all be
``main()``.

GLSL Example
~~~~~~~~~~~~

This example applies the first texture of the model using the first texture
coordinate set, but switches the red and blue channels around.

This is the vertex shader, named myshader.vert:

.. code-block:: glsl

   #version 130

   // Uniform inputs
   uniform mat4 p3d_ModelViewProjectionMatrix;

   // Vertex inputs
   in vec4 p3d_Vertex;
   in vec2 p3d_MultiTexCoord0;

   // Output to fragment shader
   out vec2 texcoord;

   void main() {
     gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
     texcoord = p3d_MultiTexCoord0;
   }

This is the fragment shader, named myshader.frag:

.. code-block:: glsl

   #version 130

   uniform sampler2D p3d_Texture0;

   // Input from vertex shader
   in vec2 texcoord;

   void main() {
     vec4 color = texture(p3d_Texture0, texcoord);
     gl_FragColor = color.bgra;
   }

Using Shaders in Panda3D
------------------------

Shaders in Panda3D use the ``Shader`` class. When a shader is loaded, an object
of this class is returned. This is then applied to a node using the
``set_shader`` method of the ``NodePath`` class.

Loading a Cg Shader
~~~~~~~~~~~~~~~~~~~

Loading a single-file Cg shader is done with the ``Shader.load()`` procedure.
The first parameter is the path to the shader file, and the second is the shader
language, which in this case is ``Shader.SL_Cg``. The following is an example of
using this procedure:

.. only:: python

   .. code-block:: python

      from panda3d.core import Shader

      myShader = Shader.load("myshader.sha", Shader.SL_Cg)

.. only:: cpp

   .. code-block:: cpp

      #include "shader.h"

      PT(Shader) myShader = Shader::load("myshader.sha", Shader.SL_Cg);

Loading a multi-file Cg shader requires a different set of parameters for the
``load()`` function; the first being the shader language, and the second, third
and fourth being paths to the vertex, fragment and geometry shaders
respectively. Here is an example:

.. only:: python

   .. code-block:: python

      myShader = Shader.load(Shader.SL_Cg,
                             vertex="myvertexshader.sha",
                             fragment="myfragmentshader.sha",
                             geometry="mygeometryshader.sha")

.. only:: cpp

   .. code-block:: cpp

      PT(Shader) myShader = Shader::load(Shader.SL_Cg, "myvertexshader.sha", "myfragmentshader.sha", "mygeometryshader.sha");

Loading a GLSL Shader
~~~~~~~~~~~~~~~~~~~~~

In the following code sample, a GLSL shader is loaded:

.. only:: python

   .. code-block:: python

      myShader = Shader.load(Shader.SL_GLSL,
                             vertex="myshader.vert",
                             fragment="myshader.frag",
                             geometry="myshader.geom")

.. only:: cpp

   .. code-block:: python

      PT(Shader) myShader = Shader::load(Shader.SL_GLSL, "myvertexshader.vert", "myfragmentshader.frag", "mygeometryshader.geom");

Applying a Shader
~~~~~~~~~~~~~~~~~

Shaders can be applied to any ``NodePath`` with the ``set_shader()`` method.
Here is an example that applies a loaded shader to a model:

.. only:: python

   .. code-block:: python

      myModel.set_shader(myShader)

.. only:: cpp

   .. code-block:: cpp

      myModel.set_shader(myShader);

The call to ``set_shader()`` causes the ``NodePath`` to be rendered with the
shader passed to it as a parameter. Shaders propagate down the scene graph, like
any other render attribute; the node and everything beneath it will use the
shader.

Fetching Data from the Panda3D Runtime
--------------------------------------

Each shader program contains a parameter list. Panda3D scans the parameter list
and interprets each parameter name as a request to extract data from the panda
runtime. For example, if the shader contains a parameter declaration ``float3
vtx_position : POSITION``, Panda3D will interpret that as a request for the
vertex position, and it will satisfy the request. Panda3D will only allow
parameter declarations that it recognizes and understands.

Panda3D will generate an error if the parameter qualifiers do not match what
Panda3D is expecting. For example, if you declare the parameter
``float3 vtx_position``, then Panda3D will be happy. If, on the other hand, you
were to declare ``uniform sampler2D vtx_position``, then Panda3D would generate
two separate errors: Panda3D knows that vtx_position is supposed to be a float-
vector, not a texture, and that it is supposed to be varying, not uniform.

Again, all parameter names must be recognized. There is a
:ref:`list of possible Cg shader inputs <list-of-possible-cg-shader-inputs>`
that shows all the valid parameter names and the data that Panda3D will supply.

Supplying data to the Shader Manually
-------------------------------------

Most of the data that the shader could want can be fetched from Panda3D at
runtime by using the appropriate parameter names. However, it is sometimes
necessary to supply some user-provided data to the shader. For this, you need
``set_shader_input()``. Here is an example:

.. only:: python

   .. code-block:: python

      myModel.set_shader_input("tint", (1.0, 0.5, 0.5, 1.0));

.. only:: cpp

   .. code-block:: cpp

      myModel.set_shader_input("tint", LVector4(1.0, 0.5, 0.5, 1.0));

The method ``set_shader_input()`` stores data that can be accessed by the
shader. It is possible to store data of type ``Texture``, ``NodePath``, and any
vector object.

The data that you store using ``set_shader_input()`` isn't necessarily used by
the shader. Instead, the values are stored in the node, but unless the shader
explicitly asks for them, they will sit unused. So the example above simply
stores the vector, but it is up to the shader whether or not it is interested in
a data item labeled "tint".

To fetch data that was supplied using ``set_shader_input()``, the shader must
use the appropriate parameter name. See the
:ref:`list of possible Cg shader inputs <list-of-possible-cg-shader-inputs>`,
many of which refer to the data that was stored using ``set_shader_input()``.

Shader Inputs propagate down the scene graph, and accumulate as they go. For
example, if you store ``set_shader_input("x", 1)`` on a node, and
``set_shader_input("y", 2)`` on its child, then the child will contain both
values. If you store ``set_shader_input("z", 1)`` on a node, and
``set_shader_input("z", 2)`` on its child, then the latter will override the
former. The method ``set_shader_input()`` accepts a third parameter, priority,
which defaults to zero. If you store ``set_shader_input("w", 1, priority=1000)``
on a node, and ``set_shader_input("w", 2, priority=500)`` on the child, then the
child will contain ("w"==1), because the priority 1000 overrides the priority
500.

Shader Render Attributes
------------------------

The functions ``nodePath.set_shader()`` and ``nodePath.set_shader_input()`` are
used to apply a shader to a node in the scene graph. Internally, these functions
manipulate a render attribute of class ``ShaderAttrib`` on the node.

In rare occasions, it is necessary to manipulate ``ShaderAttrib`` objects
explicitly. As an example, the code below shows how to create a ``ShaderAttrib``
and apply it to a camera:

.. only:: python

   .. code-block:: python

      attrib = ShaderAttrib.make()
      attrib = attrib.setShader(Shader.load("myshader.sha"))
      attrib = attrib.setShaderInput("tint", (1.0, 0.5, 0.5, 1.0))
      base.cam.node().setInitialState(attrib)

.. only:: cpp

   .. code-block:: cpp

      CPT(ShaderAttrib) attrib = ShaderAttrib::make();
      attrib = attrib.set_shader(Shader::load("myshader.sha"));
      attrib = attrib.set_shader_input("tint", LVector4(1.0, 0.5, 0.5, 1.0));
      camera.set_initial_state(attrib);

Be careful: attribs are immutable objects. So when you apply a function like
``set_shader()`` or ``set_shader_input()`` to a ``ShaderAttrib``, you aren't
modifying the attrib. Instead, these functions work by returning a new attrib
(which contains the modified data).

Deferred Shader Compilation
---------------------------

When you create a Cg shader object, it compiles the shader, checking for syntax
errors. But it does not check whether or not your video card is powerful enough
to handle the shader. This only happens later on, when you try to render
something with the shader. In the case of GLSL shaders, all of this will only
happen when the shader is first used to render something.

In the unusual event that your computer contains multiple video cards, the
shader may be compiled more than once. It is possible that the compilation could
succeed for one video card, and fail for the other.
