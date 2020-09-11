.. _camera-control:

Camera Control
==============

Panda3D's camera is considered a :class:`.PandaNode`. It can therefore be
manipulated as any other node.

The actual camera is defined in ShowBase as a :class:`.NodePath` named
:py:obj:`base.cam <direct.showbase.ShowBase.ShowBase.cam>`.
There is also a plain node above the camera, which is a NodePath called
:py:obj:`base.camera <direct.showbase.ShowBase.ShowBase.camera>`.
Generally you want to control the latter with your code.


.. toctree::
   :maxdepth: 2

   default-camera-driver
   perspective-lenses
   orthographic-lenses
