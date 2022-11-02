:orphan:

.. _interrogate:

Interrogate
===========

Interrogate
-----------

Interrogate is a program to parse a body of C++ code and build up a table of
classes, methods, functions, and symbols found, for the purposes of calling into
the codebase via a non-C++ scripting language like Python (Scheme and Smalltalk
were also tried at some point) The design of interrogate is such that it should
be able to produce wrappers for any other language without too much trouble.
You'll have to be responsible for writing and maintaining the interface layer to
produce the wrappers, though.

In addition to identifying all the classes and their relationships, interrogate
will generate a wrapper function for each callable function. The wrapper
functions will be callable directly from the scripting language, with no
understanding of C++ necessary; these wrapper functions will in turn call the
actual C++ functions or methods.

C++ Parser
----------

Interrogate contains a capable C++ parser supporting most exportable features of
C++, including templates, default parameters, and function overloading. Various
C++11 features are supported as well.

It also extends the C++ language with various keywords that have special meaning
to Interrogate. These are used to define which interfaces are published, and
some can be used to tell Interrogate to generate additional interfaces for the
scripting language, such as properties and getters returning a list.

For Interrogate to generate bindings for a particular class, one of the
following conditions needs to hold true:

-  It has one or more methods marked with ``__published`` access.
-  The ``-promiscuous`` option is passed to Interrogate.
-  It is specified by a ``forcetype`` directive in a special .N file.

The first method is the most common approach. It is conventional to define a
``PUBLISHED`` macro that will expand to ``public`` when compiling the C++ code
and ``__published`` macro when parsing the source with Interrogate, as follows:

.. code-block:: cpp

   // dtoolbase.h defines the PUBLISHED macro if the CPPPARSER macro is defined
   #include "dtoolbase.h"

   class MyBufferClass {
   PUBLISHED:
     // This method is publicly accessible to Python and C++
     void set_data(const string &str);

   public:
     // C++-only method
     char *get_buffer();
   };


Parser Includes
~~~~~~~~~~~~~~~

Sometimes, a project may use a header file that Interrogate has difficulty
parsing. In many cases, this is simply due to Interrogate not having been
configured correctly, but it is nevertheless easier to tell Interrogate to skip
these external headers.

This is especially true for many standard library headers, which provide many
interfaces that Interrogate will not need, and often contain a lot of compiler
magic that Interrogate has trouble understanding.

In these situations, the easiest approach is to place a header in a *parser-inc*
directory, which is passed to Interrogate using the ``-s`` option. This causes
Interrogate to read these mock header files instead of the actual versions, and
pick up the declarations therein.

This header file may be empty if the code does not need to use any of the
interfaces defined therein, or may contain some simple forward declarations and
typedefs so that Interrogate knows of the existence of these external
interfaces, even though it doesn't need to do anything with them.

The Panda3D SDK provides a parser-inc directory that for many standard headers
and definitions, as well as headers for the various thirdparty libraries that
Panda3D relies on. However, it is always possible to create a custom parser-inc
directory and add it to interrogate with the ``-S`` option.

Creating Python bindings
------------------------

There are a few steps involved in generating Python wrappers using interrogate.

-  Run interrogate to parse the header files, which will generate a C++ source
   file and an .in file::

      interrogate -module test -oc test_igate.cxx -od test.in -python-native test.h

-  Most likely, you want to specify more flags to the interrogate command, like
   -string, -fnames, -refcount, or -assert. Consult the interrogate help file
   for more information about that (run interrogate with -h option)

-  Now, you will need to call interrogate_module and generate an
   interrogate_module.cxx file based on your two files from the previous step::

      interrogate_module -module test -library test -oc test_module.cxx -python-native test.in

-  Note that you can also run interrogate with the ``-do-module`` option which
   will automatically make sure interrogate_module gets called too. However,
   this is the disadvantage that you cannot combine the result of multiple
   interrogate runs into a single module.

-  Compile and link these C++ files together into a dynamic library. Instead of
   giving it the .dll extension, give it the .pyd extension, which will make it
   directly importable from Python. Note that the name of the library must be
   the same as the one passed to the ``-module`` option.

-  You can now put it on your Python path (or make sure it's in the same
   directory) and import it directly by the name of your library:

   .. code-block:: python

      from test import TestClass

If you get this error message::

   ImportError: dynamic module does not define init function (inittest)

One of three things could have gone wrong: you did not pass the
``-python-native`` option to both the interrogate and the interrogate_module
steps, you did not link the C++ file generated by interrogate_module into the
.pyd module, or you did not pass the correct ``-module test`` option to
interrogate and interrogate_module that matches the basename of the .pyd file.

Interrogate Options
-------------------

This section will explain how to call interrogate and will briefly address the
most important options. For the full documentation, however, refer to the
interrogate help file (accessible by calling interrogate with the -h option).

When calling interrogate, you will need to include the -oc and -od options,
which specify where the generated code and function tables, respectively, will
be written.

The -module and -library options are used to specify the name of your module and
library. These options are mainly code-organizational. You can omit both
options.

With -D you can ignore or make interrogate interpret symbols differently. For
example, if your code uses a non-standard C macro like ``__inline``, you would
need to call interrogate with ``-D__inline``. Or, if you would like certain
defines to be defined differently, you can use ``-Ddefvar=value``.

Furthermore, there are a few special flags that you most likely want to include.
There is the -string option, which treats the C++ ``char*`` and STL strings as
special cases, and maps them to the scripting language's string equivalent,
instead of a wrapper to ``basic_string<char>``. The option -refcount makes the
wrappers compatible with Panda3D's smart reference counting system, if your
library depends on Panda3D you will want to include it too. The -assert option
is just used for Python wrappers and specifies that when the C++ code throws an
assert, this will be translated to an AssertionError exception in python.

Interface Makers
~~~~~~~~~~~~~~~~

Interrogate provides a selection of several interface makers:

-  The -c option will generate function wrappers using the C calling convention.
   Any scripting language that can call a C function should be able to make
   advantage of the interrogate database.
-  The -python option will generate function wrappers using the Python calling
   convention. In this case, the shared library will directly be loadable as
   python module (after interrogate_module is called), although C++ objects and
   methods will be converted into an object handle and a list of independent
   Python functions.
-  The -python-native option generates true python objects for C++ objects, and
   translates all C++ methods to true Python methods. This is the option you
   will most likely want to use.

You can also specify a combination of any of those. If all are omitted, the
default is -c.

Example
~~~~~~~

Here's a small example::

   interrogate -DCPPPARSER -D__STDC__=1 -D__cplusplus=201103L -S/usr/include/panda3d/parser-inc -S/usr/include/ -I/usr/include/panda3d/ -oc myModule_igate.cxx -od myModule.in -fnames -string -refcount -assert -python-native -module libMyModule -library libMyModule myModule.h

   interrogate_module -oc myModule_module.cxx -module libMyModule -library libMyModule -python-native myModule.in


More Information
----------------

-  You can run the interrogate commands with the -h option to get a more
   detailed explanation of the options available.
-  There is a sample C++ extension in the skel/ directory in the Panda3D source
   to use as reference and sandbox.
-  David Rose, from Walt Disney VR Studio, has held a lecture about interrogate.
   You can watch a video recording of it
   `here <https://www.youtube.com/watch?v=rh8X5pImzrI>`__. (Recorded June 4,
   2008)
