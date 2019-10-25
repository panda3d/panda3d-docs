# PandAI Author: Srinavin Nair
# Original Author: Ryan Myers
# Models: Jeff Styers, Reagan Heller

# Last Updated: 6/13/2005
#
# This tutorial provides an example of creating a character and having it walk
# around on uneven terrain, as well as implementing a fully rotatable camera.
# It uses PandAI pathfinding to move the character.

from direct.showbase.ShowBase import ShowBase
from panda3d.core import CollisionTraverser, CollisionNode
from panda3d.core import CollisionHandlerQueue, CollisionRay
from panda3d.core import Filename
from panda3d.core import PandaNode, NodePath, TextNode
from panda3d.core import Vec3, BitMask32
from direct.gui.OnscreenText import OnscreenText
from direct.actor.Actor import Actor
from direct.task.Task import Task
from direct.showbase.DirectObject import DirectObject
import sys
import os

from panda3d.ai import *

base = ShowBase()

SPEED = 0.5

# Figure out what directory this program is in.
MYDIR = os.path.abspath(sys.path[0])
MYDIR = Filename.fromOsSpecific(MYDIR).getFullpath()

font = loader.loadFont("cmss12")


# Function to put instructions on the screen.
def addInstructions(pos, msg):
    return OnscreenText(text=msg, style=1, fg=(1, 1, 1, 1), font=font,
                        pos=(-1.3, pos), align=TextNode.ALeft, scale=.05)


# Function to put title on the screen.
def addTitle(text):
    return OnscreenText(text=text, style=1, fg=(1, 1, 1, 1), font=font,
                        pos=(1.3, -0.95), align=TextNode.ARight, scale=.07)


class World(DirectObject):

    def __init__(self):
        self.switchState = True
        self.switchCam = False
        self.path_no = 1
        self.keyMap = {
            "left": 0,
            "right": 0,
            "forward": 0,
            "cam-left": 0,
            "cam-right": 0
        }
        base.win.setClearColor((0, 0, 0, 1))
        base.cam.setPosHpr(17.79, -87.64, 90.16, 38.66, 325.36, 0)
        # Post the instructions

        addTitle("Pandai Tutorial: Roaming Ralph (Walking on Uneven Terrain) "
                 "working with pathfinding")
        addInstructions(0.95, "[ESC]: Quit")
        addInstructions(0.90, "[Space - do Only once]: Start Pathfinding")
        addInstructions(0.85, "[Enter]: Change camera view")
        addInstructions(0.80, "[Up Arrow]: Run Ralph Forward")
        addInstructions(0.70, "[A]: Rotate Camera Left")
        addInstructions(0.65, "[S]: Rotate Camera Right")

        # Set up the environment
        #
        # This environment model contains collision meshes.  If you look
        # in the egg file, you will see the following:
        #
        #    <Collide> { Polyset keep descend }
        #
        # This tag causes the following mesh to be converted to a collision
        # mesh -- a mesh which is optimized for collision, not rendering.
        # It also keeps the original mesh, so there are now two copies ---
        # one optimized for rendering, one for collisions.

        self.environ = loader.loadModel("models/world")
        self.environ.reparentTo(render)
        self.environ.setPos(12, 0, 0)

        self.box = loader.loadModel("models/box")
        self.box.reparentTo(render)
        self.box.setPos(-29.83, 0, 0)
        self.box.setScale(1)

        self.box1 = loader.loadModel("models/box")
        self.box1.reparentTo(render)
        self.box1.setPos(-51.14, -17.90, 0)
        self.box1.setScale(1)

        # Create the main character, Ralph

        #ralphStartPos = self.environ.find("**/start_point").getPos()
        ralphStartPos = Vec3(-98.64, -20.60, 0)
        self.ralph = Actor("models/ralph",
                           {"run": "models/ralph-run",
                            "walk": "models/ralph-walk"})
        self.ralph.reparentTo(render)
        self.ralph.setScale(1)
        self.ralph.setPos(ralphStartPos)

        self.ralphai = Actor("models/ralph",
                             {"run": "models/ralph-run",
                              "walk": "models/ralph-walk"})

        self.pointer = loader.loadModel("models/arrow")
        self.pointer.setColor(1, 0, 0)
        self.pointer.setPos(-7.5, -1.2, 0)
        self.pointer.setScale(3)
        self.pointer.reparentTo(render)

        self.pointer1 = loader.loadModel("models/arrow")
        self.pointer1.setColor(1, 0, 0)
        self.pointer1.setPos(-98.64, -20.60, 0)
        self.pointer1.setScale(3)
        #self.pointer.reparentTo(render)

        # Create a floater object.  We use the "floater" as a temporary
        # variable in a variety of calculations.

        self.floater = NodePath(PandaNode("floater"))
        self.floater.reparentTo(render)

        # Accept the control keys for movement and rotation

        self.accept("escape", sys.exit)
        self.accept("enter", self.activateCam)
        self.accept("arrow_left", self.setKey, ["left", 1])
        self.accept("arrow_right", self.setKey, ["right", 1])
        self.accept("arrow_up", self.setKey, ["forward", 1])
        self.accept("a", self.setKey, ["cam-left", 1])
        self.accept("s", self.setKey, ["cam-right", 1])
        self.accept("arrow_left-up", self.setKey, ["left", 0])
        self.accept("arrow_right-up", self.setKey, ["right", 0])
        self.accept("arrow_up-up", self.setKey, ["forward", 0])
        self.accept("a-up", self.setKey, ["cam-left", 0])
        self.accept("s-up", self.setKey, ["cam-right", 0])

        #taskMgr.add(self.move,"moveTask")

        # Game state variables
        self.isMoving = False

        # Set up the camera

        #base.disableMouse()
        #base.camera.setPos(self.ralph.getX(), self.ralph.getY() + 10, 2)

        # We will detect the height of the terrain by creating a collision
        # ray and casting it downward toward the terrain.  One ray will
        # start above ralph's head, and the other will start above the camera.
        # A ray may hit the terrain, or it may hit a rock or a tree.  If it
        # hits the terrain, we can detect the height.  If it hits anything
        # else, we rule that the move is illegal.

        self.cTrav = CollisionTraverser()

        self.ralphGroundRay = CollisionRay()
        self.ralphGroundRay.setOrigin(0, 0, 1000)
        self.ralphGroundRay.setDirection(0, 0, -1)
        self.ralphGroundCol = CollisionNode('ralphRay')
        self.ralphGroundCol.addSolid(self.ralphGroundRay)
        self.ralphGroundCol.setFromCollideMask(BitMask32.bit(0))
        self.ralphGroundCol.setIntoCollideMask(BitMask32.allOff())
        self.ralphGroundColNp = self.ralph.attachNewNode(self.ralphGroundCol)
        self.ralphGroundHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.ralphGroundColNp, self.ralphGroundHandler)

        self.camGroundRay = CollisionRay()
        self.camGroundRay.setOrigin(0, 0, 1000)
        self.camGroundRay.setDirection(0, 0, -1)
        self.camGroundCol = CollisionNode('camRay')
        self.camGroundCol.addSolid(self.camGroundRay)
        self.camGroundCol.setFromCollideMask(BitMask32.bit(0))
        self.camGroundCol.setIntoCollideMask(BitMask32.allOff())
        self.camGroundColNp = base.camera.attachNewNode(self.camGroundCol)
        self.camGroundHandler = CollisionHandlerQueue()
        self.cTrav.addCollider(self.camGroundColNp, self.camGroundHandler)

        # Uncomment this line to see the collision rays
        #self.ralphGroundColNp.show()
        #self.camGroundColNp.show()

        #Uncomment this line to show a visual representation of the
        #collisions occuring
        #self.cTrav.showCollisions(render)

        self.setAI()

    def activateCam(self):
        self.switchCam = not self.switchCam
        if self.switchCam is True:
            base.cam.setPosHpr(0, 0, 0, 0, 0, 0)
            base.cam.reparentTo(self.ralph)
            base.cam.setY(base.cam.getY() + 30)
            base.cam.setZ(base.cam.getZ() + 10)
            base.cam.setHpr(180, -15, 0)
        else:
            base.cam.reparentTo(render)
            base.cam.setPosHpr(17.79, -87.64, 90.16, 38.66, 325.36, 0)
            #base.camera.setPos(self.ralph.getX(),self.ralph.getY()+10,2)

    # Records the state of the arrow keys
    def setKey(self, key, value):
        self.keyMap[key] = value

    # Accepts arrow keys to move either the player or the menu cursor,
    # Also deals with grid checking and collision detection
    def move(self):

        # Get the time elapsed since last frame. We need this
        # for framerate-independent movement.
        elapsed = globalClock.getDt()

        # If the camera-left key is pressed, move camera left.
        # If the camera-right key is pressed, move camera right.
        if self.switchState is False:
            base.camera.lookAt(self.ralph)
            if self.keyMap["cam-left"] != 0:
                base.camera.setX(base.camera, -(elapsed * 20))
            if self.keyMap["cam-right"] != 0:
                base.camera.setX(base.camera, +(elapsed * 20))

        # save ralph's initial position so that we can restore it,
        # in case he falls off the map or runs into something.

        startpos = self.ralph.getPos()

        # If a move-key is pressed, move ralph in the specified direction.

        if self.keyMap["left"] != 0:
            self.ralph.setH(self.ralph.getH() + elapsed * 300)
        if self.keyMap["right"] != 0:
            self.ralph.setH(self.ralph.getH() - elapsed * 300)
        if self.keyMap["forward"] != 0:
            self.ralph.setY(self.ralph, -(elapsed * 25))

        # If ralph is moving, loop the run animation.
        # If he is standing still, stop the animation.

        if self.keyMap["forward"] != 0 or self.keyMap["left"] != 0 or self.keyMap["right"] != 0:
            if self.isMoving is False:
                self.ralph.loop("run")
                self.isMoving = True
        else:
            if self.isMoving:
                self.ralph.stop()
                self.ralph.pose("walk", 5)
                self.isMoving = False

        # If the camera is too far from ralph, move it closer.
        # If the camera is too close to ralph, move it farther.
        if self.switchState is False:
            camvec = self.ralph.getPos() - base.camera.getPos()
            camvec.setZ(0)
            camdist = camvec.length()
            camvec.normalize()
            if camdist > 10.0:
                base.camera.setPos(base.camera.getPos() + camvec * (camdist - 10))
                camdist = 10.0
            if camdist < 5.0:
                base.camera.setPos(base.camera.getPos() - camvec * (5 - camdist))
                camdist = 5.0

        # Now check for collisions.

        self.cTrav.traverse(render)

        # Adjust ralph's Z coordinate.  If ralph's ray hit terrain,
        # update his Z. If it hit anything else, or didn't hit anything, put
        # him back where he was last frame.

        #print(self.ralphGroundHandler.getNumEntries())

        entries = []
        for i in range(self.ralphGroundHandler.getNumEntries()):
            entry = self.ralphGroundHandler.getEntry(i)
            entries.append(entry)
        entries.sort(lambda x, y: cmp(y.getSurfacePoint(render).z,
                                      x.getSurfacePoint(render).z))
        if entries and entries[0].getIntoNode().getName() == "terrain":
            self.ralph.setZ(entries[0].getSurfacePoint(render).z)
        else:
            self.ralph.setPos(startpos)

        # Keep the camera at one foot above the terrain,
        # or two feet above ralph, whichever is greater.

        if self.switchState is False:
            entries = []
            for i in range(self.camGroundHandler.getNumEntries()):
                entry = self.camGroundHandler.getEntry(i)
                entries.append(entry)
            entries.sort(lambda x, y: cmp(y.getSurfacePoint(render).z,
                                          x.getSurfacePoint(render).z))
            if entries and entries[0].getIntoNode().getName() == "terrain":
                base.camera.setZ(entries[0].getSurfacePoint(render).z + 1.0)
            if base.camera.getZ() < self.ralph.getZ() + 2.0:
                base.camera.setZ(self.ralph.getZ() + 2.0)

            # The camera should look in ralph's direction,
            # but it should also try to stay horizontal, so look at
            # a floater which hovers above ralph's head.

            self.floater.setPos(self.ralph.getPos())
            self.floater.setZ(self.ralph.getZ() + 2.0)
            base.camera.setZ(base.camera.getZ())
            base.camera.lookAt(self.floater)

        self.ralph.setP(0)
        return Task.cont

    def setAI(self):
        # Creating AI World
        self.AIworld = AIWorld(render)

        self.accept("space", self.setMove)
        self.AIchar = AICharacter("ralph", self.ralph, 60, 0.05, 25)
        self.AIworld.addAiChar(self.AIchar)
        self.AIbehaviors = self.AIchar.getAiBehaviors()

        self.AIbehaviors.initPathFind("models/navmesh.csv")

        # AI World update
        taskMgr.add(self.AIUpdate, "AIUpdate")

    def setMove(self):
        self.AIbehaviors.addStaticObstacle(self.box)
        self.AIbehaviors.addStaticObstacle(self.box1)
        self.AIbehaviors.pathFindTo(self.pointer)
        self.ralph.loop("run")

    # To update the AIWorld
    def AIUpdate(self, task):
        self.AIworld.update()
        self.move()

        if self.path_no == 1 and self.AIbehaviors.behaviorStatus("pathfollow") == "done":
            self.path_no = 2
            self.AIbehaviors.pathFindTo(self.pointer1, "addPath")
            print("inside")

        if self.path_no == 2 and self.AIbehaviors.behaviorStatus("pathfollow") == "done":
            print("inside2")
            self.path_no = 1
            self.AIbehaviors.pathFindTo(self.pointer, "addPath")

        return Task.cont


w = World()
base.run()
