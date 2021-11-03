.. _creating-new-textures-from-scratch:

Creating New Textures from Scratch
==================================

The PNMImage Class
------------------

This class is how Panda3D handles regular images (.gif, .jpg, and the like).
This class allows you to manipulate individual pixels of the image. You can load
existing images using the function :meth:`read(filename) <.PNMImage.read>` where
``filename`` is the path to the image file. Or, you can create a brand new image
from scratch, by passing the x, y size to the constructor.

.. only:: python

   .. code-block:: python

      myImage = PNMImage()
      myImage.read("testImg.png")

      myEmptyImage = PNMImage(256, 256)

.. only:: cpp

   .. code-block:: cpp

      PNMImage my_image;
      my_image.read(Filename("testImg.png"));

      PNMImage my_empty_image(256, 256);

You can get the size of the image you have read using the
:meth:`~.PNMImage.get_x_size()` and :meth:`~.PNMImage.get_y_size()` methods.
Although you cannot change the size of an image directly, you can rescale an
image by filtering it into a larger or smaller PNMImage:

.. only:: python

   .. code-block:: python

      fullSize = PNMImage(Filename("testImg.png"))
      reduced = PNMImage(256, 256)
      reduced.gaussianFilterFrom(1.0, fullSize)

.. only:: cpp

   .. code-block:: cpp

      PNMImage full_size(Filename("testImg.png"));
      PNMImage reduced(256, 256);
      reduced.gaussian_filter_from(1.0, full_size);

You can get individual RGB values using the
:meth:`get_red(x, y) <.PNMImage.get_red>`,
:meth:`get_green(x, y) <.PNMImage.get_green>`,
:meth:`get_blue(x, y) <.PNMImage.get_blue>` or
:meth:`get_red_val(x, y) <.PNMImage.get_red_val>`,
:meth:`get_green_val(x, y) <.PNMImage.get_green_val>`,
:meth:`get_blue_val(x, y) <.PNMImage.get_blue_val>` methods, where x and y are
the coordinates of the pixel to sample (the upper-left corner is ``0, 0``
whereas the lower-right corner is ``size.x - 1, size.y - 1``).
The difference between these functions is that the regular getters functions
return a number between 0.0 and 1.0, while the ones marked with "val" return
their raw value as an integer. For example, if your image uses 8-bit-per-channel
color, calling :meth:`~.PNMImage.get_green_val()` will return 255 for a fully
green pixel whereas calling :meth:`~.PNMImage.get_green()` will return 1.0.
You can also get all the RGB information at the same time using
:meth:`get_xel(x, y) <.PNMImage.get_xel>` and
:meth:`get_xel_val(x, y) <.PNMImage.get_xel_val>`, which return a 3-component
vector containing the red, green and blue channels, respectively.

.. only:: python

   .. code-block:: python

      # The pixel at 0,0 is red and we're using 8-bit color
      myImage.getRedVal(0, 0) # Returns 255
      myImage.getRed(0, 0) # Returns 1

      colors = myImage.getXelVal(0,0) # Returns (255,0,0)
      colorVal = myImage.getXel(0,0) # Returns (1,0,0)

The methods for setting pixel information are
:meth:`set_red(x, y, value) <.PNMImage.set_red>`,
:meth:`set_green(x, y, value) <.PNMImage.set_green>`,
:meth:`set_blue(x, y, value) <.PNMImage.set_blue>`,
:meth:`set_xel(x, y, color) <.PNMImage.set_xel>`, or
:meth:`set_red_val(x, y, value) <.PNMImage.set_red_val>`,
:meth:`set_green_val(x, y, value) <.PNMImage.set_green_val>`,
:meth:`set_blue_val(x, y, value) <.PNMImage.set_blue_val>`,
:meth:`set_xel_val(x, y, color) <.PNMImage.set_xel_val>`.
The same as above applies regarding the dichotomy between the regular setters
and the ones marked with "val". You can also fill an image with a color by using
:meth:`fill(r, g, b) <.PNMImage.fill>` and
:meth:`fill_val(r, g, b) <.PNMImage.fill_val>`.

.. only:: python

   .. code-block:: python

      myImage.setGreenVal(0, 0, 255) # If pixel (0, 0) was red before, now it is yellow
      myImage.setBlue(0, 0, 1) # Pixel (0, 0) is now white

      gray = Vec3(0.5, 0.5, 0.5)

      # Both of these set the origin to gray
      myImage.setXelVal(0, 0, gray * 255)
      myImage.setXel(0, 0, gray)

      # Makes every pixel red
      myImage.fillVal(255, 0, 0)
      # Makes every pixel green
      myImage.fill(0, 1, 0)

There are also gets and sets for the alpha channel using the same interface as
above. However, if you use them on an image that doesn't have an alpha channel
you will cause a crash. To see if an image has an alpha channel use
:meth:`~.PNMImage.has_alpha()` which returns True if there is an alpha channel
and False otherwise. You can add an alpha channel using
:meth:`~.PNMImage.add_alpha()`. You can also remove it using
:meth:`~.PNMImage.remove_alpha()`.

You can also make an image grayscale using :meth:`~.PNMImage.make_grayscale()`.
To set or get a grayscale value, you can use :meth:`~.PNMImage.get_gray()` and
:meth:`~.PNMImage.set_gray()`. (Using these functions on a color image will just
affect the value in the blue channel.) If you want to get the grayscale
value of a pixel regardless of whether the image is a grayscale or a color
image, you can use :meth:`get_bright(x, y) <.PNMImage.get_bright>`, which works
equally well on color or on grayscale images. If you want to weight the colors
use :meth:`get_bright(x, y, r, g, b) <.PNMImage.get_bright>`, where r, g, b are
the weights for the respective channels.

There are several other useful functions in the class, which are described on
the :class:`~panda3d.core.PNMImage` page in the API Reference.

Storing a Texture into an Image
-------------------------------

The Panda :class:`.Texture` class does not allow for pixel manipulation. But the
:class:`.PNMImage` class does. Therefore, if you want to change the image in a
:class:`.Texture` object you must call :meth:`store(image) <.Texture.store>`,
which saves the image of the texture into the given image object.

.. only:: python

   .. code-block:: python

      myImage = PNMImage()
      myTexture = loader.loadTexture("myTex.jpg")

      # After this call, myImage now holds the same image as the texture
      myTexture.store(myImage)

Loading a PNMImage into a Texture
---------------------------------

Once you have changed all the data in the image you can now load it into a
texture using the texture's :meth:`load(myImage) <.Texture.load>` method, where
``myImage`` is the PNMImage to make the texture from.

.. only:: python

   .. code-block:: python

      # Assume we already have myImage which is our modified PNMImage
      myTexture = Texture("texture name")

      # This texture now contains the data from myImage
      myTexture.load(myImage)

.. only:: cpp

   .. code-block:: cpp

      // Assume we already have myImage which is our modified PNMImage
      PT(Texture) my_texture = new Texture("texture name");

      // This texture now contains the data from myImage
      my_texture->load(myImage);

Remember however, that most graphics cards require that the dimensions of
texture have to be a power of two. :class:`.PNMImage` does not have this
restriction and Panda will not automatically scale the image when you put it
into a texture.
