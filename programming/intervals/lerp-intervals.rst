.. _lerp-intervals:

Lerp Intervals
==============

The "lerp interval" is the main workhorse of the Interval system. The word
"lerp" is short for "linearly interpolate" and means to smoothly adjust
properties, such as position, from one value to another over a period of time.
You can use lerp intervals to move and rotate objects around in your world.
The lerp interval is also the most complex of all of the intervals, since
there are many different parameters that you might want to specify to control
the lerp.

.. only:: python

   An overview of the NodePath-based LerpIntervals
   -----------------------------------------------

   Most ``LerpIntervals`` adjust the various transform properties of a
   ``NodePath``, such as ``pos``, ``hpr``, and ``scale``, and they all have a
   similar form. Consider the ``LerpPosInterval``, which will smoothly move a
   model from one point in space to another:

   .. code-block:: python

      from direct.interval.LerpInterval import LerpPosInterval
      i = LerpPosInterval(nodePath,
                          duration,
                          pos,
                          startPos=None,
                          other=None,
                          blendType='noBlend',
                          bakeInStart=1,
                          fluid=0,
                          name=None)

   The only required parameters are the model whose position is being changed,
   the length of time to apply the move, and the model's new position. The
   remaining parameters are all optional and are often omitted. Here is a
   breakdown of what each parameter means:

   nodePath
      The model whose position is being changed.

   duration
      The duration of the lerp in seconds.

   pos
      The model's target position (the new position it will move to). Usually
      this is a ``Point3(x, y, z)``, but as a special advanced feature, it might
      be a Python function that, when called, returns a ``Point3``. If it is a
      function, then it will be called at the time the lerp actually begins to
      play.

   startPos
      The starting position of the model at the beginning of the lerp. If this
      is omitted, the model will start from its current position. As with
      ``pos``, above, this might be a Python function, which will be called at
      the time the lerp actually begins.

      Note that if you intend to move an object from its current position, it is
      better to omit this parameter altogether rather than try to specify it
      explicitly with something like ``startPos=object.getPos()`` since the
      latter will be evaluated at the time the interval is created; not when it
      is played. This is especially true if you plan to embed a series of
      consecutive ``LerpIntervals`` within a
      :ref:`Sequence <sequences-and-parallels>`.

   other
      Normally this is set to None to indicate a normal lerp. If a ``NodePath``
      is passed in, however, it indicates that this is a relative lerp, and the
      ``pos`` and ``startPos`` will be computed as a relative transform from
      that ``NodePath``. The relative transform is recomputed each frame, so if
      the other ``NodePath`` is animating during the lerp, the animation will be
      reflected here. For this reason, you should not attempt to lerp a model
      relative to itself.

   blendType
      This specifies how smoothly the lerp starts and stops. It may be any of
      the following values:

      +-----------------+------------------------------------------------------+
      | ``'easeIn'``    | The lerp begins slowly, ramps up to full speed, and  |
      |                 | stops abruptly.                                      |
      +-----------------+------------------------------------------------------+
      | ``'easeOut'``   | The lerp begins at full speed, and then slows to a   |
      |                 | gentle stop at the end.                              |
      +-----------------+------------------------------------------------------+
      | ``'easeInOut'`` | The lerp begins slowly, ramps up to full speed, and  |
      |                 | then slows to a gentle stop.                         |
      +-----------------+------------------------------------------------------+
      | ``'noBlend'``   | The lerp begins and ends abruptly.                   |
      +-----------------+------------------------------------------------------+

   bakeInStart
      This is an advanced feature. Normally this is 1, which means the original
      starting position of the model is determined when the interval starts to
      play and saved for the duration of the interval. You almost always want to
      keep it that way. If you pass this as 0, however, the starting position is
      cleverly re-inferred at each frame, based on the model's current position
      and the elapsed time in the lerp; this allows your application to move the
      model even while it is being lerped, and the lerp will adapt. This has
      nothing to do with controlling when the ``startPos`` parameter is
      evaluated.

   fluid
      If this is 1, then the lerp uses ``setFluidPos()`` rather than
      ``setPos()`` to animate the model. See :ref:`rapidly-moving-objects`.
      This is meaningful only when the collision system is currently active on
      the model. Since usually there is no reason to have the collision system
      active while a model is under direct application control, this parameter
      is rarely used.

   name
      This specifies the name of the lerp, and may be useful for debugging.
      Also, by convention, there may only be one lerp with a given name playing
      at any given time, so if you put a name here, any other interval with the
      same name will automatically stop when this one is started. The default is
      to assign a unique name for each interval.

   Convenience Short-Hands
   -----------------------

   Various convenience methods are defined on the NodePath class which provide
   a short-hand syntax for creating a LerpInterval for that NodePath.
   These are called ``posInterval()``, ``hprInterval()``, ``quatInterval``, and
   so on. As an example:

   .. code-block::

      # This lets the actor move to point 10, 10, 10 in 1.0 second.
      myInterval1 = myActor.posInterval(1.0, Point3(10, 10, 10))

      # This move takes 2.0 seconds to complete.
      myInterval2 = myActor.posInterval(2.0, Point3(8, -5, 10))

      # You can specify a starting position, too.
      myInterval3 = myActor.posInterval(1.0, Point3(2, -3, 8), startPos=Point3(2, 4, 1))

      # This rotates the actor 180 degrees on heading and 90 degrees on pitch.
      myInterval4 = myActor.hprInterval(1.0, Vec3(180, 90, 0))

   The rest of the NodePath-based LerpIntervals
   --------------------------------------------

   Many ``NodePath`` properties other than position may be controlled via a
   lerp. Here is the list of the various ``LerpIntervals`` that control
   ``NodePath`` properties:

   .. code-block:: python

      LerpPosInterval(nodePath, duration, pos, startPos)
      LerpHprInterval(nodePath, duration, hpr, startHpr)
      LerpQuatInterval(nodePath, duration, quat, startHpr, startQuat)
      LerpScaleInterval(nodePath, duration, scale, startScale)
      LerpShearInterval(nodePath, duration, shear, startShear)
      LerpColorInterval(nodePath, duration, color, startColor)
      LerpColorScaleInterval(nodePath, duration, colorScale, startColorScale)

   Each of the above has a similar set of parameters as those of
   ``LerpPosInterval``. They also have a similar shortcut (e.g.
   ``model.hprInterval()``, etc.) Finally, there is a handful of combination
   ``LerpIntervals`` that perform multiple lerps at the same time. (You can also
   achieve the same effect by combining several ``LerpIntervals`` within a
   :ref:`Parallel <sequences-and-parallels>`, but these combination intervals
   are often simpler to use, and they execute just a bit faster.)

   .. code-block:: python

      LerpPosHprInterval(nodePath, duration, pos, hpr, startPos, startHpr)
      LerpPosQuatInterval(nodePath, duration, pos, quat, startPos, startQuat)
      LerpHprScaleInterval(nodePath, duration, hpr, scale, startHpr, startScale)
      LerpQuatScaleInterval(nodePath, duration, quat, scale, startQuat, startScale)
      LerpPosHprScaleInterval(nodePath, duration, pos, hpr, scale, startPos, startHpr, startScale)
      LerpPosQuatScaleInterval(nodePath, duration, pos, quat, scale, startPos, startQuat, startScale)
      LerpPosHprScaleShearInterval(nodePath, duration, pos, hpr, scale, shear, startPos, startHpr, startScale, startShear)
      LerpPosQuatScaleShearInterval(nodePath, duration, pos, quat, scale, shear, startPos, startQuat, startScale, startShear)

   Other types of LerpInterval
   ---------------------------

   Beyond animating NodePaths, you can create a ``LerpInterval`` that blends any
   parameter of any object over time. This can be done with a
   ``LerpFunctionInterval``:

   .. code-block:: python

      def myFunction(t):
          # Do something based on t.

      i = LerpFunc(myFunction,
                   fromData=0,
                   toData=1,
                   duration=0.0,
                   blendType='noBlend',
                   extraArgs=[],
                   name=None)

   This advanced interval has many things in common with all of the above
   ``LerpIntervals``, but instead of directly animating a value, it instead
   calls the function you specify, passing a single floating-point parameter,
   ``t``, that ranges from ``fromData`` to ``toData`` over the duration of the
   interval. It is then up to your function to set whatever property of whatever
   object you like according to the current value of ``t``.

.. only:: cpp

   See the API reference for :class:`.CLerpNodePathInterval` to understand how
   to construct such an interval.
