.. _flee:

Flee
====

'Flee' is an AI behavior where an AICharacter will move in the opposite
direction to a target NodePath or position.

https://www.youtube.com/watch?v=sXzzuK2Vnnk

In PandAI, 'Flee' is defined as:

.. code-block:: python

   aiBehaviors.flee(NodePath target, double panic_distance, double relax_distance, float priority)
   aiBehaviors.flee(Vec3 position, double panic_distance, double relax_distance, float priority)

where:

Panic Distance is the radius of detection.

Relax Distance is the distance from the panic distance radius after which the
object should stop fleeing once flee has been initiated.

priority is by default set to 1.0 and is used when using two or more steering
behaviors on an AICharacter.

--------------

The velocity at which the AICharacter flees is determined when you first create
your AICharacter object using the AICharacter constructor.

-  Note: 'Flee' takes in a target or a position to be fled away from; this
   position should be static. (For moving objects use Evade).

--------------

A fully working flee demo :

.. code-block:: python

   import direct.directbase.DirectStart
   from panda3d.core import *
   from direct.showbase.DirectObject import DirectObject
   from direct.task import Task
   from direct.actor.Actor import Actor
   #for Pandai
   from panda3d.ai import *

   class World(DirectObject):

       def __init__(self):
           base.disableMouse()
           base.cam.setPosHpr(0,0,55,0,-90,0)

           self.loadModels()
           self.setAI()

       def loadModels(self):
           # Seeker
           ralphStartPos = Vec3(2, 0, 0)
           self.fleer = Actor("models/ralph",
                                    {"run":"models/ralph-run"})
           self.fleer.reparentTo(render)
           self.fleer.setScale(0.5)
           self.fleer.setPos(ralphStartPos)
           # Target
           self.target = loader.loadModel("models/arrow")
           self.target.setColor(1,0,0)
           self.target.setPos(5,0,0)
           self.target.setScale(1)
           self.target.reparentTo(render)

       def setAI(self):
           #Creating AI World
           self.AIworld = AIWorld(render)

           self.AIchar = AICharacter("fleer",self.fleer, 100, 0.05, 5)
           self.AIworld.addAiChar(self.AIchar)
           self.AIbehaviors = self.AIchar.getAiBehaviors()

           self.AIbehaviors.flee(self.target, 5, 5)
           self.fleer.loop("run")

           #AI World update
           taskMgr.add(self.AIUpdate,"AIUpdate")

       #to update the AIWorld
       def AIUpdate(self,task):
           self.AIworld.update()
           return Task.cont

   w = World()
   base.run()

--------------

To get a working demo of this example, please visit:

https://sites.google.com/site/etcpandai/documentation/steering-behaviors/flee/PandAIFleeExample.zip?attredirects=0&d=1
