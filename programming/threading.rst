.. _threading:

Threading
=========

Panda3D provides a safe threading interface you can use, which works very
similar to Python's threading modules. Panda3D is compiled by default to use
"true" threading, which makes it safe to use Python threading interfaces (or any
other threading library) in conjunction with or in lieu of Panda's own built-in
threading interfaces described below.

If you want to test whether threading is enabled in your build of panda, use the
following program:

.. only:: python

   .. code-block:: python

      from panda3d.core import Thread
      print(Thread.isThreadingSupported())

.. only:: cpp

   .. code-block:: cpp

      #include "thread.h"

      int main() {
        std::cerr << Thread::is_threading_supported() << std::endl;
        return 0;
      }

If threading is enabled, it's also possible to turn it off, for example if you
want to test if a certain problem you are experiencing is related to threading.
Put this in your :ref:`Config.prc <configuring-panda3d>`:

.. code-block:: text

   support-threads #f

Asynchronous Operations
-----------------------

Panda3D provides several useful high-level functions for loading models and
doing other expensive operations in a thread, so the user of your application
will not notice chugs in the frame rate. These functions are managed by Panda3D
automatically, so do not require knowledge of threading. It is recommended that
you first seek out these features before implementing threading yourself.

See :ref:`async-loading` for more information about these features.

Threading
---------

If you want to use threading with Panda3D, it's not recommended to use Python's
built-in threading modules, since you will most likely run into issues (for
Panda3D is written in C++ and thus does not use the Python threading modules).
However, Panda3D offers a threading implementation that is safe to use, by
reimplementing Python's "thread" and "threading" modules, these work the same as
the Python built-in threading modules but are actually safe to use with Panda3D.

You can get access to Panda3D's implementation of Python's :py:mod:`thread`
module by importing the :py:mod:`~direct.stdpy.thread` module from
:py:mod:`direct.stdpy`:

.. code-block:: python

   # WRONG:
   import thread
   # RIGHT:
   from direct.stdpy import thread

For the Python module :py:mod:`threading`, Panda3D offers two equivalents,
:py:mod:`~direct.stdpy.threading` and :py:mod:`~direct.stdpy.threading2`, which
you can find both in :py:mod:`direct.stdpy` also.
The :py:mod:`~direct.stdpy.threading` module implements the threading module
with a thin layer over Panda's threading constructs. As such, the semantics are
close to, but not precisely, the semantics documented for Python's standard
threading module. If you really do require strict adherence to Python's
semantics, see the :py:mod:`~direct.stdpy.threading2` module instead.

In fact, the :py:mod:`~direct.stdpy.threading2` module is a bald-face copy of
Python's :py:mod:`threading` module from Python 2.5, with a few lines at the top
to import Panda's thread reimplementation instead of the system thread module,
and so it is therefore layered on top of Panda's thread implementation.

However, if you don't need such strict adherence to Python's original semantics,
the "threading" module is probably a better choice. It is likely to be slightly
faster than the threading2 module (and even slightly faster than Python's own
threading module). It is also better integrated with Panda's threads, so that
Panda's thread debug mechanisms will be easier to use and understand.

.. code-block:: python

   # WRONG:
   import threading
   # RIGHT:
   from direct.stdpy import threading
   # ALSO RIGHT:
   from direct.stdpy import threading2 as threading

It is permissible to mix-and-match both threading and threading2 within the same
application.

File I/O
--------

Panda3D also offers a thread-safe replacement for the Python file module. You
can find it in :py:mod:`direct.stdpy.file`. The interface is exactly the same as
Python's, so it's safe to put this import above all the files where you want to
use the :py:func:`open()` function:

.. code-block:: python

   from direct.stdpy.file import *

This module reimplements Python's file I/O mechanisms using Panda constructs.
This enables Python to interface more easily with Panda's virtual file system,
and it also better-supports Panda's SIMPLE_THREADS model, by avoiding blocking
all threads while waiting for I/O to complete.

Compiling Panda3D with threading support
----------------------------------------

There are two different interfaces for threading which you can enable using the
definitions HAVE_THREADS and SIMPLE_THREADS. The former is a full and heavy
implementation of threading and compiling with that option will slow down the
Panda3D build, unless you fully make use of the benefits that threading gives.
The latter, however, is a more simple threading interface that doesn't give you
the runtime overhead HAVE_THREADS gives you.

Note that you will have to define both HAVE_THREADS and SIMPLE_THREADS at the
same time to enable the simple interface, or you will not have threading.

The public builds enable true threading by default, so you will not need to
build Panda3D yourself if you want to take advantage of true threading.

If you wish to disable threading, you can pass the option
``--override HAVE_THREADS=UNDEF`` to makepanda.py. If you wish to use the simple
threading model, you may pass ``--override SIMPLE_THREADS=1`` instead.
