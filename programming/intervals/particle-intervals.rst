.. _particle-intervals:

Particle Intervals
==================

Particle effects can be run from inside intervals as well, using the
:py:class:`~direct.interval.ParticleInterval.ParticleInterval` class:

.. code-block:: python

   intervalName = ParticleInterval(
       particleEffect,
       parent,
       worldRelative=True,
       duration=myDuration
   )

Read more about :ref:`particle-effects`.
