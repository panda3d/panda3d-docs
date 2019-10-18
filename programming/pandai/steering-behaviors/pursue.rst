.. _pursue:

Pursue
======

'Pursue' is a behavior where an AICharacter moves in the direction of a target
NodePath until it reaches that entity, performing a change in direction of
motion according to the entity's motion.

https://www.youtube.com/watch?v=QdcbN3FLYVs

--------------

In PandAI, 'Pursue' is defined as:

.. code-block:: python

   aiBehaviors.pursue(NodePath target, float priority)

priority is by default set to 1.0 and is used when using two or more steering
behaviors on an AICharacter.

--------------

The velocity at which the AICharacter pursues is determined when you first
create your AICharacter object using the AICharacter constructor.

.. note::

   Pursue's direction is recalculated every frame to handle any change in the
   target's position.

The actual code working in Panda3D:

.. code-block:: python

   import direct.directbase.DirectStart
   from panda3d.core import *
   from direct.showbase.DirectObject import DirectObject
   from direct.task import Task
   from direct.actor.Actor import Actor
   from direct.gui.OnscreenText import OnscreenText

   from panda3d.ai import *

   # Globals
   speed = 0.75

   # Function to put instructions on the screen.
   font = loader.loadFont("cmss12")
   def addInstructions(pos, msg):
       return OnscreenText(text=msg, style=1, fg=(1, 1, 1, 1), font=font,
                           pos=(-1.3, pos), align=TextNode.ALeft, scale=.05)

   class World(DirectObject):

       def __init__(self):
           base.disableMouse()
           base.cam.setPosHpr(0, 0, 55, 0, -90, 0)

           self.loadModels()
           self.setAI()
           self.setMovement()

       def loadModels(self):
           # Seeker
           ralphStartPos = Vec3(-10, 0, 0)
           self.pursuer = Actor("models/ralph",
                                {"run":"models/ralph-run"})
           self.pursuer.reparentTo(render)
           self.pursuer.setScale(0.5)
           self.pursuer.setPos(ralphStartPos)
           # Target
           self.target = loader.loadModel("models/arrow")
           self.target.setColor(1, 0, 0)
           self.target.setPos(5, 0, 0)
           self.target.setScale(1)
           self.target.reparentTo(render)

       def setAI(self):
           #Creating AI World
           self.AIworld = AIWorld(render)

           self.AIchar = AICharacter("pursuer",self.pursuer, 100, 0.05, 5)
           self.AIworld.addAiChar(self.AIchar)
           self.AIbehaviors = self.AIchar.getAiBehaviors()

           self.AIbehaviors.pursue(self.target)
           self.pursuer.loop("run")

           #AI World update
           taskMgr.add(self.AIUpdate, "AIUpdate")

       #to update the AIWorld
       def AIUpdate(self,task):
           self.AIworld.update()
           return Task.cont

       #All the movement functions for the Target
       def setMovement(self):
           self.keyMap = {"left": 0, "right": 0, "up": 0, "down": 0}
           self.accept("arrow_left", self.setKey, ["left", 1])
           self.accept("arrow_right", self.setKey, ["right", 1])
           self.accept("arrow_up", self.setKey, ["up", 1])
           self.accept("arrow_down", self.setKey, ["down", 1])
           self.accept("arrow_left-up", self.setKey, ["left", 0])
           self.accept("arrow_right-up", self.setKey, ["right", 0])
           self.accept("arrow_up-up", self.setKey, ["up", 0])
           self.accept("arrow_down-up", self.setKey, ["down", 0])
           #movement task
           taskMgr.add(self.Mover, "Mover")

           addInstructions(0.9, "Use the Arrow keys to move the Red Target")

       def setKey(self, key, value):
           self.keyMap[key] = value

       def Mover(self, task):
           startPos = self.target.getPos()
           if self.keyMap["left"] != 0:
               self.target.setPos(startPos + Point3(-speed, 0, 0))
           if self.keyMap["right"] != 0:
               self.target.setPos(startPos + Point3(speed, 0, 0))
           if self.keyMap["up"] != 0:
               self.target.setPos(startPos + Point3(0, speed, 0))
           if self.keyMap["down"] != 0:
               self.target.setPos(startPos + Point3(0, -speed, 0))

           return Task.cont

   w = World()
   base.run()

To get the full working demo, please visit:

https://sites.google.com/site/etcpandai/documentation/steering-behaviors/pursue/PandAIPursueExample.zip?attredirects=0&d=1
