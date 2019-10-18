.. _seek:

Seek
====

'Seek' is a behavior where an AICharacter moves in the direction of a target
NodePath or position until it reaches that entity.

Video of this behavior in Panda3D:

https://www.youtube.com/watch?v=-UMeYgZLa8Q

--------------

In PandAI, seek is defined as :

.. code-block:: python

   aiBehaviors.seek(NodePath target, float priority)
   aiBehaviors.seek(Vec3 position, float priority)

priority is by default set to 1.0 and is used when using two or more steering
behaviors on an AICharacter.

--------------

The velocity at which the AICharacter seeks is determined when you first create
your AICharacter object using the AICharacter constructor.

.. note::

   Seek's direction is calculated only during the first instance of the call and
   so is more efficient than pursue, if all you want is an object to go to a
   point.

--------------

Here is a full program written implementing 'seek' using PandAI :

.. code-block:: python

   import direct.directbase.DirectStart
   from panda3d.core import *
   from direct.showbase.DirectObject import DirectObject
   from direct.task import Task
   from direct.actor.Actor import Actor

   from panda3d.ai import *

   class World(DirectObject):

       def __init__(self):
           base.disableMouse()
           base.cam.setPosHpr(0, 0, 55, 0, -90, 0)

           self.loadModels()
           self.setAI()

       def loadModels(self):
           # Seeker
           ralphStartPos = Vec3(-10, 0, 0)
           self.seeker = Actor("models/ralph",
                               {"run": "models/ralph-run"})
           self.seeker.reparentTo(render)
           self.seeker.setScale(0.5)
           self.seeker.setPos(ralphStartPos)
           # Target
           self.target = loader.loadModel("models/arrow")
           self.target.setColor(1,0,0)
           self.target.setPos(5,0,0)
           self.target.setScale(1)
           self.target.reparentTo(render)

       def setAI(self):
           #Creating AI World
           self.AIworld = AIWorld(render)

           self.AIchar = AICharacter("seeker",self.seeker, 100, 0.05, 5)
           self.AIworld.addAiChar(self.AIchar)
           self.AIbehaviors = self.AIchar.getAiBehaviors()

           self.AIbehaviors.seek(self.target)
           self.seeker.loop("run")

           #AI World update
           taskMgr.add(self.AIUpdate, "AIUpdate")

       #to update the AIWorld
       def AIUpdate(self, task):
           self.AIworld.update()
           return Task.cont

   w = World()
   base.run()

--------------

To get the full working demo for this, please visit:

https://sites.google.com/site/etcpandai/documentation/steering-behaviors/seek/PandAISeekExample.zip?attredirects=0&d=1
