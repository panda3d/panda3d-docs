.. _the-python-debugger:

The Python Debugger
===================

Python is a very powerful interactive and interpreted language. Python's
development cycle is very fast. Often the most effective way to to debug is to
output relevant information. Having said that, there are many ways to enhance
productivity with knowledge of good debugging techniques.

Using python -i mode
--------------------

Python programs may be developed and tested with the help of the interactive
mode of the Python interpreter, which, allows program components to be debugged,
traced, profiled, and tested interactively. When invoking python with -i, this
ensures that an interactive session of python is invoked. With regards to
Panda3D this requires a little explanation. Panda3D programs typically have a
command called ``base.run()`` to start rendering, so here's one way to start an
interactive session. On the command prompt type::

   python -i myPandaFile.py

After Panda3D has loaded, make sure the command window has focus and type
Ctrl-C. This will show a python prompt like so:

   >>>

Now on the command prompt you can execute any python commands, related or
unrelated to your Panda3D program. This is useful for looking at information
at that specific point in time. You could even change that information for
that running instance of the program.

pdb
---

Python offers hooks enabling interactive debugging. Module pdb supplies a
simple text-mode interactive debugger. It supports setting (conditional)
breakpoints and single stepping at the source line level, inspection of stack
frames, source code listing, and evaluation of arbitrary Python code in the
context of any stack frame. It also supports post-mortem debugging and can be
called under program control.

The debugger's prompt is "(Pdb) ". There are many ways to enter the debugger.
Typical usage to run a program under control of the debugger is:

   >>> import pdb
   >>> import <mymodule>
   >>> pdb.run('mymodule.test()')
   > <string>(0)?()
   (Pdb) continue
   > <string>(1)?()
   (Pdb) continue
   NameError: 'spam'
   <string>(1)?()
   (Pdb)

Detailed information about pdb can be found
`here <https://docs.python.org/library/pdb.html>`__. In addition to pdb, Python
also has two modules called ``inspect`` and ``traceback``. ``inspect`` supplies
functions to extract information from all kinds of objects, including the Python
call stack and source files. The ``traceback`` module lets you extract, format
and output information about tracebacks as normally produced by uncaught
exceptions.
