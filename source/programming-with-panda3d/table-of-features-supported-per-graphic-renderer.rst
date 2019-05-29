.. _table-of-features-supported-per-graphic-renderer:

Table of features supported per graphic renderer
================================================

This is a table of features that are not supported by all of the available
Panda3D graphics back-end plug-ins. For brevity, features supported by all of
the renderers are omitted.

This is by no means a complete list. The OpenGL renderer is by far the most
complete back-end, and many features that it supports are not yet listed
below.

=================== ========== ============= =========== ===========
\                   OpenGL     Direct3D 9    GLES, WebGL Tinydisplay
=================== ========== ============= =========== ===========
Rendering           Hardware   Hardware      Hardware    Software
Cg shaders          Yes        Yes           No          No
GLSL shaders        Yes        No            Yes         No
Geometry shaders    Yes        No            No          No
Shader generation   Yes        Partial       No          No
sRGB support        Yes        Yes           No          Yes
Depth textures      Yes        No\ :sup:`1`  Yes         No
3-D textures        Yes        Yes           Yes         No
Buffer textures     Since 1.10 No            No          No
Multisampling       Yes        Yes\ :sup:`2` Yes         No
Thick wireframe     Yes        No            Yes         No
Geometry instancing Yes        No            Since 1.9.1 No
=================== ========== ============= =========== ===========

:sup:`1` You can achieve shadow mapping by using shaders instead of the depth
buffer at a minimal performance cost.

:sup:`2` Supported through the configuration setting
``dx-multisample-antialiasing-level``.
