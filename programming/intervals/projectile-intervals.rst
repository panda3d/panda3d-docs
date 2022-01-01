.. _projectile-intervals:

Projectile Intervals
====================

Projectile intervals are used to move a NodePath through the trajectory of a
projectile under the influence of gravity.

.. code-block:: python

   myInterval = ProjectileInterval(<Node Path>,
       startPos=Point3(X, Y, Z), endPos=Point3(X, Y, Z),
       duration=<Time in seconds>, startVel=Point3(X, Y, Z),
       endZ=Z, gravityMult=<multiplier>, name=<Name>)

All parameters don't have to be specified. Here are a combination of parameters
that will allow you to create a projectile interval. (If startPos is not
provided, it will be obtained from the node's position at the time that the
interval is first started. Note that in this case you must provide a duration.)

-  startPos, endPos, duration - go from startPos to endPos in duration seconds
-  startPos, startVel, duration - given a starting velocity, go for a specific
   time period
-  startPos, startVel, endZ - given a starting velocity, go until you hit a
   given Z plane

In addition you may alter gravity by providing a multiplier in 'gravityMult'.
'2' will make gravity twice as strong, '.5' half as strong.'-1' will reverse
gravity.

Here's a little snippet of code that will demonstrate projectile intervals:

.. code-block:: python

   camera.setPos(0,-45,0)

   # load the ball model
   self.ball = loader.loadModel("smiley")
   self.ball.reparentTo(render)
   self.ball.setPos(-15,0,0)

   # setup the projectile interval
   self.trajectory = ProjectileInterval(self.ball, duration=1,
                                        startPos=Point3(-15,0,0),
                                        endPos=Point3(15,0, 0))
   self.trajectory.loop()
