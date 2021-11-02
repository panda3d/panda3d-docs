.. _fog:

Fog
===

Basic Fog
---------

To turn on fog, create an object of class :class:`.Fog`, and then apply it using
the :meth:`.NodePath.set_fog` method:

.. only:: python

   .. code-block:: python

      myFog = Fog("Fog Name")
      myFog.setColor(R, G, B)
      myFog.setExpDensity(Float 0 to 1)
      render.setFog(myFog)

.. only:: cpp

   .. code-block:: cpp

      PT(Fog) my_fog = new Fog("Fog Name");
      my_fog->set_color(R, G, B);
      my_fog->set_exp_density(Float 0 to 1);
      render.set_fog(my_fog);

However, there is more here than meets the eye. We have created a fog node,
which goes into the scene graph. Therefore, the fog has a position, a place
where the fog is (conceptually) thickest.

If the fog object is not parented into the scene graph (in the example above,
for instance), then the fog's position is ignored, and the fog is
camera-relative. Likewise, if the fog is exponential, the fog's position is
ignored, and the fog is camera-relative.

The :meth:`~.NodePath.set_fog` method creates a fog attribute object.
Like any :ref:`Render Attribute <render-attributes>`, the fog attribute affects
the node that it is attached to, and any nodes below it in the scene graph. So
you can easily cause only a subset of the objects (or just a single model) to be
affected by the fog, by calling :meth:`~.NodePath.set_fog` on the root of
the subgraph you want to be affected.
To remove the fog attribute later, use the :meth:`~.NodePath.clear_fog` method:

.. only:: python

   .. code-block:: python

      render.clearFog()

.. only:: cpp

   .. code-block:: cpp

      render.clear_fog();

While you have fog in effect, it is often desirable to set the background color
to match the fog:

.. only:: python

   .. code-block:: python

      base.setBackgroundColor(myFogColor)

.. only:: cpp

   .. code-block:: cpp

      window->get_display_region_3d()->set_clear_color(myFogColor);

Fog Modes
---------

There are three fog modes in Panda: ``Fog.MExponential``,
``Fog.MExponentialSquared`` and ``Fog.MLinear``. You can switch the mode of a
:class:`.Fog` object using :meth:`fog.get_mode() <.Fog.get_mode>` and
:meth:`fog.set_mode(Fog.Mode) <.Fog.set_mode>`.
This explicit mode switching isn't normally necessary, as
:class:`.Fog` methods implicitly switch the mode for you.

A :class:`.Fog` object in Panda3D is a node that can be parented into the scene
graph with a position, colour and orientation like any other node (importantly,
:class:`.Fog` is a subclass of :class:`.PandaNode`, not of :class:`.NodePath`)
(do :class:`.Fog` nodes have a scale?).

The position of a :class:`.Fog` node in the scene graph does not determine which
objects the fog affects, it determines the origin and direction of the fog when
it is in linear mode. When a fog node is in exponential mode its position and
orientation in the scene graph are irrelevant. Either way, a
:class:`.Fog` node must be activated by calling
:meth:`nodePath.set_fog(fogNode) <.NodePath.set_fog>` on some :class:`.NodePath`
in the scene graph.
Which :class:`.NodePath` you call the :meth:`~.NodePath.set_fog` method on
determines which parts of the scene will be fogged: that :class:`.NodePath` and
all its children.

Linear Fog
~~~~~~~~~~

This is the default mode. In this mode the position and orientation of a
:class:`.Fog` node are important.
A linear-mode :class:`.Fog` node must first be parented into the scene graph,
then activated by calling :meth:`set_fog(fogNode) <.NodePath.set_fog>` on some
:class:`.NodePath` in the scene graph.

Setup a linear fog node at the origin:

.. only:: python

   .. code-block:: python

      color = (0.5, 0.8, 0.8)
      linfog = Fog("A linear-mode Fog node")
      linfog.setColor(*color)
      linfog.setLinearRange(0, 320)
      linfog.setLinearFallback(45, 160, 320)
      render.attachNewNode(linfog)
      render.setFog(linfog)

.. only:: cpp

   .. code-block:: cpp

      LColor color(0.5,0.8,0.8);
      PT(Fog) linfog = new Fog("A linear-mode Fog node");
      linfog->set_color(color);
      linfog->set_linear_range(0, 320);
      linfog->set_linear_fallback(45, 160, 320);
      render.attach_new_node(linfog);
      render.set_fog(linfog);

In linear mode, the onset and opaque distances of the fog are defined as offsets
along the local forward (+Y) axis of the fog node. The onset distance is the
distance from the fog node at which the fog will begin to have effect, and the
opaque distance is the distance from the fog node at which the fog will be
completely opaque. From reading the API page for the :class:`.Fog`
class, it sounds as if beyond this opaque point there is no fog (rather than
continuing opaque fog up to the location of the fog node as you might expect):
"the fog will be rendered as if it extended along the vector from the onset
point to the opaque point."

These settings can be modified using the methods
:meth:`~.Fog.get_linear_onset_point()`, :meth:`~.Fog.get_linear_opaque_point()`,
:meth:`~.Fog.set_linear_onset_point()`, :meth:`~.Fog.set_linear_opaque_point()`
and :meth:`~.Fog.set_linear_range()` of :class:`.Fog`.

There is a hardware issue with rendering fog which means that linear fog can
break down and vanish depending on the angle from which it is viewed:

   "the underlying fog effect supported by hardware is generally only
   one-dimensional, and must be rendered based on linear distance from the
   camera plane. Thus, this in-the-world effect is most effective when the fog
   vector from onset point to opaque point is most nearly parallel to the
   camera’s eye vector. As the angle between the fog vector and the eye vector
   increases, the accuracy of the effect diminishes, up to a complete
   breakdown of the effect at a 90 degree angle."

The :class:`.Fog` method
:meth:`set_linear_fallback(float angle, float onset, float opaque) <.Fog.set_linear_fallback>`
defines how the fog should be rendered when the fog effect is diminished in this
way. ``angle`` is the minimum viewing angle (angle between the camera direction
and fog direction) at which the fallback effect will be employed. ``onset`` and
``opaque`` specify camera-relative onset and opaque distances that will be
fallen back on, overriding the :class:`.Fog` node’s own onset and
opaque distances.

The linear fallback workaround will only look good in certain situations, for
example when the fog is deep inside a dark cave. So in general, exponential mode
fog is more useful than the default linear mode fog.

Exponential Fog
~~~~~~~~~~~~~~~

In exponential fog mode the position and orientation of your fog node in the
scene graph and the onset and opaque points are ignored (in fact you don’t even
have to put your fog node in the scene graph). Instead, fog is rendered camera
relative according to a density factor: the fog begins at the camera and
continues to infinity, with an exponentially increasing density determined by
the density factor. The fog moves with the camera as the camera’s position and
orientation changes:

   "the onset point and opaque point are not used, and the fog effect is based
   on the value specified to :meth:`~.Fog.set_exp_density()`, and it doesn’t
   matter to which node the fog object is parented, or if it is parented
   anywhere at all."

The :meth:`.Fog.set_exp_density()` method determines the density value used for
exponential fog calculations.  The below example uses it to set up some scene-
wide exponential fog:

.. only:: python

   .. code-block:: python

      color = (0.5, 0.8, 0.8)
      expfog = Fog("Scene-wide exponential Fog object")
      expfog.setColor(*color)
      expfog.setExpDensity(0.005)
      render.setFog(expfog)
      base.setBackgroundColor(*color)

.. only:: cpp

   .. code-block: cpp

      LColor color(0.5, 0.8, 0.8, 1);
      PT(Fog) expfog = Fog("Scene-wide exponential Fog object");
      expfog->set_color(color);
      expfog->set_exp_density(0.005);
      window->get_render().set_fog(expfog);
      window->get_display_region_3d()->set_clear_color(color);

The last line in the sample above doesn't actually affect the fog, however, it
generally looks better if the scene background color matches the color of the
fog.

Since :meth:`~.NodePath.set_fog()` is called on ``render`` it affects the entire
scene. :meth:`~.NodePath.set_fog()` can just as easily be called on some other
:class:`.NodePath` and will affect only that :class:`.NodePath` and its
children.

The exponential fog effect can be turned off again using
:meth:`~.NodePath.clear_fog()`:

.. only:: python

   .. code-block:: python

      render.clearFog()

.. only:: cpp

   .. code-block:: cpp

      render.clear_fog();
