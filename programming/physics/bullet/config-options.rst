.. _config-options:

Bullet Config Options
=====================

The following list is a listing of all config variables defined by the Panda3D
Bullet module.

=========================================== ========== ======= =========================================================================================================================================================================================================================
Variable                                    Value Type Default Description
=========================================== ========== ======= =========================================================================================================================================================================================================================
bullet-max-objects                          int        1024    Specifies the maximum number of individual objects within a bullet physics world.
bullet-gc-lifetime                          int        256     Specifies the lifetime of data clean up be the soft body world info garbage collector.
bullet-broadphase-algorithm                 enum       aabb    Specifies the broadphase algorithm to be used by the physics engine. Default value is 'aabb' (dynamic aabb tree). A second value is 'sap' (sweep and prune).
bullet-sap-extents                          float      1000.0  Specifies the world extent in all directions. The config variable is only used if bullet-broadphase-algorithm is set to 'sap' (sweep and prune).
bullet-enable-contact-events                bool       false   Specifies if events should be send when new contacts are created or existing contacts get remove. Warning: enabling contact events might create more load on the event queue then you might want! Default value is FALSE.
bullet-solver-iterations                    int        10      Specifies the number of iterations for the Bullet contact solver. This is the native Bullet property btContactSolverInfo::m_numIterations.
bullet-additional-damping                   bool       false   Enables additional damping on each rigid body, in order to reduce jitter. Additional damping is an experimental feature of the Bullet physics engine. Use with care."
bullet-additional-damping-linear-factor     float      0.005   Only used when bullet-additional-damping is set to TRUE.
bullet-additional-damping-angular-factor    float      0.01    Only used when bullet-additional-damping is set to TRUE.
bullet-additional-damping-linear-threshold  float      0.01    Only used when bullet-additional-damping is set to TRUE.
bullet-additional-damping-angular-threshold float      0.01    Only used when bullet-additional-damping is set to TRUE.
=========================================== ========== ======= =========================================================================================================================================================================================================================
