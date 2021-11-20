.. _rendering-images:

Rendering Images
================

In order to render an image, it is necessary to first create a flat piece of
geometry consisting of two triangles (usually called a *quad* or a *card*) and
then apply the desired image as a texture. Panda3D provides convenience methods
for creating such a card automatically.

.. only:: python

   .. _onscreenimage:

   OnscreenImage
   -------------

   .. only:: cpp

      .. note::

         This convenience class is only available in the Python API.

   Just like :ref:`onscreentext`, you can use OnscreenImage as a quick way to put
   an image onscreen. Use an OnscreenImage whenever you want a quick way to display
   an ordinary image without a lot of fancy requirements.

   .. code-block:: python

      from direct.gui.OnscreenImage import OnscreenImage
      imageObject = OnscreenImage(image='myImage.jpg', pos=(-0.5, 0, 0.02))

   If you want, you can change the image into another one using setImage():

   .. code-block:: python

      imageObject.setImage('myImage2.jpg')

   When you want to take the image away, use:

   .. code-block:: python

      imageObject.destroy()

   A full list of arguments that can be passed to the constructor is available
   on the :py:class:`~.direct.gui.OnscreenText.OnscreenText` page of the API
   reference.

Generating a card
-----------------

:class:`.CardMaker` is a convenience class that can be used to generate a card
with arbitrary dimensions. It can be used for rendering an image in the 3D or 2D
scene. The image should be loaded as a texture and then applied to the generated
card:

.. only:: python

   .. code-block:: python

      cm = CardMaker('card')
      card = render2d.attachNewNode(cm.generate())

      tex = loader.loadTexture('maps/noise.rgb')
      card.setTexture(tex)

.. only:: cpp

   .. code-block:: cpp

      CardMaker cm("card");
      NodePath card = render2d.attach_new_node(cm.generate());

      PT(Texture) tex = TexturePool::load_texture("maps/noise.rgb");
      card.set_texture(tex);

This will generate a card that causes the image to be stretched to cover the
entire screen. To preserve the aspect ratio of the image, it is necessary to
instead parent it to "aspect2d", as well as use either
:meth:`.NodePath.set_scale()` or :class:`.CardMaker.set_frame()` to adjust the
card dimensions to match the aspect ratio of the image.

See the :class:`.CardMaker` class in the API reference for a full list of
methods to configure the generated card.

Transparency
------------

To enable transparency in images, you must tell Panda3D to enable a transparency
mode on the object, otherwise the transparent parts of the image will show up as
black. This can be done using the following code:

.. only:: python

   .. code-block:: python

      from panda3d.core import TransparencyAttrib

      image = OnscreenImage(image='myImage.png', pos=(0, 0, 0))
      image.setTransparency(TransparencyAttrib.MAlpha)

.. only:: cpp

   .. code-block:: cpp

      card.set_transparency(TransparencyAttrib::M_alpha);

See the section on :ref:`transparency-and-blending` for some caveats about
rendering objects with transparency.
