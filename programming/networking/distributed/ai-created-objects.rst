.. _ai-created-objects:

AI-side Created Objects
=======================

Similar to the client-side created objects, AI server-side created objects will
be created and managed on the AI server. The difference is that the classes
with the AI suffix will be used to create the DistributedObject. The respective
class without the AI suffix will be created on clients that stated
with the AI appending will usually be used for creation and hence the AI
functionality of those nodes can be accessed. Those objects will also be
distributed to the clients.

An example for creating an AI object directly on the AI server follows.

.. code-block:: python

   self.gameDistObjectAI = self.createDistributedObject(
       className = 'DGameObjectAI',
       zoneId = 2)

For a client to know when such an object has been manifested locally, the
distributed object class (without the AI postfix) can overwrite the
:meth:`~direct.distributed.DistributedObject.DistributedObject.announceGenerate()` method
of :class:`.DistributedObject`. This method is called whenever the object has been
created and is ready for further processing on the client. In this method, you
can for example send the :term:`doId` with a custom event or simply store some
information in the client repository to later ease the access to those objects.
