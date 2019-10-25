# This tutorial provides an example of creating a character and having it walk
# around using PandAI pathfinding with static obstacle avoidance

from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import *
from direct.task import Task
from direct.actor.Actor import Actor
import sys
import os
from direct.gui.DirectGui import *
from direct.gui.OnscreenText import OnscreenText

from panda3d.ai import *

base = ShowBase()

speed = 0.75

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

        self.keyMap = {"left": 0, "right": 0, "up": 0, "down": 0}

        addTitle("Pandai Tutorial: Adding Dynamic Obstacles")
        addInstructions(0.95, "[ESC]: Quit")
        addInstructions(0.90, "[Enter]: Start Pathfinding")
        addInstructions(0.85, "[Arrow Keys]: Move Arrow")
        addInstructions(0.80, "[1]: Small box")
        addInstructions(0.75, "[2]: Big box")
        addInstructions(0.70, "[Space]: Place box")

        #base.disableMouse()
        base.cam.setPosHpr(0, -210, 135, 0, 327, 0)
        self.box = 0
        self.pointer_move = False

        self.loadModels()
        self.setAI()

    def loadModels(self):

        self.environ1 = loader.loadModel("models/skydome")
        self.environ1.reparentTo(render)
        self.environ1.setScale(1)

        self.environ2 = loader.loadModel("models/skydome")
        self.environ2.reparentTo(render)
        self.environ2.setP(180)
        self.environ2.setH(270)
        self.environ2.setScale(1)

        self.environ = loader.loadModel("models/groundPlane")
        self.environ.reparentTo(render)

        # Create the main character, Ralph

        #ralphStartPos = self.environ.find("**/start_point").getPos()
        ralphStartPos = Vec3(-51, -64, 0)
        self.ralph = Actor("models/ralph",
                           {"run": "models/ralph-run",
                            "walk": "models/ralph-walk"})
        self.ralph.reparentTo(render)
        self.ralph.setScale(2)
        self.ralph.setPos(ralphStartPos)

        self.pointer = loader.loadModel("models/arrow")
        self.pointer.setColor(1, 0, 0)
        self.pointer.setPos(60, -60, 0)
        self.pointer.setScale(3)
        self.pointer.reparentTo(render)

    def setAI(self):
        # Creating AI World
        self.AIworld = AIWorld(render)

        self.accept("enter", self.setMove)
        self.accept("1", self.addBlock)
        self.accept("2", self.addBigBlock)
        self.accept("space", self.addStaticObstacle)

        # Movement
        self.accept("arrow_left", self.setKey, ["left", 1])
        self.accept("arrow_right", self.setKey, ["right", 1])
        self.accept("arrow_up", self.setKey, ["up", 1])
        self.accept("arrow_down", self.setKey, ["down", 1])
        self.accept("arrow_left-up", self.setKey, ["left", 0])
        self.accept("arrow_right-up", self.setKey, ["right", 0])
        self.accept("arrow_up-up", self.setKey, ["up", 0])
        self.accept("arrow_down-up", self.setKey, ["down", 0])

        self.AIchar = AICharacter("ralph", self.ralph, 60, 0.05, 15)
        self.AIworld.addAiChar(self.AIchar)
        self.AIbehaviors = self.AIchar.getAiBehaviors()

        self.AIbehaviors.initPathFind("models/navmesh.csv")

        # AI World update
        taskMgr.add(self.AIUpdate, "AIUpdate")

        # Movement task
        taskMgr.add(self.Mover, "Mover")

        self.dirnlight1 = DirectionalLight("dirn_light1")
        self.dirnlight1.setColor((1.0, 1.0, 1.0, 1.0))
        self.dirnlightnode1 = render.attachNewNode(self.dirnlight1)
        self.dirnlightnode1.setHpr(0, 317, 0)
        render.setLight(self.dirnlightnode1)

    def setMove(self):
        self.AIbehaviors.pathFindTo(self.pointer)
        self.ralph.loop("run")

    def addBlock(self):
        self.pointer_move = True
        self.box = loader.loadModel("models/box")
        self.box.setPos(0, -60, 0)
        self.box.setScale(1)
        self.box.reparentTo(render)

    def addBigBlock(self):
        self.pointer_move = True
        self.box = loader.loadModel("models/box")
        self.box.setPos(0, -60, 0)
        self.box.setScale(2)
        self.box.setColor(1, 1, 0)
        self.box.reparentTo(render)

    def addStaticObstacle(self):
        if self.box != 0:
            self.AIbehaviors.addStaticObstacle(self.box)
            self.box = 0
            self.pointer_move = False

    # To update the AIWorld
    def AIUpdate(self, task):
        self.AIworld.update()
        #if self.AIbehaviors.behaviorStatus("pathfollow") == "done":
        #    self.ralph.stop("run")
        #    self.ralph.pose("walk", 0)

        return Task.cont

    def setKey(self, key, value):
        self.keyMap[key] = value

    def Mover(self, task):
        startPos = self.pointer.getPos()
        if self.keyMap["left"] != 0:
            self.pointer.setPos(startPos + Point3(-speed, 0, 0))
        if self.keyMap["right"] != 0:
            self.pointer.setPos(startPos + Point3(speed, 0, 0))
        if self.keyMap["up"] != 0:
            self.pointer.setPos(startPos + Point3(0, speed, 0))
        if self.keyMap["down"] != 0:
            self.pointer.setPos(startPos + Point3(0, -speed, 0))

        if self.pointer_move is True and self.box != 0:
            self.box.setPos(self.pointer.getPos())

        return Task.cont


w = World()
base.run()
