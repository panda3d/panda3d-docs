.. _bullet_samples:

Bullet Samples
==============

Learning the Bullet module is best done by looking at working samples. A bunch
of tutorials can be downloaded from the following link. The samples include
all models and textures.

https://www.panda3d.org/download/noversion/bullet-samples.zip

More samples contributed by various users follow below here:

Stack of cubes falling on top of each other:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. only:: python

   .. code-block:: python

      import direct.directbase.DirectStart
      from panda3d.core import Vec3
      from panda3d.bullet import BulletWorld
      from panda3d.bullet import BulletPlaneShape
      from panda3d.bullet import BulletRigidBodyNode
      from panda3d.bullet import BulletBoxShape

      base.cam.setPos(10, -30, 20)
      base.cam.lookAt(0, 0, 5)

      # World
      world = BulletWorld()
      world.setGravity(Vec3(0, 0, -9.81))

      # Plane
      shape = BulletPlaneShape(Vec3(0, 0, 1), 1)
      node = BulletRigidBodyNode('Ground')
      node.addShape(shape)
      np = render.attachNewNode(node)
      np.setPos(0, 0, -2)
      world.attachRigidBody(node)

      # Boxes
      model = loader.loadModel('models/box.egg')
      model.setPos(-0.5, -0.5, -0.5)
      model.flattenLight()
      shape = BulletBoxShape(Vec3(0.5, 0.5, 0.5))
      for i in range(10):
          node = BulletRigidBodyNode('Box')
          node.setMass(1.0)
          node.addShape(shape)
          np = render.attachNewNode(node)
          np.setPos(0, 0, 2+i*2)
          world.attachRigidBody(node)
          model.copyTo(np)

      # Update
      def update(task):
        dt = globalClock.getDt()
        world.doPhysics(dt)
        return task.cont

      taskMgr.add(update, 'update')
      base.run()
