.. _particle-renderers:

Particle Renderers
==================

Particle renderers add particles to the visible scene graph according to the
information stored in the particle objects and the type of renderer. All
particle renderers have the following parameters:

============ ===================================== =======================================================
**Variable** **Definition**                        **Values**
alphaMode    Alpha setting over particle lifetime  PR_ALPHA_NONE, PR_ALPHA_OUT, PR_ALPHA_IN, PR_ALPHA_USER
userAlpha    Alpha value for ALPHA_USER alpha mode Boolean
============ ===================================== =======================================================


The following list contains the different types of renderers and their unique
parameters.

PointParticleRenderer
~~~~~~~~~~~~~~~~~~~~~


Renders particles as pixel points.

============ ============================================================= ================================
**Variable** **Definition**                                                **Values**
pointSize    Width and height of points, in pixels                         [0, infinity)
startColor   Starting color                                                (r, g, b, a)
endColor     Ending color                                                  (r, g, b, a)
blendType    How the particles blend from the start color to the end color ONE_COLOR, BLEND_LIFE, BLEND_VEL
blendMethod  Interpolation method between colors                           LINEAR, CUBIC
============ ============================================================= ================================


ONE_COLOR: point is always the starting color.

BLEND_LIFE: color is interpolated from start to end according to the age of
the point

BLEND_VEL: color is interpolated between start to end according to the
velocity/terminal velocity.

LineParticleRenderer
~~~~~~~~~~~~~~~~~~~~


Renders particles as lines between their current position and their last
position.

============ ===================== ============
**Variable** **Definition**        **Values**
headColor    Color of leading end  (r, g, b, a)
tailColor    Color of trailing end (r, g, b, a)
============ ===================== ============


SparkleParticleRenderer
~~~~~~~~~~~~~~~~~~~~~~~


Renders particles star or sparkle objects, three equal-length perpendicular
axial lines, much like jacks. Sparkle particles appear to sparkle when viewed
as being smaller than a pixel.

============ ====================================================== ===============
**Variable** **Definition**                                         **Values**
centerColor  Color of center                                        (r, g, b, a)
edgeColor    Color of edge                                          (r, g, b, a)
birthRadius  Initial sparkle radius                                 [0, infinity)
deathRadius  Final sparkle radius                                   [0, infinity)
lifeScale    Whether or not sparkle is always of radius birthRadius NO_SCALE, SCALE
============ ====================================================== ===============


SpriteParticleRenderer
~~~~~~~~~~~~~~~~~~~~~~


Renders particles as an image, using a Panda3D texture object. The image is
always facing the user.

================ ========================================================================= =============
**Variable**     **Definition**                                                            **Values**
texture          Panda texture object to use as the sprite image                           (r, g, b, a)
color            Color                                                                     (r, g, b, a)
xScaleFlag       If true, x scale is interpolated over particle’s life                     Boolean
yScaleFlag       If true, y scale is interpolated over particle’s life                     Boolean
animAngleFlag    If true, particles are set to spin on the Z axis                          Boolean
initial_X_Scale  Initial x scaling factor                                                  [0, infinity)
final_X_Scale    Final x scaling factor                                                    [0, infinity)
initial_Y_Scale  Initial y scaling factor                                                  [0, infinity)
final_Y_Scale    Final y scaling factor                                                    [0, infinity)
nonAnimatedTheta If false, sets the counterclockwise Z rotation of all sprites, in degrees Boolean
alphaBlendMethod Sets the interpolation blend method                                       LINEAR, CUBIC
alphaDisable     If true, alpha blending is disabled                                       Boolean
================ ========================================================================= =============


GeomParticleRenderer
~~~~~~~~~~~~~~~~~~~~


Renders particles as full 3D objects. This requires a geometry node.

============ =========================== ==========
**Variable** **Definition**              **Values**
geomNode     A geometry scene graph node
============ =========================== ==========
