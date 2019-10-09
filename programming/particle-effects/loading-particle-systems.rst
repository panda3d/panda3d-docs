.. _loading-particle-systems:

Loading Particle Systems
========================

The Panda3D engine uses text files for storing particle configurations, which
are usually created with the Particle Panel. Before being able to use particles,
you'll need to tell Panda3D to enable particles:

.. code-block:: python

   base.enableParticles()

This function tells Panda3D to enable its built-in physics engine which is also
used by particles.

To be able to create ParticleEffect objects, you'll need this import:

.. code-block:: python

   from direct.particles.ParticleEffect import ParticleEffect

Next, create a ParticleEffect object and tell it to use a particle configuration
file.

.. code-block:: python

   p = ParticleEffect()
   p.loadConfig(filename)

To start the ParticleEffect, do this:

.. code-block:: python

   p.start(parent = render, renderParent = render)

``start()`` takes two arguments: ``parent`` is the node the particles will be
"birth-relative" to. ``renderParent`` is the node level the particles will be
rendered at. If you want your particles to spawn from your node, but not follow
it around, set ``renderParent`` to something else like ``render``.

ParticleEffect inherits from NodePath, so you can use NodePath methods like
``setPos()`` on it.

To reset the ParticleEffect, use:

.. code-block:: python

   p.reset()

To stop the ParticleEffect, use:

.. code-block:: python

   p.disable()

To completely remove the ParticleEffect, use:

.. code-block:: python

   p.cleanup()

Note that ``cleanup()`` calls ``disable()`` internally, so you don't need to
call it yourself before calling ``cleanup()``

Like ``loadConfig()``, you can use ``saveConfig()`` to save the ParticleEffect
to a particle configuration file (\*.ptf):

.. code-block:: python

   p.saveConfig(filename)
