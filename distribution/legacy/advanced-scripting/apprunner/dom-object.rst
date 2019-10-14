.. _the-apprunner.dom-object:

The appRunner.dom object
========================

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

Another important member of base.appRunner is the "dom" object. This is the
top of the JavaScript DOM ("Document Object Model") hierarchy, and corresponds
to the global scope (that is, the "window" object) in JavaScript.

In general, global objects and functions in JavaScript will be visible to the
Python code as members of appRunner.dom. In particular,
base.appRunner.dom.document corresponds to the toplevel "document" object,
which you can use to access the contents of the embedding web page itself.

For example, to update the value in a field called "username" on form called
"login" on the web page, you could write Python code like this:

.. code-block:: python

    login = base.appRunner.dom.document.getElementById('login')
    login.username.value = 'username'

In general, anything you can do in JavaScript, you can do in Python, via the
base.appRunner.dom object.

The dom object is always available; it is not limited by the
:ref:`p3d-origin-security` features.
