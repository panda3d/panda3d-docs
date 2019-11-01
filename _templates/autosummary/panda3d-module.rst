{{ fullname | escape | underline }}

.. automodule:: {{ fullname }}
   :no-members:

   {% if classes %}
   .. autosummary::
      :toctree: .
      :template: autosummary/panda3d-class.rst

      {% for item in classes %}
      {{ item }}
      {%- endfor %}
   {% endif %}

   {% if functions %}
   .. rubric:: Global Functions

   {% for item in functions %}
   .. autofunction:: {{ item }}
   {%- endfor %}
   {% endif %}
