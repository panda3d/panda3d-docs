.. _related-object-manager:

Related Object Manager
======================

The related object manager is a handy class that can be utilized to wait for the
creation of multiple DOs. You simply pass the IDs of the objects you want to
wait for as a list and a callback method. If all objects are successfully
created, the callback method will be called.
This manager is readily available in repository based classes like the
Client Repository.


.. code-block:: python

   # Use the client repositories manager
   cr.relatedObjectMgr.requestObjects(
       [
        playerDoId,
        levelDoId,
        someOtherObjectDoId
       ],
       allCallback = self.allObjectsManifested)

   def allObjectsManifested(self, allObjects):
       # allObjects now contains the DOs for the player, level
       # and someOtherObject
