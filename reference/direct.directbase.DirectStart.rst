direct.directbase.DirectStart
=============================

.. only:: python

   .. module:: direct.directbase.DirectStart

   This is a shortcut, instantiating :class:`~direct.showbase.ShowBase.ShowBase`
   automatically on import.  Doing so opens a graphical window, sets up the
   :ref:`scene graph <the-scene-graph>`, and many other subsystems of Panda3D.
   This example demonstrates its use:

      .. code-block:: python

         import direct.directbase.DirectStart
         base.run()

   While it may be considered useful for quick prototyping in the interactive
   Python shell, using it in applications is not considered good style. As such,
   it has been deprecated starting with Panda3D 1.9.  Any import to DirectStart
   is equivalent to and may be replaced with the following code:

      .. code-block:: python

         from direct.showbase.ShowBase import ShowBase
         base = ShowBase()

   The :data:`~builtins.base` variable is automatically written to the built-in
   scope, so that it can be directly accessed anywhere in any Python module.
   Various other variables are written to the global scope as well, see
   :mod:`builtins` for a listing.

   See the :class:`~.ShowBase.ShowBase` class for further information on the
   :data:`~builtins.base` variable.
