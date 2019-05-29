.. _onscreenimage:

OnscreenImage
=============

Just like :ref:`onscreentext`, you can use OnscreenImage as a quick way to put
an image onscreen. Use an OnscreenImage whenever you want a quick way to
display an ordinary image without a lot of fancy requirements.



.. code-block:: python

    from direct.gui.OnscreenImage import OnscreenImage
    imageObject = OnscreenImage(image = 'myImage.jpg', pos = (-0.5, 0, 0.02))



If you want, you can change the image into another one using setImage():



.. code-block:: python

    imageObject.setImage('myImage2.jpg')



When you want to take the image away, use:



.. code-block:: python

    imageObject.destroy()



The following keyword parameters may be specified to the constructor:

====== ==================================================================================================================================================================================================================================================
image  the actual geometry to display or a file name. This may be omitted and specified later via setImage() if you don’t have it available.
      
       Note: Omitting this parameter results in the OnscreenImage being created as an empty NodePath, meaning that many NodePath methods (including setPos()) are not valid and should raise assertion errors until an image is specified via setImage().
pos    the x, y, z position of the geometry on the screen. This maybe a 3-tuple of floats or a vector. y should be zero
scale  the size of the geometry. This may either be a single float, a 3-tuple of floats, or a vector, specifying a different x, y, z scale. y should be 1
hpr    the h, p, r of the geometry on the screen. This maybe a 3-tuple of floats or a vector.
color  the (r, g, b, a) color of the geometry. This is normally a 4-tuple of floats or ints.
parent the NodePath to parent the text to initially; the default is aspect2d.
====== ==================================================================================================================================================================================================================================================

**NOTE:** To enable transparency in images, you must first set the
TransparencyAttrib, otherwise the transparent parts of the image will be shown
black:



.. code-block:: python

    from panda3d.core import TransparencyAttrib
    self.myImage=OnscreenImage(image = 'myImage.png', pos = (0, 0, 0))
    self.myImage.setTransparency(TransparencyAttrib.MAlpha)



Since GIF's are not supported you should use PNG or TGA if you need
transparency.
