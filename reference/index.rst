.. _api-reference:

API Reference
=============

panda3d - Core library
----------------------

.. autosummary::

   panda3d.core
   panda3d.direct

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
      :toctree: .
      :template: autosummary/package.rst

.. only:: cpp

   Since this module is written in Python, it is not available to C++ users.
   To switch to the Python version of the manual, use the link in the sidebar.
