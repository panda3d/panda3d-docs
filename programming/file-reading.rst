.. _file-reading:

File Reading
============

General file reading in Panda is handled by the Virtual File System.

Although it presents the files and directories that it provides access to as a
single, unbroken file system, it can in fact include files from multiple
sources (such as :ref:`multifiles`) in the hierarchy, regardless of the
underlying structure.

This has the advantage of allowing one to access files and directories without
worrying overmuch about where they actually reside, and even access Multifile
archives as a directory hierarchy.

NB: While present in C++, on the Python side Panda does not offer file writing
functionality, with the exception of writing to certain specialized file
types. For general file writing, however, Python itself offers file-handling
functionality, including potentially-useful features such as reading to the
end of the line in a single call.

.. only:: python

   Thread-safe file I/O
   --------------------

   In versions 1.6.0 and above, Panda3D offers a :ref:`thread <threading>`-safe
   replacement for the Python file module. You can find it in direct.stdpy.file.
   The interface is exactly the same as Python's, so it's safe to put this import
   above all the files where you want to use the "file" or "open" functions:

   .. code-block:: python

      from direct.stdpy.file import *

   This module
   reimplements Python's file I/O mechanisms using Panda constructs. This enables
   Python to interface more easily with Panda's virtual file system, and it also
   better-supports Panda's SIMPLE_THREADS model, by avoiding blocking all threads
   while waiting for I/O to complete.


.. note:: This section is incomplete.
