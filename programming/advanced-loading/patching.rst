.. _patching:

Patching
========

Patching is a process of generating the difference between 2 files:

.. code-block:: python

   p = Patchfile()
   p.build('version_1.mf', 'version_2.mf', 'v1_to_v2.patch')

This will generate the file v1_to_v2.patch based on the differences between
version_1.mf and version_2.mf. Then when you have version_1.mf and
v1_to_v2.patch, you can produce version_2.mf with:

.. code-block:: python

   p = Patchfile()
   p.apply(Filename('v1_to_v2.patch'), Filename('version_1.mf'))

There are other, more esoteric options, for limiting memory usage during
patching, or for patching in increments instead of all at once so you can update
a progress bar.

In the example above the files are named \*.mf. This example suggests that you
might be patching files in Panda's Multifile format (\*.mf). The multifiles can
store multiple resources like bams, textures, mp3's, and so on, and Panda can
load them from directly from the multifiles without having to unpack them first.

The Patchfile object works on any arbitrary binary files; you don't need to
limit yourself to just patching multifiles. However, the Patchfile does
recognize a multifile and treats it as a special case; it can build patches for
large multifiles without running out of memory, while building a patch for a
large generic binary file might require so much memory it brings your system to
its knees. (Applying patches doesn't require much memory, however.)

Patchfiles are not automatically compressed. You can do that yourself. Also, I
recommend patching uncompressed source files for best results. (You can build
patches against compressed source files, but the resulting patchfiles will tend
to be much larger than the same patchfiles built against the original
uncompressed files.)
