.. _converting-from-other-formats:

Converting from other Formats
=============================

There are several tools included with Panda that can convert various file
formats into egg file format:

========
lwo2egg
dxf2egg
flt2egg
vrml2egg
x2egg
========


Note that Panda can load any of these file formats without conversion, doing
so causes the conversion to occur at runtime.

Also, be aware that many of these file formats are limited. Most do not
include bone or animation data. Some do not store normals. Currently the .x
format is the only one of these that stores bones, joints and animations.
