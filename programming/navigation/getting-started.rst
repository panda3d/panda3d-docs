.. _getting-started:

Getting Started
===============

Navigation and Navmeshgen are two libraries which can be used together to perform fast pathfinding operations on Panda3d geoms.

To use the navmeshgen library into your game you need to import it into your game
code.
The generated mesh is stored as an object of class NavMesh, which can be accessed by importing navigation.

The navmeshgen library has the class NavMeshBuilder, the main operation of which is to build the navigation mesh.
The navigation library has the class NavMesh, which stores the mesh build by NavMeshBuilder or some other library.
It has also has class NavMeshQuery, which is responsible for handling the query operations like pathfinding over the mesh.
