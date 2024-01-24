.. _inspection-utilities:

Utility Functions
=================

Panda3D has a set of utilities that may be used to learn more about various
objects and methods within an application.

One of these commands is :py:func:`~direct.tkpanels.Inspector.inspect()`.
This command will create a window with methods and attributes on one side, and
the details of a selected attribute on the other. It also displays the current
values of a class’ attributes. If these attributes are changing, you may have to
click on a value to refresh it. To use it you have to do the following:

.. code-block:: python

   from direct.tkpanels.Inspector import inspect
   inspect(NodePath)
   # e.g. inspect(camera)

While the directtools suite calls upon a number of tools, if the suite is
disabled, the user may activate certain panels of the suite. The ``place()``
command opens the object placer console. The ``explore()`` opens the scene graph
explorer, which allows you to inspect the hierarchy of a NodePath. Finally, in
order to change the color of a NodePath, the ``rgbPanel()`` command opens color
panel.

.. code-block:: python

   camera.place()
   render.explore()
   panda.rgbPanel()
