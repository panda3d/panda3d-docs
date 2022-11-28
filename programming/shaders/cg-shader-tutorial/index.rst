.. _cg-shader-tutorial:

Cg Shader Tutorial
==================

.. caution::

   Support for Cg shaders will be deprecated in an upcoming version of Panda3D.

Cg Shader Tutorials
-------------------

Panda has the ability to process shaders written in the Cg shader language. In
this tutorial series, you will learn how to write shaders for Panda3D in Cg.
While there are panda specific things in this tutorial you should be able to
learn how to write Cg shaders that can be used in other engines.

Pre-requisites
--------------

You should be able to write a simple math program in C. Do not underestimate
this. If you start writing your own shaders without any prior knowledge about a
C-like language it is as hard as starting to write a Panda3D application without
knowing anything about Python. Some resources you might want to look at:

-  `C Programming Wikibook <https://en.wikibooks.org/wiki/C_Programming>`__

You should have a solid grasp of Panda basics. Read
:ref:`the hello world <tutorial>` tutorial and understand the "Solar System"
sample that comes with the Panda3D distribution. You should also have a good
understanding of how the :ref:`scene graph <the-scene-graph>` works. If you're
interested in writing a shadow mapping shader, it helps to have a solid
understanding of how the :ref:`depth buffer <depth-test-and-depth-write>` works.

Read the first chapter from
`NVIDIA's Cg Tutorial <https://developer.download.nvidia.com/CgTutorial/cg_tutorial_chapter01.html>`__.
You do not have to understand it fully, but at least you know who invented Cg
and what it is for. The `NVIDIA <https://developer.nvidia.com>`__ and
`ATI <https://developer.amd.com>`__ developer sites also have plenty of useful
information about shaders.

You should also have the
:ref:`List of Possible Shader Inputs <list-of-possible-cg-shader-inputs>` page
handy.

Tutorials
---------
#. :ref:`Baseline Panda application <cg-tutorial-part-1>`
#. :ref:`The Simplest Possible Shader <cg-tutorial-part-2>`. So simple that it's
   useless.
#. :ref:`The simplest possible useful shader <cg-tutorial-part-3>`.

.. toctree::
   :titlesonly:
   :hidden:

   part-1
   part-2
   part-3

.. note:: The use of Cg will be deprecated in a future version of Panda3D.
