Built-in Global Variables
=========================

.. py:module:: builtins

.. py:currentmodule:: builtins

.. only:: cpp

   This page is not relevant for C++ users.

.. only:: python

   When an instance of the :py:class:`~direct.showbase.ShowBase.ShowBase` class
   is created, many of its member variables are written to the built-in scope
   of the Python interpreter, making them available to any Python module without
   the need for extra imports.

   While these are handy for prototyping, we do not recommend using them in
   bigger projects as it can make the code confusing to read to other Python
   developers to whom it may not be obvious from where these variables are
   originating.

   Many of these built-in variables are alternatively accessible as members of
   the global :py:data:`base` instance, or can instead be imported from the
   :py:mod:`~direct.showbase.ShowBaseGlobal` module.

   The variables written to the built-in scope are:

   .. py:data:: base

      A global instance of the :py:class:`~direct.showbase.ShowBase.ShowBase`
      class is available to any Python scope as ``base``.  This allows access to
      the graphical display, the scene graph, the input devices, the task and
      event managers, and all the other things that ShowBase is responsible for
      setting up and managing.

      Although it is not a required component, most Panda3D applications are
      created using the ShowBase abstraction layer, because it sets up nearly
      everything needed by most games and simulations, with only a minimal
      amount of set up required.  In fact, to start up a ShowBase application,
      it is only necessary to call:

      .. code-block:: python

         from direct.showbase.ShowBase import ShowBase

         base = ShowBase()
         base.run()

      There can only be one ShowBase instance at a time; call
      :py:meth:`~direct.showbase.ShowBase.ShowBase.destroy()` to get rid of it,
      which will allow another instance to be created.

      :type: .ShowBase

   .. py:data:: render

      A NodePath created as the root of the default 3-D
      :ref:`scene graph <the-scene-graph>`. Parent models to this node to make
      them show up in the 3-D display region.

      :type: ~panda3d.core.NodePath

   .. py:data:: render2d

      Like :py:data:`render`, but created as root of the 2-D scene graph.
      The coordinate system of this node runs from -1 to 1, with the X axis
      running from left to right and the Z axis from bottom to top.

      :type: ~panda3d.core.NodePath

   .. py:data:: aspect2d

      The root of the 2-D scene graph used for GUI rendering.  Unlike
      :py:data:`render2d`, which may result in elements being stretched in
      windows that do not have a square aspect ratio, this node is scaled
      automatically to ensure that nodes parented to it do not appear stretched.

      :type: ~panda3d.core.NodePath

   .. py:data:: pixel2d

      This is a variant of :py:data:`aspect2d` that is scaled up such that one
      Panda unit is equal to one pixel on screen. It can be used if
      pixel-perfect layout of UI elements is desired. Its pixel origin is also
      in the top-left corner of the screen. Because Panda uses a Z-up coordinate
      system, however, please note that the Z direction goes up the screen
      rather than down, and therefore it is necessary to use negative instead of
      positive coordinates in the Z direction.

      :type: ~panda3d.core.NodePath

   .. py:data:: hidden

      This is a scene graph that is not used for anything, to which nodes can be
      parented that should not appear anywhere.  This is esoteric and rarely
      needs to be used; the use of :py:meth:`~panda3d.core.NodePath.stash()`
      will suffice in most situations wherein a node needs to be temporarily
      removed from the scene graph.

      :type: ~panda3d.core.NodePath

   .. py:data:: camera

      A node that is set up with the camera used to render the default 3-D scene
      graph (:py:data:`render`) attached to it.  This is the node that should be
      used to manipulate this camera, but please note that it is necessary to
      first call :py:meth:`base.disableMouse()
      <direct.showbase.ShowBase.ShowBase.disableMouse>` to ensure that the
      default mouse controller releases its control of the camera.

      :type: ~panda3d.core.NodePath

   .. py:data:: loader

      This is the primary interface through which assets such as models,
      textures, sounds, shaders and fonts are loaded.
      See :ref:`model-files` and :ref:`simple-texture-replacement`.

      :type: ~direct.showbase.Loader.Loader

   .. py:data:: taskMgr

      The global :ref:`task manager <tasks>`, as imported from
      :py:mod:`direct.task.TaskManagerGlobal`.

      :type: ~direct.task.Task.TaskManager

   .. py:data:: jobMgr

      The global job manager, as imported from
      :py:mod:`direct.showbase.JobManagerGlobal`.

      :type: ~direct.showbase.JobManager.JobManager

   .. py:data:: eventMgr

      The global event manager, as imported from
      :py:mod:`direct.showbase.EventManagerGlobal`.

      :type: ~direct.showbase.EventManager.EventManager

   .. py:data:: messenger

      The global messenger, imported from
      :py:mod:`direct.showbase.MessengerGlobal`, is responsible for
      :ref:`event handling <event-handlers>`.  The most commonly used method of
      this object is perhaps :py:meth:`messenger.send("event")
      <direct.showbase.Messenger.Messenger.send>`, which dispatches a custom
      event.

      :type: ~direct.showbase.Messenger.Messenger

   .. py:data:: bboard

      The global bulletin board, as imported from
      :py:mod:`direct.showbase.BulletinBoardGlobal`.

      :type: ~direct.showbase.BulletinBoard.BulletinBoard

   .. py:data:: ostream

      The default Panda3D output stream for notifications and logging, as
      a short-hand for :py:meth:`Notify.out() <panda3d.core.Notify.out>`.

      :type: ~panda3d.core.Ostream

   .. _the-global-clock:

   .. py:data:: globalClock

      The clock object used by default for timing information, a short-hand for
      :py:meth:`ClockObject.getGlobalClock() <panda3d.core.ClockObject.getGlobalClock>`.

      The most common use is to obtain the time elapsed since the last frame
      (for calculations in movement code), using :py:obj:`globalClock.dt
      <panda3d.core.ClockObject.dt>`.  The value is given in seconds.

      Another useful function is to get the frame time (in seconds, since the
      program started):

      .. code-block:: python

         frameTime = globalClock.getFrameTime()

      :type: ~panda3d.core.ClockObject

   .. py:data:: vfs

      A global instance of the :ref:`virtual file system <virtual-file-system>`,
      as a short-hand for :py:meth:`VirtualFileSystem.getGlobalPtr()
      <panda3d.core.VirtualFileSystem.getGlobalPtr>`.

      :type: ~panda3d.core.VirtualFileSystem

   .. py:data:: cpMgr

      Provides access to the loaded configuration files.
      Short-hand for :py:meth:`ConfigPageManager.getGlobalPtr()
      <panda3d.core.ConfigPageManager.getGlobalPtr>`.

      :type: ~panda3d.core.ConfigPageManager

   .. py:data:: cvMgr

      Provides access to configuration variables.
      Short-hand for :py:meth:`ConfigVariableManager.getGlobalPtr()
      <panda3d.core.ConfigVariableManager.getGlobalPtr>`.

      :type: ~panda3d.core.ConfigVariableManager

   .. py:data:: pandaSystem

      Provides information about the Panda3D distribution, such as the version,
      compiler information and build settings.
      Short-hand for :py:meth:`PandaSystem.getGlobalPtr()
      <panda3d.core.PandaSystem.getGlobalPtr>`.

      :type: ~panda3d.core.PandaSystem

   .. py:function:: inspect(obj)

      Short-hand for :py:func:`direct.tkpanels.Inspector.inspect()`, which opens
      up a GUI panel for inspecting an object's properties.

      See :ref:`inspection-utilities`.

   .. py:data:: config

      The deprecated :py:mod:`~direct.showbase.DConfig` interface for
      :ref:`accessing config variables <accessing-config-vars-in-a-program>`.

   .. py:function:: run()

      Calls the task manager main loop, which runs indefinitely.  This is a
      deprecated short-hand for
      :py:meth:`base.run() <direct.showbase.ShowBase.ShowBase.run>`.

      See :ref:`main-loop`.
