.. _client-repositories:

Client Repositories
===================

Similar to the server repositories, client repositories are there to handle the
lower level connection code to the server. As seen earlier in the AI
Repositories chapter, client repositories doesn’t necessarily have to be on end
user machines but can also be used on servers. A basic client repository code
may look as follow or should at least implement the following set of functions
to work properly.

.. code-block:: python

   from direct.distributed.ClientRepository import ClientRepository
   from panda3d.core import URLSpec, ConfigVariableInt, ConfigVariableString
   from DGameObject import DGameObject

   class GameClientRepository(ClientRepository):

       def __init__(self):
           dcFileNames = ['direct.dc', 'yourOwnDCFile.dc']

           # a distributed object of our game.
           self.distributedObject = None
           self.aiDGameObect = None

           ClientRepository.__init__(
               self,
               dcFileNames = dcFileNames,
               threadedNet = True)

           # Set the same port as configured on the server to be able to connect
           # to it
           tcpPort = ConfigVariableInt('server-port', 4400).getValue()

           # Set the IP or hostname of the server we want to connect to
           hostname = ConfigVariableString('server-host', '127.0.0.1').getValue()

           # Build the URL from the server hostname and port. If your server
           # uses another protocol then http you should change it accordingly.
           # Make sure to pass the connectMethod to the ClientRepository.__init__
           # call too.  Available connection methods are:
           # self.CM_HTTP, self.CM_NET and self.CM_NATIVE
           self.url = URLSpec('http://{}:{}'.format(hostname, tcpPort))

           # Attempt a connection to the server
           self.connect([self.url],
                        successCallback = self.connectSuccess,
                        failureCallback = self.connectFailure)

       def lostConnection(self):
           """ This should be overridden by a derived class to handle an
           unexpectedly lost connection to the gameserver. """
           # Handle the disconnection from the server.  This can be a reconnect,
           # simply exiting the application or anything else.
           exit()

       def connectFailure(self, statusCode, statusString):
           """ Something went wrong """
           exit()

       def connectSuccess(self):
           """ Successfully connected.  But we still can't really do
           anything until we've got the doID range. """

           # Make sure we have interest in the by the AIRepository defined
           # TimeManager zone, so we always see it even if we switch to
           # another zone.
           self.setInterestZones([1])

           # We must wait for the TimeManager to be fully created and
           # synced before we can enter another zone and wait for the
           # game object.  The uniqueName is important that we get the
           # correct, our sync message from the TimeManager and not
           # accidentaly a message from another client
           self.acceptOnce(self.uniqueName('gotTimeSync'), self.syncReady)

       def syncReady(self):
           """ Now we've got the TimeManager manifested, and we're in
           sync with the server time.  Now we can enter the world.  Check
           to see if we've received our doIdBase yet. """

           # This method checks whether we actually have a valid doID range
           # to create distributed objects yet
           if self.haveCreateAuthority():
               # we already have one
               self.gotCreateReady()
           else:
               # Not yet, keep waiting a bit longer.
               self.accept(self.uniqueName('createReady'), self.gotCreateReady)

       def gotCreateReady(self):
           """ Ready to enter the world.  Expand our interest to include
           any other zones """

           # This method checks whether we actually have a valid doID range
           # to create distributed objects yet
           if not self.haveCreateAuthority():
               # Not ready yet.
               return

           # we are ready now, so ignore further createReady events
           self.ignore(self.uniqueName('createReady'))

           # Now the client is ready to create DOs and send and receive data
           # to and from the server

First of all, we need to initialize the ClientRepository. This will handle the
connection code to the server. We pass it our dc files as well as the
threadedNet parameter which will have the same affect as described in the Server
Repositories.

.. code-block:: python

   ClientRepository.__init__(
       self,
       dcFileNames = dcFileNames,
       threadedNet = True)

Having the clientRepository ready, we can try to connect to the desired server
with the connect call. Dependent on the outcome, one of the functions given to
the call will be used.

.. code-block:: python

   self.connect([self.url],
                successCallback = self.connectSuccess,
                failureCallback = self.connectFailure)

In the connectSuccess method we have to make sure that the client is interested
in the correct zones in which a time manager has been instantiated. The Time
Manager, how it will be set up and what it is used for will be shown in a later
section. For now we just expect it to exist in zone 1 on the AI Server.

As soon as the client is synced, the TimeManager will send a gotTimeSync event.
It may be encouraged to show some kind of waiting screen to the user here until
the client is fully connected to the server.

In the syncReady and gotCreateReady methods you’ll see the haveCreateAuthority
function called. This is a check to see if we are already able to create DOs and
give them a correct doId. You can create DOs earlier already, but they may have
invalid doIds then.

At the end of the gotCreateReady method you can fully use the client and create
whatever DOs you may need and add other client related logic.

At this stage, you may also want to set interest in different Zones for the
client to see server created objects placed in those specific zones.
