.. _apprunner:

AppRunner
=========

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

AppRunner is the Python class that supervises the launching of your
application in a p3d file. There is a global instance of AppRunner available
in base.appRunner whenever your application is running as a p3d file. In fact,
this is a reliable way to test your run mode:



.. code-block:: python

    if base.appRunner:
        print("Running in a p3d file")
    else:
        print("Running interactively")



All of your interaction with the web environment will go through
base.appRunner. There are several important members and methods of
base.appRunner that facilitate communication with JavaScript and with the
embedding web page. They are described in detail in the following pages.


.. toctree::
   :maxdepth: 2

   main-object
   dom-object
   reading-html-tokens
   other-members
