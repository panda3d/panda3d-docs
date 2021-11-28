.. _shaders:

Shaders
=======

What are Shaders?
-----------------

Once upon a time, each 3D video card had a fixed list of things that it could
do. At first, the feature lists were short: the cards could draw polygons, do
some basic texturing, a little alpha blending, and that was it. As time went
on, the list of features increased and increased: offscreen buffers,
multisampling, hardware transform and lighting, and so forth. Every time
somebody thought of some new rendering trick they wanted to try, they had to
design a new video card with the new ability. People are creative, so soon,
the list of known features exceeded 350 - this is not an exaggeration, see the
OpenGL extension registry! Each of these features corresponded to each of the
hundreds of rendering tricks that people had thought of so far. Yet, people
kept designing new video card features, because their creativity for inventing
new rendering tricks had not nearly been exhausted.

Eventually, somebody realized that video cards needed to be more like
computers. When you want your computer to have a new capability, you don't
design a new computer. You install a new piece of software. Adding software
gives a computer new capabilities. If you could download new software to your
video card, they reasoned, you wouldn't need design a new video card every
time you thought of a new rendering trick. You could upgrade the new feature
right into the card, right when you needed it.

And so, shaders were invented. Shaders are software for video cards. Shaders
look just like computer programs, but they're executed by the video card, not
the computer. If a video card supports shaders, it can be upgraded to support
almost any desired behavior. Pretty much, the only thing that limits a
shader-based video card is its speed.

Automatic use of Shaders
------------------------

Panda3D supports several advanced rendering techniques such as per-pixel
lighting, normal mapping, gloss mapping, glow mapping, HDR, bloom, and cartoon
inking out of the box. In order to make these work, Panda is quietly uploading
shaders to your video card. You don't need to write shaders to use these
features, or even know much about shaders. You just turn these features on. To
learn how to turn these features on, read about these features in their own
sections of the manual.

Writing your own Shaders
------------------------

If what you want to do is one of the things that Panda already supports
automatically, such as per-pixel lighting, normal mapping, gloss mapping, glow
mapping, HDR, bloom, or cartoon inking, you don't need to write any shaders.
Just let Panda handle it.

But if you want to do anything else --- for instance, if you wanted to do
painterly rendering, or water reflections, or lens flare, or ... well, your
imagination's the limit --- in that case, you need to write your own shaders.
The following sections will tell you about how to do that in Panda3D.


.. toctree::
   :maxdepth: 2

   shader-basics
   list-of-glsl-inputs
   list-of-cg-inputs
   coordinate-spaces
   known-shader-issues
   shader-generator
   compute-shaders
   cg-shader-tutorial/index
