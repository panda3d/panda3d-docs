.. _alpha-testing:

Alpha Testing
=============

The alpha test attribute governs whether or not a part of a node will be
rendered based on the alpha value of its texture. This is particularly useful
for rendering complex geometry into the depth or stencil buffer with a textured
card rather than explicitly creating the shapes. This test is different from
rendering with respect to alpha transparency value. If you set an alpha test
attribute on a node which is rendering into the color buffer, you may be
surprised by the result. All pixels that pass the alpha test will be rendered
just as if no test had been performed, including their appropriate transparency
and pixels that fail the test will not be rendered at all.

Remember to set your attribute's priority to override any other alpha test
attributes inherited from higher in the scene graph. In the following example,
we create an attribute that would cause objects to render only if their alpha
value is below one quarter intensity.

.. only:: python

   .. code-block:: python

      lowPassFilter = AlphaTestAttrib.make(RenderAttrib.MLess,0.25)

.. only:: cpp

   .. code-block:: cpp

      CPT(RenderAttrib) low_pass_filter = AlphaTestAttrib::make(PandaCompareFunc::M_less, 0.25);

And now, this attribute can be added to a node to enable the action.

.. only:: python

   .. code-block:: python

      nodePath.setAttrib(lowPassFilter)

.. only:: cpp

   .. code-block:: cpp

      nodePath.set_attrib(low_pass_filter);


