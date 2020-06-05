.. _distributed-smooth-node:

Distributed Smooth Node
=======================

A more sophisticated DO is the :class:`.DistributedSmoothNode`. This class will
handle moved objects like players in a distributed environment. It ensures that
the created node will move smoothly from one point to the next when moved on
the client.

This DO can be used if the repository has been initialized with the direct.dc
added to the dc files list.
