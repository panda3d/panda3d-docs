.. _compute-shaders:

Compute Shaders
===============

Introduction
------------

Compute shaders, introduced in 1.9, are a type of general-purpose shader program
that can be used to perform a wide variety of functions on the video card.
They are fundamentally different from other types of shaders in that they aren't
assigned to a node and modify how the node is rendered, but are executed
(*dispatched*) in a standalone fashion and perform an operation on an arbitrary
set of data. They may read from and write to texture images at will. This is
particularly useful for image processing or GPU-based particle algorithms, to
name a few examples.

Compute shaders are only available on hardware supporting OpenGL 4.3, which
includes NVIDIA GeForce 400 series and above and AMD Radeon HD 5000 series and
above.

It is important to know that compute shaders are an advanced, low-level, and
relatively recent feature. This means that it is very easy to get strange and
unexplainable results, including garbled texture data, or even video card
crashes and system freezes in some cases. Using them certainly requires a
certain amount of expertise with graphics programming. In many cases, similar
results can be achieved with render-to-texture processes.

This page only aims to give a cursory overview of compute shaders where it is
relevant to Panda3D's interfaces. It is by no means a comprehensive manual
covering everything about compute shaders. In particular, image access
concurrency, shared or coherent variables, and memory barriers are not covered
here at all. Please refer to the
`OpenGL documentation <https://www.khronos.org/opengl/wiki/Compute_Shader>`__
for more information.

Work groups
-----------

Normally, a regular shader is executed on a predetermined set of data (such as
an amount of vertices or pixels), in which case the amount of shader invocations
is known beforehand. However, since compute shaders can operate on an arbitrary
set of data, the amount of invocations has to be explicitly specified.

Compute shader invocations are divided up in batches called *work groups*, which
specify how many invocations happen simultaneously. The different invocations in
a work group may occur at the same time, but you should never rely on the
different work groups being executed in a particular order or simultaneous to
each other; this is up to the graphics driver to decide.

Although the local size of a work group is typically relatively small (you can
count on 1024 total invocations within a single work group), you may invoke any
number of these work groups. The work group count is not hard-coded within the
shader, but specified by the application. One common workflow for an image
processing shader is to divide up the image into tiles of fixed size, and then
to specify in the application how many tiles are in the image to be processed.

The work group size and count are specified using a three-dimensional size
value, so that it is conveniently possible to use compute shaders on sets of
data with up to three physical dimensions, such as 3-D textures or cube maps.
However, the Z component of these values may be set to 1 if the shader is
designed to operate on a 2-D set of data, and the Y component may be 1 if the
shader is designed to work on a one-dimensional array. The way this is specified
merely determines how the coordinates are provided to the shader; in the end,
what counts is the total number of invocations in the work group, which is equal
to the product of these three numbers.

So, if you have an image processing shader that operates on a 512x512 image, you
may set the local work group size in your shader to 16x16x1, whereas in your
application, you would specify a work group count of 32x32x1 since there are 32
of these tiles in each of the X and Y directions.

Example shader
--------------

A typical compute shader (GLSL) looks as follows. All that the shader does is
copy the contents of one texture to another, except that it swaps two channels.

.. code-block:: glsl

   #version 430

   // Set the number of invocations in the work group.
   // In this case, we operate on the image in 16x16 pixel tiles.
   layout (local_size_x = 16, local_size_y = 16) in;

   // Declare the texture inputs
   uniform readonly image2D fromTex;
   uniform writeonly image2D toTex;

   void main() {
     // Acquire the coordinates to the texel we are to process.
     ivec2 texelCoords = ivec2(gl_GlobalInvocationID.xy);

     // Read the pixel from the first texture.
     vec4 pixel = imageLoad(fromTex, texelCoords);

     // Swap the red and green channels.
     pixel.rg = pixel.gr;

     // Now write the modified pixel to the second texture.
     imageStore(toTex, texelCoords, pixel);
   }

This page does not attempt to teach how to make GLSL compute shaders - please
refer to the GLSL documentation for that information.

Loading a compute shader
------------------------

A compute shader is typically never combined with other types of shaders, and
therefore, loading a compute shader happens via a special call. At present, only
GLSL compute shaders may be loaded.

.. only:: python

   .. code-block:: python

      shader = Shader.load_compute(Shader.SL_GLSL, "compute_shader.glsl")

.. only:: cpp

   .. code-block:: cpp

      PT(Shader) shader;
      shader = Shader::load_compute(Shader::SL_GLSL, "compute_shader.glsl");

The :meth:`.Shader.make_compute()` call can be used to load the shader from a
string instead of a filename.

Dispatching a compute shader
----------------------------

Since a compute shader is not applied to a model but may be invoked arbitrarily,
there has to be a different interface for dispatching a compute shader.
Usually, you would do this by creating a :class:`.ComputeNode` object, which is
inserted into the scene graph. When Panda3D encounters one of these nodes during
the draw process, it will ask OpenGL to dispatch the compute shader assigned to
that node for the given amount of work groups.

.. only:: python

   .. code-block:: python

      # Create the node
      node = ComputeNode("compute")

      # We want to call it on a 512x512 image, keeping in
      # mind that the shader has a work group size of 16x16.
      node.add_dispatch(512 / 16, 512 / 16, 1)

      # Put the node into the scene graph.
      node_path = render.attach_new_node(node)

      # Assign the shader and the shader inputs.
      shader = Shader.load_compute(Shader.SL_GLSL, "compute_shader.glsl")
      node_path.set_shader(shader)
      node_path.set_shader_input("fromTex", myTex1)
      node_path.set_shader_input("toTex", myTex2)

.. only:: cpp

   .. code-block:: cpp

      PT(ComputeNode) node = new ComputeNode("compute");

      // We want to call it on a 512x512 image, keeping in
      // mind that the shader has a work group size of 16x16.
      node->add_dispatch(512 / 16, 512 / 16, 1);

      // Put the node into the scene graph.
      NodePath node_path = render.attach_new_node(node);

      // Assign the shader and the shader inputs.
      PT(Shader) shader = Shader::load_compute(Shader::SL_GLSL, "compute_shader.glsl");
      node_path.set_shader(shader);
      node_path.set_shader_input("fromTex", myTex1);
      node_path.set_shader_input("toTex", myTex2);

The ordering of nodes becomes especially important; you may not want a
procedural texture to be rendered on another node before it is first generated
using a compute shader, for example. You may have to use cull bins or display
regions in order to explicitly control when the :class:`.ComputeNode` is
encountered during the draw process.

Keep in mind that a :class:`.ComputeNode` is never culled away by default, since
it is not associated with any geometry. You may override this behaviour by
assigning a custom :class:`.BoundingVolume`.

However, whereas the :class:`.ComputeNode` interface is useful for operations
that are done every frame, it is not very useful for one-off calls, since it is
cumbersome to add a node to the scene graph only to remove it again in the next
frame. For these use cases, there is a more lower-level operation to dispatch a
compute shader:

.. only:: python

   .. code-block:: python

      # Create a dummy node and apply the shader to it
      shader = Shader.load_compute(Shader.SL_GLSL, "compute_shader.glsl")
      dummy = NodePath("dummy")
      dummy.set_shader(shader)
      dummy.set_shader_input("fromTex", myTex1)
      dummy.set_shader_input("toTex", myTex2)

      # Retrieve the underlying ShaderAttrib
      sattr = dummy.get_attrib(ShaderAttrib)

      # Dispatch the compute shader, right now!
      base.graphicsEngine.dispatch_compute((32, 32, 1), sattr, base.win.get_gsg())

.. only:: cpp

   .. code-block:: cpp

      // Create a dummy node and apply the shader to it
      PT(Shader) shader = Shader::load_compute(Shader::SL_GLSL, "compute_shader.glsl");
      NodePath dummy("dummy");
      dummy.set_shader(shader);
      dummy.set_shader_input("fromTex", myTex1);
      dummy.set_shader_input("toTex", myTex2);

      // Retrieve the underlying ShaderAttrib
      CPT(ShaderAttrib) sattr = DCAST(ShaderAttrib,
        dummy.get_attrib(ShaderAttrib::get_class_type()));

      // Our image has 32x32 tiles
      LVecBase3i work_groups(512/16, 512/16, 1);

      // Dispatch the compute shader, right now!
      GraphicsEngine *engine = GraphicsEngine::get_global_ptr();
      engine->dispatch_compute(work_groups, sattr, win->get_gsg());

Keep in mind that each call to :meth:`~.GraphicsEngine.dispatch_compute()`
causes Panda3D to wait for the current frame to finish rendering. This can be a
very inefficient process, and you are not advised to use this method for
operations that happen on a regular basis.

Image access
------------

Though it is still possible to use regular texture samplers, these aren't very
well suited for many types of image processing. Regular samplers take texture
coordinates in a [0, 1] range, the extra filtering processes add an unnecessary
overhead, and it is not possible to write back to textures using this interface.

However, there is a lower level method to read from and write to texture images.
As you have already seen in the example above, this can be done by using an
``image2D`` declaration instead of ``sampler2D``, and instead of using the
``texture`` family of functions to sample them, you would use ``imageLoad`` and
``imageStore``, which now take integer texel coordinates.

On the application side, however, telling the shader which image to use still
happens in the same way as usual, using the
:meth:`~.NodePath.set_shader_input()` function. However, it is very important
that the texture has a *sized* format, rather than a regular format:

.. only:: python

   .. code-block:: python

      # WRONG
      tex.set_format(Texture.F_rgba)

      # RIGHT
      tex.set_format(Texture.F_rgba8)

      node_path.set_shader_input('fromTex', tex)

.. only:: cpp

   .. code-block:: cpp

      // WRONG
      tex->set_format(Texture::F_rgba);

      // RIGHT
      tex->set_format(Texture::F_rgba8);

      node_path.set_shader_input("fromTex", tex);

At time of writing, it is only possible to access the first mipmap level. It is
not possible to automatically generate the other mipmap levels at the time of
writing, so it is advised to turn mipmap filtering off for the relevant
textures. This is a feature we still mean to add.

Accessing depth textures is impossible via this interface. It is not possible to
write to them, and reading from them has to be done using a ``sampler2D`` or
``sampler2DShadow`` object. You can use the ``texelFetch`` function with
samplers so that you can still use integer texel coordinates.

`Atomic image access <https://www.khronos.org/opengl/wiki/Image_Load_Store#Atomic_operations>`__
is only supported for textures with the integer ``F_r32i`` format. Atomic image
operations are slower, but they come with an extra guarantee that no two
invocations write or read from the image texel at the same time.

It should be noted that this low-level image interface is also supported for
other types of shaders when write access to images is desired.

Texture Clear
-------------

When using a compute shader to operate on a texture image, such as in procedural
texture generation, you may require the texture data to be cleared to an initial
value before it is used. This is now possible using the
:meth:`~.Texture.set_clear_color()` function, which specifies the color that
Panda3D will clear the texture to. This color is used in absence of actual image
data.

.. only:: python

   .. code-block:: python

      # Set up a texture for procedural generation.
      tex = Texture("procedural-normal-map")
      tex.setup_2d_texture(512, 512, Texture.T_unsigned_byte, Texture.F_rgb8)

      # Set the initial color of the texture.
      tex.set_clear_color((0.5, 0.5, 1.0, 0.0))

.. only:: cpp

   .. code-block:: cpp

      // Set up a texture for procedural generation.
      PT(Texture) tex = new Texture("procedural-normal-map");
      tex->setup_2d_texture(512, 512, Texture::T_unsigned_byte, Texture::F_rgb8);

      // Set the initial color of the texture.
      LColor clear_color(0.5f, 0.5f, 1.0f, 0.0f);
      tex->set_clear_color(clear_color);

The initial clear is implicit, but clearing a texture in a later frame requires
explicit use of the :meth:`~.Texture.clear_image()` function, which instructs
Panda3D to clear the texture the next time it is used. It also clears any RAM
images that may have been associated with the texture (similar to
:meth:`~.Texture.clear_ram_image()`).

.. only:: python

   .. code-block:: python

      # Tell Panda to fill the texture with a red color on the GPU.
      tex.set_clear_color((1.0, 0.0, 0.0, 0.0))
      tex.clear_image()

.. only:: cpp

   .. code-block:: cpp

      // Tell Panda to fill the texture with a red color on the GPU.
      LColor clear_color(1.0f, 0.0f, 0.0f, 0.0f);
      tex->set_clear_color(clear_color);
      tex->clear_image();

When doing this, it is recommended that you enable the use of immutable texture
storage, which is an experimental feature that allows Panda3D to allocate the
texture memory beforehand and perform more efficient initial clears. It can be
activated using the following configuration variable::

   gl-immutable-texture-storage true

Memory barriers
---------------

Whenever you write to an image using an ``image2D`` uniform, Panda3D assumes
that the image has been modified by the shader. Panda3D will automatically issue
a memory barrier when the texture is used in a following operation, such as when
the texture is used for rendering or bound to a different shader, to make sure
that the reads and writes are synchronized.

Since Panda3D does not know whether you have actually written to the image or
whether you have declared an image variable as ``coherent``, it may do this too
often, causing slight performance degradation. If you are confident that you
don't need this feature, you may set ``gl-enable-memory-barriers`` variable to
``false`` in your Config.prc to disable this behavior.

Keep in mind that Panda3D's memory barriers only play a role when an image is
modified by one shader and read by another; it does not affect reads and writes
performed within the same shader. It is still necessary to use the appropriate
GLSL qualifiers and memory barrier commands for these purposes.
