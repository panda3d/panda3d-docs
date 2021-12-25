#include "pandaFramework.h"
#include "pandaSystem.h"

int main(int argc, char *argv[]) {
  // Load the window and set its title.
  PandaFramework framework;
  framework.open_framework(argc, argv);
  framework.set_window_title("My Panda3D Window");
  WindowFramework *window = framework.open_window();
  // Get the camera and store it in a variable.
  NodePath camera = window->get_camera_group();

  // Load the environment model.
  NodePath scene = window->load_model(framework.get_models(), "models/environment");
  // Reparent the model to render.
  scene.reparent_to(window->get_render());
  // Apply scale and position transforms to the model.
  scene.set_scale(0.25, 0.25, 0.25);
  scene.set_pos(-8, 42, 0);

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
