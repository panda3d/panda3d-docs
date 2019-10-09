.. _render-to-texture-and-image-postprocessing:

Render-to-Texture and Image Postprocessing
==========================================

Render-to-Texture Basics
------------------------


Conceptually, you can think of render-to-texture as being like rendering a
scene into a hidden window, and then copying the contents of the window into a
texture. Such hidden windows are not actually called windows, they're called
"buffers." Furthermore, the data is usually not copied into the texture, it's
usually transferred into the texture using a more efficient mechanism. Details
aside, though, if you think of it as rendering into a hidden window and then
copying into a texture, you have a pretty accurate idea of what
render-to-texture does.

Render-to-texture is particularly useful when you'd like to apply a "filter"
to your scene. If you've ever used Photoshop, you know what a filter is:
Photoshop has lots of interesting filters that do blurring, texturizing, edge
detection, and more. The first step in implementing a filter is to render the
entire scene into a texture. Then, the texture is applied to a full-screen
quad and displayed in a window. So far, it looks the same as if you simply
rendered the scene into the window. However, by applying a shader to the
full-screen quad, you can implement your filter.

There are several other interesting uses for render-to-texture: water
reflections, environment mapping, creating virtual televisions, shadow
mapping... the list is quite long.

The Low-Level API and the High-Level Utilities
----------------------------------------------


Panda3D contains a very low-level API for creating offscreen buffers, creating
render-target textures, and the like. This low-level API is extremely
flexible: it gives you a great deal of control over what kinds of buffers you
create, over what gets rendered into them, over how the data gets transferred
to a texture, and so forth. The advantage of using the low-level API is that
you can control everything. The disadvantage is that you have to control
everything, and there's a lot of stuff to control.

Panda3D also provides a number of utilities that make it convenient to use
render-to-texture for certain specific applications. For example, there is a
utility that helps set up common image filters. There is another that helps
set up cube-map environment maps. The downside of these utilities is that each
one performs a fairly specific function, and if there isn't one for your
particular application, you'll need to resort to the lower-level API.

In the following sections, we document the high-level utilities first, because
these are what most people are going to use. If none of the utilities does
what you need, then the last subsection explains the low-level API.


.. toctree::
   :maxdepth: 2

   common-image-filters
   generalized-image-filters
   dynamic-cube-maps
   low-level-render-to-texture
