.. _pusher-example:

Pusher Example
==============

.. only:: python

   Here is a short example that shows two small spheres using a
   ``CollisionHandlerPusher``:

   .. code-block:: python

      from direct.showbase.ShowBase import ShowBase
      from panda3d.core import CollisionTraverser, CollisionHandlerPusher
      from panda3d.core import CollisionNode, CollisionSphere
      from panda3d.core import Point3

      # Initialize the scene.
      ShowBase()

      # Initialize the collision traverser.
      base.cTrav = CollisionTraverser()

      # Initialize the Pusher collision handler.
      pusher = CollisionHandlerPusher()

      # Load a model.
      smiley = loader.loadModel('smiley')
      # Reparent the model to the camera so we can move it.
      smiley.reparentTo(camera)
      # Set the initial position of the model in the scene.
      smiley.setPos(0, 25.5, 0.5)

      # Create a collision node for this object.
      cNode = CollisionNode('smiley')
      # Attach a collision sphere solid to the collision node.
      cNode.addSolid(CollisionSphere(0, 0, 0, 1.1))
      # Attach the collision node to the object's model.
      smileyC = smiley.attachNewNode(cNode)
      # Set the object's collision node to render as visible.
      smileyC.show()

      # Load another model.
      frowney = loader.loadModel('frowney')
      # Reparent the model to render.
      frowney.reparentTo(render)
      # Set the position of the model in the scene.
      frowney.setPos(5, 25, 0)

      # Create a collision node for this object.
      cNode = CollisionNode('frowney')
      # Attach a collision sphere solid to the collision node.
      cNode.addSolid(CollisionSphere(0, 0, 0, 1.1))
      # Attach the collision node to the object's model.
      frowneyC = frowney.attachNewNode(cNode)
      # Set the object's collision node to render as visible.
      frowneyC.show()

      # Add the Pusher collision handler to the collision traverser.
      base.cTrav.addCollider(frowneyC, pusher)
      # Add the 'frowney' collision node to the Pusher collision handler.
      pusher.addCollider(frowneyC, frowney, base.drive.node())

      # Have the 'smiley' sphere moving to help show what is happening.
      frowney.posInterval(5, Point3(5, 25, 0), startPos=Point3(-5, 25, 0), fluid=1).loop()

      # Run the scene. Move around with the mouse to see how the moving sphere changes
      # course to avoid the one attached to the camera.
      run()

.. only:: cpp

