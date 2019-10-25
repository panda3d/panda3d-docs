.. _the-apprunner.main-object:

The appRunner.main object
=========================

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

The most important member of base.appRunner is the "main" object. This object
is the same object as plugin.main as seen from the JavaScript side (where
"plugin" is the DOM object corresponding to the application's <object>
element).

That is to say, any data members you store on base.appRunner.main will be
visible to JavaScript as members of plugin.main. Any function pointers that
you store on base.appRunner.main will be callable from JavaScript as functions
of plugin.main. Any objects that you store on base.appRunner.main will be
visible as objects of plugin.main, along with all methods and nested objects.
(But see :ref:`p3d-origin-security`.)

Conversely, any members stored on plugin.main by JavaScript will be accessible
as members of base.appRunner.main on the Python side, and similarly for
functions and nested objects.

For instance, if you write Python code that does this:

.. code-block:: python

   base.appRunner.main.base = base

Then your JavaScript code could do this:

.. code-block:: javascript

   plugin = document.getElementById('myPlugin')
   plugin.main.base.toggleWireframe()

which calls base.toggleWireframe(), a method that toggles wireframe rendering
in the Panda3D window.

Normally, you would use base.appRunner.main as a place to store values,
objects, and functions that you want to make accessible to your JavaScript
code.

Note that, for security purposes, by default JavaScript is prevented from
doing any of this: it cannot access base.appRunner.main, or call any Python
methods that you expose either intentionally or unintentionally, unless you
specifically allow it, by setting the p3d file's script_origin. See
:ref:`p3d-origin-security`.
