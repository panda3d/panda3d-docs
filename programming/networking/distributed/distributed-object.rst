.. _distributed-object:

Distributed Objects
===================

DistributedObjects are the base for all things that should be managed over the
distributed network. This may include players, level objects, the level itself,
a message object for chat messages and really anything else in the application
world.

As seen in earlier sections, they can be created on the client repositories and,
when created, they will automatically be distributed to other clients.

To define who will see :term:`DOs <DO>`, they can be set in specific zones.
Zones are just numbers that have to be set on a :term:`DO` and a client needs to
show interest in them to be able to see objects in them.
In addition, objects that a client doesn't own can't be updated by that client.
Only the object's owner can change fields in it, except if they are specially
marked with the ``clsend`` keyword in the DC definition file.

Most DOs will have a basic class definition (eg. "Foo") and an AI definition
which would be called "FooAI".  The Foo class will be used on clients and the
FooAI class will be generated on the AI servers.

An example of a distributed object class implementation may look like the
following:

Client-side DGameObject.py:

.. code-block:: python

   from direct.distributed.DistributedObject import DistributedObject

   class DGameObject(DistributedObject):
       def __init__(self, cr):
           DistributedObject.__init__(self, cr)

       def d_sendGameData(self):
           """ A method to send an update message to the server.  The d_ stands
           for distributed """

           # send the message to the server
           self.sendUpdate('sendGameData', [('ValueA', 123, 1.25)])

AI Server side DGameObjectAI.py

.. code-block:: python

   from direct.distributed.DistributedObjectAI import DistributedObjectAI

   class DGameObjectAI(DistributedObjectAI):
       def __init__(self, aiRepository):
           DistributedObjectAI.__init__(self, aiRepository)

       def sendGameData(self, data):
           """ Method that can be called from the clients with an sendUpdate call """
           print(data)

Here we see that a new object derives from :class:`.DistributedObject` and
:class:`.DistributedObjectAI` respectively. Usually those classes will be filled
with methods that follow the form of foo, d_foo and b_foo.

The foo method is the one that will have an effect locally.

The d_foo (d\_ stands for distributed) method will send a message to the server
and hence to other clients as needed and will update them. As you see, you can
simply send data to the server with a self.sendUpdate call.
There is also another method called
:meth:`.DistributedObjectAI.sendUpdateToAvatarId` which accepts a :term:`doId`
of a client and will send the message directly to it. This method is only
available on the :term:`AI` and :term:`UD` side.

the b_foo (b\_ stands for both) method will update both, the local object as
well as send the data to the server. This can usually easily be achieved by
simply calling both, the foo and d_foo method within the b_foo method.

Special Methods
---------------

Aside of your own methods for sending and receiving messages between the
client and server-side objects, there are some methods worth knowing which are
implemented by the :class:`.DistributedObject` class. Those methods will usually
be overwritten when creating a distributed object class and fitted to your own
needs.

:meth:`~.DistributedObject.announceGenerate`: This method will be called as soon as the object has
been manifested. On the client side, you may want to use this for AI-created
objects. For example:

.. code-block:: python

   def announceGenerate(self):

       base.messenger.send(self.cr.uniqueName('myObject-generated'), [self.doId])

       # call the base class method
       DistributedObject.announceGenerate(self)

:meth:`~.DistributedObject.disable`: This method will be called when the object gets disabled. This
usually comes prior to a delete call.

:meth:`~.DistributedObject.delete`: This method is called whenever a DO gets deleted. For example
if the client who created it has left the zone or server. DOs should implement
cleanup code here.

:meth:`~.DistributedObject.generate`: This method is called at generation time of the DO.
