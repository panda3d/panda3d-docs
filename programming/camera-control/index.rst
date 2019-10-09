.. _camera-control:

Camera Control
==============

Panda3D's camera is considered a PandaNode. It can therefore be manipulated as
any other node.

The actual camera is defined in ShowBase as a NodePath named
``base.cam``. There is also a plain
node above the camera, which is a NodePath called
``base.camera``. Generally you want to
control the ``base.camera`` NodePath
with your code.


.. toctree::
   :maxdepth: 2

   default-camera-driver
   perspective-lenses
   orthographic-lenses
