.. _loading-resources-from-memory:

Loading Resources from Memory
=============================

If you have want to load a resource from a different spot then a hard drive or
inside a multifile, say for instance database or network packet you can using
a StringStream.

Here is an example that reads and image into data and then uses StringStream
to feed that data into the image.

.. code-block:: python

   data = open('my-image-file.png', 'rb').read()
   # send data over network or any other place and pass it on
   p = PNMImage()
   p.read(StringStream(data))
   tex = Texture()
   tex.load(p)

But, you can go one step further. Instead of just loading textures, models,
sounds or other data one at a time this way, you can load an entire multifile,
which as we learned in the previous section can contain any number of models,
textures, sounds and other data.

.. code-block:: python

   data = open('my-multifile.mf', 'rb').read()
   stream = StringStream(data)
   mf = Multifile()
   mf.openRead(stream)
   vfs = VirtualFileSystem.getGlobalPtr()
   vfs.mount(mf, '/mf', 0)
   smiley = loader.loadModel('/mf/smiley.egg')
