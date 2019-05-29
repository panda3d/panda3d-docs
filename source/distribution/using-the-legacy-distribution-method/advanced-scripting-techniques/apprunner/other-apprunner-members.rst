.. _other-apprunner-members:

Other appRunner members
=======================

Note: This article describes a deprecated feature as of Panda3D 1.10.0.

-  appRunner.Undefined

The JavaScript language has two different value types that are conceptually
similar to Python's None type: the null type, and the void or undefined type.
The plugin system could convert both of these to Python's None, but sometimes
it is important to make a distinction between them.

To solve this problem, the plugin converts the Javascript null type to
Python's None, and the void/undefined type to base.appRunner.Undefined, which
is a special singleton that has no properties, similar to None. To check for
undefined, you can use (object == base.appRunner.Undefined) or (object is
base.appRunner.Undefined). Since Undefined evaluates to false in a boolean
test, you could also just use "if object:" to test for whether an object is
neither None nor Undefined.

-  appRunner.ConcreteStruct

Most Python objects are passed to JavaScript by reference, the same way Python
deals with them internally. This means that if you store an object on
base.appRunner.main, the JavaScript code can query and update its members
individually, and those changes are visible on the Python side.

Often, you only need to provide a read-only object to JavaScript, and you
don't want the additional overhead that's required to make the object
writable. In this case, you can make your object an instance of (or inherit
from) appRunner.ConcreteStruct. This tells the plugin that there is no need
for JavaScript to modify its contents, and it will copy all of its members to
JavaScript once, at the time that JavaScript first accesses the overall
object, and not have to go back-and-forth between Python and JavaScript with
each individual member access. Only the data members are transmitted; callable
methods of ConcreteStruct are not supported. This is a performance
optimization only; everything will still work perfectly well if you don't do
this.

Note that in order to gather the full benefit of this optimization, your
JavaScript code should access the Python object only once and store it
locally, rather than querying it repeatedly out of plugin.main.

-  appRunner.multifileRoot

When the AppRunner mounts your p3d file into the VirtualFileSystem, it
installs it in the directory named by appRunner.multifileRoot. This directory,
then, is the root directory of the contents of your p3d file. If you need to
load a file directly out of your p3d file, look for it here. At the moment,
this is a constant string; but future releases of Panda might need to install
the multifile into a different place each time, so you should not write code
that depends on this string being fixed.

-  appRunner.exceptionHandler

You can assign a Python function object to this member. This function will be
called whenever a Python exception propagates to the top of the call stack;
you can use this to deal appropriately with unexpected behavior in your
application. If you do not assign this, the default behavior for an uncaught
exception will be to terminate the app.

-  appRunner.windowProperties

This is the WindowProperties structure that is used for the initial window
that is created when you import DirectStart; you can use this if you want to
re-create a new window in the same place later (for instance, because you have
an in-game option to switch between fullscreen and embedded mode).

-  appRunner.installPackage()

Call this method to download and install a Panda3D package, as built by the
ppackage.p3d utility, at runtime. This allows you to install the package at
your leisure, instead of requiring the package to be downloaded before
starting the p3d application.

Note that this method runs synchronously: it will download the package
on-the-spot, however long that takes, and not return until it has finished. If
you want to use an asynchronous download instead, downloading a package in the
background while gameplay continues, you should use the
:ref:`packageinstaller` interface instead.

-  appRunner.notifyRequest()

This allows you to define your own callback events, similar to the built-in
ones described in :ref:`plugin-notify-callbacks`. Simply call
base.appRunner.notifyRequest(name), where name is the name of your callback
event; for example base.appRunner.notifyRequest('onGameRestart'). There is no
facility to pass parameters; if you need to call a JavaScript function with
parameters, use a different mechanism, such as calling the function directly
through appRunner.dom, or use appRunner.evalScript(), below.

-  appRunner.evalScript()

Whatever string you pass to base.appRunner.evalScript() is evaluated and
executed directly in the JavaScript environment. By default, the return value,
if any, is not preserved; but if you need the return value you can also pass
needsResponse = True.
