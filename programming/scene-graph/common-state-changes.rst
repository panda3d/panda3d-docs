.. _common-state-changes:

Common State Changes
====================

This page lists some of the most common changes you can make to a 3D node. This
page is really only a quick cheat-sheet summary: the detailed documentation for
these operations comes later in the manual. A full list of manipulations can be
found on the API reference page for the :class:`.NodePath` class.

Positioning Nodes
-----------------

Two of the most common changes are position and orientation.

.. only:: python

   .. code-block:: python

      myNodePath.setPos(X, Y, Z)
      myNodePath.setHpr(Yaw, Pitch, Roll)

.. only:: cpp

   .. code-block:: cpp

      myNodePath.set_pos(X, Y, Z);
      myNodePath.set_hpr(Yaw, Pitch, Roll);

By default in Panda3D, the X axis points to the right, the Y axis is forward,
and Z is up. An object's rotation is usually described using Euler angles called
Heading, Pitch, and Roll (sometimes called Yaw, Pitch, and Roll in other
packages)--these specify angle rotations in degrees. (If you are more
comfortable using quaternions, the :meth:`~.NodePath.set_quat()` method can be
used to specify the rotation as a quaternion.)

You can change an object's size, either uniformly, or with a different value of
x, y, and z.

.. only:: python

   .. code-block:: python

      myNodePath.setScale(S)

.. only:: cpp

   .. code-block:: cpp

      myNodePath.set_scale(S);

Sometimes it is convenient to adjust a single component individually:

.. only:: python

   .. code-block:: python

      myNodePath.setX(X)
      myNodePath.setY(Y)
      myNodePath.setZ(Z)
      myNodePath.setH(H)
      myNodePath.setP(P)
      myNodePath.setR(R)
      myNodePath.setSx(SX)
      myNodePath.setSy(SY)
      myNodePath.setSz(SZ)

.. only:: cpp

   .. code-block:: cpp

      myNodePath.set_x(X);
      myNodePath.set_y(Y);
      myNodePath.set_z(Z);
      myNodePath.set_h(H);
      myNodePath.set_p(P);
      myNodePath.set_r(R);
      myNodePath.set_sx(SX);
      myNodePath.set_sy(SY);
      myNodePath.set_sz(SZ);

Or all at the same time:

.. only:: python

   .. code-block:: python

      myNodePath.setPosHprScale(X, Y, Z, H, P, R, SX, SY, SZ)

.. only:: cpp

   .. code-block:: cpp

      myNodePath.set_pos_hpr_scale(X, Y, Z, H, P, R, SX, SY, SZ);

You can also query the current transform information for any of the above:

.. only:: python

   .. code-block:: python

      myNodePath.getPos()
      myNodePath.getX()
      myNodePath.getY()
      myNodePath.getZ()

.. only:: cpp

   .. code-block:: cpp

      myNodePath.get_pos();
      myNodePath.get_x();
      myNodePath.get_y();
      myNodePath.get_z();

As a more advanced feature, you may also set or query the position (or any of
the above transform properties) of a particular NodePath with respect to another
one. To do this, specify the relative NodePath as the first parameter:

.. only:: python

   .. code-block:: python

      myNodePath.setPos(otherNodePath, X, Y, Z)
      myNodePath.getPos(otherNodePath)

.. only:: cpp

   .. code-block:: cpp

      myNodePath.set_pos(otherNodePath, X, Y, Z);
      myNodePath.get_pos(otherNodePath);

Putting a NodePath as the first parameter to any of the transform setters or
getters makes it a relative operation. The above :meth:`~.NodePath.set_pos()`
means to set myNodePath to the position (X, Y, Z), relative to otherNodePath--
that is, the position myNodePath would be in if it were a child of otherNodePath
and its position were set to (X, Y, Z). The :meth:`~.NodePath.get_pos()` call
returns the position myNodePath would have if it were a child of otherNodePath.

It is also important to note that you can use the NodePath in its own relative
sets and gets. This may be helpful in situations where you are concerned with
distances. For example:

.. only:: python

   .. code-block:: python

      # Move myNodePath 3 units forward in the x
      myNodePath.setPos(myNodePath, 3, 0, 0)

.. only:: cpp

   .. code-block:: cpp

      // Move myNodePath 3 units forward in the x
      myNodePath.set_pos(myNodePath, 3, 0, 0);

These relative sets and gets are a very powerful feature of Panda's scene graph,
but they can also be confusing; don't worry if it doesn't make sense right now.

The :meth:`~.NodePath.look_at()` method rotates a model to face another object;
that is, it rotates the first object so that its +Y axis points toward the
second object. Note that a particular model might or might not have been
generated with the +Y axis forward, so this doesn't necessarily make a model
"look at" the given object.

.. only:: python

   .. code-block:: python

      myNodePath.lookAt(otherObject)

.. only:: cpp

   .. code-block:: cpp

      myNodePath.look_at(otherObject);

.. only:: python

   .. tip::
      If you have trouble to place, scale or rotate your nodes you can use the
      ``place()`` function to bring up a small GUI which will help you. You need to
      have Tkinter installed to use it.

      .. code-block:: python

         myNodePath.place()

Changing the Parent
-------------------

One of the most fundamental scene graph manipulations is changing a node's
parent. You need to do this at least once after you load a model, to put it
under render for viewing:

.. only:: python

   .. code-block:: python

      myModel.reparentTo(render)

.. only:: cpp

   .. code-block:: cpp

      myModel.reparent_to(window->get_render());

As you become more comfortable with scene graph operations, you may find
yourself taking more and more advantage of a deeply nested scene graph, and you
may start to parent your models to other nodes than just render. Sometimes it is
convenient to create an empty node for this purpose, for instance, to group
several models together:

.. only:: python

   .. code-block:: python

      dummyNode = render.attachNewNode("Dummy Node Name")
      myModel.reparentTo(dummyNode)
      myOtherModel.reparentTo(dummyNode)

.. only:: cpp

   .. code-block:: cpp

      NodePath dummy_node = window->get_render().attach_new_node("Dummy Node Name");
      myModel.reparent_to(dummy_node);
      myOtherModel.reparent_to(dummy_node);

Since a node inherits its position information from its parent node, when you
reparent a node in the scene graph you might inadvertently change its position
in the world. If you need to avoid this, you can use a special variant on
:meth:`~.NodePath.reparent_to()`:

.. only:: python

   .. code-block:: python

      myModel.wrtReparentTo(newParent)

.. only:: cpp

   .. code-block:: cpp

      myModel.wrt_reparent_to(new_parent);

The "wrt" prefix stands for "with respect to". This special method works like
:meth:`~.NodePath.reparent_to()`, except that it automatically recomputes the
local transform on myModel to compensate for the change in transform under the
new parent, so that the node ends up in the same position relative to the world.

Note that the computation required to perform
:meth:`~.NodePath.wrt_reparent_to()` is a floating-point matrix computation and
is therefore inherently imprecise. This means that if you use
:meth:`~.NodePath.wrt_reparent_to()` repeatedly, thousands of times on the same
node, it may eventually accumulate enough numerical inaccuracies to introduce a
slight scale on the object (for instance, a scale of 1, 1, 0.99999); if left
unchecked, this scale could eventually become noticeable.

Beginners tend to overuse this method; you should not use
:meth:`~.NodePath.wrt_reparent_to()` unless there is a real reason to use it.

Changing the Color
------------------

Color changes are another common alteration. Values for color are floating point
numbers from 0 to 1, 0 being black, 1 being white.

.. only:: python

   .. code-block:: python

      myNodePath.setColor(R, G, B, A)

.. only:: cpp

   .. code-block:: cpp

      myNodePath.set_color(R, G, B, A);

If models have textures, they may not be distinguishable or even visible at
certain color settings. Setting the color to white may restore the visibility of
the texture, but it is better to simply clear the current color settings.

.. only:: python

   .. code-block:: python

      myNodePath.clearColor()

.. only:: cpp

   .. code-block:: cpp

      myNodePath.clear_color();

Note the fourth component of color is alpha. This is usually used to indicate
transparency, and it is usually 1.0 to indicate the object is not transparent.
If you set the alpha to a value between 0 and 1, you can fade the object to
invisible. However, in order for the alpha value to be respected, you must first
enable transparency:

.. only:: python

   .. code-block:: python

      myNodePath.setTransparency(TransparencyAttrib.MAlpha)

.. only:: cpp

   .. code-block:: cpp

      myNodePath.set_transparency(TransparencyAttrib::M_alpha);

The parameter to :meth:`~.NodePath.set_transparency()` is usually
``TransparencyAttrib.M_alpha``, which is ordinary transparency. You can also
explicitly turn transparency off with ``TransparencyAttrib.M_none``. (Other
transparency modes are possible, but that is a more advanced topic. Some older
code may pass just 0 or 1 for this parameter, but it is better to name the
mode.) If you don't explicitly enable transparency first, the alpha component of
color may be ignored. Be sure you don't enable transparency unnecessarily, since
it does enable a more expensive rendering mode.

Setting an object's color completely replaces any color on the vertices.
However, if you have created a model with per-vertex color, you might prefer to
modulate the object's color without losing the per-vertex color. For this there
is the :meth:`~.NodePath.set_color_scale()` variant, which multiplies the
indicated color values by the object's existing color:

.. only:: python

   .. code-block:: python

      myNodePath.setColorScale(R, G, B, A)

.. only:: cpp

   .. code-block:: cpp

      myNodePath.set_color_scale(R, G, B, A);

One use of :meth:`~.NodePath.set_color_scale()` is to apply it at the top of the
scene graph (e.g. render) to darken the entire scene uniformly, for instance to
implement a fade-to-black effect.

Since alpha is so important, there is also a method for scaling it without
affecting the other color components:

.. only:: python

   .. code-block:: python

      myNodePath.setAlphaScale(SA)

.. only:: cpp

   .. code-block:: cpp

      myNodePath.set_alpha_scale(SA);

Hiding and Showing
------------------

To temporarily prevent an object from being drawn on all cameras, use
:meth:`~.NodePath.hide()` and :meth:`~.NodePath.show()`:

.. only:: python

   .. code-block:: python

      myNodePath.hide()
      myNodePath.show()

.. only:: cpp

   .. code-block:: cpp

      myNodePath.hide();
      myNodePath.show();

If you want to hide an object for one camera but not another, you can use the
:meth:`~.NodePath.hide()` and :meth:`~.NodePath.show()` commands in conjunction
with the :meth:`.Camera.set_camera_mask()` function:

.. only:: python

   .. code-block:: python

      camera1.node().setCameraMask(BitMask32.bit(0))
      camera2.node().setCameraMask(BitMask32.bit(1))
      myNodePath.hide(BitMask32.bit(0))
      myNodePath.show(BitMask32.bit(1))
      # Now myNodePath will only be shown on camera2...

.. only:: cpp

   .. code-block:: cpp

      camera1.node()->set_camera_mask(BitMask32::bit(0));
      camera2.node()->set_camera_mask(BitMask32::bit(1));
      myNodePath.hide(BitMask32::bit(0));
      myNodePath.show(BitMask32::bit(1));
      // Now myNodePath will only be shown on camera2...

Please note that using hide/show without an argument will mess up any hide/shows
with the argument (show(bit) will not undo a hide()...) To hide an object from
all cameras instead use ``nodepath.hide(BitMask32.all_on())``.

.. only:: python

   To set the camera mask for the default camera use base.cam, not base.camera,
   as base.camera is not an actual camera but a dummy node to hold cameras.
   Please see the camera section for information on how to set up multiple
   cameras.

Any object that is parented to the object that is hidden will also be hidden.
However, you can call :meth:`~.NodePath.show_through()` on the nested element
to force it to show up even if its parent node is hidden.

Hiding a model will only cause it to stop rendering, but other operations (such
as checking for collisions) will still continue to take place. To deactivate a
node and its children entirely, you can call the :meth:`~.NodePath.stash()` and
:meth:`~.NodePath.unstash()` methods instead.

Storing Custom Information
--------------------------

Also, by using the functions :meth:`~.NodePath.set_tag()` and
:meth:`~.NodePath.get_tag()` you can store your own information in key-value
pairs. For example:

.. only:: python

   .. code-block:: python

      myNodePath.setTag("Key", "value")

.. only:: cpp

   .. code-block:: cpp

      myNodePath.set_tag("Key", "value");

.. only:: python

   You can also store Python objects as tags by using the
   :meth:`~.NodePath.set_python_tag()` function with the same arguments.

Removing Nodes
--------------

To completely remove a node from the scene graph you can call the following,
which has the effect of emptying the node and releasing the memory taken up by
the node. Use it only when you have no further use for the node:

.. only:: python

   .. code-block:: python

      myModel.removeNode()

.. only:: cpp

   .. code-block:: cpp

      myModel.remove_node();

Please note, however, that this does not really do much more than just calling
:meth:`~.NodePath.detach_node()` followed by dropping the `myModel` variable.
If the model is still referenced from other places, such as the model pool, it
will still take up memory. If releasing the model from memory is desired, use
the following code:

.. only:: python

   .. code-block:: python

      ModelPool.releaseModel("path/to/model.egg")

.. only:: cpp

   .. code-block:: cpp

      ModelPool::release_model("path/to/model.egg");
