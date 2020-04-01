.. _path-follow:

Path Follow
===========

'Path Follow' is a behavior where an AICharacter moves from one path to the
other without stopping at any path. It can be used for a patrolling type of
behavior.

https://www.youtube.com/watch?v=hIDyzUJgu2w

--------------

In PandAI, path follow is defined as :


.. code-block:: python

   aiBehaviors.pathFollow(float priority)
   aiBehaviors.addToPath(Vec3 position)

   aiBehaviors.startFollow() // Required to start the follow

Position is a point in
3D space which falls on the path which the AI Character needs to traverse.

(Note: that you need to add multiple positions to create a path say for
example Vec3(-10,10,0) Vec3(0,0,0) Vec3(10,10,0) Vec3(-10,10,0) will generate
a rectangular path in the XY plane)

Note: the addToPath works backwards. So, your last call to addToPath will be
your first position your AICharacter will go to.

--------------

The full working code in Panda3D is :


.. code-block:: python

   import direct.directbase.DirectStart
   from panda3d.core import *
   from direct.task import Task
   from direct.actor.Actor import Actor
   from panda3d.ai import *

   class World(object):

       def __init__(self):
           base.disableMouse()
           base.cam.setPosHpr(0, 0, 55, 0, -90, 0)

           self.loadModels()
           self.setAI()

       def loadModels(self):
           # Seeker
           ralphStartPos = Vec3(-10, 0, 0)
           self.seeker = Actor("models/ralph",
                               {"run":"models/ralph-run"})
           self.seeker.reparentTo(render)
           self.seeker.setScale(0.5)
           self.seeker.setPos(ralphStartPos)
           # Target1
           self.target1 = loader.loadModel("models/arrow")
           self.target1.setColor(1,0,0)
           self.target1.setPos(10,-10,0)
           self.target1.setScale(1)
           self.target1.reparentTo(render)
           # Target2
           self.target2 = loader.loadModel("models/arrow")
           self.target2.setColor(0,1,0)
           self.target2.setPos(10,10,0)
           self.target2.setScale(1)
           self.target2.reparentTo(render)
           # Target3
           self.target3 = loader.loadModel("models/arrow")
           self.target3.setColor(0,0,1)
           self.target3.setPos(-10,10,0)
           self.target3.setScale(1)
           self.target3.reparentTo(render)
           # Target4
           self.target4 = loader.loadModel("models/arrow")
           self.target4.setColor(1,0,1)
           self.target4.setPos(-10,-10,0)
           self.target4.setScale(1)
           self.target4.reparentTo(render)

           self.seeker.loop("run")

       def setAI(self):
           # Creating AI World
           self.AIworld = AIWorld(render)

           self.AIchar = AICharacter("seeker", self.seeker, 60, 0.05, 5)
           self.AIworld.addAiChar(self.AIchar)
           self.AIbehaviors = self.AIchar.getAiBehaviors()

           # Path follow (note the order is reveresed)
           self.AIbehaviors.pathFollow(1.0)
           self.AIbehaviors.addToPath(self.target4.getPos())
           self.AIbehaviors.addToPath(self.target3.getPos())
           self.AIbehaviors.addToPath(self.target2.getPos())
           self.AIbehaviors.addToPath(self.target1.getPos())

           self.AIbehaviors.startFollow()

           #AI World update
           taskMgr.add(self.AIUpdate, "AIUpdate")

       def AIUpdate(self,task):
           self.AIworld.update()
           return Task.cont

   w = World()
   base.run()

To get the full working demo, please visit:

https://sites.google.com/site/etcpandai/documentation/steering-behaviors/path-follow/PandAIPathFollowTutorial.zip?attredirects=0&d=1
