.. _distribution:

Distributing Panda3D Applications
=================================

Starting with Panda3D 1.10.0, Python applications using Panda3D can be packaged
in a distributable form (e.g., zip archives, Windows installers, tarballs) using
`Setuptools <https://setuptools.readthedocs.io/en/latest/>`__. These packages
can then be hosted on a website or store front for distribution to end users.

The new Setuptools-based process is a replacement for
:ref:`the old distribution method <using-the-legacy-distribution-method>`, which was more complex to
use and maintain, required special builds of Panda3D, and did not work with
Python 3.

From the `Setuptools
documentation <https://setuptools.readthedocs.io/en/latest/>`__, "Setuptools
is a fully-featured, actively-maintained, and stable library designed to
facilitate packaging Python projects." The Setuptools documentation should be
referred to for more details, but the basics of using Setuptools is:

#. Create a setup.py
#. Execute commands with
   ``python setup.py command``

The basic structure of a setup.py file is:

.. code-block:: python

   from setuptools import setup

   setup(
       ...
   )

With the ``setup()`` function taking many arguments. See the
:ref:`setuptools-examples` page for example ``setup.py`` files for common
project structures.

The ``panda3d`` package adds two new commands to Setuptools:

:ref:`build_apps <building-binaries>`: build binaries that can be run without Python or Panda3D pre-installed on the end-user's system

:ref:`bdist_apps <packaging-binaries>`: package binaries into various archives and installers for distribution (also runs ``build_apps``)

Thus, the basic steps to deploy a Panda3D application (or set of applications)
are:

#. Create a ``setup.py`` file for your application
#. Execute ``python setup.py bdist_apps``
#. Copy the archives/packages (e.g., zip, tar.gz, exe) from the build directory
   to a location that users can access

Refer to the Asteroids sample program for an example of a ``setup.py`` file that
can be used with Panda3D.

.. toctree::
   :maxdepth: 2

   building-binaries
   packaging-binaries
   setuptools-examples
   thirdparty-licenses
   legacy/index
