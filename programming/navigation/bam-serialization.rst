.. _bam-serialization:

BAM serialization
=================

Panda3D provides the feature to write the Panda3D objects to the disk 
using the BAM operations. In the navigation library, the BAM operations have 
been implemented over the NavMeshNode class.

.. code-block:: python

   navmeshnode = navigation.NavMeshNode("firstnavmeshnode", navmesh)
   navmeshnodepath = self.scene.attachNewNode(navmeshnode)

Write BAM
~~~~~~~~~

You can write the 'navmeshnodepath' to the disk as a BAM file.

.. code-block:: python

   navmeshnodepath.write_bam_file("firstnavmeshnode.bam")

The BAM File 'firstnavmeshnode.bam' is stored on the disk and can be used directly 
in the games or the programs without building and navigation mesh again. This 
helps in saving time and computation power.

Read BAM
~~~~~~~~

You can read the BAM File from the disk and load it as NodePath to NavMeshNode.

.. code-block:: python

   navmesh = loader.loadModel("firstnavmeshnode.bam")
