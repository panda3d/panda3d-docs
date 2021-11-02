.. _stencil-attribute:

Stencil Attribute
=================

The :class:`.StencilAttrib` is used for testing and writing to the stencil
buffer. Note that both of these actions can be performed simultaneously with a
single StencilAttrib.

The stencil buffer is an ancillary graphics buffer, in addition to the more
well-known color and depth buffers. It provides a per-pixel mask for the
rendering pipeline which can be exploited to selectively render objects or parts
of objects. Typical applications of the stencil buffer include binary masking,
shadowing and planar reflections.

Usually, using the stencil buffer involves creating some objects which are not
rendered into the color buffer. Their contribution to the rendered scene is to
provide an invisible boundary that can be used to turn color buffer rendering on
and off for other objects in the scene. Think of it as a cardboard cut-out
through which the world is viewed.

During a stencil comparison, the StencilAttrib's reference value is compared
against the value stored in the stencil buffer. The order matters here. For
example, consider comparison function StencilAttrib.SCFGreaterThan with
reference value r=1. A pixel passes the stencil test if r > S\ :sub:`p`, where
S\ :sub:`p` is the value in the stencil buffer at pixel p. Objects contributing
values to the stencil buffer that will be read by other StencilAttributes'
comparison functions must be rendered first, or unexpected results will occur.
See :ref:`how-to-control-render-order`.

The stencil buffer is disabled by default. In order to use StencilAttribs, you
must add the following line to your config.prc file::

   framebuffer-stencil true

StencilAttribs are defined exclusively by their constructor functions, so let's
examine one to understand what each part does. The following code creates an
attribute which tells an object to render only if the stencil buffer is exactly
1, and does not itself modify the stencil buffer.

.. code-block:: python

   stencilReader =
       StencilAttrib.make(1, StencilAttrib.SCFEqual,StencilAttrib.SOKeep,
                             StencilAttrib.SOKeep,StencilAttrib.SOKeep,1,1,0)

The first parameter is a boolean. If this parameter is zero, the StencilAttrib
is not processed. Next is the comparison function this attribute uses, in this
case Equal. The next three parameters determine what happens to the stencil
buffer depending on the result of the comparison. We'll get to these in a
minute. The three Keep values tell this attribute never to modify the values in
the buffer. Next is the reference value for the comparison function. Before the
reference value is passed to the comparison function, however, it is bitwise
ANDed with a mask. In our case, we're interested in reading but not in writing
to the stencil buffer, so we pass 1 and 0 for the read and write masks,
respectively. These masks are the last two parameters for the StencilAttrib.

Next, we'll look at a stencil attribute that writes to the stencil buffer.
Presumably, these two functions will work in tandem to create an effect.

.. code-block:: python

   constantOneStencil =
       StencilAttrib.make(1, StencilAttrib.SCFAlways,StencilAttrib.SOZero,
                             StencilAttrib.SOReplace,StencilAttrib.SOReplace,1,0,1)

Again we start by enabling the attribute. The comparison function here is
Always, meaning that the test passes no matter the parameters. Next is the
operation to perform on the stencil buffer if the test fails (which in this case
will never happen) -- we set the stencil buffer value to zero. The next
parameter determines what should happen if the stencil function passes, but the
depth test fails, and finally, what should happen if both the stencil and depth
tests pass. In our case we want to set the value of the stencil buffer whether
we pass the depth test or not, so both are set to Replace. The reference value
to set in the stencil buffer is 1. We're writing regardless of what's in the
buffer already, so we'll set the read and write masks to 0 and 1, respectively.

Now we can add these attributes to nodes in the scene to exploit the effect.
Here is the entire script.

.. code-block:: python

   from panda3d.core import *

   # Do this before the next import:
   loadPrcFileData("", "framebuffer-stencil #t")

   import direct.directbase.DirectStart

   constantOneStencil = StencilAttrib.make(1,StencilAttrib.SCFAlways,
   StencilAttrib.SOZero,StencilAttrib.SOReplace,
   StencilAttrib.SOReplace,1,0,1)

   stencilReader = StencilAttrib.make(1,StencilAttrib.SCFEqual,
   StencilAttrib.SOKeep, StencilAttrib.SOKeep,
   StencilAttrib.SOKeep,1,1,0)

   cm = CardMaker("cardmaker")
   cm.setFrame(-.5,.5,-.5,.5)

   # To rotate the card to face the camera, we create
   # it and then parent it to the camera.
   viewingSquare = render.attachNewNode(cm.generate())
   viewingSquare.reparentTo(base.camera)
   viewingSquare.setPos(0, 5, 0)

   viewingSquare.node().setAttrib(constantOneStencil)
   viewingSquare.node().setAttrib(ColorWriteAttrib.make(0))
   viewingSquare.setBin('background',0)
   viewingSquare.setDepthWrite(0)

   view = loader.loadModel("panda")
   view.reparentTo(render)
   view.setScale(3)
   view.setY(150)
   view.node().setAttrib(stencilReader)

   base.run()

You can get a little more insight into stencils in this thread on the forums:
https://discourse.panda3d.org/t/using-stencils-solved/7409/7
