.. _the-2d-display-region:

The 2D Display Region
=====================

There is one more DisplayRegion that Panda normally creates automatically for
the main window. This is the 2-D DisplayRegion that renders the onscreen GUI
or heads-up display. It is simply another DisplayRegion that covers the entire
screen, like the 3-D DisplayRegion it layers on top of, except that its camera
has an :ref:`Orthographic Lens <orthographic-lenses>` instead of a normal
:ref:`Perspective Lens <lenses-and-field-of-view>`.

.. image:: displayregion-gui.jpg

This is the DisplayRegion associated with render2d, and is normally used to
render all of the gui elements and onscreen text items you may lay on top of
the screen.

If you are creating a secondary window or buffer, and you would like to layer
2-D elements on top of the screen, you can do so by simply creating a 2-D scene
similar to render2d. Some sample code to do so is shown here:

.. only:: python

   .. code-block:: python

      dr = win.makeDisplayRegion()
      dr.sort = 20

      myCamera2d = NodePath(Camera('myCam2d'))
      lens = OrthographicLens()
      lens.setFilmSize(2, 2)
      lens.setNearFar(-1000, 1000)
      myCamera2d.node().setLens(lens)

      myRender2d = NodePath('myRender2d')
      myRender2d.setDepthTest(False)
      myRender2d.setDepthWrite(False)
      myCamera2d.reparentTo(myRender2d)
      dr.setCamera(myCamera2d)

.. only:: cpp

   .. code-block:: cpp

      PT(DisplayRegion) dr = win->make_display_region();
      dr->set_sort(20);

      NodePath myCamera2d(new Camera("myCam2d"));
      PT(OrthographicLens) lens = new OrthographicLens;
      lens->set_film_size(2, 2);
      lens->set_near_far(-1000, 1000)
      ((Camera *)myCamera2d.node())->set_lens(lens);

      NodePath myRender2d("myRender2d");
      myRender2d.set_depth_test(false);
      myRender2d.set_depth_write(false);
      myCamera2d.reparent_to(myRender2d);
      dr->set_camera(myCamera2d)

The first group of commands creates a new DisplayRegion on the window and sets
its sort value to 20, so that it will be drawn after the main DisplayRegion has
been drawn. This is important in order to layer text on top of the 3-D scene,
of course.

The second group of commands creates a camera with an OrthographicLens. The
lens is created with a wide near/far clipping plane: -1000 to 1000. This
probably doesn't matter too much since we expect that everything we parent to
this scene graph will have a Y value of 0 (which is easily between -1000 and
1000), but this allows us to accept a wide range of Y values.

The third group of commands sets up the myRender2d scene graph. It is just an
ordinary node, with a few properties set on it, and the 2-D camera we have just
created attached to it. We turn off the depth test and depth write properties
because these are not important for a 2-D scene graph, and we don't want them
to get in the way of our gui elements.

.. only:: python

   DirectGui in your new window
   ----------------------------

   Note that if you wish to create any :ref:`DirectGui <directgui>` elements,
   like buttons or other clickable widgets, in the new 2-D scene graph, and
   interact with them, you have just a bit more set-up to do. DirectGui has a
   special mechanism to connect it to the mouse pointer, which requires that all
   of its interactive objects be attached directly or indirectly to a PGTop
   node. In the default main window, this PGTop node is aspect2d, a special node
   created both to compensate for the non-square aspect ratio of the window, and
   also to be the special PGTop node required by DirectGui. If you are creating
   your own 2-D scene graph, you can create your own aspect2d node something
   like this:

   .. code-block:: python

      aspectRatio = base.getAspectRatio()
      myAspect2d = myRender2d.attachNewNode(PGTop('myAspect2d'))
      myAspect2d.setScale(1.0 / aspectRatio, 1.0, 1.0)
      myAspect2d.node().setMouseWatcher(base.mouseWatcherNode)

   If this is for a different window than base.win, you will probably need to
   also create your own MouseWatcher, other than base.mouseWatcherNode, to
   manage the mouse associated with your new window. See elsewhere for more
   information about this.
