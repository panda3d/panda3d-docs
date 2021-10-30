.. _datagram-protocol:

Datagram Protocol
=================

Underpinning Panda's networking capabilities are the classes that compose the
datagram protocol. These classes allow for developer-defined packets to be
transmitted using either the UDP or TCP protocols. Panda's datagram layer can
serve as a solid foundation for developing higher-level networking
abstractions.

This section describes the classes used to establish a connection
(:class:`.QueuedConnectionManager`, :class:`.QueuedConnectionListener`,
:class:`.QueuedConnectionReader`, and :class:`.ConnectionWriter`), as well as
the classes that transmit information (:class:`.NetDatagram`, :class:`.PyDatagram`,
and :class:`.PyDatagramIterator`).


.. toctree::
   :maxdepth: 2

   client-server-connection
   transmitting-data
