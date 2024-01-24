.. _mesh-generation:

Mesh Generation
===============

Navigation Mesh

To create a navigation mesh, you need a 3D software such as 3DS Max, Maya or
Blender. Please follow the tutorial videos below to understand the process:

Step 1:

https://www.youtube.com/watch?v=ACLuXWkpJhU

Step 2:

https://www.youtube.com/watch?v=Rug0eYBa88M

Note: There are separate versions of the mesh generation tool for "Maya/Max"
users and "Blender" users. Make sure you download the correct version.

--------------

Maya Users (IMPORTANT)

Since the egg file produced by Maya uses a different format from 3DSMax, you
will need to first convert them into the same format (triangles) by using the
following command:

.. parsed-literal::

   C:\\Panda3D-\ |release|\ -x64\\bin\\egg-trans -C -o out.egg in.egg

The egg file that is thereby generated should be passed to the Mesh Generation
Tool.

--------------

Blender Users (IMPORTANT)

-  Creation of the full and collision meshes is to be done on the x-y plane.
   This makes it much easier to just get in to Blender and create a mesh since
   the starting view is a top view of the x-y plane.

-  NOTE : We advice to make meshes with a scale of 50 or above for best
   results. It would be wise to make your world based on this scale. Much
   smaller meshes bug out a bit.

-  NOTE : To make faces on your plane mesh, use the subdivide utility in
   Blender in Edit Mode and to delete faces option when you enter Face
   Selection Mode while you are in Edit Mode.

--------------

PLEASE NOTE : Download the mesh generators from here :

1. Maya and Max :

https://sites.google.com/site/etcpandai/download/meshgen_v1.0_exec.zip?attredirects=0&d=1

2. Blender : (source also available in the Open Source section)

https://sites.google.com/site/etcpandai/download/BlenderMeshGen.zip?attredirects=0&d=1
