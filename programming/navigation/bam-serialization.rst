.. _bam-serialization:

BAM serialization
=================

Panda3D provides the feature to write the Panda3D objects to the disk 
using the BAM operations. In the navigation library, the BAM operations have 
been implemented over the NavMeshNode class.

.. only:: python

   .. code-block:: python

      navmeshnode = navigation.NavMeshNode("firstnavmeshnode", navmesh)
      navmeshnodepath = scene.attach_new_node(navmeshnode)

.. only:: cpp

   .. code-block:: cpp

      NavMeshNode navmeshnode = new NavMeshNode("firstnavmeshnode", navmesh);
      NodePath navmeshnodepath = scene.attach_new_node(navmeshnode);


Write BAM
~~~~~~~~~

You can write the 'navmeshnodepath' to the disk as a BAM file.

.. only:: python

   .. code-block:: python

      navmeshnodepath.write_bam_file("firstnavmeshnode.bam")

.. only:: cpp

   .. code-block:: cpp

      navmeshnodepath.write_bam_file("firstnavmeshnode.bam");

The BAM File 'firstnavmeshnode.bam' is stored on the disk and can be used directly 
in the games or the programs without building and navigation mesh again. This 
helps in saving time and computation power.

Read BAM
~~~~~~~~

You can read the BAM File from the disk and load it as NodePath to NavMeshNode.

.. only:: python

   .. code-block:: python

      navmesh = loader.load_model("firstnavmeshnode.bam")

.. only:: cpp

   .. code-block:: cpp

      PandaFramework framework;
      framework.open_framework(argc, argv);
      framework.set_window_title("My Panda3D Window");
      WindowFramework *window = framework.open_window();
      NodePath navmesh = window->load_model(framework.get_models(), "firstnavmeshnode.bam");

