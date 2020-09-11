.. _orthographic-lenses:

Orthographic Lenses
===================

The previous page described the :class:`.PerspectiveLens` class, and the various
properties of a perspective lens, especially its field of view. There is
another kind of lens that is frequently used in 3-D rendering, but it doesn't
have a field of view in the same sense at all. This is an orthographic lens.

|Lens tutorial, orthographic lenses|

In an orthographic lens, there is no perspective--parallel lines viewed by the
lens don't converge; instead, they remain absolutely parallel in the image.
While a :class:`.PerspectiveLens` closely imitates the behavior of a real,
physical camera lens, there is no real lens that does what an
:class:`.OrthographicLens` does. An :class:`.OrthographicLens`, therefore, is
most useful for special effects, where you want that unnatural look, or to
emulate the so-called 2½-D look of several popular real-time strategy games, or
strictly to render 2-d objects that shouldn't have any perspective anyway. In
fact, the default camera created for the render2d scene graph, which is used
to draw all of the onscreen GUI elements in Panda, uses an OrthographicLens.

Since an orthographic lens doesn't have a field of view angle, the
:meth:`lens.set_fov() <.Lens.set_fov>` method does nothing. To
adjust the amount that the orthographic lens sees, you must adjust its film
size. And unlike a :class:`.PerspectiveLens`, the film size units are not
arbitrary--for an :class:`.OrthographicLens`, the film size should be specified
in spatial units, the same units you used to model your scene. For instance, the
film size of the :class:`.OrthographicLens` in the above illustration was set
with the call :meth:`lens.set_film_size(20, 15) <.Lens.set_film_size>`, which
sets the film size to 20 feet by 15 feet--because the scene is modeled in feet,
and the panda is about 12 feet tall.

Another nice property of an orthographic lens is that the near distance does
not have to be greater than zero. In fact, it can be negative--you can put the
near plane behind the camera plane, which means the camera will see objects
behind itself. The :class:`.OrthographicLens` for :py:obj:`~builtins.render2d`
is set up with :meth:`.set_near_far(-1000, 1000) <.Lens.set_near_far>`, so it
will render any objects with a Y value between -1000 and 1000 (assuming the
default Z-up coordinate system). (Of course, in render2d almost all objects have
a Y value of 0, so it doesn't matter much.)

If you like, you can change the default camera to use an orthographic lens
with something like this:

.. only:: python

   .. code-block:: python

      lens = OrthographicLens()
      lens.setFilmSize(20, 15)  # Or whatever is appropriate for your scene
      base.cam.node().setLens(lens)

.. only:: cpp

   .. code-block:: cpp

      PT(OrthographicLens) lens = new OrthographicLens();
      lens->set_film_size(20, 15); // Or whatever is appropriate for your scene
      window->get_camera(0)->set_lens(lens);

Note that using an orthographic lens can be nonintuitive at times--for
instance, objects don't get larger as you come closer to them, and they don't
get smaller as you get farther away--so it may be impossible to tell your
camera is even moving!

.. |Lens tutorial, orthographic lenses| image:: lens-tutorial-orthographic.jpg
