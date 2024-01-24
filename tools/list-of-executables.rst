:orphan:

.. _list-of-panda3d-executables:

List of Panda3D Executables
===========================

This is meant to be a list of the executables in the /bin/ folder of Panda3D.
You can get a detailed synopsis of what the executables do by running them with
-h as the argument.

===================== =============================================================================================================================================================================================================
Filename              Description
===================== =============================================================================================================================================================================================================
bam-info.exe          Scans one or more .bam files and outputs their contents. See executable for more information.
bam2egg.exe           Converts models in the .bam format to the .egg format. For more information see :ref:`converting-egg-to-bam`.
cgc.exe               A compiler for NVidia’s Cg language. For more information see :ref:`Using Cg Shaders <shader-basics>`.
dxf-points.exe        Reads in an AutoCad .dxf file and prints out the points contained in it. See executable for more information.
dxf2egg.exe           Converts models from the AutoCad format to the .egg format. For more information see :ref:`converting-to-egg`
egg-crop.exe          Strips an .egg file of all parts that fall outside the given bounding volume. See executable for more information.
egg-make-tube.exe     Creates an .egg file representing a “tube” model. See executable for more information.
egg-mkfont.exe        Makes a .egg file from a FreeType (.ttf) font. For more information see :ref:`text-fonts`.
egg-optchar.exe       Optimizes models by removing unused joints. Also allow you to label parts of the model. For more information see :ref:`manipulating-a-piece-of-a-model`.
egg-palettize.exe     Tries to combine textures in an egg file. Also performs some texture manipulation. See executable for more information.
egg-qtess.exe         Performs a tesselation on all of the NURBS surfaces in a .egg file. See executable for more information.
egg-texture-cards.exe Creates an egg that automatically rotates through multiple textures. For more information see :ref:`automatic-texture-animation`.
egg-topstrip.exe      Unapplies the animations from one of the top joints in a model. Useful for character models that stack on top of each other. See executable for more information
egg-trans.exe         Produces out essentially the same .egg file. Useful for applying rotational and positional transformations. See executable for more information.
egg2bam.exe           Converts files in the .egg format to the .bam format. For more information see :ref:`converting-egg-to-bam`.
egg2c.exe             Reads a .egg file and produce C/C++ code that will almost compile. See executable for more information.
egg2dxf.exe           Converts files in the .egg format to the AutoCad format.
egg2flt.exe           Converts files in the .egg format to the Open Flight format.
egg2x.exe             Converts files in the .egg format to the DirectX format. Especially useful because it holds bone, joint and animation data.
flt-info.exe          Reads an OpenFlight file and prints out information about its contents. See executable for more information.
flt-trans.exe         Produces essentially the same .flt file. Useful for positional and rotational transformations. See executable for more information.
flt2egg.exe           Converts files in the OpenFlight format to the .egg format. For more information see :ref:`converting-to-egg`.
image-info.exe        Reports the sizes of one or more images. See executable for more information.
image-resize.exe      Resizes an image. See executable for more information.
image-trans.exe       Produces an identical picture. Can also be used for file format conversion. See executable for more information.
interrogate.exe       Parses C++ code and creates wrappers so that it can be called in a Scripting language. For more information see :ref:`interrogate`
lwo-scan.exe          Prints the contents of a .lwo file. See executable for more information.
lwo2egg.exe           Converts files in the LightWave 3D format to the .egg format. For more information see :ref:`converting-to-egg`.
make-prc-key.exe      Generates one or more new key to be used for signing a prc file. See executable for more information.
maya2egg5.exe         Converts files in the Maya 5 format to the .egg format. For more information see :ref:`converting-from-maya`.
maya2egg6.exe         Converts files in the Maya 6 format to the .egg format. For more information see :ref:`converting-from-maya`.
maya2egg65.exe        Converts files in the Maya 6.5 format to the .egg format. For more information see :ref:`converting-from-maya`.
multify.exe           Stores and extracts files from a Panda MultiFile. Can also extract file in program using the VirtualFileSystem (see API for usage). For more information see executable.
pdecrypt.exe          Decompress a file compressed by pencrypt. See executable for more information.
pencrypt.exe          Runs an encryption algorithm on the specified file. The original file can only be recovered by using pdecrypt. See executable for more information.
python.exe            The Python interpreter. For more information see :ref:`starting-panda3d`
pstats.exe            Panda’s built in performance tool. For more information see :ref:`measuring-performance-with-pstats`
pview.exe             Used to view models in the .egg or .bam format without having to create a Panda program. For more information see :ref:`pview`.
vrml2egg.exe          Converts files in the Virtual Reality Modeling Language format to the .egg format. For more information see :ref:`converting-to-egg`.
x2egg.exe             Converts files in the Direct X format to the .egg format. Especially useful because it holds bone, joint and animation data. For more information see :ref:`converting-to-egg`.
===================== =============================================================================================================================================================================================================
