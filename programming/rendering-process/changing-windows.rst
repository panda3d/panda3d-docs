.. _changing-windows:

Changing Windows
============================

The ``WindowProperties`` class can be used to alter the behavior of existing windows. If "base" is your showbase instance, change properties of your window like this:
        
.. only:: python

   .. code-block:: python
        from panda3d.core import WindowProperties
        # ...
        wp = WindowProperties()
        wp.setSize(1920),1080)
        wp.setFullscreen(True)
        wp.setTitle("My Awesome Game")
        base.win.requestProperties(wp)

The API for lists ``WindowProperties`` some other functions for common operations, so if you are doing this, it is worth browsing what is available.
