.. _showbase:

ShowBase
========

.. only:: python

    Overview
    --------

    If you are already up to speed with Python, the following code may look like a
    black box:

    .. code-block:: python

        from direct.showbase.ShowBase import ShowBase

        base = ShowBase()
        base.run()

    The class
    `ShowBase <https://www.panda3d.org/reference/devel/python/direct.showbase.ShowBase.ShowBase>`__
    inherits from DirectObject. Under Linux, the relevant file can be found in:

    ``/usr/share/panda3d/direct/showbase/``

    On Windows, the code is (by default) located in:

    ``C:\Panda3D-1.X.X\direct\showbase``

    An important item created meanwhile is a base task manager as
    ``taskMgr``. The function
    ``run()`` is in fact a single
    call to launch this task manager.

    Global Variables with \__builtin_\_
    -----------------------------------

    Some key variables used in all Panda3D scripts are actually attributes of the
    ShowBase instance. Here is the relevant code making these attribute global in
    scope:

    .. code-block:: python

        __builtin__.base = self
        __builtin__.render2d = self.render2d
        __builtin__.aspect2d = self.aspect2d
        __builtin__.pixel2d = self.pixel2d
        __builtin__.render = self.render
        __builtin__.hidden = self.hidden
        __builtin__.camera = self.camera
        __builtin__.loader = self.loader
        __builtin__.taskMgr = self.taskMgr
        __builtin__.jobMgr = self.jobMgr
        __builtin__.eventMgr = self.eventMgr
        __builtin__.messenger = self.messenger
        __builtin__.bboard = self.bboard
        __builtin__.run = self.run
        __builtin__.ostream = Notify.out()
        __builtin__.directNotify = directNotify
        __builtin__.giveNotify = giveNotify
        __builtin__.globalClock = globalClock
        __builtin__.vfs = vfs
        __builtin__.cpMgr = ConfigPageManager.getGlobalPtr()
        __builtin__.cvMgr = ConfigVariableManager.getGlobalPtr()
        __builtin__.pandaSystem = PandaSystem.getGlobalPtr()
        __builtin__.wantUberdog = base.config.GetBool('want-uberdog', 1)

    This is where the commonly used objects
    ``base``,
    ``render``,
    ``render2d``,
    ``camera``,
    ``messenger``, and
    ``taskMgr`` are created. There are
    more such variables added to
    ``__builtin__``. Consult the code if
    you want to find them all.

    Note that this way of exposing these attributes make them available globally
    even though these will not be returned by a call to the built-in function
    ``dir()``.

.. only:: cpp

    This section does not apply to C++.
