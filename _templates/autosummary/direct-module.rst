:github_url: https://github.com/panda3d/panda3d/blob/master/{{ fullname | replace("direct.", "direct/src/") | replace(".", "/") }}.py

{{ fullname | escape | underline }}

.. only:: cpp

   This page describes a Python module, which is not available to C++ users.
   To switch to the Python version of the manual, use the link in the sidebar.

.. only:: python

   .. code-block:: python

      {% if classes %}
      from {{ fullname }} import {{ (classes + functions) | join(', ') }}
      {% else %}
      import {{ fullname }}
      {% endif %}

   .. default-role:: obj

   .. automodule:: {{ fullname }}
      :members:
      :undoc-members:
      :ignore-module-all:

      {% if classes %}
      .. rubric:: Inheritance diagram

      .. inheritance-diagram:: {{ fullname }}
         :parts: 1
      {% endif %}
