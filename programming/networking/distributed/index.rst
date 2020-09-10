.. _distributed-networking:

Distributed Networking
======================

Distributed Networking is Panda3D's high-level network API. When a distributed
object is created all interested clients will automatically create a copy of
that object. Updates to the object will automatically propagate to the copies.

The distributed network is composed of several layers: the dc file which
defines the communication, ServerRepositories which handle communication
between clients, ClientRepositories which interact and manage the distributed
objects, and the distributed objects themselves.

Several abbreviations will be used in the following pages that you may come
across when using the system. To not repeat them every time or for you to look
up whenever you stumble upon one, we'll list them here.

.. glossary::

   DO
      Distributed Object, see :ref:`distributed-object`.

   DOG
      Distributed Object Global

   doId
      Distributed Object Identifier

   AI
      Artificial Intelligence

   UD
      Uber DOG, see :ref:`uber-dogs`.

   OV
      Owner View, see :ref:`owner-view`.

   DC
      Distributed Class, see :ref:`dc-definition-files`.

   SR
      Server Repository, see :ref:`server-repositories`.

   CR
      Client Repository, see :ref:`client-repositories`.

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2

   servers
   server-repositories
   ai-repositories
   clients
   client-repositories
   dc-definition-files
   client-created-objects
   ai-created-objects
   uber-dogs
   owner-view
   time-manager
   related-object-manager
   distributed-object
   distributed-node
   distributed-smooth-node
