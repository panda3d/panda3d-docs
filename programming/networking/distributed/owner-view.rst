.. _owner-view:

Owner view
==========

.. note::
   Currently this type of object is not directly available in Panda3D. It is
   implemented in the former prject developed by Disney and can also be used
   with available open source extensions like the Astron suite.

Owner view (OV) objects are special implementations for DOs that are created and
used on the clients. OVs are very similar to AIs in that they handle game logic
but instead of being implemented on the server, they are introduced on the
client side. That way clients can directly update fields in these objects.
To do so, the respective calls must be marked with the ownsend tag in the dc
definition file.
