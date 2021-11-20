.. _directframe:

DirectFrame
===========

.. only:: python

   A frame is a container object for multiple DirectGUI objects. This allows for
   the control over several objects that are reparented to the same frame. When
   DirectGUI objects are parented to a frame, they will be positioned relative to
   the frame.

   DirectFrame has no unique keywords, since it is mostly used to arrange other
   objects.

   Like any other DirectGUI object, the DirectFrame is called as such:

   .. code-block:: python

      DirectFrame(keyword=value, keyword=value, ...)

   For a basic frame, the most used keywords are
   ``frameSize``,
   ``frameColor`` and
   ``pos``. For a full list of
   keywords available for this object you can click, see the :ref:`directgui`
   page.

   As we established above, the most common keywords are:

   ========== ==================================== =======================
   Keyword    Definition                           Value
   ========== ==================================== =======================
   frameSize  Sets the size of the frame           (Left,Right,Bottom,Top)
   frameColor sets the color of the object’s frame (R,G,B,A)
   pos        sets the position of the object      (X,Y,Z)
   ========== ==================================== =======================

   Now as an example let us make a single frame appear on the screen, for that
   the code would be the following:

   .. code-block:: python

      from direct.gui.DirectGui import DirectFrame

      myFrame = DirectFrame(frameColor=(0, 0, 0, 1),
                            frameSize=(-1, 1, -1, 1),
                            pos=(1, -1, -1))

   This will give you a black frame appearing at the lower right section of the
   Panda window.

   Keep in mind, if your screen is non-square you will see the background color
   you have set (or the default one if you have not set any) where there is no
   frame on screen.

   By default, as with any DirectGUI object, DirectFrame is reparented to
   aspect2d so the will stay fixed on-screen even when your camera moves. Newly
   created objects usually are drawn on top of already existing ones, unless you
   change it manually.

   Additionally you can position the frame using
   ``setPos()``. This works with other
   aspects like scale as well.

   The example above would change as follows:

   .. code-block:: python

      from direct.gui.DirectGui import DirectFrame

      myFrame = DirectFrame(frameColor=(0, 0, 0, 1),
                            frameSize=(-1, 1, -1, 1))
      myFrame.setPos(-0.5, 0, -0.5)

   This will give us a black frame that is located at the lower left side of the
   screen.

   Usually one would decide on one of the ways to read and write values for
   DirectGUI objects a third way to access and change properties is the
   following:

   .. code-block:: python

      myDirectobject["yourKeyword"] = value
