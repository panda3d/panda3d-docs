.. _set-actor-parameters:

Setting Actors Parameters
=========================

The navigation mesh is built based on the parameters set for the actor, or say,
the capabilities of the actors. The navigation mesh varies to accomodate 
the size of actor, the climbing capabilities.

Implementation:

First we need to create an object for the class NavMeshBuilder via:

.. code-block:: python

   builder = navmeshgen.NavMeshBuilder()

Now, you can set parameters for a navigation mesh in the following way.
Remember to set parameters before building the mesh by calling the build() function. 

Actor Height:

The default value of actor height is 2 units. You can set the height of actor to 3.5 units as:

.. code-block:: python

   builder.set_actor_height(3.5)

Actor Radius:

The default value of actor radius is 0.6 units. You can set the radius of actor to 1.0 unit as:

.. code-block:: python

   builder.set_actor_radius(1)

Actor Climb:

The default value of actor's climbing capability is 0.9 units. You can set the radius of actor to 1.5 unit as:

.. code-block:: python

   builder.set_actor_climb(1.5)

You can also get the parameters value as:

.. code-block:: python

   height = builder.get_actor_height()
   radius = builder.get_actor_radius()
   climb = builder.get_actor_climb()

Apart from setting actor's parameters, we can also decide on the partition type for navigation mesh.
The default partition type is 'watershed' but can be set to 'monotone' or 'layer' as:

.. code-block:: python

   builder.set_partition_type('monotone')

Reset Parameters:

The parameters can be reset to default as:

.. code-block:: python

   builder.reset_common_settings()
