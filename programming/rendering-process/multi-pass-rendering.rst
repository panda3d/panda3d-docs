.. _multi-pass-rendering:

Multi-Pass Rendering
====================

Sometimes you may need to draw the same scene more than once per frame, each
view looking different. This is where multi-pass rendering comes into play.

The easiest way to do implement multi-pass rendering is to render offscreen to
a separate buffer. You:

#. set up a :class:`.GraphicsBuffer` object
#. create a camera for it and
#. place the camera in the scene.

However, this method assumes you have two independent scene graphs. If you use
this method to render the same scene graph, it is only useful for showing the
scene from a different camera view. To actually make the scenes have different
:ref:`RenderStates <render-attributes>` (i.e. one without lighting, one with
lighting) you must also change how each Camera renders the scene.

Each :class:`.Camera` node has a function called :meth:`set_initial_state(state)
<.Camera.set_initial_state>`. It makes every object in the scene get drawn as if
the top node in its scene graph has ``state`` as its :class:`.RenderState`.
This still means that :ref:`attributes <render-attributes>` can be
changed/overridden after the :class:`.Camera` has been put on a scene.

.. only:: python

   .. code-block:: python

      # This makes everything drawn by the default camera use myNodePath's
      # RenderState.
      base.cam.node().setInitialState(myNodePath.getState())

.. only:: cpp

   .. code-block:: cpp

      // This makes everything drawn by the default camera use myNodePath's
      // RenderState.
      window->get_camera(0)->set_initial_state(myNodePath.get_state());

You may, however, want more control over what :class:`.RenderState` gets
assigned to each node in the scene. You can do this using the :class:`.Camera`
methods :meth:`set_tag_state_key(key) <.Camera.set_tag_state_key>` and
:meth:`set_tag_state(value, state) <.Camera.set_tag_state>`. For any
:class:`.NodePath`\ s that you want to recieve special treatment you call
:meth:`set_tag(key, value) <.NodePath.set_tag>` (see
:ref:`common-state-changes`). Now, any time the camera sees an object with a tag
named ``key``, it is assigned whatever state is associated with ``value``.

.. only:: python

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

.. only:: cpp

   .. code-block:: cpp

      // Assume we have Shader instances toon_shader and blur_shader
      // and we have a Camera whose NodePath is myCamera

      // Create a temporary node in order to create a usable RenderState.
      NodePath tempnode("temp node");
      tempnode.set_shader(toon_shader);
      window->get_camera(0)->set_tag_state_key("Toon Shading");
      window->get_camera(0)->set_tag_state("True", tempnode.get_state());

      NodePath tempnode("temp node");
      tempnode.set_shader(blur_shader);
      ((Camera *)myCamera.node())->set_tag_state_key("Blur Shading");
      ((Camera *)myCamera.node())->set_tag_state("True", tempnode.get_state());

      // this makes myNodePath and its children get toonShaded
      // when rendered by the default camera
      myNodePath.set_tag("Toon Shading", "True");
      // ....
      // now if you want myNodePath to be blurred when seen by myCamera,
      // it's as easy as adding a tag
      myNodePath.set_tag("Blur Shading", "True");

For a full guide about Multi-Pass rendering in Panda3D, please read the
`Howto on Multipass Rendering <https://raw.githubusercontent.com/panda3d/panda3d/release/1.10.x/panda/src/doc/howto.use_multipass.txt>`__
of the original Panda3D documentation.
