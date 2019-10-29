.. _actor-intervals:

Actor Intervals
===============

.. only:: python

   Actor intervals allow actor animations to be played as an interval, which
   allows them to be combined with other intervals through sequences and
   parallels.

   The subrange of the animation to be played may be specified via frames
   (``startFrame`` up to and including ``endFrame``) or seconds (``startTime``
   up to and including ``endTime``). It may also be specified with a
   ``startFrame`` or ``startTime`` in conjunction with the duration, in seconds.
   If none of these is specified, then the default is to play the entire range
   of the animation.

   If ``endFrame`` is before ``startFrame``, or if the play rate is negative,
   then the animation will be played backwards.

   You may specify a subrange that is longer than the actual animation, but if
   you do so, you probably also want to specify either ``loop=1`` or
   ``constrainedLoop=1``; see below.

   The loop parameter is a boolean value. When it is true, it means that the
   animation restarts and plays again if the interval extends beyond the
   animation's last frame. When it is false, it means that the animation stops
   and holds its final pose when the interval extends beyond the animation's
   last frame. Note that, in neither case, will the ActorInterval loop
   indefinitely: all intervals always have a specific, finite duration, and the
   duration of an ActorInterval is controlled by either the duration parameter,
   the ``startTime``/``endTime`` parameters, or the ``startFrame``/``endFrame``
   parameters. Setting ``loop=1`` has no effect on the duration of the
   ActorInterval, it only controls what the actor does if you try to play past
   the end of the animation.

   The parameter ``constrainedLoop`` works similarly to loop, but while
   ``loop=1`` implies a loop within the entire range of animation,
   ``constrainedLoop=1`` implies a loop within ``startFrame`` and ``endFrame``
   only. That is, if you specify ``loop=1`` and the animation plays past
   ``endFrame``, in the next frame it will play beginning at frame 0; while if
   you specify ``constrainedLoop=1`` instead, then the next frame after
   ``endFrame`` will be ``startFrame`` again.

   All parameters other than the animation name are optional.

   .. code-block:: python

      from direct.interval.ActorInterval import ActorInterval

      myInterval = myactor.actorInterval(
          "Animation Name",
          loop=<0 or 1>,
          constrainedLoop=<0 or 1>,
          duration=D,
          startTime=T1,
          endTime=T2,
          startFrame=N1,
          endFrame=N2,
          playRate=R,
          partName=PN,
          lodName=LN,
      )

.. only:: cpp

   As ActorInterval is implemented in Python, this section does not apply to C++.
