.. _common-state-changes:

Common State Changes
====================

Summary
-------

This page lists some of the most common changes you can make to a 3D node. This
page is really only a quick cheat-sheet summary: the detailed documentation for
these operations comes later in the manual.

State Change Cheat Sheet
------------------------

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
comfortable using quaternions, the ``setQuat()`` method can be used to specify
the rotation as a quaternion.)

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

Also, by using the functions ``setTag()`` and ``getTag()`` you can store your
own information in key value pairs. For example:

.. only:: python

   .. code-block:: python

      myNodePath.setTag("Key", "value")

.. only:: cpp

   .. code-block:: cpp

      myNodePath.set_tag("Key", "value");

.. only:: python

   You can also store Python objects as tags by using the ``setPythonTag``
   function with the same arguments.


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
getters makes it a relative operation. The above ``setPos()`` means to set
myNodePath to the position (X, Y, Z), relative to otherNodePath--that is, the
position myNodePath would be in if it were a child of otherNodePath and its
position were set to (X, Y, Z). The ``getPos()`` call returns the position
myNodePath would have if it were a child of otherNodePath.

It is also important to note that you can use the NodePath in its own relative
sets and gets. This maybe helpful in situations where you are concerned with
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

The ``lookAt()`` method rotates a model to face another object; that is, it
rotates the first object so that its +Y axis points toward the second object.
Note that a particular model might or might not have been generated with the +Y
axis forward, so this doesn't necessarily make a model "look at" the given
object.

.. only:: python

   .. code-block:: python

      myNodePath.lookAt(otherObject)

.. only:: cpp

    .. code-block:: cpp

      myNodePath.look_at(otherObject);

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

The parameter to ``setTransparency()`` is usually
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
is the ``setColorScale()`` variant, which multiples the indicated color values
by the object's existing color:

.. only:: python

   .. code-block:: python

      myNodePath.setColorScale(R, G, B, A)

.. only:: cpp

   .. code-block:: cpp

      myNodePath.set_color_scale(R, G, B, A);


One use of ``setColorScale()`` is to apply it at the top of the scene graph
(e.g. render) to darken the entire scene uniformly, for instance to implement a
fade-to-black effect.

Since alpha is so important, there is also a method for scaling it without
affecting the other color components:

.. only:: python

   .. code-block:: python

      myNodePath.setAlphaScale(SA)

.. only:: cpp

   .. code-block:: cpp

      myNodePath.set_alpha_scale(SA);

To temporarily prevent an object from being drawn on all cameras, use ``hide()``
and ``show()``:

.. only:: python

   .. code-block:: python

      myNodePath.hide()
      myNodePath.show()

.. only:: cpp

   .. code-block:: cpp

      myNodePath.hide();
      myNodePath.show();

If you want to hide an object for one camera but not another, you can use the
``hide()`` and ``show()`` commands in conjunction with the
``camera.setCameraMask()`` function:

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
all cameras instead use ``nodepath.hide(BitMask32.allOn())``.

.. only:: python

   To set the camera mask for the default camera use base.cam, not base.camera,
   as base.camera is not an actual camera but a dummy node to hold cameras.
   Please see the camera section for information on how to set up multiple
   cameras.

Any object that is parented to the object that is hidden will also be hidden.

.. only:: python

   .. tip::
      If you have trouble to place, scale or rotate your nodes you can use the
      ``place()`` function to bring up a small GUI which will help you. You need to
      have Tkinter installed to use it.

      .. code-block:: python

         myNodePath.place()
