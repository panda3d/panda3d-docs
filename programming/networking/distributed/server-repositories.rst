.. _server-repositories:

Server Repositories
===================

The server repository manages client connections and keeps track of any
connected clients.

Due to Panda3D doing most of the heavy work, setting up this part of the server
in a basic form is very easy.

.. code-block:: python

   from direct.distributed.ServerRepository import ServerRepository
   from panda3d.core import ConfigVariableInt

   class GameServerRepository(ServerRepository):
       def __init__(self):
           tcpPort = ConfigVariableInt('server-port', 4400).getValue()
           dcFileNames = ['direct.dc', 'yourOwnDCFile.dc']
           ServerRepository.__init__(self, tcpPort, dcFileNames=dcFileNames, threadedNet=True)

As you see in the example above, we simply have to gather the port and a list
of DC files, which we will take a closer look in a later section, and pass all
of that to the :class:`.ServerRepository` constructor.

The threadedNet parameter if true, tells the underlying networking system to
use threads to listen for incoming data. It has a subtle effect on performance,
but can also occasionally cause problems.
