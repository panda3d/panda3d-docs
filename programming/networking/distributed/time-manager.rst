.. _time-manager:

Time Manager
============

A very specific distributed object which usually resides on the AI server is
the :class:`.TimeManager`. This object, when created is also propagated to the
clients if they define interest in the specific zone the manager has been
created in.

Clients may also simply access the time manager from the timeManager variable
defined in the CR when it has been created on the AI and the client has stated
interest in the zone the time manager lives in.

To make the time manager available from the AI server, create a
:class:`.TimeManagerAI` instance. Simply do the same as you’d do to create a
DirectObject.

.. code-block:: python

   self.timeManager = self.createDistributedObject(
       className = 'TimeManagerAI',
       zoneId = 1)
