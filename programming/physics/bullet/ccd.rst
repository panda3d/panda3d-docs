.. _ccd:

Bullet Continuous Collision Detection
=====================================

CCD is short for Continuous Collision Detection, which is a workaround for a
common problem in game physics: a fast moving body might not collide with an
obstacle if in one frame it is "before" the obstacle, and in the next one it
is already "behind" the obstacle. At no frame the fast moving body overlaps
with the obstacle, and thus no response is created. This is what CCD is for.
CCD checks for collisions in between frames, and thus can prevent fast moving
objects from passing through thin obstacles.

Bullet has built-in support for CCD, but bodies have to be configured properly
to enable CCD checks.

When checking for collision in between frames Bullet does not use the full
collision shape (or shapes) of a body - this would make continuous collision
detection too slow. Instead Bullet uses a sphere shape, the so-called "swept
sphere". "swept" because the sphere is swept from the original position to the
new position of the body. So, in order to enable CCD checks on a body we have
to setup this sphere, and a CCD motion threshold:

.. only:: python

   .. code-block:: python

      bodyNP.node().setCcdMotionThreshold(1e-7)
      bodyNP.node().setCcdSweptSphereRadius(0.50)

.. only:: cpp

   .. code-block:: cpp

      TODO

We have to set up the swept sphere only on the fast moving dynamic bodies.
There is no need to do anything for the static or slow moving obstacles.

One particular use for CCD is firing a bullet (bullet is lowercase here,
indicating that a projectile is meant, not the Bullet physics engine). Below
is a sample showing one way to implement shooting bullets.

.. only:: python

   .. code-block:: python

      bullets = []

      def removeBullet(task):
        if len(bullets) < 1: return

        bulletNP = bullets.pop(0)
        world.removeRigidBody(bulletNP.node())

        return task.done

      def shootBullet(ccd):
        # Get from/to points from mouse click
        pMouse = base.mouseWatcherNode.getMouse()
        pFrom = Point3()
        pTo = Point3()
        base.camLens.extrude(pMouse, pFrom, pTo)

        pFrom = render.getRelativePoint(base.cam, pFrom)
        pTo = render.getRelativePoint(base.cam, pTo)

        # Calculate initial velocity
        v = pTo - pFrom
        v.normalize()
        v *= 10000.0

        # Create bullet
        shape = BulletBoxShape(Vec3(0.5, 0.5, 0.5))
        body = BulletRigidBodyNode('Bullet')
        bodyNP = render.attachNewNode(body)
        bodyNP.node().addShape(shape)
        bodyNP.node().setMass(2.0)
        bodyNP.node().setLinearVelocity(v)
        bodyNP.setPos(pFrom)
        bodyNP.setCollideMask(BitMask32.allOn())

        # Enable CCD
        bodyNP.node().setCcdMotionThreshold(1e-7)
        bodyNP.node().setCcdSweptSphereRadius(0.50)

        world.attachRigidBody(bodyNP.node())

        # Remove the bullet again after 1 second
        bullets.append(bodyNP)
        taskMgr.doMethodLater(1, removeBullet, 'removeBullet')

.. only:: cpp

   .. code-block:: cpp

      TODO

Most of the code is related to finding the initial velocity vector for the
bullet, which is calculated from the mouse position when shooting the bullet.
