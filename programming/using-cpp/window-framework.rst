:orphan:

.. _the-window-framework:

The Window Framework
====================

.. only:: python

   The WindowFramework class is for use in C++ only. If you use Python, you can
   just use ShowBase to open a window and skip this page.

.. only:: cpp

   This page will explain how to use the WindowFramework class in C++ to open a
   blank window. First of all, we need to include the appropriate header files:

   .. code-block:: cpp

      #include "pandaFramework.h"
      #include "pandaSystem.h"

   Second, we need to create an instance of the PandaFramework class, and use it
   to open a window.

   .. code-block:: cpp

      PandaFramework framework;
      framework.open_framework(argc, argv);
      framework.set_window_title("Hello World!");

      WindowFramework *window = framework.open_window();

   Optionally, we can enable keyboard support, in case we want to check for
   keyboard presses, and we can enable the default camera trackball. Note that
   you also need to enable keyboard support to receive mouse button events,
   since it sets up the button event handlers.

   .. code-block:: cpp

      // Enable keyboard detection
      window->enable_keyboard();
      // Enable default camera movement
      window->setup_trackball();

   Now, we're going to check if the window has opened successfully. If so, the
   main loop must be called, using the function framework.main_loop(). This is
   equivalent to the ``base.run()`` function in Python.

   .. code-block:: cpp

      if (window != nullptr) {
        nout << "Opened the window successfully!\n";

        // Put here your own code, such as the loading of your models

        framework.main_loop();
      } else {
        nout << "Could not load the window!\n";
      }

   Afterwards, we need to close the framework:

   .. code-block:: cpp

      framework.close_framework();
      return (0);


   Now, :ref:`compile and run <running-your-program>` your file and you have
   your own window opened!

   This is the completed application:

   .. code-block:: cpp

      // Include all the stuff
      #include "pandaFramework.h"
      #include "pandaSystem.h"

      int main(int argc, char *argv[]) {
        // Open the framework
        PandaFramework framework;
        framework.open_framework(argc, argv);
        // Set a nice title
        framework.set_window_title("Hello World!");
        // Open it!
        WindowFramework *window = framework.open_window();

        // Check whether the window is loaded correctly
        if (window != nullptr) {
          nout << "Opened the window successfully!\n";

          window->enable_keyboard(); // Enable keyboard detection
          window->setup_trackball(); // Enable default camera movement

          // Put here your own code, such as the loading of your models

          // Do the main loop
          framework.main_loop();
        } else {
          nout << "Could not load the window!\n";
        }
        // Close the framework
        framework.close_framework();
        return (0);
      }

   The WindowFramework class also provides all the basic things that the Python
   equivalent ShowBase would normally take care of:

   .. code-block:: cpp

      const NodePath &get_render();
      const NodePath &get_render_2d();
      const NodePath &get_aspect_2d();

      void set_wireframe(bool enable);
      void set_texture(bool enable);
      void set_two_sided(bool enable);
      void set_one_sided_reverse(bool enable);
      void set_lighting(bool enable);

      const NodePath &get_camera_group();

      int get_num_cameras() const;
      Camera *get_camera(int n) const;

      // WindowFramework also provides access to the GraphicsWindow.
      // for example, to set the background color to black, you can do this:
      window->get_graphics_window()->set_clear_color(LColor(0, 0, 0, 1));

   It's very useful to study the file ``panda/src/framework/windowFramework.h``,
   since you will need to use it often.
