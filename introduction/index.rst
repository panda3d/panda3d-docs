.. _intro:

Introduction to Panda3D
=======================

Panda3D is a 3D engine: a library of subroutines for 3D rendering and game
development on windows, mac, linux and android.

The library is C++ with a set of Python bindings. It can be used with
C++ and/or Python.

Panda3D was developed by Disney for their massively multiplayer online game,
Toontown Online. It was released as free software in 2002. Carnegie Mellon
University's Entertainment Technology Center was actively involved in the development of Panda3D
into an open source project. It is now developed by contributors from around the world.

You can read more about Panda3D's :ref:`features`.

Feature Overview
----------------

While Panda3D is not cutting edge today, it was developed to support 
most basic features that are still essential for game development:
convenient support for normal mapping, gloss mapping, HDR, cartoon shading and
inking, bloom, and a number of other things. It also allows you to write your
own shaders.

Panda3D supports easy importing and conversions of assets 
from `blender<https://blender.org>` 

To gauge Panda3D's capabilities you can take a look at the 
:ref:`Sample Programs <samples>`. These are short programs that 
demonstrate a sampling of Panda3D's capabilities.

Panda3D's Software License
--------------------------

Since version 1.5.3, Panda3D has been released under the so-called "Modified BSD
license," which is a free software license with very few restrictions on usage.

In versions 1.5.2 and before, it used a proprietary license which was very
similar in intention to the BSD and MIT licenses, though there was some
disagreement about the freeness of two of the clauses. The old license can still
be accessed `here <https://raw.githubusercontent.com/panda3d/panda3d/41876b5829d921ade92d0795bb7091d009e3f9b7/doc/LICENSE>`__.

Although the engine itself is completely free, it comes with various third-party
libraries that are not free software. Some of them (like FMOD) even restrict you
from using them in commercial games unless you have licensed copies. Because of
this reason, Panda3D makes it easy to disable or remove these restricted third-
party libraries, and most of the time it offers an alternative. For example, it
also comes with OpenAL which you can use instead of FMOD.

You can read `Panda3D's License <https://www.panda3d.org/license/>`__.

Code Overview
-------------

There is a place for this, but not on the landing page.

People sometimes have the mistaken impression that Panda3D is written in Python,
which would make it very slow. But Panda3D is not written in Python; it's
written in C++. Python is just used for scripting. Developers usually write the
performance-intensive bits, if any, in C++ or something similar
`Cython <https://www.panda3d.org/blog/panda3d-and-cython/>`__. To see what kind
of framerate a small Panda3D program typically gets, take a look at the
screenshots of the :ref:`Sample Programs <samples>`. It doesn't happen 
automatically. Panda3D includes profiling tools
you need to hit 60 fps.


Who is Working on Panda3D
-------------------------

Panda3d is now mostly an open source community project.

