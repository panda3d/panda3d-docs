.. _softbodies:

Bullet Softbodies
=================

Soft bodies are similar to rigid bodies, just they are not rigid but soft.
This means that the shape of a soft body can change - they are deformable.
Bullet is capable of simulating soft body deformation in real-time. This is
not to be confused with playback of animation. Animation are computed up in
front, usually not in real-time, and then saved to a file.

Bullet simulates soft bodies internally by making up a complex compound
objects, consisting of nodes and links. The nodes can be best compared to the
vertices of a mesh used to render 3D geometry. The links can be visualized as
springs in between the nodes; just that this kind of spring not only responds
to compression, but also to bending.

Depending on how the nodes and links are arranged it is possible to create
three different kinds of soft bodies:

-  A one dimensional chain of nodes, called a **rope**. Each node has two
   links, one to the previous node, and one to the next node. The only
   exception are the first node and the last node - they have only one link.
-  A two dimensional mesh of nodes, called a **patch**. The two dimensional
   mesh can be closed, e. g. the surface of a sphere. In this case Bullet can
   also assume the volume inside the closed surface mesh should be contained,
   more or less depending on the setting for the pressure inside the soft
   body. Typical uses for this kind of soft body are a flag or cloth, or if
   the soft body is closed an air-filled tire.
-  Finally a three dimensional mesh made up from **tetrahedrons**. For this
   kind of soft body a surface mesh is not enough. The whole volume of the
   body has to be composed from small tetrahedrons.


All three kinds of soft bodies are simulated using the same class,
:class:`.BulletSoftBodyNode`. It's just a matter of how the links between the
nodes are created.

Panda3D currently provides no low-level interface for creating and modifying
the soft body nodes and links directly. Soft bodies are created using factory
methods which simplify the process for you.

Warning: Bullet soft body support within Panda3D is at an early stage. Use it
with care. It is also highly recommended to keep the original Bullet
documentation close at hand, in order to find the right values e. g. for
cluster or collision configuration.
