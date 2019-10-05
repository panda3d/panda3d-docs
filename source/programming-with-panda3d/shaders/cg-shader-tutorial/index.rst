.. _cg-shader-tutorial:

Cg Shader Tutorial
==================

Cg Shader Tutorials
-------------------


Panda has the ability to process shaders written in the Cg shader language. In
this tutorial series, you will learn how to write shaders for Panda in Cg.
While there are panda specific things in this tutorial you should be able to
learn how to write Cg shaders that can be used in other engines.

Pre-requisites
--------------


You should be able to write a simple math program in C. Do not underestimate
this. If you start writing your own shaders without any prior knowledge about
a C like language it is as hard as starting to write a Panda3D application
without knowing anything about Python. Some resources you might want to look
at:

-  `C Programming Wikibook <http://en.wikibooks.org/wiki/C_Programming>`__

You should have a solid grasp of Panda basics. Read
:ref:`the hello world <tutorial>` tutorial and understand the "Solar System"
sample that comes with the panda distribution. You should also have a good
understanding of how the :ref:`scene graph <the-scene-graph>` works. If you're
interested in writing a shadow mapping shader, it helps to have a solid
understanding of how the :ref:`depth buffer <depth-test-and-depth-write>`
works.

Read the first chapter from `NVIDIA's Cg
Tutorial <http://http.developer.nvidia.com/CgTutorial/cg_tutorial_chapter01.html>`__.
You do not have to understand it fully, but at least you know who invented Cg
and what it is for. The `NVIDIA <http://developer.nvidia.com>`__ and
`ATI <http://developer.amd.com>`__ developer sites also have plenty of useful
information about shaders.

You should also have the
:ref:`List of Possible Shader Inputs <list-of-possible-cg-shader-inputs>` page
handy.

Tutorials
---------


#. :ref:`Baseline Panda application <cg-tutorial-part-1>`
#. :ref:`The Simplest Possible Shader <cg-tutorial-part-2>`. So simple that
   its useless.
#. The simplest possible useful shader.
#. Applying colors to the model as defined in the model file.
#. Applying colors with the vertex and fragment shaders. Pass information
   between the vertex and fragment shader.
#. Passing inputs to the shader and controlling it from Panda
#. Applying one texture to your models, disregarding colors.
#. Applying two textures to your models.
#. Explaining details about diffuse lighting.
#. Per vertex diffuse lighting with shaders. The concept of spaces is
   introduced here.
#. Per pixel lighting with one point light. Normalization problems that may
   arise are explained here.
#. Per pixel lighting with multiple point lights and attenuation.

Incomplete Section
------------------


Note: this section is incomplete. It will be updated soon.

Although some pages aren't written yet, the sourcecode for all the tutorials
is complete. Read this forum topic for more info and links to codes:
https://discourse.panda3d.org/t/improving-the-manual/11599


.. toctree::
   :maxdepth: 2

   cg-tutorial-part-1
   cg-tutorial-part-2
   cg-tutorial-part-3
