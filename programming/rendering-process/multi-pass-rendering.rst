.. _multi-pass-rendering:

Multi-Pass Rendering
====================

Multi-Pass Rendering
--------------------

Sometimes you may need to draw the same scene more than once per frame, each
view looking different. This is where multi-pass rendering comes into play.

The easiest way to do implement multi-pass rendering is to render offscreen to
a separate buffer. You:

#. setup a GraphicsBuffer object
#. create a camera for it and
#. place the camera in the scene.

However, this method assumes you have two independent scene graphs. If you use
this method to render the same scene graph, it is only useful for showing the
scene from a different camera view. To actually make the scenes have different
:ref:`RenderStates <render-attributes>` (i.e. one without lighting, one with
lighting) you must also change how each Camera renders the scene.

Each Camera node has a function called ``setInitialState(state)``. It makes
every object in the scene get drawn as if the top node in its scene graph has
``state`` as its :ref:`RenderState <render-attributes>`. This still means that
:ref:`attributes <render-attributes>` can be changed/overridden after the Camera
has been put on a scene.

.. code-block:: python

   # This makes everything drawn by the default camera use myNodePath's
   # RenderState.  Note:  base.cam is not base.camera.  If you have an
   # reference to base.camera, use base.camera.node().
   base.cam.setInitialState(myNodePath.getState())

You may, however, want more control over what RenderState gets assigned to each
node in the scene. You can do this using the Camera class methods
``setTagStateKey(key)`` and ``setTagState(value, state)``. For any NodePaths
that you want to recieve special treatment you call ``setTag(key, value)`` (See
:ref:`common-state-changes`). Now, anytime the Camera sees a NodePath with a tag
named ``key`` the Camera assigns it whatever RenderState is associated with
``value``.

.. code-block:: python

   # Assume we have Shader instances toon_shader and blur_shader
   # and we have a Camera whose NodePath is myCamera

   # Create a temporary node in order to create a usable RenderState.
   tempnode = NodePath("temp node")
   tempnode.setShader(toon_shader)
   base.cam.setTagStateKey("Toon Shading")
   base.cam.setTagState("True", tempnode.getState())

   tempnode = NodePath("temp node")
   tempnode.setShader(blur_shader)
   myCamera.node().setTagStateKey("Blur Shading")
   myCamera.node().setTagState("True", tempnode.getState())

   # this makes myNodePath and its children get toonShaded
   # when rendered by the default camera
   myNodePath.setTag("Toon Shading", "True")
   # ....
   # now if you want myNodePath to be blurred when seen by myCamera,
   # it's as easy as adding a tag
   myNodePath.setTag("Blur Shading", "True")

For a full guide about Multi-Pass rendering in Panda3D, please read the
`Howto on Multipass Rendering <https://raw.githubusercontent.com/panda3d/panda3d/v1.9.4/panda/src/doc/howto.use_multipass.txt>`__
of the original Panda3D documentation.
