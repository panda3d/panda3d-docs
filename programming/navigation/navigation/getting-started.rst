.. _getting-started:

Getting Started
===============

The navigation library can be imported into python as:

.. code-block:: python

   from panda3d import navigation

First we need to set up navigation mesh into an object of class NavMesh.
We can do it in multiple ways. 

We may build a navmesh using build function in NavMeshBuilder class as:

.. code-block:: python

   from panda3d import navmeshgen
   scene = loader.loadModel("samples/street-navigation/models/street.obj")
   builder = navmeshgen.NavMeshBuilder()
   builder.fromNodePath(scene)
   navmesh = builder.build()

Here, 'navmesh' is an object of class NavMesh.
The other way to set up navigation mesh could be reading from BAM, which you
can learn more about in the BAM-serialization section.

You can also set it up by passing your own vertices and polygons for the navigation mesh 
using NavMeshParams class. For it work properly, you will have be sure about the parameters
you set. It is necessary to set all the parameters.

.. code-block:: python

   params = navigation.NavMeshParams()
   params.vert_count = nverts

Here we set vert_count to nverts (which we assume already has an integer value).
Similarly, we can set other parameters. The parameters along with their datatypes are listed below

================= ===========
Parameter         Data-type
vert_count        int32
poly_count        int32
nvp               int32
detail_vert_count int32
detail_tri_count  int32
walkable_height   float
walkable_radius   float
walkable_climb    float
cs                float
ch                float
b_min             float array
b_max             float array
verts             int16 array
polys             int16 array
poly_flags        int16 array
poly_areas        int8 array
detail_meshes     int32 array
detail_verts      float array
detail_tris       int8 array
================= ===========

This way of setting up navigation mesh, though can get heavy to implement, but can be useful 
when you build navigation mesh using some other library and then wish use the library 
navigation over it.
