.. _particle-factories:

Particle Factories
==================

There are two types of particle factories, Point and ZSpin. The particle panel
shows a third, Oriented, but this factory does not currently work. The
differences between these factories lie in the orientation and rotational
abilities. First, there are some common variables to the factories.

====================== ================================== =============
**Variable**           **Definition**                     **Values**
lifespanBase           Average lifespan in seconds        [0, infinity)
lifespanSpread         Variation in lifespan              [0, infinity)
massBase               Average particle mass              [0, infinity)
massSpread             Variation in particle mass         [0, infinity)
terminalVelocityBase   Average particle terminal velocity [0, infinity)
terminalVelocitySpread Variation in terminal velocity     [0, infinity)
====================== ================================== =============


Point particle factories generate simple particles. They have no additional
parameters. ZSpin particle factories generate particles that spin around the Z
axis, the vertical axis in Panda3D. They have some additional parameters.

================== ========================= ==========
**Variable**       **Definition**            **Values**
initialAngle       Starting angle in degrees [0, 360]
initialAngleSpread Spread of initial angle   [0, 360]
finalAngle         Final angle in degrees    [0, 360]
fnalAngleSpread    Spread of final angle     [0, 360]
================== ========================= ==========
