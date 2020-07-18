.. _navigation:

Pathfinding using Navigation
============================

Panda3D is integrated with the Recast-Detour library as navmeshgen and navigation libraries.

Navmeshgen is an AI library for Panda3D which, for a given geom, generates a navigation mesh, a mesh containing only the walkable surfaces.

Navigation is an AI library for Panda3D which operates on an input navigation mesh. The input navigation can be generated using navmeshgen library or by the user's preferred external library. The navigation library lets us query over the navigation mesh and find the path between any two points over the mesh.


.. toctree::
   :maxdepth: 2

   getting-started
   navmeshgen/index
   navigation/index
