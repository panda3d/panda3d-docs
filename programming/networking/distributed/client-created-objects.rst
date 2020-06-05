.. _client-created-objects:

Client-Side Created Objects
===========================

After setting up a basic client and server and having them connect, the next
step is to create some objects that will get distributed over this existing
network connection.

Client-side created DirectObjects are objects that the will be created using
the :class:`.ClientRepository` on the end users client.

There are multiple ways to create a DirectObject. You can either create an
instance of a DO and pass it to the
:meth:`.ClientRepository.createDistributedObject` call of the CR instance or
simply pass its name.

For example, the following code creates a DGameObject which inherited from
DistributedObject.

.. code-block:: python

   distributedObject = DGameObject()
   cr.createDistributedObject(
       distObj = distributedObject,
       zoneId = 2)

This example creates a DGameObject only from the name as defined in the DC
definition files.

.. code-block:: python

   self.gameDistObject = self.createDistributedObject(
       className = 'DGameObject',
       zoneId = 2)

As you have seen we’ve set the zoneId to 2. This tells the object to live in
this specific zone and all clients that have defined an interest in this zone
with :meth:`.ClientRepository.setInterestZones()` will automatically “see” this
object.

Further details about distributed objects and their usage will be shown in
later sections.
