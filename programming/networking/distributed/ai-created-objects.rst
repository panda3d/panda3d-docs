.. _ai-created-objects:

AI Side Created Objects
=======================

Similar to the client-side created objects, AI server-side created objects will
be created and managed on the AI server. The difference here is that the DOs
with the AI appending will usually be used for creation and hence the AI
functionality of those nodes can be accessed. Those objects will also be
distributed to the clients.

Example for creating an AI object directly on the AI server

.. code-block:: python

   self.gameDistObjectAI = self.createDistributedObject(
       className = 'DGameObjectAI',
       zoneId = 2)

For a client to know when such an object has been manifested locally, the
distributed object class (without the AI postfix) can overwrite the
:meth:`.announceGenerate()` method of :class:`.DirectObject`. This method is
called whenever the object has been created and is ready for further processing
on the client. In this method, you can for example send the doId with a custom
event or simply store some information in the client repository to later ease
the access to those objects.
