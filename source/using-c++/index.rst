.. _using-c++:

Using C++
=========

Though Panda3D is often used with Python, it is possible to program a complete
game in C++ without any line of Python. To start a C++ project, rebuilding
Panda3D from source is not needed. This is done by including the right headers
and linking with the right libraries.

This section will explain how to use C++ to create your Panda3D programs instead
of the default Python language.

The manual and the API are mainly focused at the use of Python, so you will need
to keep a few things in mind:

-  You need to include the file ``pandabase.h``, which is needed to initialize
   the Panda3D library.
-  There's no DirectStart. You need to create windows yourself using the
   :ref:`Window Framework <the-window-framework>`.
-  You can import the classes you need just by including their header file, like
   this::

   #include "textNode.h"

-  The functions are called the same way, but in lowercase and spaces between
   the words.

   So ``instanceTo()`` in Python becomes ``instance_to()`` in C++.


.. toctree::
   :maxdepth: 2

   how-to-compile-a-c++-panda3d-program/index
   the-window-framework
   texturing-in-c++
   reference-counting
