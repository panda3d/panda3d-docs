.. _event-handlers:

Event Handlers
==============

.. only:: cpp

   .. note:: This page has not yet been updated to cover the C++ event API.

Events occur either when the user does something (such as clicking a
:ref:`mouse <mouse-support>` or pressing a :ref:`key <keyboard-support>`) or
when sent by the script using
:py:func:`messenger.send() <direct.showbase.Messenger.Messenger.send>`.
When an event occurs, Panda's "messenger" will check to see if you have written
an "event handler" routine. If so, your event handler will be called. The
messenger system is object-oriented, to create an event handler, you have to
first create a class that inherits from DirectObject. Your event handler will be
a method of your class.

Defining a class that can Handle Events
---------------------------------------

The first step is to import the :py:mod:`~direct.showbase.DirectObject` module:

.. code-block:: python

   from direct.showbase import DirectObject

With DirectObject loaded, it is possible to create a subclass of DirectObject.
This allows the class to inherit the messaging API and thus listen for events.

.. code-block:: python

   class myClassName(DirectObject.DirectObject):

The sample below creates a class that can listen for events. The "accept"
function notifies panda that the printHello method is an event handler for the
mouse1 event. The "accept" function and the various event names will be
explained in detail later.

.. code-block:: python

   class Hello(DirectObject.DirectObject):
       def __init__(self):
           self.accept('mouse1', self.printHello)

       def printHello(self):
           print('Hello!')

   h = Hello()

Event Handling Functions
------------------------

Events first go to a mechanism built into panda called the "Messenger." The
messenger may accept or ignore events that it receives. If it accepts an event,
then an event handler will be called. If ignored, then no handler will be
called.

An object may accept an event an infinite number of times or accept it only
once. If checking for an accept within the object listening to it, it should be
prefixed with self. If the accept command occurs outside the class, then the
variable the class is associated with should be used.

.. code-block:: python

   myDirectObject.accept('Event Name', myDirectObjectMethod)
   myDirectObject.acceptOnce('Event Name', myDirectObjectMethod)

Specific events may be ignored, so that no message is sent. Also, all events
coming from an object may be ignored.

.. code-block:: python

   myDirectObject.ignore('Event Name')
   myDirectObject.ignoreAll()

Finally, there are some useful utility functions for debugging. The messenger
typically does not print out when every event occurs. Toggling verbose mode will
make the messenger print every event it receives. Toggling it again will revert
it to the default. A number of methods exist for checking to see what object is
checking for what event, but the print method will show who is accepting each
event. Also, if accepts keep changing to the point where it is too confusing,
the clear method will start the messenger over with a clear dictionary.

.. code-block:: python

   messenger.toggleVerbose()
   print(messenger)
   messenger.clear()

Sending Custom Events
---------------------

Custom events can be sent by the script using the code

.. code-block:: python

   messenger.send('Event Name')

A list of parameters can optionally be sent to the event handler. Parameters
defined in ``accept()`` are passed first, and then the parameters defined in
``send()``. for example this would print out "eggs sausage foo bar":

.. code-block:: python

   class Test(DirectObject):
       def __init__(self):
           self.accept('spam', self.on_spam, ['eggs', 'sausage'])

       def on_spam(self, a, b, c, d):
           print(a, b, c, d)

   test = Test()
   messenger.send('spam', ['foo', 'bar'])
   base.run()

A Note on Object Management
---------------------------

When a DirectObject accepts an event, the messenger retains a reference to that
DirectObject. To ensure that objects that are no longer needed are properly
disposed of, they must ignore any messages they are accepting.

For example, the following code may not do what you expect:

.. code-block:: python

   import direct.directbase.DirectStart
   from direct.showbase import DirectObject
   from panda3d.core import *

   class Test(DirectObject.DirectObject):
       def __init__(self):
           self.accept("FireZeMissiles", self._fireMissiles)

       def _fireMissiles(self):
           print("Missiles fired! Oh noes!")

   foo = Test() # create our test object
   del foo      # get rid of our test object

   messenger.send("FireZeMissiles") # oops! Why did those missiles fire?
   base.run()

Try the example above, and you'll find that the missiles fire even though the
object that would handle the event had been deleted.

One solution (patterned after other parts of the Panda3D architecture) is to
define a "destroy" method for any custom classes you create, which calls
"ignoreAll" to unregister from the event-handler system.

.. code-block:: python

   import direct.directbase.DirectStart
   from direct.showbase import DirectObject
   from panda3d.core import *

   class Test(DirectObject.DirectObject):
       def __init__(self):
           self.accept("FireZeMissiles", self._fireMissiles)

       def _fireMissiles(self):
           print("Missiles fired! Oh noes!")

       # function to get rid of me
       def destroy(self):
           self.ignoreAll()

   foo = Test()  # create our test object
   foo.destroy() # get rid of our test object

   del foo

   messenger.send("FireZeMissiles") # No missiles fire
   base.run()

Coroutine Event Handlers
------------------------

It is permissible for any event handler to be a :term:`coroutine` (i.e. marked
as an ``async def``), which permits use of the ``await`` keyword inside the
handler. Usage is otherwise identical to a regular event handler.

.. code-block:: python

   class Test(DirectObject):
       def __init__(self):
           self.accept('space', self.on_space)

       async def on_space(self):
           await Task.pause(1.0)
           print("The space key was pressed one second ago!")
