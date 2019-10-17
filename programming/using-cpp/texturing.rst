.. _texturing-in-c++:

Texturing in C++
================

.. only:: python

   This page is related to C++ usage of Panda3D and not to Python usage. If you
   are a Python user, please skip this page. For C++ users, please toggle to the
   C++ version of this page.

.. only:: cpp

   Texturing in C++
   ----------------

   Panda's C++ interface to texturing is basically the same as it's Python
   interface, That's why it is very recommended to read the entire section
   including the Python examples.

   However, there are two major differences, which are explained in this page.

   1. C++ does not have a loader.loadTexture. You need to use the TexturePool to
      load textures. Please note that the Texture class is
      :ref:`reference counted <reference-counting>`.

   .. code-block:: cpp

      #include "texturePool.h"

      PT(Texture) tex;
      tex = TexturePool::load_texture("maps/noise.rgb");

      NodePath smiley;
      smiley = window->load_model(window->get_render(),"smiley.egg");
      smiley.set_texture(tex, 1);

   2. You don't directly need CardMaker to display your texture in a 2D or 3D
      scene. You can load it as if it were a model, and treat it like any other
      model.

   .. code-block:: cpp

      NodePath noiseplane;
      noiseplane = window->load_model(window->get_render(), "maps/noise.rgb");

   This short piece of code will result in a single polygon in the scene with
   the noise texture applied to it. If you need it in the 2-D scene, you can use
   get_aspect2d() or get_render2d() instead of get_render().
