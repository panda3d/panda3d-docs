.. _simple-texture-replacement:

Simple Texture Replacement
==========================

Although usually you will load and display models that are already textured,
you can also apply or replace a texture image on a model at runtime. To do
this, you must first get a handle to the texture, for instance by loading it
directly:



.. code-block:: python

    myTexture = loader.loadTexture("myTexture.png")



The above loadTexture() call will search along the current model-path for the
named image file (in this example, a file named "myTexture.png"). If the
texture is not found or cannot be read for some reason, None is returned.

Once you have a texture, you can apply it to a model with the
``setTexture()`` call. For instance,
suppose you used the CardMaker class to generate a plain white card:



.. code-block:: python

    cm = CardMaker('card')
    card = render.attachNewNode(cm.generate())



Then you can load up a texture and apply it to the card like this:



.. code-block:: python

    tex = loader.loadTexture('maps/noise.rgb')
    card.setTexture(tex)



(Note that it is not necessary to use the override parameter to the
setTexture() call--that is, you do not need to do card.setTexture(tex,
1)--because in this case, the card does not already have any other texture
applied to it, so your texture will be visible even without the override.)

In order for this to work, the model you apply it to must already have texture
coordinates defined (see :ref:`simple-texturing`). As it happens, the
CardMaker generates texture coordinates by default when it generates a card,
so no problem there.

You can also use ``setTexture()`` to
replace the texture on an already-textured model. In this case, you must
specify a second parameter to setTexture, which is the same optional Panda
override parameter you can specify on any kind of Panda state change.
Normally, you simply pass 1 as the second parameter to setTexture(). Without
this override, the texture that is assigned directly at the Geom level will
have precedence over the state change you make at the model node, and the
texture change won't be made.

For instance, to change the appearance of smiley:



.. code-block:: python

    smiley = loader.loadModel('smiley.egg')
    smiley.reparentTo(render)
    tex = loader.loadTexture('maps/noise.rgb')
    smiley.setTexture(tex, 1)



|Smiley with noise.egg applied|

Often, you want to replace the texture on just one piece of a model, rather
than setting the texture on every element. To do this, you simply get a
NodePath handle to the piece or pieces of the model that you want to change,
as described in the section :ref:`manipulating-a-piece-of-a-model`, and make
the ``setTexture()`` call on those
NodePaths.

For instance, this car model has multiple textures available in different
colors:

|Description|

For the most part, this car was painted with one big texture image, which
looks like this:

|Description|

But we also have a blue version of the same texture image:

|Description|

Although it is tempting to use setTexture() to assign the blue texture to the
whole car, that would also assign the blue texture to the car's tires, which
need to use a different texture map. So instead, we apply the blue texture
just to the pieces that we want to change:



.. code-block:: python

    car = loader.loadModel('bvw-f2004--carnsx/carnsx.egg')
    blue = loader.loadTexture('bvw-f2004--carnsx/carnsx-blue.png')
    car.find('**/body/body').setTexture(blue, 1)
    car.find('**/body/polySurface1').setTexture(blue, 1)
    car.find('**/body/polySurface2').setTexture(blue, 1)



And the result is this:

|Description|

If you are interested in changing the image of a texture during program
execution, say to adjust some of its pixels, see
:ref:`creating-new-textures-from-scratch`.

.. |Smiley with noise.egg applied| image:: texture-smiley-noise.png
.. |Description| image:: car-red.png
.. |Description| image:: carnsx.png
.. |Description| image:: carnsx-blue.png
.. |Description| image:: car-with-blue.png

