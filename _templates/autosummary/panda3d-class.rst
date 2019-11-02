{{ fullname | escape | underline }}

.. currentmodule:: {{ module }}

.. only:: python

   .. code-block:: python

      from {{ module }} import {{ name }}

.. autoclass:: {{ objname }}
   :members:
   :undoc-members:

   .. rubric:: Inheritance diagram

   .. inheritance-diagram:: {{ objname }}
      :parts: 1
