.. _too-many-shader-instructions:

Performance Issue: Too Many Shader Instructions
===============================================

This only can happen if you have at least one
``NodePath.setShader`` or
``NodePath.setShaderAuto`` method call in your
application, or you are using a post processing filter from CommonManager.

Too Many Vertex Shader Instructions
-----------------------------------


Try so simplify your scene. Objects that are far away don't need millions of
vertices. Look at LODNode and FadeLODNode.

Too Many Fragment/Pixel Shader Instructions
-------------------------------------------


An easy way to detect whether this is a bottleneck in your application, try
resizing the window. If the framerate heavily varies with the window size or
screen resolution, you're most likely dealing with this problem.

If your frame rate strong depends on the window or screen resolution, this may
be one hint that your fragment shader has too many instructions. Another
problem is if your depth complexity is too high. Try to look at your scene
from different angles and positions. If your frame rate varies then the
overdraw from one specific view angle is to high.

Try to minimize the objects Panda3D needs to draw. Use
``lens.setFar``, or fallback to a
simpler fragment shaders for objects that are far away. If an object is far
away from the viewer it doesn't make sense to apply normal mapping. LODNode
and FadeLODNode may help.

If your fragment shader is self made, then try to offload some work to your
vertex shader.

There is a simple method to test your scene. Replace your whole fragment
shader with the following snippet:

``o_color = float4(1.0, 0.0, 1.0, 0.0);``

If the frame rate doesn't change, then it is the depth complexity. It if
changes it may be the depth complexity or the shader.
