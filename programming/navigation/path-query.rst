.. _path-query:

Pathfinding on NavMesh
======================

The most important feature of navigation library is pathfinding.
The library uses A* pathfinding algorithm over polygons of navigation 
mesh, though you do not need to worry about those stuffs.

Update the Code
~~~~~~~~~~~~~~~

.. only:: cpp

   Include the header required for making queries on navmesh:

   .. code-block:: cpp

      #include "navMeshQuery.h"

Make a object of NavMeshQuery Class which will then do query operations 
for pathfinding.

.. only:: python

   .. code-block:: python

      query = navigation.NavMeshQuery(navmesh)

.. only:: cpp

   .. code-block:: cpp

      NavMeshQuery query = new NavMeshQuery(navmesh);

Now, you should define the two points between which path has to be found.

.. only:: python

   .. code-block:: python

      from panda3d.core import LPoint3
      pos1 = LPoint3(0, 0, 0);
      pos2 = LPoint3(50, 60, 3);

.. only:: cpp

   .. code-block:: cpp

      #include "lpoint3.h"
      LPoint3 pos1 = new Lpoint3(0,0,0);
      LPoint3 pos2 = new Lpoint3(50,60,3);


To find the path between the two positions, you can simple use the following:

.. only:: python

   .. code-block:: python

      path = query.find_path(pos1, pos2)

.. only:: cpp

   .. code-block:: cpp

      PTA_LVecBase3 path = query.find_path(pos1, pos2);

Here, find_path function finds the points on the navigation mesh closest to 
the input positions. So, you need not worry about them not being exactly over 
the navigation mesh. 

If you find / print the point on the navigation mesh closest to the position, you can 
do it in the following way:

.. only:: python

   .. code-block:: python

      pos = LPoint3(0, 1, 5)
      query.nearest_point(pos)
      print(pos)

.. only:: cpp

   .. code-block:: cpp

      LPoint3 pos = new LPoint3(0, 1, 5);
      query.nearest_point(pos);

You have the path stored in the 'path' variable, which has array of points joining
the path. You can use LineSegs to visualize the path as follows:

.. only:: python

   .. code-block:: python

      from panda3d.core import LineSegs

      pathLine = LineSegs()
      pathLine.set_color(0, 1, 0)
      pathLine.set_thickness(5)
      for i in range(len(path)):
         pathLine.draw_to(path[i])

      lineNode = pathLine.create()
      lineNodePath = scene.attach_new_node(lineNode)

.. only:: cpp

   .. code-block:: cpp

      #include "lineSegs.h"

      LineSegs pathLine = new LineSegs();
      pathLine.set_color(0, 1, 0);
      pathLine.set_thickness(5);
      for(int i=0 ; i < path.size() ; i++) {
         pathLine.draw_to(path[i]);
      }

      GeomNode *lineNode = pathLine.create();
      NodePath lineNodePath = scene.attach_new_node(lineNode);

Run the Program
~~~~~~~~~~~~~~~

Go ahead and run the program. You should see this:

.. image:: path1.png

The green lines show the path between the positions.

Using straight path
~~~~~~~~~~~~~~~~~~~

You can also a different path querying function. Update the code as follows 
by replacing the definition of 'path' before visualization using LineSegs:

.. only:: python

   .. code-block:: python

      path = query.find_straight_path(pos1, pos2)

.. only:: cpp

   .. code-block:: cpp

      PTA_LVecBase3 path = query.find_straight_path(pos1, pos2);

After running the program, you should see this:

.. image:: path2.png
