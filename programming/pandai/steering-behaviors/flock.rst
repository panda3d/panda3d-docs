.. _flock:

Flock
=====

What is flocking? Flocking is an emergent behavior and is the resultant of the
following forces:

cohesion -- finds average position of neighbors and tries to move to that
position separation -- object keeps a certain distance between itself and its
neighbor alignment -- finds average direction in which all neighbors are moving
and tries to move in that direction

Each NPC has a "visibility cone" and this is used to compute it's neighbors.
The neighbors contribute towards the forces mentioned above.

Tuners:

1. The angle and length of each NPC's "visibility cone".
2. Weight of cohesion, separation, and alignment (how much each sub-behavior of
   flock affects the overall flocking behavior).

.. note::

   Flocking behavior is NOT a standalone behavior. It needs to be combined with
   other steering behaviors such as seek, pursue, flee, evade etc. to function.

https://www.youtube.com/watch?v=dkfnlqH06IY

--------------

Using PandAI's flocking system:

.. code-block:: python

   // To create the flock
   flockObject = Flock(unsigned int flock_id, double vcone_angle,
                       double vcone_radius, unsigned int cohesion_wt,
                       unsigned int separation_wt, unsigned int alignment_wt)

"flock_id" is a value identifying the flock.

"vcone_angle" is the visibility angle of the character (represented by a cone
around it)

"vcone_radius" is the length of the visibility cone.

"cohesion_wt", "separation_wt" and "alignment_wt" is the amount of separation
force that contributes to the overall flocking behavior.

--------------

Some standard values to start you off with:

Type vcone_angle vcone_radius separation_wt cohesion_wt alignment_wt

Normal Pack 270 10 2 4 1

Loose Pack 180 10 2 4 5

Tight Pack 45 5 2 4 5

You could try experimenting with your own values to customize your flock.

--------------

To add your AI Character to the above created flock

.. code-block:: python

   flockObject.addAiChar(aiChar)     # aiChar is an AICharacter object.

After all the AI Characters are added to the flock, add the flock to the
world.

.. code-block:: python

   aiWorld.addFlock(flockObject)    # aiWorld is an AIWorld object.

Specify the flock behavior priority. As mentioned earlier, flock behavior
works with other steering behaviors.

.. code-block:: python

   # aiBehaviors is an AIBehaviors object.
   aiBehaviors.flock(float priority)

   # Turns the flock behavior off.
   aiWorld.flockOff(unsigned int flock_id)

   # Turns the flock behavior on.
   aiWorld.flockOn(unsigned int flock_id)

   # Removes the flock behavior.
   # Note: This does NOT remove the AI characters of the flock.
   aiWorld.removeFlock(unsigned int flock_id)

   # Returns a handle to the flock object.
   aiWorld.getFlock(unsigned int flock_id)

--------------

The full working code in Panda3D :

.. code-block:: python

   import direct.directbase.DirectStart
   from panda3d.core import *
   from direct.showbase.DirectObject import DirectObject
   from direct.task import Task
   from direct.actor.Actor import Actor
   #for Pandai
   from panda3d.ai import *
   #for Onscreen GUI
   from direct.gui.OnscreenText import OnscreenText

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
           base.cam.setPosHpr(0, 0, 85, 0, -90, 0)

           self.loadModels()
           self.setAI()
           self.setMovement()

       def loadModels(self):
           # Seeker
           self.flockers = []
           for i in range(10):
               ralphStartPos = Vec3(-10+i, 0, 0)
               self.flockers.append(Actor("models/ralph",
                                        {"run": "models/ralph-run"}))
               self.flockers[i].reparentTo(render)
               self.flockers[i].setScale(0.5)
               self.flockers[i].setPos(ralphStartPos)
               self.flockers[i].loop("run")

           # Target
           self.target = loader.loadModel("models/arrow")
           self.target.setColor(1,0,0)
           self.target.setPos(0,20,0)
           self.target.setScale(1)
           self.target.reparentTo(render)

       def setAI(self):
           #Creating AI World
           self.AIworld = AIWorld(render)

           #Flock functions
           self.MyFlock = Flock(1, 270, 10, 2, 4, 0.2)
           self.AIworld.addFlock(self.MyFlock)
           self.AIworld.flockOn(1)

           self.AIchar = []
           self.AIbehaviors = []
           for i in range(10):
               char = AICharacter("flockers" + str(i), self.flockers[i], 100, 0.05, 5)
               self.AIchar.append(char)
               self.AIworld.addAiChar(char)
               self.AIbehaviors.append(char.getAiBehaviors())
               self.MyFlock.addAiChar(char)
               self.AIbehaviors[i].flock(0.5)
               self.AIbehaviors[i].pursue(self.target, 0.5)

           #AI World update
           taskMgr.add(self.AIUpdate, "AIUpdate")

       #to update the AIWorld
       def AIUpdate(self, task):
           self.AIworld.update()
           return Task.cont

       # All the movement functions for the Target
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

       def Mover(self,task):
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

https://sites.google.com/site/etcpandai/documentation/steering-behaviors/flock/PandAIFlockExample.zip?attredirects=0&d=1
