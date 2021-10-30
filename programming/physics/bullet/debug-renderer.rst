.. _debug-renderer:

Bullet Debug Renderer
=====================

In the previous "hello world" sample we have been introduced to a few Bullet
physics objects, for example the rigid body (:class:`.BulletRigidBodyNode`) or
box and plane collision shapes (:class:`.BulletPlaneShape`,
:class:`.BulletBoxShape`).

These objects are part of the Panda3D scene graph. But they are not visible.
In order to be able to actually see a rigid body we had to reparent a visible
geometry below the rigid body node. This is fine, since we (1) can control the
way an object looks like, by choosing whatever visible geometry we want, and
(2) we can create invisible objects too, by not reparenting any geometry below
a rigid body.

But when developing a game it sometimes would be handy to actually see where
the physical objects are. This is what the :class:`.BulletDebugNode` is for.
It's not meant for users playing the game, but as an aid in finding problems
while developing the game.

The debug node is pretty easy to use. We just need to create such a node,
place it in the scene graph, and tell the Bullet world that we have such a
node. From now on Bullet will create a "debug" visualisation of the world's
content within the debug node, whenever
:meth:`~panda3d.bullet.BulletWorld.do_physics()` is called. The following code
snippet shows how to do this:

.. only:: python

   .. code-block:: python

      from panda3d.bullet import BulletDebugNode

      debugNode = BulletDebugNode('Debug')
      debugNode.showWireframe(True)
      debugNode.showConstraints(True)
      debugNode.showBoundingBoxes(False)
      debugNode.showNormals(False)
      debugNP = render.attachNewNode(debugNode)
      debugNP.show()

      world = BulletWorld()
      world.setGravity(Vec3(0, 0, -9.81))
      world.setDebugNode(debugNP.node())

.. only:: cpp

   .. code-block:: cpp

      #include "panda3d/bulletDebugNode.h"
      ...
      PT(BulletDebugNode) bullet_dbg_node;
      bullet_dbg_node = new BulletDebugNode("Debug");
      bullet_dbg_node->show_bounding_boxes(true);
      bullet_dbg_node->show_constraints(true);
      bullet_dbg_node->show_normals(true);
      bullet_dbg_node->show_wireframe(true);

      NodePath np_dbg_node = window->get_render().attach_new_node(get_physics_debug_node());
      np_dbg_node.show();

      physics_world->set_debug_node(get_physics_debug_node());
      ...

We can control the amount of information rendered using the following methods:

:meth:`~.panda3d.bullet.BulletDebugNode.show_wireframe()`
   Displays collision shapes in wireframe mode.

:meth:`~.panda3d.bullet.BulletDebugNode.show_constraints()`
   Display limits defined for constraints, e.g. a pivot axis or maximum
   amplitude.

:meth:`~.panda3d.bullet.BulletDebugNode.show_bounding_boxes()`
   Displays axis aligned bounding boxes for objects.

:meth:`~.panda3d.bullet.BulletDebugNode.show_normals()`
   Displays normal vectors for triangle mesh and heightfield faces.

There is one thing to pay attention to: By default the :class:`.BulletDebugNode`
is hidden right after creation. If we want to see the debug visualisation from
the first frame on we have to unhide it, using :meth:`~.NodePath.show()`.

Since debug rendering is not very fast we can turn debug rendering on and off,
without having to remove the debug node from the scene graph. Turning debug
rendering on and of is simply done by hiding or showing the debug node. The
following code shows how to toggle debug node visibility on and off, using the
F1 key:

.. only:: python

   .. code-block:: python

      from direct.showbase.DirectObject import DirectObject

      o = DirectObject()
      o.accept('f1', toggleDebug)

      def toggleDebug():
          if debugNP.isHidden():
              debugNP.show()
          else:
              debugNP.hide()

.. only:: cpp

   .. code-block:: cpp

      ...
      void toggle_physics_debug(const Event *e, void *data) {
          static bool show_state = true;
          show_state = !show_state;
          bullet_dbg_node->show_bounding_boxes(show_state);
          bullet_dbg_node->show_constraints(show_state);
          bullet_dbg_node->show_normals(show_state);
          bullet_dbg_node->show_wireframe(show_state);
      }
      ...
      framework.define_key("f1", "Toggle Physics debug", toggle_physics_debug, nullptr);
      ....

   You can notice that CXX code made Toggle action in different way than Python
   code, the reason is simple, CXX uses the BulletDebugNode instead of NodePath
   that parent first node, anyway you can apply the last one using global
   variables or static function calls, or use directly BulletDebugNode like the
   following program.

   .. code-block:: cpp

      // Bullet Debug Node Example.
      // The following example is done from Python sources, Panda Reference and Panda Manual,
      // for more information, visit Panda3D and/or Bullet physics web site.

      // Compiling and Linking documentation and notes are not
      // covered in this file, check manual for mor information.

      #include "panda3d/pandaFramework.h"
      #include "panda3d/windowFramework.h"
      #include "panda3d/nodePath.h"
      #include "panda3d/clockObject.h"

      #include "panda3d/asyncTask.h"
      #include "panda3d/genericAsyncTask.h"

      #include "panda3d/bulletWorld.h"
      #include "panda3d/bulletDebugNode.h"
      #include "panda3d/bulletPlaneShape.h"
      #include "panda3d/bulletBoxShape.h"

      BulletWorld *get_physics_world() {
          // physics_world is supposed to be an global variable,
          // but declaring global variables is not cool
          // for good programmers lol, instead, should use static keyword.
          static BulletWorld *physics_world = new BulletWorld();
          return physics_world;
      }

      BulletDebugNode *get_physics_debug_node() {
          // Global variable.
          static BulletDebugNode *bullet_dbg_node = new BulletDebugNode("Debug");
          return bullet_dbg_node;
      }

      void toggle_physics_debug(const Event *e, void *data) {
          static bool show_state = true;
          show_state = !show_state;
          get_physics_debug_node()->show_bounding_boxes(show_state);
          get_physics_debug_node()->show_constraints(show_state);
          get_physics_debug_node()->show_normals(show_state);
          get_physics_debug_node()->show_wireframe(show_state);
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
          PT(AsyncTaskManager) task_mgr;

          // Init everything :D
          framework.open_framework(argc, argv);
          framework.set_window_title("Bullet Physics");

          window = framework.open_window();
          window->enable_keyboard();
          window->setup_trackball();

          task_mgr = AsyncTaskManager::get_global_ptr();

          // Make physics simulation.
          // Static world stuff.
          get_physics_world()->set_gravity(0, 0, -9.8);

          PT(BulletPlaneShape) floor_shape = new BulletPlaneShape(LVecBase3(0, 0, 1), 1);
          PT(BulletRigidBodyNode) floor_rigid_node = new BulletRigidBodyNode("Ground");

          floor_rigid_node->add_shape(floor_shape);

          NodePath np_ground = window->get_render().attach_new_node(floor_rigid_node);
          np_ground.set_pos(0, 0, -2);
          get_physics_world()->attach(floor_rigid_node);

          // Dynamic world stuff.
          PT(BulletBoxShape) box_shape = new BulletBoxShape(LVecBase3(0.5, 0.5, 0.5));
          PT(BulletRigidBodyNode) box_rigid_node = new BulletRigidBodyNode("Box");

          box_rigid_node->set_mass(1.0); // Gravity affects this rigid node.
          box_rigid_node->add_shape(box_shape);

          NodePath np_box = window->get_render().attach_new_node(box_rigid_node);
          np_box.set_pos(0, 0, 2);
          get_physics_world()->attach(box_rigid_node);

          NodePath np_box_model = window->load_model(framework.get_models(), "models/box");
          np_box_model.set_pos(-0.5, -0.5, -0.5);
          np_box.flatten_light();
          np_box_model.reparent_to(np_box);

          // Debug stuff.
          get_physics_debug_node()->show_bounding_boxes(true);
          get_physics_debug_node()->show_constraints(true);
          get_physics_debug_node()->show_normals(true);
          get_physics_debug_node()->show_wireframe(true);

          NodePath np_dbg_node = window->get_render().attach_new_node(get_physics_debug_node());
          np_dbg_node.show();

          get_physics_world()->set_debug_node(get_physics_debug_node());
          framework.define_key("f1", "Toggle Physics debug", toggle_physics_debug, nullptr);

          // Setup tasks and keys.
          PT(GenericAsyncTask) task;
          task = new GenericAsyncTask("Scene update", &update_scene, nullptr);
          task_mgr->add(task);

          framework.main_loop();
          framework.close_framework();

          return (0);
      }
