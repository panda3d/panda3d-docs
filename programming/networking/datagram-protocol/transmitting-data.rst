.. _transmitting-data:

Transmitting Data
=================

Once a connection has been established, data can be transmitted from one Panda
program to another using the classes described in this section. Communication
can happen in both directions (i.e. client-to-server or server-to-client);
once the connection has been established, either side may send messages along
the connection to the other side.

This section describes message passing in detail, first transmission, then
receipt of a message.

Sending a message
-----------------

To send a message along an established connection, the sender must first
construct a PyDatagram containing the message. This involves instantiating a
PyDatagram object and then populating its contents with the desired data. The
type of the data is determined by the functions used to pack it; see the full
documentation of the PyDatagram class for more details.

.. code-block:: python

   # Developer-defined constants, telling the server what to do.
   # Your style of how to store this information may differ; this is
   # only one way to tackle the problem
   PRINT_MESSAGE = 1

   def myNewPyDatagram(self):
       # Send a test message
       myPyDatagram = PyDatagram()
       myPyDatagram.addUint8(PRINT_MESSAGE)
       myPyDatagram.addString("Hello, world!")
       return myPyDatagram

As shown in the previous section, once the datagram is constructed you may then
send it using a ConnectionWriter.

.. code-block:: python

   cWriter.send(myPyDatagram, aConnection)

Receiving a message
-------------------

As shown in the previous section, when a message is received via a
QueuedConnectionReader, it can be retrieved into a NetDatagram:

.. code-block:: python

   datagram = NetDatagram()
   if cReader.getData(datagram):
       myProcessDataFunction(datagram)

A NetDatagram contains the original information that was stored in the
transmitted PyDatagram. It also contains knowledge of the connection over which
it was received and the address of the connection. To retrieve the connection,
use the getConnection method:

.. code-block:: python

   sourceOfMessage = datagram.getConnection()

To retrieve the contents of the message, use the PyDatagramIterator. The
iterator class acts as the complement of the PyDatagram class; its methods can
be used to retrieve the content that was encoded using PyDatagram.

.. code-block:: python

   def myProcessDataFunction(netDatagram):
       myIterator = PyDatagramIterator(netDatagram)
       msgID = myIterator.getUint8()
       if msgID == PRINT_MESSAGE:
           messageToPrint = myIterator.getString()
           print(messageToPrint)

.. note::

   It is assumed that the message recipient will retrieve the same type of
   content in the same order that the message sender packed the content. No
   mechanism exists in the PyDatagramIterator to ensure that the data being
   unpacked matches the requested type. Unpacking the data using a different
   type function will probably result in unexpected behavior.
