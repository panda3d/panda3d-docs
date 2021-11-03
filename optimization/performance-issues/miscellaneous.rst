.. _miscellaneous:

Miscellaneous
=============

This page lists a number of miscellaneous things that can possibly be a cause
of bad performance in your game.

-  You are using textures with a width or height that is not a power of two.
   This could cause Panda3D to resize the textures, which can slow your game
   down a lot. Always try to stick to powers of two when
   :ref:`choosing a Texture Size <choosing-a-texture-size>`.
-  You are printing too much to the console every frame. Printing to the
   console, especially on Windows, can cause a slow-down of your application.
   Always check your console whether its not flooded with errors or debug
   messages. You might want to consider output buffering or, on Windows, using
   pythonw (python running with windows subsystem instead of console subsystem)
   if you are experiencing this issue.
