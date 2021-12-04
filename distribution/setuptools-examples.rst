:orphan:

.. _setuptools-examples:

Setuptools Examples
===================

Simple Console Application
--------------------------

The most basic and simplest application to package is a simple console app with
no dependencies:

.. code-block:: python

   print("Hello world")

Assuming this is saved as ``main.py``, we can use the following
``requirements.txt`` file::

   panda3d

The corresponding ``setup.py`` file could look like so:

.. code-block:: python

   import setuptools

   setup(
       name="Hello World",
       options = {
           'build_apps': {
               'console_apps': {'hello_world': 'main.py'},
           }
       }
   )

Then, we can build the binaries using ``python setup.py build_apps``.

A ``build`` directory will be created and contain a directory for each platform
that binaries were built for. Since no platforms were specified, the defaults
were used (manylinux1_x86_64, macosx_10_6_x86_64, win_amd64).

Note, win32 is missing from the defaults. If a win32 build is desired, then
platforms must be defined in ``setup.py`` and ``win_amd64`` added to the list:

.. code-block:: python

   import setuptools

   setup(
       name="Hello World",
       options = {
           'build_apps': {
               'console_apps': {'hello_world': 'main.py'},
               'platforms': [
                   'manylinux1_x86_64',
                   'macosx_10_6_x86_64',
                   'win_amd64',
                   'win32',
               ],
           }
       }
   )

Asteroids Sample
----------------

Below is an example of a setup.py that can be used to build the Asteroids sample
program.

.. code-block:: python

   from setuptools import setup

   setup(
       name="asteroids",
       options = {
           'build_apps': {
               'include_patterns': [
                   '**/*.png',
                   '**/*.jpg',
                   '**/*.egg',
               ],
               'gui_apps': {
                   'asteroids': 'main.py',
               },
               'plugins': [
                   'pandagl',
                   'p3openal_audio',
               ],
           }
       }
   )

With the setup.py in place, it can be run with: ``python setup.py bdist_apps``

The name field and options dictionary in the above setup.py can also be replaced
by the following setup.cfg file:

.. code-block:: ini

   [metadata]
   name = asteroids

   [build_apps]
   include_patterns =
       **/*.png
       **/*.jpg
       **/*.egg
   gui_apps =
       asteroids = main.py
   plugins =
       pandagl
       p3openal_audio
