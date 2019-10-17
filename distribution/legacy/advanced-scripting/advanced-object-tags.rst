.. _advanced-object-tags:

Advanced object tags
====================

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

When you embed a Panda3D application in a web page, either with the <object>
tag or with P3D_RunContent, you specify certain key pieces of information such
as window size and p3d URL.

You can specify more exotic things too:

=============== ====================================================================================================================================================
Token           Meaning
=============== ====================================================================================================================================================
auto_start      "1" to launch the app without waiting for the green "play" button
hidden          "1" to avoid opening a Panda3D window
keep_pythonpath "1" to allow the user's PYTHONPATH environment variable to remain intact, and thus to override Python files within the app (requires -D on p3d file)
log_basename    Specifies the log file within Panda3D/log to write to for this app
prc_name        Specifies a directory name within Panda3D/prc from which user prc files custom to this app will be loaded
alt_host        Specifies one of the "alternate host" keywords defined for the p3d file's download host, to enable alternate download contents
=============== ====================================================================================================================================================

In addition to the above list, you may specify any of numerous splash image
URL's, or any of the plugin notify callbacks; these are described on the
following pages.

Furthermore, you can specify tokens that have particular meaning to your own
application. Any additional tokens you specify are passed to the application
and can be queried by Python code via base.appRunner.getToken('keyword'), so
any application is free to define its own custom tokens.

To use any of the above, specify the token and the value as a pair in the
embedding HTML syntax. In the Internet Explorer syntax, this means you use the
<param> element, e.g.:

.. code-block:: html

   <object width="640" height="480"
     classid="CLSID:924B4927-D3BA-41EA-9F7E-8A89194AB3AC">
       <param name="data" value="myapp.p3d">
       <param name="splash_img" value="my_splash.jpg">
       <param name="auto_start" value="1">
   </object>

In the non-Internet Explorer syntax, you can use the <param> element as above,
or you can insert the token directly within the <object> tag, e.g.:

.. code-block:: html

   <object width="640" height="480"
     type="application/x-panda3d" data="myapp.p3d"
     splash_img="my_splash.jpg" auto_start="1">
   </object>

When using RunPanda3D, you just add the token and value as a pair of strings to
the P3D_RunContent() call:

.. code-block:: javascript

   P3D_RunContent('data', 'myapp.p3d', 'id', 'myapp_id',
       'width', '640', 'height', '480',
       'splash_img', 'my_splash.jpg', 'auto_start', '1')
   }
