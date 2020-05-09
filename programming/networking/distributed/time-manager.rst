.. _time-manager:

Time Manager
============

A very specific Distributed Object which usually resides on the AI Server is the
time manager. This object, when created is also propagated to the clients if
they define interest in the specific zone the manager has been created in.

Clients may also simply access the time manager from the timeManager variable
defined in the CR when it has been created on the AI.

To create a Time Manager instance simply do the same as you’d do to create a DO.

.. code-block:: python

   self.timeManager = self.createDistributedObject(
       className = 'TimeManagerAI',
       zoneId = 1)
