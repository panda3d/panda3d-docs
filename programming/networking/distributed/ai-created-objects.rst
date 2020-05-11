.. _ai-created-objects:

AI Side Created Objects
=======================

Similar to the client-side created objects, AI server-side created objects will
be created and managed on the AI server. The difference here is that the DOs
with the AI appending will usually be used for creation and hence the AI
functionality of those nodes can be accessed. Those objects will also be
distributed to the clients. As clients don’t know the ids of those objects, a
method can be used to create an initial broadcast call to let the clients know
the AI side created object has correctly manifested.
