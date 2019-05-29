.. _distributed-networking:

Distributed Networking
======================

Distributed Networking is Panda3D's high level network API. When a distributed
object is created all interested clients will automatically create a copy of
that object. Updates to the object will automatically propagate to the copies.

The distributed network is composed of several layers: the dc file which
defines the communication, ServerRepositories which handle inter client
communication, ClientRepositories which interact and manage the distributed
objects, and the distributed objects themselves.

The documentation on these features is still in development. Read the forums
for the most up-to-date information.
