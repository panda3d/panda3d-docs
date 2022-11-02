.. _writing-3d-models-out-to-disk:

Writing 3D Models out to Disk
=============================

Panda has two native file formats for models.

Egg files (with the extension ``.egg``) are written in an
ASCII human readable format. The egg format is designed to be easy to read and
modify if necessary, and easy to write a convert into from another third-party
format. Also, the egg format is intended to be backward-compatible from all
future versions of Panda3D, so if you have an egg file that Panda can load
now, it should always be able to load that file. (Well, we can't really make
guarantees, but this is what we shoot for.)
See :ref:`parsing-and-generating-egg-files` for more information about the egg
format.

BAM Files
---------

Because of the way the egg syntax is designed, an egg file might be very
large, sometimes many times larger than the file it was converted from. It can
also sometimes take several seconds for Panda to load a large egg file.

Bam files (with the extension ``.bam``), on the other hand,
are binary files that are more closely tied to a particular version of Panda3D.
The bam format is designed to be as similar as possible to the actual Panda data
structures, so that a bam file is relatively small and can be loaded very
quickly. However, you should not consider the bam file format to be a good
long-term storage format for your models, since a future version of Panda3D
may not be able to load bam files from older versions. (That said, we have been
pretty good at retaining backward compatibility for .bam files anyway, so you
may find it possible to ignore this advice, albeit at your peril.)

You can always convert egg files to bam files using the program
:ref:`egg2bam <converting-egg-to-bam>`. For many simple models, it is also
possible to convert back again with the program
:ref:`bam2egg <list-of-panda3d-executables>`, but you should not rely on this,
since it does not convert advanced features like animation; and some structure
of the original egg file may be lost in the conversion.

You can load files of these formats, as well as
:ref:`any other supported format <supported-model-formats>`, using the
:ref:`loader.loadModel <model-files>` interface. Any file types other than
``.bam`` or ``.egg`` will be automatically converted at runtime, exactly as if
you had run the appropriate command-line conversion tool first.

The Bam Interface
-----------------

The easiest way to save geometry is to use to call
:meth:`write_bam_file(filename) <.NodePath.write_bam_file>` from the NodePath
that contains your geometry.

.. code-block:: python

   myPanda = loader.loadModel("panda")

   # do some fancy calculations on the normals, or texture coordinates that you
   # dont want to do at runtime

   # Save your new custom Panda
   myPanda.writeBamFile("customPanda.bam")

The Egg Interface
-----------------

One easy way to create ``.egg`` file for geometry that has already been made is
to create a ``.bam`` file and use bam2egg.
However, you will often want to use the egg interface to create geometry in
the first place; this is usually the easiest way to create geometry in Panda3D.

The complete documentation for using the egg interfaces has yet to be written,
but the egg library is really quite simple to use. The basic idea is that you
create an EggData, and an EggVertexPool to hold your vertices; and then you
can create a series of EggVertex and EggPolygon objects. If you want to create
some structure in your egg file, you can create one or more EggGroups to
separate the polygons into different groups. Here is an example:

.. code-block:: python

   from panda3d.core import Point3D, deg2Rad, NodePath, Filename, CSZupRight
   from panda3d.egg import EggPolygon, EggVertexPool, EggData, EggVertex, loadEggData, EggCoordinateSystem
   import math

   ...

   def makeWedge(angleDegrees = 360, numSteps = 16):

       z_up = EggCoordinateSystem()
       z_up.setValue(CSZupRight)

       data = EggData()
       data.addChild(z_up)

       vp = EggVertexPool('fan')
       data.addChild(vp)

       poly = EggPolygon()
       data.addChild(poly)

       v = EggVertex()
       v.setPos(Point3D(0, 0, 0))
       poly.addVertex(vp.addVertex(v))

       angleRadians = deg2Rad(angleDegrees)

       for i in range(numSteps + 1):
           a = angleRadians * i / numSteps
           y = math.sin(a)
           x = math.cos(a)

           v = EggVertex()
           v.setPos(Point3D(x, 0, y))
           poly.addVertex(vp.addVertex(v))

       return data
   ...

   # Creating egg data
   data = makeWedge()

   # To write the egg file to disk, use this:
   data.writeEgg(Filename("wedge.egg"))

   # To load the egg file and render it immediately, use this:
   model = NodePath(loadEggData(data))
   model.reparentTo(render)


See the generated API documentation of :mod:`panda3d.egg` for more complete
information about the egg library.
