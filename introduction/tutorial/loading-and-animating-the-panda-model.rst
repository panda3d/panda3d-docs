.. _loading-and-animating-the-panda-model:

Loading and Animating the Panda Model
=====================================

.. only:: python

   :ref:`Actors <loading-actors-and-animations>`
   ---------------------------------------------

   The ``Actor`` class is for animated models. Note that we use ``loadModel()``
   for static models and ``Actor`` only when they are animated. The two
   constructor arguments for the ``Actor`` class are the name of the file
   containing the model and a Python dictionary containing the names of the
   files containing the animations.

Update the Code
---------------

.. only:: python

   Now that the scenery is in place, we will load an ``Actor``. Update your code
   to look like this:

   .. code-block:: python

      from math import pi, sin, cos

      from direct.showbase.ShowBase import ShowBase
      from direct.task import Task
      from direct.actor.Actor import Actor

      class MyApp(ShowBase):
          def __init__(self):
              ShowBase.__init__(self)

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

          # Define a procedure to move the camera.
          def spinCameraTask(self, task):
              angleDegrees = task.time * 6.0
              angleRadians = angleDegrees * (pi / 180.0)
              self.camera.setPos(20 * sin(angleRadians), -20.0 * cos(angleRadians), 3)
              self.camera.setHpr(angleDegrees, 0, 0)
              return Task.cont

      app = MyApp()
      app.run()

   The command ``loop("walk")`` causes the walk animation to begin looping.

.. only:: cpp

   The ``Actor`` class which is available to python users is not available to
   C++ users. you should create your own Actor class which at least should do
   the following:

   -  load the Actor Model
   -  load the animations
   -  bind the model and the animations using AnimControl or
      AnimControlCollection

   The next sample will load the panda model and the walk animation. the call:
   ``window->loop_animations(0);`` does the magic of binding all the loaded
   models and their animations under the node path: render . it's very important
   to note that any animations loaded after the above call will not show until
   the same method is called again. also any animations loaded under a node path
   which doesn't belong to render (for example: render_2d) will not show even if
   the call: ``window->loop_animations(0);`` is made. For such animations to
   show, other steps must be applied (more on this later).

   .. code-block:: cpp

       #include "pandaFramework.h"
       #include "pandaSystem.h"

       #include "genericAsyncTask.h"
       #include "asyncTaskManager.h"

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
           NodePath scene = window->load_model(framework.get_models(), "models/environment");
           scene.reparent_to(window->get_render());
           scene.set_scale(0.25 , 0.25, 0.25);
           scene.set_pos(-8, 42, 0);

           // Load our panda
           NodePath pandaActor = window->load_model(framework.get_models(), "models/panda-model");
           pandaActor.set_scale(0.005);
           pandaActor.reparent_to(window->get_render());

           // Load the walk animation
           window->load_model(pandaActor, "models/panda-walk4");
           window->loop_animations(0); // bind models and animations
                                       //set animations to loop

           // Add our task do the main loop, then rest in peace.
           taskMgr->add(new GenericAsyncTask("Spins the camera", &SpinCameraTask, nullptr));
           framework.main_loop();
           framework.close_framework();
           return (0);
       }

   We are first loading the model file and the animation file like ordinary
   models. Then, we are simply calling loop_animations(0) to loop all
   animations.

Run the Program
---------------

The result is a panda walking in place as if on a treadmill:

|Tutorial3.jpg|

.. |Tutorial3.jpg| image:: tutorial3.jpg
