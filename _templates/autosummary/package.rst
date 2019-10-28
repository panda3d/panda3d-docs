:github_url: https://github.com/panda3d/panda3d/tree/master/{{ fullname | replace("direct.", "direct/src/") | replace(".", "/") }}/

{{ fullname | escape | underline }}

.. only:: cpp

   This page describes a Python module, which is not available to C++ users.
   To switch to the Python version of the manual, use the link in the sidebar.

.. only:: python

   .. automodule:: {{ fullname }}
      :members:
      :undoc-members:

      .. autopackagesummary:: {{ fullname }}
         :toctree: .
