.. _reference:

API Reference
=============

.. only:: python

   The Panda3D Python API consists of two packages: the :py:mod:`panda3d` core
   library, which is written in C++, and the :py:mod:`direct` library, which
   is written in Python.  This section of the documentation aims to give a
   complete overview of all the classes and functions defined in these two
   libraries.

.. only:: cpp

   The C++ part of the API reference is incomplete.  Missing information can be
   looked up in the older Doxygen reference:

   https://www.panda3d.org/reference/cxx/

.. toctree::
   :hidden:

   panda3d
   direct

panda3d - Core library
----------------------

.. py:module:: panda3d

.. autopackagesummary:: panda3d

direct - Python support library
-------------------------------

.. py:module:: direct

DIRECT is a set of Python-based tools that are layered on top of core Panda3D,
which is written in C++. It includes the DirectGUI tools, the task system, the
Interval system, a high-level class for animated characters, and several other
systems.

There are additional C++ classes to support these modules, which can be found
in the :py:mod:`panda3d.direct` module.

.. only:: python

   .. autopackagesummary:: direct

.. only:: cpp

   Since this module is written in Python, it is not available to C++ programs.
   To switch to the Python version of the manual, use the link in the sidebar.
