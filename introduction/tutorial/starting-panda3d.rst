.. _starting-panda3d:

Starting Panda3D
================

.. only:: python

   Creating a New Panda3D Application
   ----------------------------------

   :ref:`showbase`
   ~~~~~~~~~~~~~~~

   To start Panda3D, create a text file and save it with the .py extension.
   PYPE, SPE and IDLE are Python-specific text-editors, but any text editor will
   work. Enter the following text into your Python file:

   .. code-block:: python

      from direct.showbase.ShowBase import ShowBase


      class MyApp(ShowBase):

          def __init__(self):
              ShowBase.__init__(self)


      app = MyApp()
      app.run()

   Here we made our main class inherit from ``ShowBase``. The ShowBase class
   loads most of the other Panda3D modules, and causes the 3D window to appear.
   The ``run()`` procedure in ShowBase contains the Panda3D main loop. It
   renders a frame, handles the background tasks, and then repeats. It does not
   normally return, so it needs to be called only once and must be the last line
   in your script. In this particular example, there will be nothing to render,
   so you should expect a window containing an empty grey area.

   DirectStart
   ~~~~~~~~~~~

   ``DirectStart`` is a shortcut that instantiates ShowBase automatically on
   import. This may be useful for quick prototyping at the expense of clean code
   layout. The following example demonstrates its use:

   .. code-block:: python

      import direct.directbase.DirectStart

      base.run()

   The import line automatically constructs an instance of ShowBase, which
   starts the engine and creates an empty window. Because ShowBase uses Python's
   ``__builtin__``, its functions are allowed to be called without storing the
   instance in a variable. For the sake of cleanliness, the rest of this
   tutorial shall use the ShowBase subclass.

   DirectStart is deprecated starting with Panda3D 1.9.0. In order to upgrade
   old code, you can simply replace the DirectStart import with the following:

   .. code-block:: python

      from direct.showbase.ShowBase import ShowBase
      base = ShowBase()


   Running the Program
   -------------------

   On Windows, Python is already included with Panda3D. To run your program,
   enter the following in a terminal (command prompt):

   .. code-block:: bash

      ppython filename.py

   To run it on GNU/Linux or macOS, enter the following in a terminal:

   .. code-block:: bash

      python filename.py

   If Panda3D has been installed properly, a grey window titled *Panda* appears.
   There is nothing we can do with this window, but that will change shortly.

.. only:: cpp

   Creating a New Panda3D Application
   ----------------------------------

   To start Panda3D, create a text file and save it with a .cxx extension. Any
   text editor will work. Enter the following text into your C++ file:

   .. code-block:: cpp

      #include "pandaFramework.h"
      #include "pandaSystem.h"

      int main(int argc, char *argv[]) {
        // Open a new window framework
        PandaFramework framework;
        framework.open_framework(argc, argv);

        // Set the window title and open the window
        framework.set_window_title("My Panda3D Window");
        WindowFramework *window = framework.open_window();

        // Here is room for your own code

        // Do the main loop, equal to run() in python
        framework.main_loop();
        framework.close_framework();
        return (0);
      }

   For information about the Window Framework to open a window, click
   :ref:`here <the-window-framework>`.

   ``pandaFramework.h`` and ``pandaSystem.h`` load most of the Panda3D modules.
   The *main_loop()* subroutine contains the Panda3D main loop. It renders a
   frame, handles the background tasks, and then repeats. It does not normally
   return, so it needs to be called only once and must be the last line in your
   script. In this particular example, there will be nothing to render, so you
   should expect a window containing an empty grey area.

   Running the Program
   -------------------

   The steps required to build and run your program were already explained in
   :ref:`a previous page <running-your-program>`.

   If Panda3D has been installed properly, a gray window titled *My Panda3D
   Window* will appear when you run your program. There is nothing we can do
   with this window, but that will change shortly.
