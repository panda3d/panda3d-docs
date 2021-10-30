.. _client-server-connection:

Client-Server Connection
========================

The first step in network communication is to establish the client-server
connection. This entails two sets of operations: one for the server side
(which listens for incoming connections), and one for the client side (which
establishes a connection to the server). Both of these processes are described
below.

Preparing the server for connection
-----------------------------------

An average Panda program acting as a server will need to create four classes:

-  A :class:`.QueuedConnectionManager`, which handles the low-level connection
   processes, establishes connections, and handles unexpected network
   termination

-  A :class:`.QueuedConnectionListener`, which waits for clients to request a
   connection

-  A :class:`.QueuedConnectionReader`, which buffers incoming data from an
   active connection

-  A :class:`.ConnectionWriter`, which allows PyDatagrams to be transmitted out
   along an active connection

The first step is to instantiate these four classes.

.. code-block:: python

   from panda3d.core import QueuedConnectionManager
   from panda3d.core import QueuedConnectionListener
   from panda3d.core import QueuedConnectionReader
   from panda3d.core import ConnectionWriter

   cManager = QueuedConnectionManager()
   cListener = QueuedConnectionListener(cManager, 0)
   cReader = QueuedConnectionReader(cManager, 0)
   cWriter = ConnectionWriter(cManager, 0)

   activeConnections = [] # We'll want to keep track of these later

This method of instantiation prepares the classes in single-thread mode, which
that realtime communication requires them to be polled periodically.

To accept client connections, the server opens a special "rendezvous" socket at
a specific port address. This port address must be known by both the client and
the server. Additionally, a backlog is specified; this is the number of incoming
connection requests that the connection will track before it starts rejecting
connection attempts. The responsibility for managing the rendezvous socket is
passed to the QueuedConnectionListener, and a task is spawned to periodically
poll the listener.

.. code-block:: python

   port_address = 9099 #No-other TCP/IP services are using this port
   backlog = 1000 #If we ignore 1,000 connection attempts, something is wrong!
   tcpSocket = cManager.openTCPServerRendezvous(port_address,backlog)

   cListener.addConnection(tcpSocket)

Since the network handlers we instantiated are polled, we'll create some tasks
to do the polling.

.. code-block:: python

   taskMgr.add(tskListenerPolling, "Poll the connection listener", -39)
   taskMgr.add(tskReaderPolling, "Poll the connection reader", -40)

When a connection comes in, the tskListenerPolling function below handles the
incoming connection and hands it to the QueuedConnectionReader. The connection
is now established.

.. code-block:: python

   from panda3d.core import PointerToConnection
   from panda3d.core import NetAddress

   def tskListenerPolling(taskdata):
       if cListener.newConnectionAvailable():

           rendezvous = PointerToConnection()
           netAddress = NetAddress()
           newConnection = PointerToConnection()

           if cListener.getNewConnection(rendezvous,netAddress,newConnection):
               newConnection = newConnection.p()
               activeConnections.append(newConnection) # Remember connection
               cReader.addConnection(newConnection)     # Begin reading connection
       return Task.cont

Once a connection has been opened, the QueuedConnectionReader may begin
processing incoming packets. This is similar to the flow of the listener's task,
but it is up to the server code to handle the incoming data.

.. code-block:: python

   from panda3d.core import NetDatagram

   def tskReaderPolling(taskdata):
       if cReader.dataAvailable():
           datagram = NetDatagram()  # catch the incoming data in this instance
           # Check the return value; if we were threaded, someone else could have
           # snagged this data before we did
           if cReader.getData(datagram):
               myProcessDataFunction(datagram)
       return Task.cont

Note that the QueuedConnectionReader retrieves data from all clients connected
to the server. The NetDatagram can be queried using NetDatagram.getConnection to
determine which client sent the message.

If the server wishes to send data to the client, it can use the ConnectionWriter
to transmit back along the connection.

.. code-block:: python

   # broadcast a message to all clients
   myPyDatagram = myNewPyDatagram()  # build a datagram to send
   for aClient in activeConnections:
       cWriter.send(myPyDatagram,aClient)

Finally, the server may terminate a connection by removing it from the
QueuedConnectionReader's responsibility. It may also deactivate its listener so
that no more connections are received.

.. code-block:: python

   # terminate connection to all clients

   for aClient in activeConnections:
       cReader.removeConnection(aClient)
   activeConnections = []

   # close down our listener
   cManager.closeConnection(tcpSocket)

Connecting with a client
------------------------

The process the client undertakes to connect to a server is extremely similar to
the process the server undertakes to receive connections. Like the server, a
client instantiates a QueuedConnectionManager, QueuedConnectionReader, and
ConnectionWriter. However, there are some differences in the process. In
general, a client has no need to open a rendezvous socket or create a
QueuedConnectionListener, since it will be doing the connecting itself. Instead,
the client connects to a specific server by specifying the server's IP address
and the correct socket ID.

.. code-block:: python

   port_address = 9099  # same for client and server

   # A valid server URL. You can also use a DNS name
   # if the server has one, such as "localhost" or "panda3d.org"
   ip_address = "192.168.0.50"

   # How long, in milliseconds, until we give up trying to reach the server?
   timeout = 3000  # 3 seconds

   myConnection = cManager.openTCPClientConnection(ip_address, port_address, timeout)
   if myConnection:
       cReader.addConnection(myConnection)  # receive messages from server

When the client has finished communicating with the server, it can close the
connection.

.. code-block:: python

   cManager.closeConnection(myConnection)
