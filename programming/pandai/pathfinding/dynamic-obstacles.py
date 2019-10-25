# This tutorial provides an example of creating a character and having it walk
# around using PandAI and dynamic obstacle pathfinding

from direct.showbase.ShowBase import ShowBase
from panda3d.core import *
from direct.showbase.DirectObject import DirectObject
from direct.interval.IntervalGlobal import *
from direct.task import Task
from direct.actor.Actor import Actor
import random
import sys
import os
from direct.gui.DirectGui import *
from direct.gui.OnscreenText import OnscreenText

from panda3d.ai import *

base = ShowBase()

speed = 0.2
turnspeed = 3.5

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

        self.keyMap = {"left": 0, "right": 0, "forward": 0}

        #base.disableMouse()
        base.cam.setPosHpr(0, -210, 135, 0, 327, 0)
        self.done = []
        for i in range(4):
            self.done.append(False)
        self.toggle = False
        self.firstTime = False

        addTitle("Pandai Tutorial: Dynamic Avoidance of Moving Obstacles")
        addInstructions(0.95, "[ESC]: Quit")
        addInstructions(0.90, "[Arrow Keys]: Move the blue Ralph")
        addInstructions(0.85, "Try and move the blue Ralph in the path of the "
                              "other Ralphs")

        self.loadModels()
        self.setAI()

    def loadModels(self):

        self.environ1 = loader.loadModel("models/skydome")
        self.environ1.reparentTo(render)
        self.environ1.setPos(0, 0, 0)
        self.environ1.setScale(1)

        self.environ2 = loader.loadModel("models/skydome")
        self.environ2.reparentTo(render)
        self.environ2.setP(180)
        self.environ2.setH(270)
        self.environ2.setScale(1)

        self.environ = loader.loadModel("models/plane_demo1")
        self.environ.reparentTo(render)
        self.environ.setPos(0, 0, 0)

        self.Target = Actor("models/ralph",
                            {"run": "models/ralph-run",
                             "walk": "models/ralph-walk"})
        self.Target.setColor(0, 0, 1)
        self.Target.setPos(60, -60, 0)
        self.Target.setScale(2)
        self.Target.reparentTo(render)
        self.Target.loop("run")
        self.Targetforward = NodePath("Targetforward")
        self.Targetforward.setPos(0, -1, 0)
        self.Targetforward.reparentTo(self.Target)

        # Create the main character, Ralph
        self.ralph = []
        self.positions = []
        self.positions_new = []
        for i in range(4):
            self.ralph.append(Actor("models/ralph",
                                    {"run": "models/ralph-run",
                                     "walk": "models/ralph-walk"}))
            self.ralph[i].reparentTo(render)
            self.ralph[i].setScale(2)

            self.positions.append(NodePath(str(i)))
            self.positions_new.append(NodePath(str(i)))
            if i < 2:
                self.ralph[i].setPos(Point3(-61, -34 + (i * 40), 0))
            else:
                self.ralph[i].setPos(Point3(61, -34 + ((i - 2) * 40), 0))

            self.positions.append(NodePath(str(i)))
            self.positions_new.append(NodePath(str(i)))

        self.positions[0].setPos(Point3(-61, -34 + ((0) * 40), 0))
        self.positions[1].setPos(Point3(-53, -34 + ((1) * 40), 0))
        self.positions[2].setPos(Point3(53, -44 + ((0) * 40), 0))
        self.positions[3].setPos(Point3(61, -24 + ((1) * 40), 0))

        self.positions_new[0].setPos(Point3(61, -44 + ((0) * 40), 0))
        self.positions_new[1].setPos(Point3(53, -44 + ((1) * 40), 0))
        self.positions_new[2].setPos(Point3(-53, -24 + ((0) * 40), 0))
        self.positions_new[3].setPos(Point3(-61, -24 + ((1) * 40), 0))

    def setAI(self):
        # Creating AI World
        self.AIworld = AIWorld(render)

        #self.accept("enter", self.setMove)
        # Movement
        self.accept("arrow_left", self.setKey, ["left", 1])
        self.accept("arrow_right", self.setKey, ["right", 1])
        self.accept("arrow_up", self.setKey, ["forward", 1])
        self.accept("arrow_left-up", self.setKey, ["left", 0])
        self.accept("arrow_right-up", self.setKey, ["right", 0])
        self.accept("arrow_up-up", self.setKey, ["forward", 0])

        self.AIchar = []
        self.AIbehaviors = []
        for i in range(4):
            maxForce = 25 - (5 * random.random())
            char = AICharacter("ralph", self.ralph[i], 60, 0.05, maxForce)
            self.AIchar.append(char)
            self.AIworld.addAiChar(char)
            self.AIbehaviors.append(char.getAiBehaviors())
            self.AIbehaviors[i].initPathFind("models/navmesh.csv")

        # AI World update
        taskMgr.add(self.AIUpdate, "AIUpdate")

        taskMgr.add(self.Mover, "mover")

        self.setMove(1)

    def setMove(self, type):
        if type == 1:
            for i in range(4):
                if i == 0:
                    self.AIbehaviors[i].pathFindTo(self.positions_new[0], "addPath")
                    self.AIbehaviors[i].addDynamicObstacle(self.ralph[2])
                if i == 1:
                    self.AIbehaviors[i].pathFindTo(self.positions_new[1], "addPath")
                    self.AIbehaviors[i].addDynamicObstacle(self.ralph[3])
                if i == 2:
                    self.AIbehaviors[i].pathFindTo(self.positions_new[2], "addPath")
                if i == 3:
                    self.AIbehaviors[i].pathFindTo(self.positions_new[3], "addPath")
                if self.firstTime is False:
                    self.AIbehaviors[i].addDynamicObstacle(self.Target)
                self.ralph[i].loop("run")

            self.firstTime = True

        if type == 2:
            for i in range(4):
                if i == 0:
                    self.AIbehaviors[i].pathFindTo(self.positions[0], "addPath")
                if i == 1:
                    self.AIbehaviors[i].pathFindTo(self.positions[1], "addPath")
                if i == 2:
                    self.AIbehaviors[i].pathFindTo(self.positions[2], "addPath")
                if i == 3:
                    self.AIbehaviors[i].pathFindTo(self.positions[3], "addPath")

                self.ralph[i].loop("run")

    # To update the AIWorld
    def AIUpdate(self, task):
        self.AIworld.update()
        for i in range(4):
            status = self.AIbehaviors[i].behaviorStatus("pursue")
            if status == "done" or status == "paused":
                self.done[i] = True

        j = 0
        for i in range(4):
            if self.done[i] is True:
                j += 1

        if j == 4:
            self.toggle = not self.toggle
            if self.toggle is True:
                self.setMove(2)
            else:
                self.setMove(1)
            for i in range(4):
                self.done[i] = False

        return Task.cont

    def setKey(self, key, value):
        self.keyMap[key] = value

    def Mover(self, task):
        startPos = self.Target.getPos()

        if self.keyMap["left"] != 0:
            self.Target.setH(self.Target.getH() + turnspeed)
        if self.keyMap["right"] != 0:
            self.Target.setH(self.Target.getH() - turnspeed)
        if self.keyMap["forward"] != 0:
            forwardvector = self.Targetforward.getPos(render) - startPos
            self.Target.setPos(startPos + forwardvector * speed)

        return Task.cont


w = World()
base.run()
