from direct.showbase.ShowBase import ShowBase
from direct.showbase.DirectObject import DirectObject
from direct.gui.OnscreenText import OnscreenText, TextNode
from panda3d.core import CollisionTraverser
from panda3d.core import CollisionHandlerQueue, CollisionNode, BitMask32
from panda3d.core import CollisionPlane, CollisionSphere, CollisionRay
from panda3d.core import Plane, Vec3, Point3


class World(DirectObject):

    def __init__(self):
        # Create a traverser that Panda3D will automatically use every frame.
        base.cTrav = CollisionTraverser()
        # Create a handler for the events.
        self.collHandler = CollisionHandlerQueue()

        # Define a few bitmasks for use.
        # Teaching the concepts of bitmasks is out of the scope of this sample.
        # This just shows a practical application of bitmasks.
        goodMask = BitMask32(0x1)
        badMask = BitMask32(0x2)
        floorMask = BitMask32(0x4)

        # Make a list of different combinations of the masks for later use.
        # We will switch between these masks later on.
        self.maskList = [
            ["floor", floorMask],
            ["smiley", goodMask],
            ["frowney", badMask],
            ["characters", goodMask | badMask],
            ["smiley and floor", goodMask | floorMask],
            ["frowney and floor", badMask | floorMask],
            ["all", floorMask | goodMask | badMask]
        ]
        # This keeps track of where we are in the dictionary.
        self.maskPos = 0

        # First we create a floor collision plane.
        floorNode = base.render.attachNewNode("Floor NodePath")
        # Create a collision plane solid.
        collPlane = CollisionPlane(Plane(Vec3(0, 0, 1), Point3(0, 0, 0)))
        # Call our function that creates a nodepath with a collision node.
        floorCollisionNP = self.makeCollisionNodePath(floorNode, collPlane)
        # Get the collision node the Nodepath is referring to.
        floorCollisionNode = floorCollisionNP.node()
        # The floor is only an into object, so just need to set its into mask.
        floorCollisionNode.setIntoCollideMask(floorMask)

        # Create a collision sphere. Since the models we'll be colliding
        # are basically the same we can get away with just creating one
        # collision solid and adding the same solid to both collision nodes.
        collSphere = CollisionSphere(0, 0, 0, 1.5)

        # Make a smiley.
        smiley = base.loader.loadModel('smiley')
        smiley.reparentTo(base.render)
        smiley.setPos(-3, 3, 3)
        smiley.setName("Smiley")
        smileyCollisionNP = self.makeCollisionNodePath(smiley, collSphere)
        # Like with the floor plane we need to set the into mask.
        # Here we shortcut getting the actual collision node.
        smileyCollisionNP.node().setIntoCollideMask(goodMask)

        # Make a frowney.
        frowney = base.loader.loadModel('frowney')
        frowney.reparentTo(base.render)
        frowney.setPos(-3, 3, 7)
        frowney.setName("Frowney")
        frowneyCollisionNP = self.makeCollisionNodePath(frowney, collSphere)
        # Use the the Nodepath.setCollideMask() function to set the into mask.
        # setCollideMask() sets the into mask of all child nodes to the given
        # mask.
        frowneyCollisionNP.setCollideMask(badMask)
        # Note that we don't call setCollideMask() from frowney because this
        # will turn the frowney mesh into a collision mesh which is unwanted.

        # Note that we didn't set a from collide mask for previous objects
        # since we're not adding them to the traverser as from objects.

        # Make a collision ray that passes through all of the objects.
        self.pointerNode = base.render.attachNewNode("Main Collider")
        self.pointerNode.setPos(-3, 3, 10)
        # Create a ray collision solid that points downwards.
        raySolid = CollisionRay(0, 0, 0, 0, 0, -1)
        mainColNP = self.makeCollisionNodePath(self.pointerNode, raySolid)
        self.mainColNode = mainColNP.node()
        # Set a from collide mask for this ray so that we can selectively
        # collide against the other objects.
        self.mainColNode.setFromCollideMask(self.maskList[self.maskPos][1])
        base.cTrav.addCollider(mainColNP, self.collHandler)

        # Set up the camera.
        base.disableMouse()
        base.camera.setPos(20, -20, 5)
        base.camera.lookAt(0, 0, 5)
        # Debug mode for collision traversers; shows collisions visually.
        base.cTrav.showCollisions(base.render)

        # Setup the title text.
        collideText = self.maskList[self.maskPos][0]
        self.title = OnscreenText(text="Colliding with %s" % (collideText),
                                  mayChange=True,
                                  pos=(0.3, 0),
                                  align=TextNode.ALeft,
                                  fg=(1, 1, 1, 1))
        OnscreenText(text="Press space to change collision mask",
                     pos=(0, 0.8),
                     fg=(1, 1, 1, 1))

        # Set space to change the from collision mask of the collision ray.
        base.accept("space", self.switchCollisionMask)

    def makeCollisionNodePath(self, nodepath, solid):
        '''
        Creates a collision node and attaches the collision solid to the
        supplied NodePath. Returns the nodepath of the collision node.

        '''
        # Creates a collision node named after the name of the NodePath.
        collNode = CollisionNode("%s c_node" % nodepath.getName())
        collNode.addSolid(solid)
        collisionNodepath = nodepath.attachNewNode(collNode)
        # Show the collision node, which makes the solids show up.
        collisionNodepath.show()

        return collisionNodepath

    def switchCollisionMask(self):
        if self.maskPos == len(self.maskList) - 1:
            self.maskPos = 0
        else:
            self.maskPos += 1

        # Changing the from collide mask of objects allows you to selectively
        # test collisions against different objects.
        name, mask = self.maskList[self.maskPos]
        self.mainColNode.setFromCollideMask(mask)
        self.title.setText("Colliding with %s" % (name))


base = ShowBase()
world = World()
base.run()
