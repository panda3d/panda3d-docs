.. _parsing-and-generating-egg-files:

Parsing and Generating Egg Files
================================

Transforms and Vertices
-----------------------

The egg syntax defines all transforms, including joint transforms, relative to
the parent node only. When the animation is played, Panda accumulates the
transforms for each joint.

Although joints are defined using a local transform, vertices are defined in
an egg file using global coordinates, which is irrespective of transforms
appearing within the egg file. This means when Panda loads the egg file is
loaded, the vertex coordinates given in the egg file must be pre-transformed
by the appropriate inverse matrix to compensate.

Custom .egg Readers/Writers
---------------------------

When writing an importer or exporter for panda, you have two choices.

One option is to use the panda runtime library, which includes code for
reading, parsing, storing, and emitting Egg files. This approach can save you
a great deal of effort. However, it does require that you link with the panda
runtime system, which may be inconvenient if you wish to distribute a small,
standalone file translator.

If you decide to use the panda runtime system, the classes you will need to
use are defined in the ``panda3d.egg``
module, such as ``panda3d.egg.EggData``,
``panda3d.egg.EggGroup``, and so forth. Like all
panda classes, these are documented in the `API reference
manual. <https://www.panda3d.org/reference/>`__

The other alternative is to parse/generate the Egg file entirely by yourself.
In this case, you will need to read the `syntax documentation for egg
files <https://raw.githubusercontent.com/panda3d/panda3d/master/panda/src/doc/eggSyntax.txt>`__.
This documentation is part of the source code on GitHub. The file format is
human-readable, and fairly straightforward.

If you are writing a program to *generate* Egg files, either approach is
equally good. However, if you are writing a program to *parse* Egg files, we
do recommend using the panda runtime library, rather than writing your own
parser, for the simple reason that it is difficult to write a parser that
accepts all valid Egg files. Also, the Egg syntax might be extended from time
to time, and relying on the runtime library to parse the Egg syntax will
ensure that your program continues to parse future Egg files.
