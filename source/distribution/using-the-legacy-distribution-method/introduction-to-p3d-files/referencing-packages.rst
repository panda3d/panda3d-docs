.. _referencing-packages:

Referencing packages
====================

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

When the Panda3D plugin system runs your p3d file, it must first download the
correct version of Panda3D, as well as any auxiliary packages your p3d file
requires in order to run. Generally, the auxiliary packages represent parts of
the Panda3D system that are not required by all p3d files, and so have been
separated to minimize unnecessary download.

The current set of auxiliary packages provided by the Panda3D team are:

fmod
   The FMod audio system, a closed-source library that is cost-free only for
   non-commercial use.
openal
   The OpenAL audio system, an audio library that is free in both senses of
   the word, but does not work well on all platforms.
audio
   Including this package implicitly includes either fmod or openal, whichever
   works best on the current platform. This is a good choice to enable audio
   for non-GPL, non-commercial applications.
egg
   The egg loader. Include this package if you wish to load egg files or use
   the egg library at runtime. Since packp3d automatically converts egg files
   to bam files, most applications don't need to include this package.
vision
   The Panda3D vision libraries, containing webcam, computer vision and
   augmented reality support.
ode
   The ODE physics engine.
physx
   The PhysX physics engine. Only functional on 32-bits Linux and Windows.
wx
   The wxPython GUI system.
tk
   The Tk GUI system.
ai
   The PandAI libraries.
morepy
   A collection of the default Python modules. You may need to mark this as
   dependency if you find default Python modules missing when running your
   game.
models
   The collection of standard models and textures that is included in the SDK.
   Note that you should not use the "models/" prefix when loading these.

There are also other packages for Python libraries, such as httplib2, numpy,
pil, pycurl, pygame, pyopengl, sqlite, tk and twisted. More packages can be
added if there is need.

To include any of the above packages in your p3d file, use the "-r" parameter
to packp3d, e.g. "packp3d -o myapp.p3d -r audio -r ode".
