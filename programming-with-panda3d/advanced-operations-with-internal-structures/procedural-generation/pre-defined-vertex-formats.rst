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



.. only:: python

    ============================== ==================== ==================== ========================================== ====================================== ===================
    **Standard format**            **vertex** (X, Y, Z) **normal** (X, Y, Z) **color**, 4-component RGBA (OpenGL style) **color**, packed RGBA (DirectX style) **texcoord** (U, V)
    GeomVertexFormat.getV3()       ✓                                                                                                                          
    GeomVertexFormat.getV3n3()     ✓                    ✓                                                                                                     
    GeomVertexFormat.getV3t2()     ✓                                                                                                                           ✓
    GeomVertexFormat.getV3n3t2()   ✓                    ✓                                                                                                      ✓
    GeomVertexFormat.getV3c4()     ✓                                         ✓                                                                                
    GeomVertexFormat.getV3n3c4()   ✓                    ✓                    ✓                                                                                
    GeomVertexFormat.getV3c4t2()   ✓                                         ✓                                                                                 ✓
    GeomVertexFormat.getV3n3c4t2() ✓                    ✓                    ✓                                                                                 ✓
    GeomVertexFormat.getV3cp()     ✓                                                                                    ✓                                     
    GeomVertexFormat.getV3n3cp()   ✓                    ✓                                                               ✓                                     
    GeomVertexFormat.getV3cpt2()   ✓                                                                                    ✓                                      ✓
    GeomVertexFormat.getV3n3cpt2() ✓                    ✓                                                               ✓                                      ✓
    ============================== ==================== ==================== ========================================== ====================================== ===================
    




.. only:: cpp

    ================================ ==================== ==================== ========================================== ====================================== ===================
    **Standard format**              **vertex** (X, Y, Z) **normal** (X, Y, Z) **color**, 4-component RGBA (OpenGL style) **color**, packed RGBA (DirectX style) **texcoord** (U, V)
    GeomVertexFormat::get_v3()       ✓                                                                                                                          
    GeomVertexFormat::get_v3n3()     ✓                    ✓                                                                                                     
    GeomVertexFormat::get_v3t2()     ✓                                                                                                                           ✓
    GeomVertexFormat::get_v3n3t2()   ✓                    ✓                                                                                                      ✓
    GeomVertexFormat::get_v3c4()     ✓                                         ✓                                                                                
    GeomVertexFormat::get_v3n3c4()   ✓                    ✓                    ✓                                                                                
    GeomVertexFormat::get_v3c4t2()   ✓                                         ✓                                                                                 ✓
    GeomVertexFormat::get_v3n3c4t2() ✓                    ✓                    ✓                                                                                 ✓
    GeomVertexFormat::get_v3cp()     ✓                                                                                    ✓                                     
    GeomVertexFormat::get_v3n3cp()   ✓                    ✓                                                               ✓                                     
    GeomVertexFormat::get_v3cpt2()   ✓                                                                                    ✓                                      ✓
    GeomVertexFormat::get_v3n3cpt2() ✓                    ✓                                                               ✓                                      ✓
    ================================ ==================== ==================== ========================================== ====================================== ===================
    

