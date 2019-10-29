.. _motion-paths:

Motion Paths
============

Motion paths in Panda3D are splines created by a modeler that are then
exported to egg files. These egg files are then imported into a program, and
various nodes can then use the motion path for complex movement. A viable egg
file for a motion path has the “curve” tag.

First, the :py:mod:`~direct.directutil.Mopath` and
:py:mod:`~direct.interval.MopathInterval` modules must be loaded. While motion
paths come with their own play functions, a motion path interval allows for
more functionality.

.. code-block:: python

   from direct.directutil import Mopath
   from direct.interval.MopathInterval import *

With the modules loaded, the motion path is loaded much like an actor is
loaded. A NodePath is created with the knowledge that it will be used for a
motion path, and then the file is loaded.

.. code-block:: python

   myMotionPathName = Mopath.Mopath()
   myMotionPathName.loadFile("File Path")

Finally, the motion path interval may be created, and played like any interval
can. The interval requires not only the name of the motion path, but also the
NodePath that will be affected by it.

.. code-block:: python

   myInterval = MopathInterval(myMotionPathName, myNodePath, name = "Name")
   myInterval.start()
