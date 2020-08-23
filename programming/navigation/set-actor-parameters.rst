.. _set-actor-parameters:

Setting Actors Parameters
=========================

The navigation mesh is built based on the parameters set for the actor, or say,
the capabilities of the actors. The navigation mesh varies to accomodate 
the size of actor, the climbing capabilities.

Implementation:

First we need to create an object for the class NavMeshBuilder via:

.. only:: python

   .. code-block:: python

      builder = navmeshgen.NavMeshBuilder()

.. only:: cpp

   .. code-block:: cpp

      NavMeshBuilder builder = new NavMeshBuilder();

Now, you can set parameters for a navigation mesh in the following way.
Remember to set parameters before building the mesh by calling the build() function. 

Actor Height:

The default value of actor height is 2 units. You can set the height of actor to 3.5 units as:

.. only:: python

   .. code-block:: python

      builder.set_actor_height(3.5)

.. only:: cpp

   .. code-block:: cpp

      builder.set_actor_height(3.5);

Actor Radius:

The default value of actor radius is 0.6 units. You can set the radius of actor to 1.0 unit as:

.. only:: python

   .. code-block:: python

      builder.set_actor_radius(1)

.. only:: cpp

   .. code-block:: cpp

      builder.set_actor_radius(1);

Actor Climb:

The default value of actor's climbing capability is 0.9 units. You can set the radius of actor to 1.5 unit as:

.. only:: python

   .. code-block:: python

      builder.set_actor_climb(1.5)

.. only:: cpp

   .. code-block:: cpp

      builder.set_actor_climb(1.5);

You can also get the parameters value as:

.. only:: python

   .. code-block:: python

      height = builder.get_actor_height()
      radius = builder.get_actor_radius()
      climb = builder.get_actor_climb()

.. only:: cpp

   .. code-block:: cpp

      float height = builder.get_actor_height();
      float radius = builder.get_actor_radius();
      float climb = builder.get_actor_climb();

Apart from setting actor's parameters, we can also decide on the partition type for navigation mesh.
The default partition type is 'watershed' but can be set to 'monotone' or 'layer'.
The input arguments are of 'enum' type, so can be accessed by integers as well, 0 for watershed, 1 for monotone and 2 for layer.

.. only:: python

   .. code-block:: python

      builder.set_partition_type(1)

.. only:: cpp

   .. code-block:: cpp

      builder.set_partition_type(1);

Reset Parameters:

The parameters can be reset to default as:

.. only:: python

   .. code-block:: python

      builder.reset_common_settings()

.. only:: cpp

   .. code-block:: cpp

      builder.reset_common_settings();
