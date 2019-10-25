.. _intro:

Introduction to Panda3D
=======================

Panda3D Basics
--------------

Panda3D is a 3D engine: a library of subroutines for 3D rendering and game
development. The library is C++ with a set of Python bindings. Game development
with Panda3D usually consists of writing a Python or C++ program that controls
the Panda3D library.

Panda3D was created for commercial game development and is still used for
developing commercial games. Because of this, the engine needs to emphasize four
areas: power, speed, completeness, and error tolerance. Everyone knows what
power and speed are. But completeness and error tolerance deserve some extra
commentary.

Completeness means that Panda3D contains many unexciting but essential tools:
scene graph browsing, performance monitoring, animation optimizers, and so
forth.

Error tolerance is about the fact that all game developers create bugs. When you
do, you want your engine to give you a clear error message and help you find the
mistake. Too many engines will just crash if you pass the wrong value to a
function. Panda3D almost never crashes, and much code is dedicated to the
problem of tracking and isolating errors.

Finally, to come back to power and speed: to gauge Panda3D's capabilities you
can take a look at the :ref:`Sample Programs <samples>`. These are short
programs that demonstrate a sampling of Panda3D's capabilities. The screenshots
have frame-rates in the upper-right corner, taken on a Radeon X700. Note that
some samples are old and use placeholder art and so are not great examples of
Panda3D's visual capabilities.

Panda3D was developed by Disney for their massively multiplayer online game,
Toontown Online. It was released as free software in 2002. Carnegie Mellon
University's Entertainment Technology Center, which currently hosts the website
and other Panda3D services, was actively involved in the development of Panda3D
into an open source project. It is now developed jointly by Disney and
contributors from around the world.

You can read more about Panda3D's :ref:`features`.

Panda3D is not a Beginner's Tool or a Toy
-----------------------------------------

To successfully use Panda3D, you must be a skilled programmer. If you do not
know what an "API" is, or if you don't know what a "tree" is, you will probably
find Panda3D overwhelming. This is no point-and-click game-maker: this is a tool
for professionals. While it is important to point that out so you have accurate
expectations, it's also relevant to be aware that Panda3D is one of the easiest
and most powerful engines you will ever use, and we welcome your participation.

If you are just getting started with programming, we suggest that your best
option is to start with a class on programming. Alternately, you could try
teaching yourself using a training tool like `Alice <https://www.alice.org>`__,
from CMU.

Panda3D supports the full range of what modern engines should: it provides
convenient support for normal mapping, gloss mapping, HDR, cartoon shading and
inking, bloom, and a number of other things. It also allows you to write your
own shaders.

People sometimes have the mistaken impression that Panda3D is written in Python,
which would make it very slow. But Panda3D is not written in Python; it's
written in C++. Python is just used for scripting. Developers usually write the
performance-intensive bits, if any, in C++ or something similar
`Cython <https://www.panda3d.org/blog/panda3d-and-cython/>`__. To see what kind
of framerate a small Panda3D program typically gets, take a look at the
screenshots of the :ref:`Sample Programs <samples>`. Those were taken using an
old Radeon x700. Of course, only a sample program can run at 400 fps like that,
but for a real game, 60 fps is quite attainable. One caveat, though: to get that
kind of performance, you need to understand 3D cards and 3D performance
optimization. It doesn't happen automatically. Panda3D includes profiling tools
you need to hit 60 fps.

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

Who is Working on Panda3D
-------------------------

There are a number of developers in the commercial and open-source community.
Currently, besides the active contributions from the open-source community, the
most active member of the development community is Disney. Disney's primary
interest in Panda3D is commercial. Panda3D is being used in the development of a
number of Disney games and amusement-park exhibits. To serve Disney's needs,
Panda3D must be a fully-featured engine, capable of all the performance and
quality one expects in any 'A-grade' commercial title.

The most supported language is Python. Though you can use C++ too, the
documentation is mostly aimed at Python use.

The Introductory Chapter
------------------------

This introductory chapter of the manual is designed to walk you through some of
the basics of using Panda3D. This chapter is structured as a tutorial, not as a
reference work.

.. toctree::
   :maxdepth: 2

   installation-windows
   installation-linux
   preparation
   running-your-program
   tutorial/index
