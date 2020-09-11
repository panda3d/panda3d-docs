.. _automatic-texture-animation:

Automatic Texture Animation
===========================

It's possible to generate a model that automatically rotates through a sequence
of textures when it is in the scene graph, without having to run a special task
to handle this.

To do this, use the ``egg-texture-cards`` command-line utility. This program
will accept a number of texture filenames on the command line, and output an egg
file that rotates through each texture at the specified frame rate::

   egg-texture-cards -o flip.egg -fps 30 explosion*.jpg

This actually creates a model with a different polygon for each frame of the
texture animation. Each polygon is put in a separate node, and all the nodes are
made a child of a special node called a :class:`.SequenceNode`.

The :class:`.SequenceNode` is a special node that only draws one of its children
at a time, and it rotates through the list of children at a particular frame
rate. You can parent the model under render and it will automatically start
animating through its textures. If you need it to start at a particular frame,
use something like this:

.. code-block:: python

   flip = loader.loadModel('flip.egg')
   flip.find('**/+SequenceNode').node().pose(startFrame)
   flip.reparentTo(render)

By default, all of the polygons created by ``egg-texture-cards`` will have the
same size. This means that all of your textures must be the same size as well.
While this is a simple configuration, it may not be ideal for certain effects.
For instance, to animate an explosion, which starts small and grows larger, it
would be better to use a small texture image on a small polygon when the image
is small, and have a larger image on a larger polygon when it grows larger. You
can achieve this effect, with the -p parameter; specifying -p scales each
frame's polygon in relation to the size of the corresponding texture::

   egg-texture-cards -o flip.egg -fps 30 -p 240,240 explosion*.jpg

There are several other parameters as well; use ``egg-texture-cards -h`` for a
complete list.
