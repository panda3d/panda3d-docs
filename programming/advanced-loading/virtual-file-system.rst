.. _virtual-file-system:

The Virtual File System
=======================

General file reading in Panda is handled by the Virtual File System.

Although it presents the files and directories that it provides access to as a
single, unbroken file system, it can in fact include files from multiple
sources (such as :ref:`multifiles`) in the hierarchy, regardless of the
underlying structure.

This has the advantage of allowing one to access files and directories without
worrying overmuch about where they actually reside, and even access Multifile
archives as a directory hierarchy.

.. only:: python

   Python Interface
   ----------------

   Panda3D offers a replacement for the Python file module that supports the
   virtual file system.  You can find it in :py:mod:`direct.stdpy.file`.
   The interface is exactly the same as Python's, so it's safe to put this
   import above all the files where you want to use the :func:`open()` function:

   .. code-block:: python

      from direct.stdpy.file import *

   This module reimplements Python's file I/O mechanisms using Panda constructs.
   This enables Python to interface more easily with Panda's virtual file
   system, and it also better-supports Panda's SIMPLE_THREADS model, by avoiding
   blocking all threads while waiting for I/O to complete.

   Besides the :py:func:`~direct.stdpy.file.open()` call, this module also
   contains replacements for various other functions provided by the Python
   :py:mod:`os` and :py:mod:`os.path` modules.
   See the :py:mod:`API reference page <direct.stdpy.file>` for a full listing.


.. note:: This section is incomplete.
