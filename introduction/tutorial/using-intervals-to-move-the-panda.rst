.. _using-intervals-to-move-the-panda:

Using Intervals to move the Panda
=================================

Intervals and Sequences
-----------------------

:ref:`intervals`
~~~~~~~~~~~~~~~~

*Intervals* are tasks that change a property from one value to another over a
specified period of time. Starting an interval effectively starts a background
process that modifies the property over the specified period of time.

:ref:`Sequences <sequences-and-parallels>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Sequences*, also called *MetaIntervals* are tasks that execute one interval
after another.

The Program
-----------

Update the Code
~~~~~~~~~~~~~~~

The next step is to cause the panda to actually move back and forth. Update the
code to the following:

.. only:: python

   .. code-block:: python

      from math import pi, sin, cos

      from direct.showbase.ShowBase import ShowBase
      from direct.task import Task
      from direct.actor.Actor import Actor
      from direct.interval.IntervalGlobal import Sequence
      from panda3d.core import Point3

      class MyApp(ShowBase):
          def __init__(self):
              ShowBase.__init__(self)

              # Disable the camera trackball controls.
              self.disableMouse()

              # Load the environment model.
              self.scene = self.loader.loadModel("models/environment")
              # Reparent the model to render.
              self.scene.reparentTo(self.render)
              # Apply scale and position transforms on the model.
              self.scene.setScale(0.25, 0.25, 0.25)
              self.scene.setPos(-8, 42, 0)

              # Add the spinCameraTask procedure to the task manager.
              self.taskMgr.add(self.spinCameraTask, "SpinCameraTask")

              # Load and transform the panda actor.
              self.pandaActor = Actor("models/panda-model",
                                      {"walk": "models/panda-walk4"})
              self.pandaActor.setScale(0.005, 0.005, 0.005)
              self.pandaActor.reparentTo(self.render)
              # Loop its animation.
              self.pandaActor.loop("walk")

              # Create the four lerp intervals needed for the panda to
              # walk back and forth.
              pandaPosInterval1 = self.pandaActor.posInterval(13,
                                                              Point3(0, -10, 0),
                                                              startPos=Point3(0, 10, 0))
              pandaPosInterval2 = self.pandaActor.posInterval(13,
                                                              Point3(0, 10, 0),
                                                              startPos=Point3(0, -10, 0))
              pandaHprInterval1 = self.pandaActor.hprInterval(3,
                                                              Point3(180, 0, 0),
                                                              startHpr=Point3(0, 0, 0))
              pandaHprInterval2 = self.pandaActor.hprInterval(3,
                                                              Point3(0, 0, 0),
                                                              startHpr=Point3(180, 0, 0))

              # Create and play the sequence that coordinates the intervals.
              self.pandaPace = Sequence(pandaPosInterval1,
                                        pandaHprInterval1,
                                        pandaPosInterval2,
                                        pandaHprInterval2,
                                        name="pandaPace")
              self.pandaPace.loop()

          # Define a procedure to move the camera.
          def spinCameraTask(self, task):
              angleDegrees = task.time * 6.0
              angleRadians = angleDegrees * (pi / 180.0)
              self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
              self.camera.setHpr(angleDegrees, 0, 0)
              return Task.cont

      app = MyApp()
      app.run()

.. only:: cpp

   .. code-block:: cpp

      #include "pandaFramework.h"
      #include "pandaSystem.h"

      #include "genericAsyncTask.h"
      #include "asyncTaskManager.h"

      #include "cIntervalManager.h"
      #include "cLerpNodePathInterval.h"
      #include "cMetaInterval.h"

      // Global stuff
      PT(AsyncTaskManager) taskMgr = AsyncTaskManager::get_global_ptr();
      PT(ClockObject) globalClock = ClockObject::get_global_clock();
      NodePath camera;

      // Task to move the camera
      AsyncTask::DoneStatus SpinCameraTask(GenericAsyncTask* task, void* data) {
        double time = globalClock->get_real_time();
        double angledegrees = time * 6.0;
        double angleradians = angledegrees * (3.14 / 180.0);
        camera.set_pos(20*sin(angleradians),-20.0*cos(angleradians),3);
        camera.set_hpr(angledegrees, 0, 0);

        return AsyncTask::DS_cont;
      }

      int main(int argc, char *argv[]) {
        // Open a new window framework and set the title
        PandaFramework framework;
        framework.open_framework(argc, argv);
        framework.set_window_title("My Panda3D Window");

        // Open the window
        WindowFramework *window = framework.open_window();
        camera = window->get_camera_group(); // Get the camera and store it

        // Load the environment model
        NodePath scene = window->load_model(framework.get_models(),
          "models/environment");
        scene.reparent_to(window->get_render());
        scene.set_scale(0.25 , 0.25, 0.25);
        scene.set_pos(-8, 42, 0);

        // Load our panda
        NodePath pandaActor = window->load_model(framework.get_models(),
          "models/panda-model");
        pandaActor.set_scale(0.005);
        pandaActor.reparent_to(window->get_render());

        // Load the walk animation
        window->load_model(pandaActor, "models/panda-walk4");
        window->loop_animations(0);

        // Create the lerp intervals needed to walk back and forth
        PT(CLerpNodePathInterval) pandaPosInterval1, pandaPosInterval2,
          pandaHprInterval1, pandaHprInterval2;
        pandaPosInterval1 = new CLerpNodePathInterval("pandaPosInterval1",
          13.0, CLerpInterval::BT_no_blend,
          true, false, pandaActor, NodePath());
        pandaPosInterval1->set_start_pos(LPoint3f(0, 10, 0));
        pandaPosInterval1->set_end_pos(LPoint3f(0, -10, 0));

        pandaPosInterval2 = new CLerpNodePathInterval("pandaPosInterval2",
          13.0, CLerpInterval::BT_no_blend,
          true, false, pandaActor, NodePath());
        pandaPosInterval2->set_start_pos(LPoint3f(0, -10, 0));
        pandaPosInterval2->set_end_pos(LPoint3f(0, 10, 0));

        pandaHprInterval1 = new CLerpNodePathInterval("pandaHprInterval1", 3.0,
          CLerpInterval::BT_no_blend,
          true, false, pandaActor, NodePath());
        pandaHprInterval1->set_start_hpr(LPoint3f(0, 0, 0));
        pandaHprInterval1->set_end_hpr(LPoint3f(180, 0, 0));

        pandaHprInterval2 = new CLerpNodePathInterval("pandaHprInterval2", 3.0,
          CLerpInterval::BT_no_blend,
          true, false, pandaActor, NodePath());
        pandaHprInterval2->set_start_hpr(LPoint3f(180, 0, 0));
        pandaHprInterval2->set_end_hpr(LPoint3f(0, 0, 0));

        // Create and play the sequence that coordinates the intervals
        PT(CMetaInterval) pandaPace;
        pandaPace = new CMetaInterval("pandaPace");
        pandaPace->add_c_interval(pandaPosInterval1, 0,
          CMetaInterval::RS_previous_end);
        pandaPace->add_c_interval(pandaHprInterval1, 0,
          CMetaInterval::RS_previous_end);
        pandaPace->add_c_interval(pandaPosInterval2, 0,
          CMetaInterval::RS_previous_end);
        pandaPace->add_c_interval(pandaHprInterval2, 0,
          CMetaInterval::RS_previous_end);
        pandaPace->loop();

        // Add our task.
        taskMgr->add(new GenericAsyncTask("Spins the camera",
          &SpinCameraTask, nullptr));

        // This is a simpler way to do stuff every frame,
        // if you're too lazy to create a task.
        Thread *current_thread = Thread::get_current_thread();
        while(framework.do_frame(current_thread)) {
          // Step the interval manager
          CIntervalManager::get_global_ptr()->step();
        }

        framework.close_framework();
        return (0);
      }

When the ``pandaPosInterval1`` interval is started, it will gradually adjust the
position of the panda from (0, 10, 0) to (0, -10, 0) over a period of 13
seconds. Similarly, when the ``pandaHprInterval1`` interval is started, the
heading of the panda will rotate 180 degrees over a period of 3 seconds.

The ``pandaPace`` sequence above causes the panda to move in a straight line,
turn, move in the opposite straight line, and finally turn again. The code
``pandaPace.loop()`` causes the Sequence to be started in looping mode.

Run the Program
~~~~~~~~~~~~~~~

The result of all this is to cause the panda to pace back and forth from one
tree to the other.
