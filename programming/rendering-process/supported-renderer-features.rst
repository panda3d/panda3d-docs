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
Depth textures      Yes        Yes           Yes         No
3-D textures        Yes        Yes           Yes         No
Buffer textures     Yes        No            No          No
Multisampling       Yes        Yes\ :sup:`1` Yes         No
Thick wireframe     Yes        No            Yes         No
Geometry instancing Yes        No            Yes         No
=================== ========== ============= =========== ===========

:sup:`1` Supported through the configuration setting
``dx-multisample-antialiasing-level``.
