.. _playing-mpg-and-avi-files:

Playing MPG and AVI files
=========================

Panda now supports AVI format for textures in Panda.

Usage
-----

.. code-block:: python

   myMovieTexture = loader.loadTexture("myMovie.avi")
   myObject.setTexture(myMovieTexture)

The movie subsystem is implemented using FFMPEG. Therefore, it supports all of
the formats that FFMPEG supports. The functions to control the movie are as
follows:

.. code-block:: python

   movie.play()
   movie.stop()
   movie.setTime(t)
   movie.getTime()
   movie.setLoopCount(n)
   movie.getLoopCount()
   movie.setPlayRate(speed)
   movie.getPlayRate()
   movie.isPlaying()

If you want to hear the movie's audio as well, you need to load it twice: once
as a texture, and once as a sound file:

.. code-block:: python

   mySound = loader.loadSfx("myMovie.avi")

Then, you can synchronize the video to the audio:

.. code-block:: python

   myMovieTexture.synchronizeTo(mySound)

From that point forward, playing the audio will cause the texture to update.
This is more accurate than synchronizing the video manually.

For powers-of-two limited graphics hardware
-------------------------------------------

If your graphics hardware does not support non power-of-two textures, your movie
texture size would be shifted up to the next larger power of two size. For
example, if you have a movie of 640 x 360 in size, the generated texture would
be actually 1024 x 512. The result is a texture that contains a movie in the
lower-left corner, and a black pad region to the right and upper portion of the
texture.

To work around this limit, you have to display just the lower-left portion of
the texture. To see a complete demonstration of this process, see the Media
Player sample program.

Issues
------

The video texture works by decoding on a frame by frame basis and copying into
the texture buffer. As such, it is inadvisable to use more than a few high res
video textures at the same time.

Certain encoding formats do not work. So far, DV format has been determined
incompatible with Panda.
