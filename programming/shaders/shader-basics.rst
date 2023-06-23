.. _shader-basics:

Shader Basics
=============

Overview of Shaders
-------------------

Panda3D uses the **GLSL** shading language. This section assumes that you have a
working knowledge of a shader language. If not, it would be wise to read about
GLSL before trying to understand how it fits into Panda3D.

Note that support for GLSL is not just limited to the OpenGL graphics
back-end; Panda3D is able to automatically transpile the shader to a different
shading language, if required by the graphics API.

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

You will usually only find a vertex and fragment shader, since geometry and
tessellation shaders are relatively new features that are useful only in more
specific cases.

GLSL Shaders
------------

GLSL shaders are always separated up into separate files for vertex, fragment
and geometry shaders, with the main entry point being called ``main()``.
All GLSL shaders begin with a ``#version`` line indicating the version of the
GLSL standard that the shader is written in. Panda3D fully supports shaders
written in GLSL 330 and above and will automatically convert them as needed to
a different version of GLSL as required by the graphics driver.

GLSL versions older than 330 are supported only for compatibility with older
Panda3D projects, and with significant limitations. It is recommended to use
only GLSL 330 or higher.

Example Shader
~~~~~~~~~~~~~~

This example applies the first texture of the model using the first texture
coordinate set, but switches the red and blue channels around.

This is the vertex shader, named ``myshader.vert``:

.. code-block:: glsl

   #version 330

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

This is the fragment shader, named ``myshader.frag``:

.. code-block:: glsl

   #version 330

   uniform sampler2D p3d_Texture0;

   // Input from vertex shader
   in vec2 texcoord;

   // Output to the screen
   out vec4 p3d_FragColor;

   void main() {
     vec4 color = texture(p3d_Texture0, texcoord);
     p3d_FragColor = color.bgra;
   }

Loading a GLSL Shader
~~~~~~~~~~~~~~~~~~~~~

To load the above shader and apply it to a model, we can use the following code:

.. only:: python

   .. code-block:: python

      shader = Shader.load(Shader.SL_GLSL,
                           vertex="myshader.vert",
                           fragment="myshader.frag")
      model.setShader(shader)

.. only:: cpp

   .. code-block:: python

      PT(Shader) shader = Shader::load(Shader.SL_GLSL, "myvertexshader.vert", "myfragmentshader.frag");
      model.set_shader(shader);

To add a geometry shader, simply add the filename of the geometry shader as
additional parameter, following the fragment shader.

Applying the Shader
-------------------

Shaders can be applied to any part of the scene graph. The call to
:meth:`.NodePath.set_shader()` causes the model to be rendered with the shader
passed to it as a parameter. Shaders propagate down the scene graph, like any
other render attribute; the node and everything beneath it will use the shader.

As with other state changes, it is possible to pass a second ``priority``
parameter to indicate that the shader specified at that node should override
shaders specified on a higher or lower node that have a lower priority value.

Fetching Data from the Panda3D Runtime
--------------------------------------

Each shader program contains a parameter list. Panda3D scans the parameter list
and interprets each parameter name as a request to extract data from the panda
runtime. For example, if the shader contains a parameter declaration
``p3d_Vertex``, Panda3D willinterpret that as a request for the vertex position, 
and it will satisfy the request. Panda3D will only allow parameter declarations 
that it recognizes and understands.

Panda3D will generate an error if the parameter qualifiers do not match what
Panda3D is expecting. For example, if you declare the parameter
``float3 vtx_position``, then Panda3D will be happy. If, on the other hand, you
were to declare ``uniform sampler2D vtx_position``, then Panda3D would generate
two separate errors: Panda3D knows that vtx_position is supposed to be a
float-vector, not a texture, and that it is supposed to be varying, not uniform.

Again, all parameter names must be recognized. There is a
:ref:`list of GLSL shader inputs <list-of-glsl-shader-inputs>` that shows
all the valid parameter names and the data that Panda3D will supply.

Supplying Data to the Shader Manually
-------------------------------------

Most of the data that the shader could want can be fetched from Panda3D at
runtime by using the appropriate parameter names. However, it is sometimes
necessary to supply some user-provided data to the shader. For this, you need
:meth:`.NodePath.set_shader_input()`. Here is an example:

.. only:: python

   .. code-block:: python

      myModel.setShaderInput("tint", (1.0, 0.5, 0.5, 1.0))

.. only:: cpp

   .. code-block:: cpp

      myModel.set_shader_input("tint", LVector4(1.0, 0.5, 0.5, 1.0));

The method :meth:`.NodePath.set_shader_input()` stores data that can be accessed
by the shader. It is possible to store data of type :class:`.Texture`,
:class:`.NodePath`, and any vector object.

The data that you store using :meth:`~.NodePath.set_shader_input()` isn't
necessarily used by the shader. Instead, the values are stored in the node, but
unless the shader explicitly asks for them, they will sit unused. So the example
above simply stores the vector, but it is up to the shader whether or not it is
interested in a data item labeled "tint".

To fetch data that was supplied using :meth:`~.NodePath.set_shader_input()`, the
shader must use the appropriate parameter name.
See the :ref:`list of GLSL shader inputs <list-of-glsl-shader-inputs>`
many of which refer to the data that was stored using
:meth:`~.NodePath.set_shader_input()`.

Shader inputs propagate down the scene graph, and accumulate as they go. For
example, if you store
:meth:`set_shader_input("x", 1) <.NodePath.set_shader_input>` on a node, and
:meth:`set_shader_input("y", 2) <.NodePath.set_shader_input>` on its child, then
the child will contain both values.
If you store :meth:`set_shader_input("z", 1) <.NodePath.set_shader_input>` on a
node, and :meth:`set_shader_input("z", 2) <.NodePath.set_shader_input>` on its
child, then the latter will override the former.

This method also accepts a third parameter, priority, which defaults to zero.
If you store
:meth:`set_shader_input("w", 1, priority=1000) <.NodePath.set_shader_input>` on
a node, and
:meth:`set_shader_input("w", 2, priority=500) <.NodePath.set_shader_input>` on
the child, then the child will contain a "w" value of 1, because the priority
1000 overrides the priority 500.

.. only:: python

   To set multiple shader inputs at once, it is most efficient to use a single
   call to :meth:`~.NodePath.set_shader_inputs()`:

   .. code-block:: python

      myModel.setShaderInputs(
          tint=(1.0, 0.5, 0.5, 1.0),
          tex=myTexture,
      )

Shader Render Attributes
------------------------

The functions :meth:`.NodePath.set_shader()` and
:meth:`~.NodePath.set_shader_input()` are used to apply a shader to a node in
the scene graph. Internally, these functions manipulate a render attribute of
class :class:`.ShaderAttrib` on the node.

In rare occasions, it is necessary to manipulate :class:`.ShaderAttrib` objects
explicitly. As an example, the code below shows how to create a
:class:`.ShaderAttrib` and apply it to a camera:

.. only:: python

   .. code-block:: python

      attrib = ShaderAttrib.make()
      attrib = attrib.setShader(Shader.load("myshader.vert", "myshader.frag"))
      attrib = attrib.setShaderInput("tint", (1.0, 0.5, 0.5, 1.0))
      base.cam.node().setInitialState(attrib)

.. only:: cpp

   .. code-block:: cpp

      CPT(ShaderAttrib) attrib = DCAST(ShaderAttrib, ShaderAttrib::make());
      attrib = attrib->set_shader(Shader::load("myshader.sha", "myshader.frag"));
      attrib = attrib->set_shader_input("tint", LVector4(1.0, 0.5, 0.5, 1.0));
      camera.set_initial_state(attrib);

Be careful: attribs are immutable objects. So when you apply a function like
:meth:`~.NodePath.set_shader()` or :meth:`~.NodePath.set_shader_input()` to a
:class:`.ShaderAttrib`, you aren't modifying the attrib. Instead, these
functions work by returning a new attrib (which contains the modified data).

Deferred Shader Compilation
---------------------------

When you create a GLSL shader object and it is used to render something, 
it compiles the shader, checking for syntax errors. But it does not check 
whether or not your video card is powerful enough to handle the shader. 
This only happens later on, when you try to render
something with the shader. 

In the unusual event that your computer contains multiple video cards, the
shader may be compiled more than once. It is possible that the compilation could
succeed for one video card, and fail for the other.
