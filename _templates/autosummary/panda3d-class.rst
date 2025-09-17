{{ objname | escape | underline }}

.. currentmodule:: {{ module }}

.. only:: python

   .. code-block:: python

      from {{ module }} import {{ name }}

   .. autoclass:: {{ objname }}
      :members:
      :undoc-members:
      :exclude-members: DtoolClassDict

      .. rubric:: Inheritance diagram

      .. inheritance-diagram:: {{ objname }}
         :parts: 1

.. only:: cpp

   .. default-domain:: cpp

   .. autoclass:: {{ objname }}
      :members:
      :undoc-members:
      :exclude-members: DtoolClassDict

      .. rubric:: Inheritance diagram

      .. inheritance-diagram:: {{ objname }}
         :parts: 1
