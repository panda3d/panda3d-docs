.. _converting-egg-to-bam:

Converting Egg to Bam
=====================

Panda's native egg file format is human-readable. This is convenient, but the
files can get very large, and they can a little bit slow to load. To accelerate
loading, Panda supports a second native format, bam. These files are smaller and
are loaded very rapidly, but they cannot be viewed or edited in a text editor.
Also, bam files are specific to the version of Panda they are created with, so
they are not a good choice for long-term storage of your models.

Texture pathnames in an egg file are first assumed to be relative to the egg
file itself. If the texture is not found at that location, panda will search its
model-path, which is specified in the panda config file. When doing this, panda
concatenates the directory which is part of the model-path to the entire string
in the egg-file. So if the model-path names the directory "/d/stuff", and the
texture-path in the egg file is "mytextures/tex.png", then panda looks in
"/d/stuff/mytextures/tex.png."

Texture pathnames in a bam file may be stored relative to the bam file itself,
relative to a directory on the model-path, or with a full pathname to the file,
depending on the parameters given to the egg2bam program.

The program egg2bam is used to convert egg files to bam files. Egg2bam will
complain if the textures aren't present. You must install the textures (into
your model path) before you convert the bam file. You can run the egg2bam
program as follows::

   egg2bam -ps rel -o bamFileName.bam eggFileName.egg

Here, "-ps rel" means to record the textures in the bam filename relative to the
filename itself; if you use this option, you should ensure that you do not move
the bam file later without also moving the textures. (The default option is to
assume the textures have already been installed along the model path, and record
them relative to the model path. If you use the default option, you should
ensure the textures are already installed in their appropriate place, and the
model-path is defined, before you run egg2bam.)

The egg2bam program accepts a number of other parameters that may be seen by
running ``egg2bam -h``.
