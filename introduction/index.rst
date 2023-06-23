.. _intro:

Introduction to Panda3D
=======================

Why Panda3D?
------------

Panda3D was created for commercial game development and is still used for
developing commercial games. It supports both Python and C++ with Python
having additional features. The engine could be a good fit for you because
of four reasons: completeness, error tolerance, speed, and power.

Completeness means that not only does Panda3D contains many unexciting but
essential tools - scene graph browsing, performance monitoring, animation optimizers, 
cross platform builds, and much more - but the engine comes with what you'll
need out of the box to create realtime games, visualizations, simulations, 
and experiments.

Error tolerance is about the fact that all game developers create bugs. When you
do, you want your engine to give you a clear error message and help you find the
mistake. Too many engines will just crash if you pass the wrong value to a
function. Panda3D almost never crashes, and much code is dedicated to the
problem of tracking and isolating errors.

As for speed Panda3D is fast to develop in because of its Python bindings 
which allow you to access to Python's massive ecosystem and community but
if you need something more low level it's easy to drop into C++ and get
what you need. Additionally the engine is very lightweight in terms of download
size and system requirements. So when you use Panda3D you don't need to worry 
about if your hardware is powerful enough or if you'll need a new hard drive,
and neither will you target audience. 

Panda3D is very powerful for not only the reasons listed above but also
because it gives you freedom to create your project the way you what while 
providing the tools to do that unlike many other tools which either lock you
into their design or expect you to create everything yourself.

So what are you waiting for? Join our friendly and helpful global community
and start using Panda3D today!

You can read more about Panda3D's :ref:`features`.

Samples
------
You can view Panda3D's samples here: :ref:`Sample Programs <samples>`.

History
-------

Panda3D was developed by Disney for their massively multiplayer online game,
Toontown Online. It was released as free software in 2002. Carnegie Mellon
University's Entertainment Technology Center, which currently hosts the website
and other Panda3D services, was actively involved in the development of Panda3D
into an open source project. 

Who is Working on Panda3D
-------------------------

There are a number of developers in the commercial and open-source community.
Currently, besides the active contributions from the open-source community, the
most active member of the development community is Disney. Disney's primary
interest in Panda3D is commercial. Panda3D is being used in the development of a
number of Disney games and amusement-park exhibits. To serve Disney's needs,
Panda3D must be a fully-featured engine, capable of all the performance and
quality one expects in any 'A-grade' commercial title.

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
