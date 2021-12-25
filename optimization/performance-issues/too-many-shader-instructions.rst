.. _too-many-shader-instructions:

Too Many Shader Instructions
============================

.. only:: python

   This can only happen if you have at least one :meth:`.NodePath.set_shader()`
   or :meth:`.NodePath.set_shader_auto()` method call in your application, or
   you are using a postprocessing filter from
   :py:class:`~direct.filter.CommonFilters.CommonFilters`.

.. only:: cpp

   This can only happen if you have at least one :meth:`.NodePath.set_shader()`
   or :meth:`.NodePath.set_shader_auto()` method call in your application.

Too Many Vertex Shader Instructions
-----------------------------------

Although relatively rare, a bottleneck can form in the vertex processing stage
if there are many vertices in the scene and the vertex shaders applied to the
scene are too complex.

Try to simplify your scene. Objects that are far away don't need millions of
vertices. Consider the use of :ref:`level-of-detail` techniques.

Alternatively, try to simplify the vertex shader. Look for calculations that
could instead be done in advance, on the CPU, and passed in as a shader input.

Too Many Fragment/Pixel Shader Instructions
-------------------------------------------

As an easy way to detect whether this is a bottleneck in your application, try
resizing the window. If the framerate heavily varies with the window size or
screen resolution, you're most likely dealing with this problem.

If your frame rate strongly depends on the window or screen resolution, this may
be a hint that your fragment shader has too many instructions. Another problem
is if your depth complexity is too high. Try to look at your scene from
different angles and positions. If your frame rate varies, then the overdraw
from one specific view angle is to high.

Try to minimize the objects Panda3D needs to draw. Use :meth:`.Lens.set_far()`,
or fall back to a simpler fragment shaders for objects that are far away. If an
object is far away from the viewer it doesn't make sense to apply normal
mapping. :class:`.LODNode` or :class:`.FadeLODNode` may help.

If your fragment shader is self-made, then try to offload some work to your
vertex shader.

There is a simple method to test your scene. Replace your whole fragment
shader with the following snippet (if using GLSL):

.. code-block:: glsl

   gl_FragColor = vec4(1.0, 0.0, 1.0, 0.0);

Or the following (if using Cg):

.. code-block:: hlsl

   o_color = float4(1.0, 0.0, 1.0, 0.0);

If the frame rate doesn't change, then it is the depth complexity. It if
changes, it may be the depth complexity or the shader.
