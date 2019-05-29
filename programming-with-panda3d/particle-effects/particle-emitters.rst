.. _particle-emitters:

Particle Emitters
=================

There are a large number of particle emitters, each categorized by the volume
of space they represent. Additionally, all emitters have three modes:
explicit, radiate, and custom. Explicit mode emits the particles in parallel
in the same direction. Radiate mode emits particles away from a specific
point. Custom mode emits particles with a velocity determined by the
particular emitter. All emitters have a number of common parameters.

==================== ================================================ ==================================
**Variable**         **Definition**                                   **Values**
emissionType         Emission mode                                    ET_EXPLICIT, ET_RADIATE, ET_CUSTOM
explicitLaunchVector Initial velocity in explicit mode                (x, y, z)
radiateOrigin        Point particles launch away from in radiate mode (x, y, z)
amplitude            Launch velocity multiplier                       (-infinity, infinity)
amplitudeSpeed       Spread for launch velocity multiplier            [0, infinity)
==================== ================================================ ==================================


The following list contains the different types of emitters, their unique
parameters, and the effect of the custom mode.

BoxEmitter
~~~~~~~~~~


============ ============================ ==========
**Variable** **Definition**               **Values**
minBound     Minimum point for box volume (x, y, z)
maxBound     Maximum point for box volume (x, y, z)
============ ============================ ==========


Custom mode generates particles with no initial velocity.

DiscEmitter
~~~~~~~~~~~


============== ===================================================== =====================
**Variable**   **Definition**                                        **Values**
radius         Radius of disc                                        [0, infinity)
outerAngle     Particle launch angle at edge of disc                 [0, 360]
innterAngle    Particle launch angle at center of disc               [0, 360]
outerMagnitude Launch velocity multiplier at edge of disc            (-infinity, infinity)
innerMagnitude Launch velocity multiplier at center of disc          (-infinity, infinity)
cubicLerping   Whether or not magnitude/angle interpolation is cubic Boolean
============== ===================================================== =====================


Custom mode uses the last five parameters. Particles emitted from areas on the
inside use interpolated magnitudes and angles, either liner or cubic.

PointEmitter
~~~~~~~~~~~~


============ ======================= ==========
**Variable** **Definition**          **Values**
location     Location of outer point (x, y, z)
============ ======================= ==========


Custom mode generates particles with no initial velocity.

RectangleEmitter
~~~~~~~~~~~~~~~~


============ =============================== ==========
**Variable** **Definition**                  **Values**
minBound     2D point defining the rectangle (x, z)
maxBound     2D point defining the rectangle (x, z)
============ =============================== ==========


Custom mode generates particles with no initial velocity.

RingEmitter
~~~~~~~~~~~


============ ===================== =============
**Variable** **Definition**        **Values**
radius       Radius of disc        [0, infinity)
angle        Particle launch angle [0, 360]
============ ===================== =============


Custom mode uses the second parameter to emit particles at an angle with
respect to the vector from the ring center to the spawn point. 0 degrees emits
particles away from the center, and 180 degrees emits particles into the
center.

SphereSurfaceEmitter
~~~~~~~~~~~~~~~~~~~~


============ ================ =============
**Variable** **Definition**   **Values**
radius       Radius of sphere [0, infinity)
============ ================ =============


Custom mode generates particles with no initial velocity.

SphereVolumeEmitter
~~~~~~~~~~~~~~~~~~~


============ ================ =============
**Variable** **Definition**   **Values**
radius       Radius of sphere [0, infinity)
============ ================ =============


Custom mode emits particles away from the sphere center. Their velocity is
dependent on their spawn location within the sphere. It is 0 at the center, of
magnitude 1 at the outer edge of the sphere, and linearly interpolated in
between.

TangentRingEmitter
~~~~~~~~~~~~~~~~~~


============ ============== =============
**Variable** **Definition** **Values**
radius       Radius of ring [0, infinity)
============ ============== =============


Custom mode emits particles tangentially to the ring edge, with a velocity
magnitude of 1.
