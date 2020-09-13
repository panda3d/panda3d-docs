.. _stereo-display-regions:

Stereo Display Regions
======================

A :class:`.StereoDisplayRegion` is a special kind of DisplayRegion that contains
two views internally: one view for the left eye, and a different view for the
right eye. If you have a special 3-D display device, then Panda can use it to
deliver each view to the appropriate eye.

Alternatively, you can also simply create the two required views
independently, one DisplayRegion for the left eye, and a separate
DisplayRegion for the right eye. However, creating a single
StereoDisplayRegion for both eyes at the same time is often more convenient.

When you call :meth:`window.make_display_region()
<.GraphicsOutput.make_display_region>`, it will implicitly return a
StereoDisplayRegion instead of a regular DisplayRegion if your window or buffer
indicates that it supports stereo output (that is, if window.isStereo() returns
true). There are four ways that you can have a graphics output that supports
stereo output:

(1) You have a special 3-D display device and the drivers to support it, and
you put ``framebuffer-stereo 1`` in your
Config.prc file. This tells Panda to activate the OpenGL interfaces to enable
the 3-D hardware.

(2) You put ``red-blue-stereo 1`` in your
Config.prc file. This tells Panda to render the two different eyes in two
different colors, so that the traditional red-blue (or red-cyan) glasses, for
instance for 3-D comic books, can be used to view the scene in 3-D. Color is
distorted, so it is best if your scene relies on unsaturated color palettes.
Shades of gray work particularly well.

(3) You put ``side-by-side-stereo 1`` in your
Config.prc file. This is similar to red-blue-stereo, above, but the two views
are rendered side-by-side in the same window. This is useful for developing
stereo applications, so you can see each view easily; it may also be useful
for environments such as head-mounted displays where the output spans two
different displays, and each display represents a different eye.

(4) As of Panda3D 1.9.0, you may create a stereo off-screen buffer without
special hardware support, assuming the card supports using multiple render
targets (most modern cards do), by setting the stereo flag in the
:class:`.FrameBufferProperties` object. Panda3D will
automatically designate one of the draw buffers to contain the stereo view for
the other eye. When binding a texture to the color attachment for
render-to-texture, Panda3D will automatically initialize it as a
:ref:`multiview texture <multiview-textures>` containing both left and right
views. This is only supported in OpenGL as of writing.

Using a StereoDisplayRegion
---------------------------

A StereoDisplayRegion actually consists of two ordinary DisplayRegions,
created automatically. If you need to, you can access them individually with
:meth:`sdr.get_left_eye() <.StereoDisplayRegion.get_left_eye>` or
:meth:`sdr.get_right_eye() <.StereoDisplayRegion.get_right_eye>`.

Both the left and the right eye DisplayRegions actually share the same Camera
object. The thing that makes the view different for the left and the right eyes
is the stereo channel setting, which you can set via
:meth:`dr.set_stereo_channel() <.DisplayRegion.set_stereo_channel>`. (You can
change this setting on any DisplayRegion you like; it doesn't have to be a
special StereoDisplayRegion. The only thing that a StereoDisplayRegion does is
it manages the internal left and right DisplayRegions automatically, but there's
no reason you need to use a StereoDisplayRegion if you want to manage them
yourself.)

You can set a DisplayRegion's stereo channel to one of ``Lens.SC_left``,
``Lens.SC_right``, or ``Lens.SC_mono``. The default for a non-stereo
DisplayRegion is ``Lens.SC_mono``, which means the normal view from the center
of the camera. If you set it to either left or right, then the point of view is
slid automatically to the left or right, respectively, according to the stereo
lens parameters.

Setting the stereo channel to left or right also resets the texture view
offset associated with the DisplayRegion: the default tex view offset is 0 for
the left eye, and 1 for the right eye. This allows dual-view stereo textures
to render properly in the DisplayRegion, so that the left view is visible in
the left eye and the right view in the right eye. See
:ref:`Stereo/Multiview Textures <multiview-textures>` for more about this
feature.

The lens parameters can be controlled via
:meth:`.Lens.set_interocular_distance()` and
:meth:`.Lens.set_convergence_distance()`, or by the equivalent Config.prc
settings ``default-iod`` and ``default-converge``. Refer to the following
illustration:

|Stereo Lens Parameters|

In this image, the camera indicated with "C" is the center view, the normal view
from the center of the camera view in the case of ``Lens.SC_mono``. "L" and "R"
represent the left and right points of view for the same camera, which will be
used in the case of ``Lens.SC_left`` or ``Lens.SC_right``. The distance between
these two eyes, line "a" on the image, is the interocular distance, which should
be in the same units as the scene you are viewing.

The gray lines on the image represent the direction the camera appears to be
facing into the scene. Both the left and the right eyes converge together at
one point, which is the convergence distance. This distance is represented by
line "b" on the image. Generally, the objects that are this distance away will
appear to be in the screen plane. Objects that are closer than the convergence
distance will appear to float in front of the screen, while objects that are
further than the convergence distance will appear to be inside the screen.

Note that the default stereo frustums that Panda creates are off-axis
frustums, not toe-in frustums. That is, both the left and the right eyes are
still pointing in the precise same direction as the center camera, but the
frustum is distorted a bit to make objects converge approximately at the
requested distance. This is generally regarded as producing a superior stereo
effect over the more naive toe-in approach, in which the left and right eyes
are simply tilted towards each other to provide the required convergence.

If you require a different stereo frustum--for instance, if you wish to use
toe-in stereo, or some other kind of stereo frustum of your choosing--you may
simply set each DisplayRegion to use its own camera (instead of both sharing
the same camera), and assign the particular frustum you wish to each eye.

.. note::

   Prior to Panda3D 1.9.0, the convergence was being calculated incorrectly.
   It has since been corrected. To restore the legacy behavior you can set the
   ``stereo-lens-old-convergence`` variable to ``true``.

.. |Stereo Lens Parameters| image:: stereo-lens-parameters.jpg
