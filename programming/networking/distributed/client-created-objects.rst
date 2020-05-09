.. _client-created-objects:

Client Side Created Objects
===========================

After setting up a basic client and server and having them connect, the next
step is to create some Objects that will get distributed on this existing
network connection.

Client side created DOs are DOs that the will be created using the
ClientRepository on the end users client.

To create a DO there are multiple ways to do so. You can either create an
instance of a DO and pass it to the create createDistributedObject call of the
CR instance or simply pass its name.

Example1, create a DGameObject which inherited from DistributedObject.

.. code-block:: python

   distributedObject = DGameObject()
   cr.createDistributedObject(
       distObj = distributedObject,
       zoneId = 2)

Example2, create a DGameObject only from the name as defined in the
DC definition files.

.. code-block:: python

   self.gameDistObject = self.createDistributedObject(
       className = 'DGameObject',
       zoneId = 2)

As you have seen we’ve set the zonId to 2. This tells the object to live in this
specific zone and all clients that have defined an interest in this zone will
automatically “see” this object.

Further details about Distributed Objects and their usage will be shown in a
later section.
