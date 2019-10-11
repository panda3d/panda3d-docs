.. _converting-from-milkshape-3d:

Converting from Milkshape 3D
============================

Currently, the best way to get data from Milkshape into Panda is to use X
(DirectX native) file format. Save the model as X from Milkshape, then load it
directly into Panda, which can read X file format. Alternately, if you're
concerned about long load times (panda has to translate the file at load time),
then pre-convert the model from X to Egg to Bam using the conversion programs
supplied with Panda3D (x2egg, egg2bam).

Note that Milkshape 3D contains two X export plugins. I have heard that one of
them does not work correctly. This may require some experimentation.

Whenever you save a model in a non-native file format, you need to ask yourself:
"does this file format support everything I need?" For example, when you save
out a model in 3DS file format, you automatically lose all bone and animation
data, because the 3DS file format doesn't contain bone and animation data. In
the case of the X file format, you're in good shape: it's a fairly powerful file
format, supporting vertices and triangles, bones and animation.

However, egg file format supports some esoteric things. For example, it supports
blend targets (morph animations), which are not supported by the X file format.

More Detailed explanations for MS3D users
-----------------------------------------

You can use MS3D to create .X files (both static or animated) to be converted by
Panda3D's x2egg converter.

In MS3D there are two Direct X .X exporter: Direct 8.0 and DirectX(JT). So far
I've managed to use only DirectX 8.0 File. (DirectX JT got a lot more parameters
and only a few combination of it seemed to work but not on a predictable basis).
I'll talk only for animation with bones (not tested other ones). But this
exporter works also for static meshes.

1. Before Exporting to .X you must ensure:

   -  No null material or null name in texture in your model (MS3D won't block
      you but will crash during the export)
   -  No hyphen in your bones names (underscore is ok) (No issue in MS3D but
      issue with panda converter).
   - Animation mode is NOT enabled

2. To export, use Direct 8.0 file export. Select the required boxes. (Meshes,
   Materials, Animations) if you selected less than all checkboxes (material
   animations...) you will have to edit manually the x files to remove the las
   1 or 2 "}" of the file before using b2egg to convert. It's OK to leave
   default settings (Lock Root Bone and 1 as Frame offset). Warning: Export can
   be very long in case of big models/animations.

3. Convert using x2egg converter

   Warning: if you run X2egg without special args, you will need to have your
   textures also in the same directory than the x files. Don't be surprised if
   .egg file size is 6 times your .X file size, it's pretty normal due to more
   explicit information in the .egg file format. In case size is an issue,
   bamming the .egg file will reduce the size and optimize loading time.

   Also, before converting to .egg, you can load your .x in pview to check
   everything is fine.

4. TIPS: depending if you make your models fully in MS3D or import it from Poser
   you may find an issue: all animations applied to root bone instead of correct
   bone. You can solve it in MS3D by regrouping all materials, export to HL SMD
   (1 or 2) then import again and export to .X.

NB: this have been written by a coder not an artist :-)

Bugs in the Process
-------------------

Caution: at one time, it was discovered that there were two bugs in panda's
X-file importer. One, it was case-sensitive and it should not be. Two, it did
not handle hyphens in identifiers correctly. It is unknown whether or not these
bugs have been fixed.
