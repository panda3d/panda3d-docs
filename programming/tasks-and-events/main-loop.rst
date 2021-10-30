.. _main-loop:

Main Loop
=========

A typical form of a Panda program might look like:

.. code-block:: python

   from direct.showbase.DirectObject import DirectObject # To listen for Events

   class World(DirectObject):
       def __init__(self):
           #initialize instance self. variables here

       def method1():
           # Panda source goes here

   w = World()
   base.run() # main loop

:py:meth:`~direct.showbase.ShowBase.ShowBase.run()` is a function that never
returns. It is the main loop.

For an alternative, ``run()`` could not be called at all. Panda doesn't really
need to own the main loop.  Instead, ``taskMgr.step()`` can be called
intermittently, which will run through one iteration of Panda's loop. In fact,
``run()`` is basically just an infinite loop that calls ``taskMgr.step()``
repeatedly.

``taskMgr.step()`` must be called quickly enough after the previous call to
``taskMgr.step()``. This must be done quick enough to be faster than the frame
rate.

This may useful when an imported third party python module that also has its own
event loop wants and wants to be in control of program flow. A third party
example may be Twisted, the event-driven networking framework.

The solution to this problem is to let Panda3D's loop be controlled entirely by
twisted's event loop. You will need to use the LoopingCall method to add Panda's
``taskMgr.step()`` method to twisted's event loop. Then, you need to call
``reactor.run()`` instead of Panda3D's ``run()`` method to run twisted's event
loop. Here's an example on how this will work:

.. code-block:: python

   from twisted.internet.task import LoopingCall
   from twisted.internet import reactor

   LoopingCall(taskMgr.step).start(1 / Desired_FPS)
   reactor.run()

You will need to replace Desired_FPS by the desired framerate, that is, how many
times you want Panda3D to redraw the frame per second. Please note that
``reactor.run()`` is blocking, just like Panda's run() method.

Another third party example is wxPython GUI, that is a blending of the wxWidgets
C++ class library with the Python programming language. Panda's ``run()``
function, and wx's ``app.MainLoop()`` method, both are designed to handle all
events and never return. They are each supposed to serve as the one main loop of
the application. Two main loops can not effectively run an application.

wxPython also supplies a method that can be called occasionally, instead of a
function that never returns. In wx's case, it's ``app.Dispatch()``.

A choice can be made whether or not to make wx handle the main loop, and call
``taskMgr.step()`` intermittently, or whether or not to make Panda handle the
main loop, and call ``app.Dispatch()`` intermittently. The better performance
choice is to have Panda handle the main loop.

In the case that Panda handles the main loop, a task needs to be started to call
``app.Dispatch()`` every frame, if needed. Instead of calling wxPython's
``app.MainLoop()``, do something like the following:

.. code-block:: python

   app = wx.App(0)

   def handleWxEvents(task):
       while app.Pending():
           app.Dispatch()

       return Task.cont

   taskMgr.add(handleWxEvents, 'handleWxEvents')
   base.run()  # Panda handles the main loop

In the case that wxPython handles the main loop using ``app.MainLoop()``, to
keep the framerate quick and reduce the CPU, add ``sleep(0.001)`` in the body of
the program. This will yield to Panda. After the sleep is over, control will
return to wxPython. wxPython can then check for user events. wxPython's user
generated callback events are generally generated only at infrequent intervals
(based on when the user is interacting with the window). This is appropriate for
a 2-D application that is completely response-driven, but not very useful for a
3-D application that continues to be active even when a user is not interacting
with it.
