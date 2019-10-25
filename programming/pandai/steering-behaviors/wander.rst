.. _wander:

Wander
======

'Wander' is an AI behavior where an AICharacter will move in a random
direction to generate realistic movement around an environment with no goal
position in mind.

https://www.youtube.com/watch?v=jy6F6HnenoE

In PandAI, 'Wander' is defined as :

.. code-block:: python

   aiBehaviors.wander(double wander_radius, int flag, double aoe, float priority)

where :

Wander Radius represents the degree of wandering. This is implemented via a
guiding circle in front of the AI Character.

Flag represents which plane to wander in (0 - XY, 1 - YZ, 2 - XZ, 3 - XYZ). By
default, it is in the XY plane.

Area of Effect is the radius from the starting point where the AICharacter
would wander within.

priority is by default set to 1.0 and is used when using two or more steering
behaviors on an AICharacter.

--------------

The velocity at which the AICharacter wanders is determined when you first
create your AICharacter object using the AICharacter constructor.

--------------

The full working code for this in Panda3D :

.. code-block:: python

   import direct.directbase.DirectStart
   from panda3d.core import *
   from direct.showbase.DirectObject import DirectObject
   from direct.task import Task
   from direct.actor.Actor import Actor
   #for Pandai
   from panda3d.ai import *

   # Globals
   speed = 0.75

   class World(DirectObject):

       def __init__(self):
           base.disableMouse()
           base.cam.setPosHpr(0,0,55,0,-90,0)

           self.loadModels()
           self.setAI()

       def loadModels(self):
           # Seeker
           ralphStartPos = Vec3(0, 0, 0)
           self.wanderer = Actor("models/ralph",
                                    {"run":"models/ralph-run"})
           self.wanderer.reparentTo(render)
           self.wanderer.setScale(0.5)
           self.wanderer.setPos(ralphStartPos)

       def setAI(self):
           #Creating AI World
           self.AIworld = AIWorld(render)

           self.AIchar = AICharacter("wanderer",self.wanderer, 100, 0.05, 5)
           self.AIworld.addAiChar(self.AIchar)
           self.AIbehaviors = self.AIchar.getAiBehaviors()

           self.AIbehaviors.wander(5, 0, 10, 1.0)
           self.wanderer.loop("run")

           #AI World update
           taskMgr.add(self.AIUpdate,"AIUpdate")

       #to update the AIWorld
       def AIUpdate(self,task):
           self.AIworld.update()
           return Task.cont

   w = World()
   run()

To get the full working
demo, please visit :

https://sites.google.com/site/etcpandai/documentation/steering-behaviors/wander/PandAIWanderExample.zip?attredirects=0&d=1
