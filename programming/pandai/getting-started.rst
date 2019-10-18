.. _getting-started:

Getting Started
===============

The basics : Theory :

The PandAI library has been built upon the design pattern of composition.

There exists a main AIWorld Class which governs all updates of any AICharacters
added to it. Each AICharacter has its own AIBehavior object which keeps track of
all position and rotation updates based on the type of AI which is acting on
that character.

So in short : AIWorld -> AICharacter -> AIBehavior

Each AIBehavior object has the functionality to implement all the steering
behaviors and pathfinding behaviors. So once you get a reference to this object
from the AICharacter, it should give you the ability to call the respective
functions.

Implementation:

Following are the steps to get the basics of PandAI working. Don't worry if you
can't understand some of them.

Step 1:

To use our AI library into your game you need to import PandAI into your game
code via:

.. code-block:: python

   from panda3d.ai import *

Step 2:

Create an object of the AIWorld class which defines your AI in your game world.

Step 3:

Setup a task which runs continuously which keeps calling the 'Update()' function
for your previously created AIWorld object

Step 4:

To test this out let us also implement a simple call to the 'seek' behavior
function in PandAI. To do this we need two objects: A seeker and a target. For
this example, we will use Ralph (seeker) and an arrow model (target).

Step 5:

Create an 'AICharacter' object and attach it to your AIWorld class (previously
created). The AICharacter constructor looks for a NodePath, this can be a Model
or an Actor or even an Empty NodePath.

Step 6:

Get a reference to the AIBehaviors object of your previously created AICharacter
class via the 'getAiBehaviors' function().

Step 7:

Call the seek function on your AIBehaviors reference (previously created). The
seek function takes a NodePath or a Vector3 position to seek to.

Step 8:

Start your AIWorld update task which you created earlier.

Step 9:

Watch how your awesome seek function works!

The actual code:

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
           # Target
           self.target = loader.loadModel("models/arrow")
           self.target.setColor(1, 0, 0)
           self.target.setPos(5, 0, 0)
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
           taskMgr.add(self.AIUpdate,"AIUpdate")

       #to update the AIWorld
       def AIUpdate(self,task):
           self.AIworld.update()
           return Task.cont

   w = World()
   base.run()

-  Note  It doesn't matter where your seek is first called (ie. before the
   AIWorld update or after) it should still work as soon as the Update starts
   processing.

-  Note: This above example is only for seek but if you go to each of the pages,
   a separate example is provided showing you each AI individually.

--------------

If you want to get a working demo of this tutorial, please visit :

https://sites.google.com/site/etcpandai/documentation/getting-started/PandAIBasicTutorial.zip?attredirects=0&d=1

--------------

Next Step:

Now that you have a basic working program of PandAI, you should proceed to the
Steering Behaviors page and gain more knowledge of the system from there.
