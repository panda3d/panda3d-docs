.. _position-rotation-and-scale-intervals:

Position, Rotation and Scale Intervals
======================================

Panda3D can automatically generate intervals for position to a certain point
or a rotation to a certain HPR value. You can do this by calling
``posInterval()`` and
``hprInterval()`` on the object.



.. code-block:: python

    # This lets the actor move to point 10, 10, 10 in 1.0 second.
    myInterval1 = myActor.posInterval(1.0, Point3(10, 10, 10))
    
    # This move takes 2.0 seconds to complete.
    myInterval2 = myActor.posInterval(2.0, Point3(8, -5, 10))
    
    # You can specify a starting position, too.
    myInterval3 = myActor.posInterval(1.0, Point3(2, -3, 8), startPos=Point3(2, 4, 1))
    
    # This rotates the actor 180 degrees on heading and 90 degrees on pitch.
    myInterval4 = myActor.hprInterval(1.0, Vec3(180, 90, 0))



You can easily create :ref:`sequences-and-parallels` from these intervals:


.. code-block:: python

    mySequence = Sequence(myInterval2, myInterval4)
    mySequence.start()
    myParallel = Parallel(myInterval3, myInterval1)
    myParallel.loop()


``scaleInterval()``,
``posHprInterval()``,
``hprScaleInterval()``, and
``posHprScaleInterval()`` work similarly.

Note: The physics engine won't affect a Node that is moved using
``posInterval()``!
