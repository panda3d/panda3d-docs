.. _excessive-fill:

Performance Issue: Excessive Fill
=================================

Transparency
------------

In general, it is better for your graphics card to render the polygons
front-to-back, because a depth test can be used to toss out the occluded
fragments before they are written to the framebuffer.

When enabling the M_alpha or M_dual transparency modes, however, Panda forces
the nodes with this transparency mode to be sorted back-to-front. This is
necessary for alpha blending to work correctly. If you have many occluded
polygons in view, for example thousands of blades of grass that are positioned
behind each other, this may quickly consume your fill rate.

Do not enable transparency modes unless it is necessary, and when you do,
consider using the M_binary mode, which does not require back-to-front sorting.
However, if alpha blending is required and if large areas of the polygons are
fully transparent, using M_dual may provide an improvement over M_alpha.

For a more in-depth explanation on the various transparency modes, see
:ref:`transparency-and-blending`.


