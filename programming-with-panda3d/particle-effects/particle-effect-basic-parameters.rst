.. _particle-effect-basic-parameters:

Particle Effect Basic Parameters
================================

Every particle effect needs at least eleven parameters. These govern the
overall properties, such as the number of particles on the screen, the birth
and death rates, and the renderer, emitter, and factory that are used.

=============================== ========================================= =============
Variable                        Definition                                Values
=============================== ========================================= =============
poolSize                        Maximum number of simultaneous particles  [0, infinity)
birthRate                       Seconds between particle births           (0, infinity)
litterSize                      Number of particles created at each birth [1, infinity)
litterSpread                    Variation of litter size                  [0, infinity)
localVelocityFlag               Whether or not velocities are absolute    Boolean
systemGrowsOlder                Whether or not the system has a lifespan  Boolean
systemLifespan                  Age of the system in seconds              [0, infinity)
BaseParticleRenderer\* renderer Pointer to particle renderer              Renderer type
BaseParticleRenderer\* emitter  Pointer to particle emitter               Emitter type
BaseParticleRenderer\* factory  Pointer to particle factory               Factory type
=============================== ========================================= =============

The renderer, emitter, and factory types will be discussed in the next three
sections.
