#include "pandaFramework.h"
#include "pandaSystem.h"

int main(int argc, char *argv[]) {
  // Open a new window framework and set the title
  PandaFramework framework;
  framework.open_framework(argc, argv);
  framework.set_window_title("My Panda3D Window");

  // Open the window
  WindowFramework *window = framework.open_window();
  NodePath camera = window->get_camera_group(); // Get the camera and store it

  // Load the environment model
  NodePath scene = window->load_model(framework.get_models(), "models/environment");
  scene.reparent_to(window->get_render());
  scene.set_scale(0.25, 0.25, 0.25);
  scene.set_pos(-8, 42, 0);

  // Load our panda
  NodePath panda = window->load_model(framework.get_models(), "models/panda-model");
  panda.set_scale(0.005);
  panda.reparent_to(window->get_render());

  // Load the walk animation
  window->load_model(panda, "models/panda-walk4");
  window->loop_animations(0); // bind models and animations
                              //set animations to loop

  // Add our task, which can be any function or lambda that returns DoneStatus.
  framework.get_task_mgr().add("SpinCameraTask", [=](AsyncTask *task) mutable {
    // Calculate the new position and orientation (inefficient - change me!)
    double angledegrees = task->get_elapsed_time() * 6.0;
    double angleradians = angledegrees * (3.14 / 180.0);
    camera.set_pos(20 * sin(angleradians), -20.0 * cos(angleradians), 3);
    camera.set_hpr(angledegrees, 0, 0);

    // Tell the task manager to continue this task the next frame.
    return AsyncTask::DS_cont;
  });

  // Run Panda's main loop until the user closes the window.
  framework.main_loop();
  return 0;
}
