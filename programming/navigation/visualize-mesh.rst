.. _visualize-mesh:

Visualize NavMesh
=================

Update the Code
~~~~~~~~~~~~~~~

After you have built the navigation mesh, you migh also wish to visualize it.
Let's say you used the following line of code to build the navigation mesh.

.. code-block:: python

   builder.set_actor_radius(1.0)
   navmesh = builder.build()

You do not want you actor to move along the walls, hence the radius has been 
set to a value of 1 unit using set_actor_radius(1.0) function.
Now, in order to visualize the mesh, you can do it in the following way:

.. code-block:: python

   node = navmesh.draw_nav_mesh_geom()

draw_nav_mesh_geom() returns the navigation mesh as a GeomNode object.

Before visualizing navigation mesh, you might also want to visualize the 
the object node over which navigation mesh is built.

You should first set up the lighting of the environment. Here, a combination of
directional and point light is used. 

.. code-block:: python

   from panda3d.core import PointLight,DirectionalLight

   plight = PointLight('plight')
   plight.setColor((20, 0.9, 0.9, 1))
   plnp = render.attachNewNode(plight)
   plnp.setPos(10, 20, 0)
   render.setLight(plnp)
   
   dlight = DirectionalLight('dlight')
   dlight.setColor((0.8, 0.5, 0.5, 1))
   dlnp = render.attachNewNode(dlight)
   dlnp.setHpr(0, -60, 0)
   render.setLight(dlnp)

To visualize the object:

.. code-block:: python

   scene.reparentTo(render)

Now in order to visualize GeomNode, you can attach the GeomNode to render
or some other NodePath already attached to render, like here it has been 
attached to 'scene'.

.. code-block:: python

   nodepath = scene.attachNewNode(node)
   nodepath.setColor(0,0,1)

Run the Program
~~~~~~~~~~~~~~~

Go ahead and run the program. You should see this:

.. image:: navmesh.png

You should see navigation mesh in blue color over the object surface.
