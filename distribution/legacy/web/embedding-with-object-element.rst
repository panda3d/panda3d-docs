.. _embedding-with-an-object-element:

Embedding with an object element
================================

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

There are two different syntaxes for embedding a p3d file in a web page.
Internet Explorer requires one particular syntax, and every other browser in
the world requires another syntax, similar but slightly different.
Fortunately, it is possible to write a single web page that supports both
syntaxes at the same time.

This discussion assumes you are comfortable with writing HTML code in a web
page. If you are unfamiliar with HTML syntax, we recommend you study a brief
tutorial on writing web pages using HTML before continuing.

For Internet Explorer, you must use the
``&lt;object&gt;`` element to embed a p3d
file, with code like this:



.. code-block:: html

    <object width="640" height="480"
      classid="CLSID:924B4927-D3BA-41EA-9F7E-8A89194AB3AC">
        <param name="data" value="myapp.p3d">
    </object>



Note that the width and height are specified as attributes to the
``&lt;object&gt;`` element. The classid
string is literal, and must always be the exact string shown above; this is
the string that identifies the Panda3D plugin. The URL of the p3d file to be
launched should be specified as an attribute of the nested
``&lt;param&gt;`` element, as shown
above.

For other browsers, you also use the
``&lt;object&gt;`` element, but it looks a
little bit different:



.. code-block:: html

    <object width="640" height="480"
      type="application/x-panda3d" data="myapp.p3d">
    </object>



In non-Internet Explorer browsers, you identify the Panda3D plugin with the
string ``type="application/x-panda3d"``, instead of with
the classid string used by Internet Explorer. Also, the URL of the p3d file is
specified as an attribute of the
``&lt;object&gt;`` element, instead of in
a nested ``&lt;param&gt;`` element.

In order to design a web page that works on any browser--and you should always
design web pages that do--you can embed one
``&lt;object&gt;`` element within the
other. This works because if a browser encounters an
``&lt;object&gt;`` element that it doesn't
understand, it is supposed to load whatever is within that
``&lt;object&gt;``'s nested scope, which
might be another ``&lt;object&gt;``
element. So, for instance, the above examples could be written like this:



.. code-block:: html

    <object width="640" height="480"
      type="application/x-panda3d" data="myapp.p3d">
        <object width="640" height="480"
          classid="CLSID:924B4927-D3BA-41EA-9F7E-8A89194AB3AC">
            <param name="data" value="myapp.p3d">
        </object>
    </object>



The outer ``&lt;object&gt;`` element is
the non-Internet Explorer version, and in case that isn't understood (for
instance, because the user is running Internet Explorer), then it will fall to
the inner ``&lt;object&gt;`` element
instead, which is the Internet Explorer version.

We recommend putting the non-Internet Explorer version on the outside, because
some versions of Safari seem to get confused if they encounter the Internet
Explorer version first.

Note that there are additional, optional attributes that may be provided to
either form of the ``&lt;object&gt;`` tag.
These are discussed in :ref:`advanced-object-tags`.
