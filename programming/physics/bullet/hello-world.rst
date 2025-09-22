.. _hello-world:

Bullet Hello World
==================

This page intends to lead through a minimal "hello world" program using
Panda3D and Bullet physics.

.. only:: cpp

   Compiling C++ Panda3D with Bullet code
   --------------------------------------

   To compile a Panda3D C++ program with Bullet, you will need to link directly
   against the Bullet libraries.

   These are not included in the Panda3D SDK, but are included in a separate
   "thirdparty tools" download on the download page. You will need to add the
   appropriate Bullet include and library directories to your compiler settings.

   On Ubuntu, we compile against the Bullet version that is included in the
   Ubuntu distribution, and you can use pkg-config to determine the include and
   library paths for Bullet.

World
-----

In order to use Bullet physics we need to have a BulletWorld. The world is
Panda3D's term for a "space" or "scene". The world holds physical objects like
rigid bodies, soft bodies or character controllers. It controls global
parameters, such a gravity, and it advances the simulation state.

.. only:: python

   .. code-block:: python

      from panda3d.bullet import BulletWorld
      world = BulletWorld()
      world.setGravity(Vec3(0, 0, -9.81))

.. only:: cpp

   First, include Panda3D bullet binding headers.

   .. code-block:: cpp

      #include "bulletWorld.h"
      #include "bulletPlaneShape.h"
      #include "bulletBoxShape.h"
      ...
      PT(BulletWorld) physics_world;
      physics_world = new BulletWorld();
      physics_world->set_gravity(0, 0, -9.81f);
      ...

The above code creates a new world, and it sets the worlds gravity to a downward
vector with length 9.81. While Bullet is in theory independent from any
particular units it is recommended to stick with SI units (kilogram, meter,
second). In SI units 9.81 m/s² is the gravity on Earth's surface.

Next we need to advance the simulation state. This is best done by a task which
gets called each frame. We find out about the elapsed time (dt), and pass this
value to the ``do_physics()`` method.

.. only:: python

   .. code-block:: python

      def update(task):
          dt = globalClock.getDt()
          world.doPhysics(dt)
          return task.cont

      taskMgr.add(update, 'update')

.. only:: cpp

   .. code-block:: cpp

      ...
      AsyncTask::DoneStatus update_scene(GenericAsyncTask* task, void* data) {
          // Get dt (from Python example) and apply to do_physics(float, int, int);
          ClockObject *co = ClockObject::get_global_clock();
          physics_world->do_physics(co->get_dt());

          return AsyncTask::DS_cont;
      }
      ...
      PT(GenericAsyncTask) task;
      task = new GenericAsyncTask("Scene update", &update_scene, nullptr);
      task_mgr->add(task); // Note: task_mgr = AsyncTaskManager::get_global_ptr();
      ...

The ``doPhysics`` method allows finer control on the way the simulation state is
advanced. Internally Bullet splits a timestep into several substeps. We can pass
a maximum number of substeps and the size of each substep, like show in the
following code.

.. only:: python

   .. code-block:: python

      world.doPhysics(dt, 10, 1.0/180.0)

.. only:: cpp

   .. code-block:: cpp

      physics_world->do_physics(co->get_dt(), 10, 1.0 / 180.0);

Here we have a maximum of 10 substeps, each with 1/180 seconds. Choosing smaller
substeps will make the simulation more realistic, but performance will decrease
too. Smaller substeps also reduce jitter.

Static bodies
-------------

So far we just have an empty world. We next need to add some objects. The most
simple objects are static bodies. Static object don't change their position or
orientation with time. Typical static objects are the ground or terrain, and
houses or other non-moveable obstacles. Here we create a simple plane which will
serve as a ground.

.. only:: python

   .. code-block:: python

      from panda3d.bullet import BulletPlaneShape
      from panda3d.bullet import BulletRigidBodyNode

      shape = BulletPlaneShape(Vec3(0, 0, 1), 1)

      node = BulletRigidBodyNode('Ground')
      node.addShape(shape)

      np = render.attachNewNode(node)
      np.setPos(0, 0, -2)

      world.attachRigidBody(node)

.. only:: cpp

   .. code-block:: cpp

      ...
      PT(BulletPlaneShape) floor_shape = new BulletPlaneShape(LVecBase3(0, 0, 1), 1);
      PT(BulletRigidBodyNode) floor_rigid_node = new BulletRigidBodyNode("Ground");

      floor_rigid_node->add_shape(floor_shape);

      NodePath np_ground = window->get_render().attach_new_node(floor_rigid_node);
      np_ground.set_pos(0, 0, -2);
      physics_world->attach(floor_rigid_node);
      ...

First we create a collision shape, in the case a ``BulletPlaneShape``. We pass
the plane's constant and normal vector within the shape's constructor. There is
a separate page about setting up the various collision shapes offered by Bullet,
so we won't go into more detail here.

Next we create a rigid body and add the previously created shape.
``BulletRigidBodyNode`` is derived from ``PandaNode``, and thus the rigid body
can be placed within the Panda3D scene graph. you can also use methods like
``setPos`` or ``setH`` to place the rigid body node where you want it to be.

Finally we need to attach the newly created rigid body node to the world. Only
rigid bodies attached to the world will be considered when advancing the
simulation state.

Dynamic bodies
--------------

Dynamic bodies are similar to static bodies. Except that dynamic bodies can be
moved around the world by applying force or torque. To setup a dynamic body is
almost the same as for static bodies. We will have to set one additional
property though, the body's mass. Setting a positive finite mass will create a
dynamic body, while setting the mass to zero will create a static body. Zero
mass is a convention for setting an infinite mass, which is the same as making
the body unmovable (static).

.. only:: python

   .. code-block:: python

      from panda3d.bullet import BulletBoxShape

      shape = BulletBoxShape(Vec3(0.5, 0.5, 0.5))

      node = BulletRigidBodyNode('Box')
      node.setMass(1.0)
      node.addShape(shape)

      np = render.attachNewNode(node)
      np.setPos(0, 0, 2)

      world.attachRigidBody(node)

.. only:: cpp

   .. code-block:: cpp

      ...
      PT(BulletBoxShape) box_shape = new BulletBoxShape(LVecBase3(0.5, 0.5, 0.5));
      PT(BulletRigidBodyNode) box_rigid_node = new BulletRigidBodyNode("Box");

      box_rigid_node->set_mass(1.0f); // Gravity affects this rigid node.
      box_rigid_node->add_shape(box_shape);

      NodePath np_box = window->get_render().attach_new_node(box_rigid_node);
      np_box.set_pos(0, 0, 2);
      physics_world->attach(box_rigid_node);
      ...

Bullet will automatically update a rigid body node's position and orientation if
is has changed after advancing the simulation state. So, if you have a
``GeomNode``- e. g. a textured box - and reparent this geom node below the rigid
body node, then the geom node will move around together with the rigid body. You
don't have to synchronize the visual world with the physics world.

The Program
-----------

Let's put everything learned on this page together into a single script, which
is shown below. It assumes that you have an .egg model of a 1 by 1 by 1 box.

when running the script you will see a box falling down onto an invisible plane.
The plane is invisible simply because we didn't parent a visual mode below the
plane's rigid body node. Of course we could have done so.

The model cube.egg used in this hello word sample can be found in the following
archive: https://www.panda3d.org/download/noversion/bullet-samples.zip

.. only:: cpp

   .. note:: Samples are currently available in Python code only.

.. only:: python

   .. code-block:: python

      import direct.directbase.DirectStart
      from panda3d.core import Vec3
      from panda3d.bullet import BulletWorld
      from panda3d.bullet import BulletPlaneShape
      from panda3d.bullet import BulletRigidBodyNode
      from panda3d.bullet import BulletBoxShape

      base.cam.setPos(0, -10, 0)
      base.cam.lookAt(0, 0, 0)

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

      # Box
      shape = BulletBoxShape(Vec3(0.5, 0.5, 0.5))
      node = BulletRigidBodyNode('Box')
      node.setMass(1.0)
      node.addShape(shape)
      np = render.attachNewNode(node)
      np.setPos(0, 0, 2)
      world.attachRigidBody(node)
      model = loader.loadModel('models/box.egg')
      model.flattenLight()
      model.reparentTo(np)

      # Update
      def update(task):
          dt = globalClock.getDt()
          world.doPhysics(dt)
          return task.cont

      taskMgr.add(update, 'update')
      base.run()

.. only:: cpp

   .. code-block:: cpp

      // Bullet Physics Example.
      // The following example is done from Python sources, Panda Reference and Panda Manual,
      // for more information, visit Panda3D and/or Bullet physics web site.

      // Compiling and Linking documentation and notes are not
      // covered in this file, check manual for more information.

      #include "pandaFramework.h"
      #include "windowFramework.h"
      #include "nodePath.h"
      #include "clockObject.h"

      #include "asyncTask.h"
      #include "genericAsyncTask.h"

      #include "bulletWorld.h"
      #include "bulletPlaneShape.h"
      #include "bulletBoxShape.h"

      BulletWorld *get_physics_world() {
        // physics_world is supposed to be an global variable,
        // but declaring global variables is not cool
        // for good programmers lol, instead, should use static keyword.
        static PT(BulletWorld) physics_world = new BulletWorld();
        return physics_world.p();
      }

      AsyncTask::DoneStatus update_scene(GenericAsyncTask* task, void* data) {
        // Get dt (from Python example) and apply to do_physics(float, int, int);
        ClockObject *co = ClockObject::get_global_clock();
        get_physics_world()->do_physics(co->get_dt(), 10, 1.0 / 180.0);

        return AsyncTask::DS_cont;
      }

      int main(int argc, char *argv[]) {
        // All variables.
        PandaFramework framework;
        WindowFramework *window;
        NodePath camera;
        PT(AsyncTaskManager) task_mgr;

        // Init everything :D
        framework.open_framework(argc, argv);
        framework.set_window_title("Bullet Physics");

        window = framework.open_window();
        window->enable_keyboard();
        window->setup_trackball();

        camera = window->get_camera_group();
        task_mgr = AsyncTaskManager::get_global_ptr();

        // Make physics simulation.
        // Static world stuff.
        get_physics_world()->set_gravity(0, 0, -9.81f);

        PT(BulletPlaneShape) floor_shape = new BulletPlaneShape(LVecBase3(0, 0, 1), 1);
        PT(BulletRigidBodyNode) floor_rigid_node = new BulletRigidBodyNode("Ground");

        floor_rigid_node->add_shape(floor_shape);

        NodePath np_ground = window->get_render().attach_new_node(floor_rigid_node);
        np_ground.set_pos(0, 0, -2);
        get_physics_world()->attach(floor_rigid_node);

        // Dynamic world stuff.
        PT(BulletBoxShape) box_shape = new BulletBoxShape(LVecBase3(0.5, 0.5, 0.5));
        PT(BulletRigidBodyNode) box_rigid_node = new BulletRigidBodyNode("Box");

        box_rigid_node->set_mass(1.0f); // Gravity affects this rigid node.
        box_rigid_node->add_shape(box_shape);

        NodePath np_box = window->get_render().attach_new_node(box_rigid_node);
        np_box.set_pos(0, 0, 2);
        get_physics_world()->attach(box_rigid_node);

        NodePath np_box_model = window->load_model(framework.get_models(), "models/box");
        np_box_model.set_pos(-0.5,-0.5,-0.5);
        np_box.flatten_light();
        np_box_model.reparent_to(np_box);

        PT(GenericAsyncTask) task;
        task = new GenericAsyncTask("Scene update", &update_scene, nullptr);
        task_mgr->add(task);

        framework.main_loop();
        framework.close_framework();

        return (0);
      }
