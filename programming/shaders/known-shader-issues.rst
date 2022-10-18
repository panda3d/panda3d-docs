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

Problem: Poor Support for Cg Shaders
------------------------------------

*Problem:* Some syntax of NVIDIA Cg shaders is poorly recognized.

*Workaround:* Since the proprietary NVIDIA Cg Toolkit is deprecated and not
available for some platforms, Panda3D 1.11 replaces it with a new compiler.
This compiler is provided as a best-effort attempt to retain backward
compatibility with existing shaders, but it is not as good as the Cg Toolkit.
Support for some language features may be flaky. Generally, it is possible to
fudge the shader so that it will compile, but we recommend writing your shaders
in GLSL 3.30 instead going forward.

If you do find a shader that used to compile with the Cg Toolkit but no longer
compiles with the new compiler, please file an issue on the issue tracker:

https://github.com/panda3d/panda3d/issues/new?assignees=&labels=&template=bug.md

Problem: Untested/Unfinished DirectX Support
--------------------------------------------

*Problem:* Shader development is currently being done in OpenGL. The DirectX
support typically lags behind, and is often less fully-tested.

*Workaround:* The default setting for Panda is to use OpenGL, not DirectX. For
now, when using shaders, do not change this setting.
