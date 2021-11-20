.. _loading-actors-and-animations:

Loading Actors and Animations
=============================

.. only:: python

   The Python class :py:class:`~direct.actor.Actor.Actor` is designed to hold an
   animatable model and a set of animations. Since the Actor class inherits from
   the :class:`.NodePath` class, all :ref:`common-state-changes` are applicable
   to actors.

   Note, however, that Actor is a Python class that extends the C++ NodePath
   class. For the most part, you don't have to think about this: Actor inherits
   sensibly from NodePath and generally does what you expect. There are a few
   subtle oddities, though. When you attach an Actor into a scene graph, the
   low-level C++ Panda constructs only record the NodePath part of the Actor in
   the scene graph, which is fine as long as you also keep a pointer to the Actor
   instance in your Python objects. If you let the Actor destruct, however, its
   visible geometry will remain, but it will cease animating (because it is no
   longer an Actor). Also, even if you keep the Actor object around, if you
   retrieve a new pointer to the Actor from the scene graph (for instance, as
   returned by the collision system), you will get back just an ordinary
   NodePath, not an Actor.

   The Actor interface provides a high-level interface on the low-level Panda
   constructs. In Panda, the low-level node that performs the animation is
   called :class:`.Character`. You can see the Character node in the scene graph
   when you call :py:meth:`actor.ls() <direct.actor.Actor.Actor.ls>`.

   Do not confuse the Actor class with the
   :ref:`ActorNode <enabling-physics-on-a-node>` class, which is used for
   physics. They are completely unrelated classes with similar names.

   Using Actors
   ------------

   The Actor class must be imported before any loading or manipulation of actors.

   .. code-block:: python

      from direct.actor.Actor import Actor

   Once this is done, the actor object can be constructed, and the model and
   animations can be loaded.

   Loading each animation requires a dictionary, where each key is a meaningful
   name given to the animation and the corresponding value is the path to the
   animation file.

   All of the above can be written as a single statement:

   .. code-block:: python

      actor = Actor('hero.egg', {
          'walk': 'hero-walk.egg',
          'swim': 'hero-swim.egg',
      })

   Note that it is also possible to store the animations and model in the same
   file. This is preferred in some other model formats, such as glTF. In that
   case, just create the Actor with just the model as parameter, without
   specifying a separate dictionary for the animations.

   When you wish to remove the actor from the scene, you need to call the
   :py:meth:`~direct.actor.Actor.Actor.cleanup()` method.  Note that calling
   :py:meth:`~direct.actor.Actor.Actor.removeNode()` is not sufficient.
   This is due to the fact that Actor is a Python class containing additional
   data that can not be destroyed by the C++ :meth:`~.NodePath.remove_node()`
   method.

   .. note::

      The paths used in the Actor constructor must follow Panda's filename
      conventions, so a forward slash is used even on Windows. See
      :ref:`filename-syntax` for more information. Loading actors and animations
      utilizes the panda model path, the same as for static models.

.. only:: cpp

   The ``Actor`` class which is available to Python users is not available to
   C++ users. If you need such a class you have to create your own class which
   at least should do the following:

   -  load the Actor Model
   -  load the animations
   -  bind the model and the animations using AnimControl or
      AnimControlCollection

   Required Includes
   '''''''''''''''''

   .. code-block:: cpp

      #include <auto_bind.h>
      #include <animControlCollection.h>

   Load the Actor Model
   ''''''''''''''''''''

   .. code-block:: cpp

      NodePath actor = window->load_model(window->get_render(), "panda-model");

   Load the Animation
   ''''''''''''''''''

   .. code-block:: cpp

      window->load_model(actor, "panda-walk");

   Bind the Model and the Animation
   ''''''''''''''''''''''''''''''''

   .. code-block:: cpp

      // don't use PT or CPT with AnimControlCollection
      AnimControlCollection anim_collection;

      //bind the animations to the model
      auto_bind(actor.node(), anim_collection);

   Control the Animations
   ''''''''''''''''''''''

   .. code-block:: cpp

      // the name of an animation is preceded in the .egg file with <Bundle>:
      // loop a specific animation
      anim_collection.loop("panda_soft", true);

      // loop all animations
      anim_collection.loop_all(true);

      // play an animation once:
      anim_collection.play("panda_soft");

      // pose
      anim_collection.pose("panda_soft", 5);

   to display names of loaded animations you could
   use:

   .. code-block:: cpp

      for (int n = 0; n < anim_controls.get_num_anims(); ++n) {
        std::cerr << anim_controls.get_anim_name(n) << std::endl;
      }

   If you add more animations to some node after calling:
   ``auto_bind(...)`` they will not be
   controllable until ``auto_bind(...)`` is
   called again with proper arguments.

   Note that it is possible to store the animations and the model in the same
   file.
