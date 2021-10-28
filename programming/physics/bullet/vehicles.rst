.. _vehicles:

Bullet Vehicles
===============

Bullet comes with a simple vehicle controller, which can be used for arcade
style vehicle simulations. Instead of simulation of each wheel and chassis as
separate rigid bodies connected by joints, it simply uses a single rigid body
for the chassis. Collision detection for the wheels is approximated by ray
casts, and the tire friction is a basic anisotropic friction model. This
approach to vehicle modelling is called "raycast vehicle", and it is used
widely in commercial and non-commercial driving games.

Setup
-----

In order to create a vehicle we first have to create an ordinary dynamic rigid
body. This rigid body will serve as the vehicle chassis. Then we can create a
new instance of :class:`.BulletVehicle`. We have to pass the
:class:`.BulletWorld` and the :class:`.BulletRigidBodyNode` as arguments to the
vehicle constructor.

.. only:: python

   The following code snippet shows how this could be done.

   .. code-block:: python

      from panda3d.bullet import BulletVehicle

      # Chassis body
      shape = BulletBoxShape(Vec3(0.7, 1.5, 0.5))
      ts = TransformState.makePos(Point3(0, 0, 0.5))

      chassisNP = render.attachNewNode(BulletRigidBodyNode('Vehicle'))
      chassisNP.node().addShape(shape, ts)
      chassisNP.setPos(0, 0, 1)
      chassisNP.node().setMass(800.0)
      chassisNP.node().setDeactivationEnabled(False)

      world.attachRigidBody(chassisNP.node())

      # Chassis geometry
      loader.loadModel('path/to/model').reparentTo(chassisNP)

      # Vehicle
      vehicle = BulletVehicle(world, chassisNP.node())
      vehicle.setCoordinateSystem(ZUp)
      world.attachVehicle(vehicle)

Wheels
------

Once we have created the chassis and the vehicle we can add wheels to the
vehicle. We can create a new wheel using the ``createWheel`` factory method of
the previously created vehicle. Once created we still have to configure the
wheel, that is set friction parameters, offset of the wheel hub with respect to
the chassis, axle direction and so on.

.. only:: python

   The following sample shows how to create and configure a wheel. In this case
   a front wheel is created. Front wheels are steerable.

   .. code-block:: python

      wheelNP = loader.loadModel('path/to/model')
      wheelNP.reparentTo(render)

      wheel = vehicle.createWheel()

      wheel.setNode(wheelNP.node())
      wheel.setChassisConnectionPointCs(Point3(0.8, 1.1, 0.3))
      wheel.setFrontWheel(True)

      wheel.setWheelDirectionCs(Vec3(0, 0, -1))
      wheel.setWheelAxleCs(Vec3(1, 0, 0))
      wheel.setWheelRadius(0.25)
      wheel.setMaxSuspensionTravelCm(40.0)

      wheel.setSuspensionStiffness(40.0)
      wheel.setWheelsDampingRelaxation(2.3)
      wheel.setWheelsDampingCompression(4.4)
      wheel.setFrictionSlip(100.0)
      wheel.setRollInfluence(0.1)

Steering and Engine/Brake
-------------------------

Finally we need to control steering and engine/brakes. This is best done using a
task, and keeping the current steering angle around somewhere in a variable.

Here we use a very simple model of controlling the steering angle. If 'turnLeft'
or 'turnRight' keys are pressed the steering angle will increase/decrease at a
constant rate, until a maximum steering angle is achieved. No relaxation is
applied. Therefor we also define constants for the maximum steering angle (here:
steeringClamp) and the rate at which the steering angle increases/decreases
(here: steeringIncrement).

The engine force and brake model shown is very simple too. If 'forward' is
pressed then the engine force will be the maximum engine force, otherwise engine
force will be zero. Likewise for the brakes.

Once the steering angle and engine/brake forces are determined they will be
applied to the wheels. Each wheel - addressed by it's index, i. e. 0 to 3 for a
four-wheel car - can be individually assigned values for steering and
engine/brake force. This way front/rear drives or four-wheel-drives can be
simulated.

.. only:: python

   The following code snippet shows pseudocode for controlling steering and
   engine/brakes.

   .. code-block:: python

      # Steering info
      steering = 0.0            # degree
      steeringClamp = 45.0      # degree
      steeringIncrement = 120.0 # degree per second

      # Process input
      engineForce = 0.0
      brakeForce = 0.0

      if inputState.isSet('forward'):
          engineForce = 1000.0
          brakeForce = 0.0

      if inputState.isSet('reverse'):
          engineForce = 0.0
          brakeForce = 100.0

      if inputState.isSet('turnLeft'):
          steering += dt * steeringIncrement
          steering = min(steering, steeringClamp)

      if inputState.isSet('turnRight'):
          steering -= dt * steeringIncrement
          steering = max(steering, -steeringClamp)

      # Apply steering to front wheels
      vehicle.setSteeringValue(steering, 0)
      vehicle.setSteeringValue(steering, 1)

      # Apply engine and brake to rear wheels
      vehicle.applyEngineForce(engineForce, 2)
      vehicle.applyEngineForce(engineForce, 3)
      vehicle.setBrake(brakeForce, 2)
      vehicle.setBrake(brakeForce, 3)

More realistic control models can be invented, in order to meet the control
requirements of individual driving games. For example:

-  Relaxing the steering angle to zero if the user does no hold down the left
   or right keys.
-  Reducing the maximum steering angle with increasing vehicle speed.
-  Setting engine force based on an analogue input, or alternatively based on
   the duration of the forward key being pressed down.

However, it is up to you do invent such controls. What Bullet requires is that
you provide the steering angle and the engine and brake force.
