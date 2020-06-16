.. _distributed-smooth-node:

Distributed Smooth Node
=======================

A more sophisticated DO is the :class:`.DistributedSmoothNode`. This class will
handle moved objects like players in a distributed environment. It ensures that
the created node will move smoothly from one point to the next when moved on
the client.

This DO can be used if the repository has been initialized with the direct.dc
added to the dc files list.

To make use of the smoothing functionality and automatic broadcasting of
position and rotation changes to other players, a few functions have to be
called.

:meth:`.DistributedSmoothNode.activateSmoothing(smoothing, prediction)`

The activateSmoothing method will tell the instance of the SmoothNode to
enable or disable smoothing of the movement on other connected clients. They
will see the player move rather seamlessly instead of a choppy placement every
few frames, dependent on how fast the network connection is. Though, even if
they move smoothly, they may lag behind by some amount. Therefore, the
prediction flag can be set. If predictive smoothing is on, the nodes will be
drawn as nearly as possible in their current position, by extrapolating from old
position reports.

:meth:`.DistributedSmoothNode.startSmooth()`

After activating the smoothing, it also has to be started. With this call the
underlying task that will handle the logic is run. Note though, while the task
is running, you won't be able to lerp the node or directly position it, as it
would be overwritten by the update task.


To stop the task that will update the smooth positioning every frame, simply
call the following method.

:meth:`.DistributedSmoothNode.stopSmooth()`


:meth:`.DistributedSmoothNode.startPosHprBroadcast(period=.2, stagger=0, type=None)`

Finally, having all that set and done, one last call is needed to propagate the
location and rotation of the node. While the other methods handle the local
smoothing on the other connected clients, the startPosHprBroadcast method will
handle the distribution of the transformations from the source node to the
connected target clients.
