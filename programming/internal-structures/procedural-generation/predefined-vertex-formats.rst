.. _pre-defined-vertex-formats:

Pre-defined vertex formats
==========================

Panda3D predefines a handful of standard :ref:`geomvertexformat` objects that
might be useful to you. If you don't have any special format needs, feel free
to use any of these standard formats, which have already been defined and
registered, and are ready to use for rendering.

Each of these formats includes one or more of the standard columns vertex,
normal, color, and/or texcoord. For the formats that include a color column,
there are two choices, since OpenGL and DirectX have competing internal
formats for color (but you can use either form regardless of your current
rendering API; Panda will automatically convert the format at render time if
necessary).

========== ==================== ==================== ========================================== ====================================== ===================
**Format** **vertex** (X, Y, Z) **normal** (X, Y, Z) **color**, 4-component RGBA (OpenGL style) **color**, packed RGBA (DirectX style) **texcoord** (U, V)
v3         ✓
v3n3       ✓                    ✓
v3t2       ✓                                                                                                                           ✓
v3n3t2     ✓                    ✓                                                                                                      ✓
v3c4       ✓                                         ✓
v3n3c4     ✓                    ✓                    ✓
v3c4t2     ✓                                         ✓                                                                                 ✓
v3n3c4t2   ✓                    ✓                    ✓                                                                                 ✓
v3cp       ✓                                                                                    ✓
v3n3cp     ✓                    ✓                                                               ✓
v3cpt2     ✓                                                                                    ✓                                      ✓
v3n3cpt2   ✓                    ✓                                                               ✓                                      ✓
========== ==================== ==================== ========================================== ====================================== ===================

The predefined formats are accessable through the API using, for example,
:meth:`.GeomVertexFormat.get_v3n3()`.
