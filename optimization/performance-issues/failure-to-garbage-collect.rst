.. _failure-to-garbage-collect:

Failure to Garbage Collect
==========================

It's easy to get used to the fact that Python's garbage collector can
automatically clean up Panda3D data structures. Unfortunately, there are a few
structures that can't be cleaned up automatically. You need to know what they
are, or you may end up with a leak.

Unloading Models and Textures
-----------------------------

Normally, models that are loaded are automatically cached in memory, in the
:class:`.ModelPool`. This is very useful if a model is loaded more than once in
an application, so that Panda3D does not need to reload the model if it is
loaded again. However, it can also mean that these models unnecessarily use up
memory even if it is no longer needed. Consult the :class:`.ModelPool` reference
to find out how to release models from this cache.

The same applies to textures, which are cached in the :class:`.TexturePool`, and
fonts, which are cached in the :class:`.FontPool`.

.. only:: python

   Reference Cycles with Python Tags
   ---------------------------------

   When using Python tags to store references to Panda3D objects, it is easy to
   accidentally create a reference cycle that Python's garbage collector cannot
   detect. This scenario is explained on the page :ref:`subclassing`.

   Removing Custom Class Instances
   -------------------------------

   When using custom Python classes that manage Panda3D objects, there are a few
   things to be aware of in order to ensure that they get cleaned up properly.
   These are explained on the page :ref:`removing-custom-class-instances`.
