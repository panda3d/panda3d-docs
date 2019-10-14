.. _softbody-config:

Bullet Softbody Config
======================

Bullet uses abbreviated properties which describe a soft bodies behaviour.
Here are explanations for the most important settings, and their mapping to
Bullet properties:

btSoftBody::Material vs. BulletSoftBodyMaterial:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

==================== ============================= ===================
btSoftBody::Material BulletSoftBodyMaterial        Description
==================== ============================= ===================
``m_kLST``           ``get/setLinearStiffness``    Linear stiffness
                                                   Range [0,1]
``m_kAST``           ``get/setAngularStiffness``   Angular stiffness
                                                   Range [0,1]
``m_kVST``           ``get/setVolumePreservation`` Volume preservation
                                                   Range [0,1]
==================== ============================= ===================


btSoftBody::Config vs. BulletSoftBodyConfig
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

================== ======================================== ============================================
btSoftBody::Config BulletSoftBodyConfig                     Description
================== ======================================== ============================================
``kSRHR_CL``       ``get/setSoftVsRigidHardness``           Soft vs rigid hardness (cluster only)
                                                            Range [0,1]
``kSKHR_CL``       ``get/setSoftVsKineticHardness``         Soft vs kinetic hardness (cluster only)
                                                            Range [0,1]
``kSSHR_CL``       ``get/setSoftVsSoftHardness``            Soft vs soft hardness (cluster only)
                                                            Range [0,1]
``kSR_SPLT_CL``    ``get/setSoftVsRigidImpulseSplit``       Soft vs rigid impulse split (cluster only)
                                                            Range [0,1]
``kSK_SPLT_CL``    ``get/setSoftVsKineticImpulseSplit``     Soft vs kinetic impulse split (cluster only)
                                                            Range [0,1]
``kSS_SPLT_CL``    ``get/setSoftVsSoftImpulseSplit``        Soft vs soft impulse split (cluster only)
                                                            Range [0,1]
``kVCF``           ``get/setVelocitiesCorrectionFactor``    Velocities correction factor (Baumgarte)
``kDP``            ``get/setDampingCoefficient``            Damping coefficient
                                                            Range [0,1]
``kDG``            ``get/setDragCoefficient``               Drag coefficient
                                                            Range [0,+inf]
``kLF``            ``get/setLiftCoefficient``               Lift coefficient
                                                            Range [0,+inf]
``kPR``            ``get/setPressureCoefficient``           Pressure coefficient
                                                            Range [-inf,+inf]
``kVC``            ``get/setVolumeConversationCoefficient`` Volume conversation coefficient
                                                            Range [0,+inf]
``kDF``            ``get/setDynamicFrictionCoefficient``    Dynamic friction coefficient
                                                            Range [0,1]
``kMT``            ``get/setPoseMatchingCoefficient``       Pose matching coefficient
                                                            Range [0,1]
``kCHR``           ``get/setRigidContactsHardness``         Rigid contacts hardness
                                                            Range [0,1]
``kKHR``           ``get/setKineticContactsHardness``       Kinetic contacts hardness
                                                            Range [0,1]
``kSHR``           ``get/setSoftContactsHardness``          Soft contacts hardness
                                                            Range [0,1]
``kAHR``           ``get/setAnchorsHardness``               Anchors hardness
                                                            Range [0,1]
``piterations``    ``get/setPositionsSolverIterations``     Positions solver iterations
                                                            Positive integer
``viterations``    ``get/setVelocitiesSolverIterations``    Velocities solver iterations
                                                            Positive integer
``diterations``    ``get/setDriftSolverIterations``         Drift solver iterations
                                                            Positive integer
``citerations``    ``get/setClusterSolverIterations``       Cluster solver iterations
                                                            Positive integer
================== ======================================== ============================================
