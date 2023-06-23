.. _known-shader-issues:

Known Shader Bugs and Limitations
=================================

Here is a list of known issues in the shader system, with workarounds:

Problem: Poor Support for Older GLSL Versions
---------------------------------------------

*Problem:* GLSL shaders older than 1.50 do not work on some platforms if
``gl-version 3 2`` is set in Config.prc, or when using DirectX.

*Workaround:* Panda3D 1.11 contains a new shader pipeline, which is able to
convert shaders to a shader language supported by the driver automatically.
However, this new shader pipeline can only compile GLSL versions 1.50 and above.
Older shaders are compiled by the driver instead, which means that you are at
the mercy of which GLSL versions are supported by the platform.

The simple solution is to upgrade your GLSL shaders. We recommend upgrading to
at least GLSL 3.30. Panda3D's shader compiler can automatically convert the
shaders back to an older GLSL version if the driver does not support GLSL 3.30.

Problem: Untested/Unfinished DirectX Support
--------------------------------------------

*Problem:* Shader development is currently being done in OpenGL. The DirectX
support typically lags behind, and is often less fully-tested.

*Workaround:* The default setting for Panda is to use OpenGL, not DirectX. For
now, when using shaders, do not change this setting.
