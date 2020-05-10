.. _distributed-boject:

Distributed Objects
===================

Distributed Objects are the base for all things that should be managed over the
distributed network. May it be players, level objects, the level itself, a
message object for chat messages and really anything else in the application
world.

As seen in earlier sections, they can be created on the client repositories and,
when created, they will automatically be distributed to other clients.

To define who will see DOs, they can be set in specific zones. Zones are just
numbers that have to be set on a DO and a client needs to show interest in them
to be able to see objects in them.

Most DOs will have a basic class definition for example Foo and an AI definition
which can be called FooAI.

The Foo class will be used on clients and the FooAI class will be generated on
the AI servers.

An example Distributed Object class may look like the following:

Client side DGameObject.py:

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

Here we see that a new object derives from DistributedObject and
DistributedObjectAI respectively. Usually those classes will be filled with
methods that follow the form of foo, d_foo and b_foo.

The foo method is the one that will have an affect locally.

The d_foo (d\_ stands for distributed) method will send a message to the server
and hence to other clients as needed and will update them. As you see, you can
simply send data to the server with a self.sendUpdate call.
There is also another method called sendUpdateToAvatarId which accepts a doId
of another client and will send the message directly to it.

the b_foo (b\_ stands for both) method will update both, the local object as well
as send the data to the server. This can usually easily be achived by simply
calling both, the foo and d_foo method within the b_foo method.
