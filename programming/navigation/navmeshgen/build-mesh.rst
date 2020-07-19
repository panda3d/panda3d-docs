.. _build-mesh:

Building Navigation Mesh
========================

Implementation:

Following are the steps to get the build a basic navigation mesh. 

Step 1:

To use the navmeshgen library into your game you need to import it into your game
code.
The generated mesh is stored as an object of class NavMesh, which can be accessed by importing navigation.

.. code-block:: python

   from panda3d import navmeshgen
   from panda3d import navigation

Step 2:

Create a geom primitive or load an external model. Here we load the model called 'street.obj'

.. code-block:: python

   scene = loader.loadModel("samples/street-navigation/models/street.obj")

Now the model is loaded in the NodePath 'scene'

Step 3:

Create an object for the class NavMeshBuilder via:

.. code-block:: python

   builder = navmeshgen.NavMeshBuilder()

Step 4:

Now, we shall build the navigation mesh for our model stored in NodePath 'scene'.

.. code-block:: python

   builder.fromNodePath(scene)

Step 5:

Finally, we build the navigation mesh using the build function. 
The output mesh is stored as an object of class NavMesh.

.. code-block:: python

   navmesh = builder.build()

Here, 'navmesh' is the object of class NavMesh and has the generated mesh.

This is how easy it is to get a basic navigation mesh generated!

Next Step:

Now that you have a basic working program, you should proceed to the
parameters page and see how navigation mesh varies with parameters.
