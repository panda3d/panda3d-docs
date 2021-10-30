.. _known-shader-issues:

Known Shader Bugs and Limitations
=================================

Here is a list of known issues in the shader system, with workarounds:

Problem: Register Allocation
----------------------------

*Problem:* nVidia's Cg compiler tries to assign registers to parameters. Under
a variety of circumstances, the Cg compiler will assign the same register to
two parameters, or to a parameter and to a constant in the program.

*Workaround:* We have found that if you manually allocate registers by
supplying a semantic string for each parameter, this problem is bypassed.

Problem: Bad Target Languages
-----------------------------

*Problem:* nVidia's Cg compiler will choose one of several different "target"
languages to translate the Cg program into. When the Cg compiler tries to
translate the program into the VP40/FP40 language, it often produces incorrect
output.

*Workaround:* We have discovered that translation into ARBvp1/ARBvp1 seems to
work reliably. Since that language is supported on essentially every video card,
it is usually safe to translate into that language. We have provided a config
variable that you can use to suppress bleeding edge stuff::

   basic-shaders-only true

This variable is disabled by default, though on most non-NVIDIA cards, the
ARBvp1/ARBfp1 profiles are still used by default in light of the problem above.

At some point, when functionality that is currently flaky becomes reliable, we
may expand the definition of what constitutes 'basic' shaders.

Problem: Invalid output when using ATI/AMD cards
------------------------------------------------

*Problem:* This is a specific case of the problem above. The Cg Toolkit only
supports two sets of profiles on most non-nVidia cards; the basic ARB profiles,
and the GLSL profiles. The ARB profiles are limited in functionality, which
prompts people to use the GLSL profiles. However, these often produce incorrect
results on ATI/AMD cards.

*Workaround:* Enable "basic-shaders-only true" as described above. For advanced
shader effects, write your shaders in GLSL instead of Cg if you intend to
support non-nVidia cards.

Problem: Cg program too complex for driver
------------------------------------------

*Problem:* Panda will translate the shader into the ARBvp1/ARBvp1 profile by
default, for the reason stated above. If instructions are used that are not
supported by these profiles, this error will occur.

*Workaround:* The recommended approach is to first try and find out which
instructions are causing it to fail to compile under the ARB profiles. The
most common problem is when a loop is used with a variable length, which
cannot be unrolled by the compiler::

   for (i = 0; i < k_iterations.x; ++i)

Instead, you should use a constant that is known at compile-time::

   #define ITERATIONS 10
   for (i = 0; i < ITERATIONS; ++i)

*Workaround:* You need to disable the basic-shaders-only flag to allow Panda to
translate the shaders into profiles that do support the used instructions::

   basic-shaders-only false

Note that by doing so you might run into the problem above, and it is not
recommended to do so unless you really need it.

Problem: Untested/Unfinished DirectX Support
--------------------------------------------

*Problem:* Shader development is currently being done in OpenGL. The DirectX
support typically lags behind, and is often less fully-tested.

*Workaround:* The default setting for Panda is to use OpenGL, not DirectX. For
now, when using shaders, do not change this setting.
