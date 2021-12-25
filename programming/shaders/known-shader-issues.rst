.. _known-shader-issues:

Known Shader Bugs and Limitations
=================================

Here is a list of known issues in the shader system, with workarounds:

Problem: GLSL Versions on macOS
-------------------------------

*Problem:* On macOS, using some modern GLSL features from GLSL versions higher
than 1.20 will fail, even if the hardware is capable of higher versions.

*Workaround:* The OpenGL driver on macOS only supports GLSL 1.50 and 3.30 when
the fixed-function pipeline is turned off. This means it becomes necessary to
use shaders for all objects, and it is no longer possible to mix-and-match
custom shaders and the fixed-function pipeline. To do this, set this in
Config.prc::

   gl-version 3 2

Problem: Untested/Unfinished DirectX Support
--------------------------------------------

*Problem:* Shader development is currently being done in OpenGL. The DirectX
support typically lags behind, and is often less fully-tested.

*Workaround:* The default setting for Panda is to use OpenGL, not DirectX. For
now, when using shaders, do not change this setting.
