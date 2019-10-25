#include "pandaFramework.h"
#include "pandaSystem.h"

int main(int argc, char *argv[]) {
  // Load the window and set its title.
  PandaFramework framework;
  framework.open_framework(argc, argv);
  framework.set_window_title("My Panda3D Window");
  WindowFramework *window = framework.open_window();

  // Load the environment model.
  NodePath scene = window->load_model(framework.get_models(), "models/environment");
  // Reparent the model to render.
  scene.reparent_to(window->get_render());
  // Apply scale and position transforms to the model.
  scene.set_scale(0.25f, 0.25f, 0.25f);
  scene.set_pos(-8, 42, 0);

  // Run the engine.
  framework.main_loop();
  // Shut down the engine when done.
  framework.close_framework();
  return 0;
}
