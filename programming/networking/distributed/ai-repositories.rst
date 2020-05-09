.. _ai-repositories:

AI Server
=========

AI Servers are to be specific, clients that reside on a server rather then on
the end users client machines. An AI Server or usually called AI Repository is
used to create distributed objects which are usually used to handle game logic
that should not be run by end user clients.

In networked games, most of the games logic should be handled by the server
side. Clients shouldn’t be trusted as it’s not possible to ensure that they
haven’t been compromised in one way or another.

Similar to the Server Repositories, for AI Repositories most of the low-level
networking code is neatly hidden by Panda3D which makes setting up a basic AI
server rather simple too. Though rather than having a dedicated AIRepository
class, we have to use the ClientRepository as, as stated before, the AI
Repository is nothing else than a client.

.. code-block:: python

   ClientRepository.__init__(
       self,
       dcFileNames = dcFileNames,
       dcSuffix = 'AI',
       threadedNet = True)

The setup is quite similar to the one of a normal client repository which we
will take a look at in the next sections. The main difference is, that for an AI
Repository we pass the dcSuffix = ‘AI’ to the ClientRepository initialization.
This makes sure that the correct definitions of the DC definition file will be
used. Another method that should be specifically defined in an AI Repository is
the following.

.. code-block:: python

   def deallocateChannel(self, doID):
       print("Client left us: ", doID)

This function will be called, whenever a client has disconnected and gives us the chance to react to it’s disconnection.
