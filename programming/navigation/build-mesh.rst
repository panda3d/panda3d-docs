.. _build-mesh:

Building Navigation Mesh
========================

Implementation:

Following are the steps to build a basic navigation mesh. 

Step 1:

.. only:: python

   To use the navmeshgen library into your game you need to import it into your game code.
   The generated mesh is stored as an object of class NavMesh, which can be accessed by importing navigation.

   .. code-block:: python

      from panda3d import navmeshgen
      from panda3d import navigation

.. only:: cpp

   The headers required to be included for building mesh are navMeshBuilder and navMesh.

   .. code-block:: cpp

      #include "pandaFramework.h"
      #include "pandaSystem.h"
      #include "navMesh.h"
      #include "navMeshBuilder.h"

Step 2:

Create a geom primitive or load an external model. Here we load the model called 'village.obj'

.. only:: python

   .. code-block:: python

      scene = loader.load_model("samples/navigation/models/village.obj")

.. only:: cpp

   .. code-block:: cpp

      PandaFramework framework;
      framework.open_framework(argc, argv);
      framework.set_window_title("My Panda3D Window");
      WindowFramework *window = framework.open_window();
      NodePath scene = window->load_model(framework.get_models(), "samples/navigation/models/village.obj");

Now the model is loaded in the NodePath 'scene'

Step 3:

Create an object for the class NavMeshBuilder via:

.. only:: python

   .. code-block:: python

     builder = navmeshgen.NavMeshBuilder()

.. only:: cpp

   .. code-block:: cpp

     NavMeshBuilder builder = new NavMeshBuilder()

Step 4:

Now, we shall build the navigation mesh for our model stored in NodePath 'scene'.

.. only:: python

   .. code-block:: python

      builder.from_node_path(scene)

.. only:: cpp

   .. code-block:: cpp

      builder.from_node_path(scene)

Step 5:

Finally, we build the navigation mesh using the build function. 
The output mesh is stored as an object of class NavMesh.

.. only:: python

   .. code-block:: python

      navmesh = builder.build()

.. only:: cpp

   .. code-block:: cpp

      PT(NavMesh) navmesh = builder.build()

Here, 'navmesh' is the object of class NavMesh and has the generated mesh.

This is how easy it is to get a basic navigation mesh generated!

Next Step:

Now that you have a basic working program, you should proceed to the
parameters page and see how navigation mesh varies with parameters.
