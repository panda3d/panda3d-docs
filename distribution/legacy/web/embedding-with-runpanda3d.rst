.. _embedding-with-runpanda3d:

Embedding with RunPanda3D
=========================

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

Using nested ``<object>`` elements
is a straightforward way to embed your p3d file, but it does have two
disadvantages. Specifically, (1) it requires you to specify all of the options
twice, which promotes errors; and (2) it doesn't work if you need to specify
an "id" attribute to access your embedded plugin object via JavaScript,
because you can't specify the same "id" attribute to two different
``<object>`` elements.

There's another alternative that solves both problems, using JavaScript. Of
course, this requires that your end-users will have JavaScript enabled, but
this is common; and your web page may have this requirement anyway if you are
planning to control your p3d application via JavaScript.

There's a JavaScript file called RunPanda3D.js that is distributed with the
Panda3D source. You'll find it in the directory direct/src/directscripts.
Simply copy this JavaScript file to your web host, and reference it in your
web page like this:

.. code-block:: html

    <head>
    ... other head content ...
    <script src="RunPanda3D.js" type="text/javascript"></script>
    ... other head content ...
    </head>
    <body>
    ... other body content ...
    <script type="text/javascript">
    P3D_RunContent('data', 'myapp.p3d', 'id', 'myapp_id',
        'width', '640', 'height', '480')
    }
    </script>
    ... other body content ...
    </body>

That is, you must include a reference to RunPanda3D.js within the

``part of your web page; and you include a call to the function``

``P3D_RunContent()`` within the part of your
web page.

``P3D_RunContent()`` will generate the
appropriate form of the ``<object>``
element for whichever browser the user is currently running: either the
Internet Explorer form, or the non-Internet Explorer form. The object element
is generated via document.write(), wherever the call to
``P3D_RunContent()`` appears within your web
page.

The parameters to ``P3D_RunContent()`` must
be given in pairs: of each two parameters, the first parameter is the keyword,
and the second parameter is the value. This is equivalent to a
``keyword="value"`` pair appearing in the
``<object>`` element. For instance,
the above call would generate an
``<object>`` element something like
this:

.. code-block:: html

    <object data="myapp.p3d" id="myapp_id" width="640" height="480">
    </object>

(though it will also add either
``classid`` or
``type``, according to the type
of browser the user is running.)

Using ``P3D_RunContent()`` also adds two
additional :ref:`splash-window-tags`, noplugin_img and noplugin_href. These
tags are not available if you embed using the
``<object>`` syntax directly.
