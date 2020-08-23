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
      pos2 = LPoint3(-50, -60, 3);

.. only:: cpp

   .. code-block:: cpp

      #include "lpoint3.h"
      LPoint3 pos1 = new Lpoint3(0,0,0);
      LPoint3 pos2 = new Lpoint3(-50,-60,3);


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


.. only:: python

   A sample program with all the functions explained in this section can be found below.

   .. code-block:: python

      from direct.showbase.ShowBase import ShowBase
      from panda3d import navigation
      from panda3d import navmeshgen
      from panda3d.core import PointLight,DirectionalLight
      from panda3d.core import LPoint3
      from panda3d.core import LineSegs
      from panda3d.core import NodePath

      class MyApp(ShowBase):

         def __init__(self):
         ShowBase.__init__(self)

         # Setting up light for better view.
         plight = PointLight('plight')
         plight.setColor((0.9, 0.9, 0.9, 0.5))
         plnp = render.attachNewNode(plight)
         plnp.setPos(10, 20, 0)
         render.setLight(plnp)
         dlight = DirectionalLight('dlight')
         dlight.setColor((0.8, 0.5, 0.5, 1))
         dlnp = render.attachNewNode(dlight)
         dlnp.setHpr(0, -60, 0)
         render.setLight(dlnp)

         # Loading the model
         self.scene = self.loader.loadModel("untitled.obj")
         self.scene.reparentTo(self.render)
         self.scene.setP(90)

         self.scene.setScale(0.25, 0.25, 0.25)
         self.scene.flatten_light()
         self.scene.setPos(-8, 42, 0)

         #NavMeshBuilder is a class that is responsible for building the polygon meshes and navigation meshes.
         self.builder = navmeshgen.NavMeshBuilder()
         # Take Nodepath as input. Nodepath should contain the required geometry.
         self.builder.fromNodePath(self.scene)

         self.builder.setActorRadius(1)
         self.builder.set_actor_height(10)
         #self.builder.set_partition_type(2)
         self.navmesh = self.builder.build()

         # Code to attach the polymesh generated to the scene graph
         self.node1 = self.navmesh.drawNavMeshGeom()
         self.node = self.scene.attachNewNode(self.node1)
         self.node.setColor(0,0,1)
         self.node.setPos(0,0,0.5)

         self.navmeshnode = navigation.NavMeshNode("firstnavmeshnode",self.navmesh)
         self.navmeshnodepath = self.scene.attachNewNode(self.navmeshnode)

         self.query = navigation.NavMeshQuery(self.navmesh)
         pos1 = LPoint3(0, 0, 0);
         pos2 = LPoint3(-50, -60, 3);
         self.path = self.query.find_straight_path(pos1, pos2)

         self.pathLine = LineSegs()
         self.pathLine.set_color(0, 1, 0)
         self.pathLine.set_thickness(5)
         for i in range(len(self.path)):
            self.pathLine.draw_to(self.path[i])
         self.lineNode = self.pathLine.create()
         self.lineNodePath = self.scene.attach_new_node(self.lineNode)
         self.lineNodePath.setPos(0,0,1)

      app = MyApp()
      app.run()
