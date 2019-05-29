.. _detectpanda3d.js:

DetectPanda3D.js
================

Note: This article describes a deprecated feature as of Panda3D 1.10.0.

There is a JavaScript function distributed with Panda, in the
direct/src/directscripts directory, that can be used to determine whether the
Panda3D plugin is installed at all. You can use this script to redirect users
to the appropriate page to install the plugin if necessary.

To use it, copy it to your web server and reference it in the section of your
HTML document like this:



.. code-block:: html

    <script src="DetectPanda3D.js" language="javascript"></script>



Then elsewhere, presumably in the section of your document, you can reference
it like this:



.. code-block:: html

    <script language="javascript">
    if (detectPanda3D()) {
       ... plugin installed
    } else {
       ... plugin not installed
    }
    </script>



The function takes two optional parameters. The first parameter, if specified,
is the URL of another page to redirect to, and the second parameter should be
True to redirect to the indicated URL if the plugin is found, or False to
redirect if the plugin is not found.

For instance, to trigger an automatic redirect to another page if the plugin
is not installed, pass that page's URL as the first parameter, and False as
the second parameter, like this:



.. code-block:: html

    <script language="javascript">
    detectPanda3D('http://my.host.net/needsPlugin.html', False);
    </script>



Note that this JavaScript function only detects whether the plugin is
installed; it cannot report the plugin version number, and even if the plugin
is installed there is no guarantee that the plugin actually runs on this
browser. In order to test either of these, you have to use the plugin to embed
a p3d file and query the resulting embedded object.

Note also that :ref:`RunPanda3D.js <embedding-with-runpanda3d>` can also be
used to do some simple plugin detection, using the noplugin_img and
noplugin_href tags.
