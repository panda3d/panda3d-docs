.. _shaders-and-coordinate-spaces:

Shaders and Coordinate Spaces
=============================

The Major Coordinate Spaces
---------------------------

When writing complex shaders, it is often necessary to do a lot of coordinate
system conversion. In order to get this right, it is important to be aware of
all the different coordinate spaces that panda uses. You must know what "space"
the coordinate is in. Here is a list of the major coordinate spaces:

Model Space
   If a coordinate is in model space, then it is relative to the center of the
   model currently being rendered. The vertex arrays are in model space,
   therefore, if you access the vertex position using vtx_position, you have a
   coordinate in model space. Model space is z-up right-handed.
World Space
   If a coordinate is in world space, then it is relative to the scene's origin.
   World space is z-up right-handed.
View Space
   If a coordinate is in view space, then it is relative to the camera. View
   space is z-up right-handed.
API View Space
   This coordinate space is identical to view space, except that the axes may be
   flipped to match the natural orientation of the rendering API. In the case of
   OpenGL, API view space is y-up right-handed. In the case of DirectX, API view
   space is y-up left-handed.
Clip Space
   Panda's clip space is a coordinate system in which (X/W, Y/W) maps to a
   screen pixel, and (Z/W) maps to a depth-buffer value. All values in this
   space range over [-1,1].
API Clip Space
   This coordinate space is identical to clip space, except that the axes may be
   flipped to match the natural orientation of the rendering API, and the
   numeric ranges may be rescaled to match the needs of the rendering API. In
   the case of OpenGL, the (Z/W) values range from [-1, 1]. In the case of
   DirectX, the (Z/W) values range from [0,1].

In OpenGL, "clip space" and "API clip space" are equivalent.

Supplying Translation Matrices to a Shader
------------------------------------------

You can use a shader parameter named "trans_x_to_y" to automatically obtain a
matrix that converts any coordinate system to any other. The words x and y can
be "model," "world," "view," "apiview," "clip," or "apiclip." Using this
notation, you can build up almost any transform matrix that you might need. Here
is a short list of popular matrices that can be recreated using this syntax. Of
course, this isn't even close to exhaustive: there are seven keywords, so there
are 7x7 possible matrices, of which 7 are the identity matrix.

======================== =========================== ======================== ====================
Desired Matrix           Source                      Syntax                   GLSL input
======================== =========================== ======================== ====================
The Modelview Matrix     gsg.getInternalTransform()  trans_model_to_apiview   p3d_ModelViewMatrix
The Projection Matrix    gsg.getProjectionMat()      trans_apiview_to_apiclip p3d_ProjectionMatrix
the DirectX world matrix model.getNetTransform()     trans_model_to_world     p3d_ModelMatrix
the DirectX view matrix  scene.getCsWorldTransform() trans_world_to_apiview   p3d_ViewMatrix
\                        scene.getCameraTransform()  trans_view_to_world
\                        scene.getWorldTransform()   trans_world_to_view
\                        gsg.getExternalTransform()  trans_model_to_view
\                        gsg.getCsTransform()        trans_view_to_apiview
\                        gsg.getInvCsTransform()     trans_apiview_to_view
======================== =========================== ======================== ====================

A note about GLSL inputs
------------------------

The p3d_ModelViewMatrix and p3d_ProjectionMatrix by default transform to and
from "apiview" space, in order to match the behavior of the equivalent
``gl_``-prefixed inputs from earlier GLSL versions. Panda3D traditionally uses a
right-handed Y-up coordinate space for all OpenGL operations because some OpenGL
fixed-function features rely on this space in order to produce the correct
results.

However, if you develop a largely shader-based application and/or don't really
use features like fixed-function sphere mapping, you may choose to disable this
conversion to Y-up space. This will define "apiview" space to be equivalent to
"view" space, which simplifies many things, and will reduce overhead due to
unnecessary coordinate space conversion, especially as "apiclip" and "clip" are
already equivalent in OpenGL as well.

To do this, place ``gl-coordinate-system default`` in your Config.prc file.

Recommendation: Don't use API View Space or API Clip Space
----------------------------------------------------------

The coordinate systems "API View Space" and "API Clip Space" are not very
useful. The fact that their behavior changes from one rendering API to the next
makes them extremely hard to work with. Of course, you have to use the composed
modelview/projection matrix to transform your vertices, and in doing so, you are
implicitly using these spaces. But aside from that, it is strongly recommended
that you not use these spaces for anything else.

Model_of_x, View_of_x, Clip_of_x
--------------------------------

When you use the word "model" in a trans directive, you implicitly mean "the
model currently being rendered." But you can make any nodepath accessible to the
shader subsystem using :meth:`.NodePath.set_shader_input()`:

.. only:: python

   .. code-block:: python

      myhouse = loader.loadModel("myhouse")
      render.setShaderInput("myhouse", myhouse)

.. only:: cpp

   .. code-block:: cpp

      NodePath myhouse = window->load_model(framework.get_models(), "myhouse");
      window->get_render().set_shader_input("myhouse", myhouse);

Then, in the shader, you can convert coordinates to or from the model-space of
this particular nodepath:

.. code-block:: glsl

   uniform float4x4 trans_world_to_model_of_myhouse

or, use the syntactic shorthand:

.. code-block:: glsl

   uniform float4x4 trans_world_to_myhouse

Likewise, you can create a camera and pass it into the shader subsystem. This is
particularly useful when doing shadow mapping:

.. only:: python

   .. code-block:: python

      render.setShaderInput("shadowcam", shadowcam)

.. only:: cpp

   .. code-block:: cpp

      render.set_shader_input("shadowcam", shadowcam);

Now you can transform vertices into the clip-space of the given camera using
this notation:

.. code-block:: glsl

   uniform float4x4 trans_model_to_clip_of_shadowcam

If you transform your model's vertices from model space into the clip space of a
shadow camera, the resulting (X/W,Y/W) values can be used as texture coordinates
to projectively texture the shadow map onto the scene (after rescaling them),
and the (Z/W) value can be compared to the value stored in the depth map (again,
after rescaling it).

Panda does support the notation "trans_x_to_apiclip_of_y", but again, our
recommendation is not to use it.

You can transform a vertex to the view space of an alternate camera, using "view
of x." In fact, this is exactly identical to "model of x," but it's probably
good form to use "view of x" when x is a camera.
