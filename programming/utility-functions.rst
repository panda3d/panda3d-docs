.. _panda3d-utility-functions:

Panda3D Utility Functions
=========================

Panda3D has a set of utilities that may be used to learn more about various
objects and methods within an application. To access these utilities you need
to import the PythonUtil module as follows.

.. code-block:: python

    from direct.showbase.PythonUtil import *

The ``*`` can be replaced by
any of the utility functions in that module.

To get a detailed listing of a class or an object's attributes and methods,
use the pdir() command. pdir() prints the information out to the command
console. pdir() can take many arguments for formatting the output but the
easiest way to use it is to provide it a NodePath.

pdir() will list all of the functions of the class of NodePath including those
of its base classes

.. code-block:: python

    pdir(NodePath)
    # e.g. pdir(camera)

There are many other useful functions in the PythonUtil module. All of these
are not necessarily Panda specific, but utility functions for python. There
are random number generators, random number generator in a gaussian
distribution curve, quadratic equation solver, various list functions, useful
angle functions etc. A full list can be found in the API.

An alternative command to
``pdir`` is
``inspect()``. This command will
create a window with methods and attributes on one side, and the details of a
selected attribute on the other.
``inspect()`` also displays the
current values of a class’ attributes. If these attributes are changing, you
may have to click on a value to refresh it. To use inspect() you have to do
the following:

.. code-block:: python

    from direct.tkpanels.inspector import inspect
    inspect(NodePath)
    # e.g. inspect(camera)

While the directtools suite calls upon a number of tools, if the suite is
disabled, the user may activate certain panels of the suite. The
``place()`` command opens the
object placer console. The
``explore()`` opens the scene graph
explorer, which allows you to inspect the hierarchy of a NodePath. Finally, in
order to change the color of a NodePath, the
``rgbPanel()`` command opens color
panel.

.. code-block:: python

    camera.place()
    render.explore()
    panda.rgbPanel()

Useful DirectTool panels are explained in the :ref:`Panda Tools <tools>`
section.
