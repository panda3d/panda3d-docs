.. _plugin-notify-callbacks:

Plugin notify callbacks
=======================

Note: This article describes a deprecated feature as of Panda3D 1.10.0.

At key points during application launch, the plugin will make optional
callbacks into JavaScript code, so your page can respond to what the
application is doing. This is done using the <object> token system, as
described in :ref:`advanced-object-tags`.

The following events may be sent:

================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================
Token              Meaning
================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================
onPluginFail       The plugin cannot load for some reason, for instance because the browser is an incompatible version, or because the plugin is critically out-of-date with its associated Core API, and needs to be updated. If you get this event, you will not receive any of the following. Note that certain kinds of browser incompatibilities result in the plugin never running in the first place, so there exist incompatibility cases in which you will not receive any event at all.
onPluginLoad       The browser has activated the object tag, and initialized the plugin. This usually happens after the standard JavaScript page load notification. See below.
onUnath            The p3d file has been scanned and needs to be approved by the user. There will be a red play button drawn in the plugin window (if it is visible); when the user clicks this button, it will pop up the certificate-approval dialog. You can simulate the user clicking the button by calling plugin.main.play().
onAuth             The p3d file has been approved by the user as a result of going through the above dialog; or the p3d file was recognized as being already approved at startup.
onDownloadBegin    The packages referenced by the p3d file are beginning to download. See below.
onDownloadNext     This event will be generated as each required package finishes downloading and the next one begins. See below.
onDownloadComplete Generated when the download finishes, or when it is determined at startup time that all packages are already downloaded.
onReady            The application is ready to begin. If you have auto_start="1", then it will launch immediately; otherwise, there will be a green play button drawn in the plugin window (if it is visible). You can simulate the user clicking the button by calling plugin.main.play().
onPythonLoad       The Python part of the application has begun. This is part of application startup. At the time you receive this event, your application has only just begun to execute; there is no guarantee that it has assigned anything to appRunner.main at this point.
onWindowOpen       The application has successfully created a graphics window, and is now considered fully launched. From the Python side, it means that your application has imported DirectStart by this point.
onWindowAttach     The application has attached its graphics window to the plugin frame, and the window is now embedded in the web page. This may be called at initial startup (possibly before onWindowOpen), and also after a subsequent call to onWindowDetach.
onWindowDetach     The application has removed its game window from the plugin frame. This may be called at application exit, or whenever the application itself removes the window from the frame (for instance, to go to a fullscreen or toplevel window instead). The Panda plugin will display active_img in the plugin frame whenever it is not occupied by the graphics window.
onPythonStop       The application has exited, either normally or due to an error.
================== ==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================

In addition to the above list, a particular application may define its own
custom callbacks, by calling base.appRunner.notify('token'), e.g.
base.appRunner.notify('onLevelStart').

To use any of the above, assign the token to a JavaScript expression which
should be evaluated when the event occurs. Usually this is a call to one of
your own JavaScript functions, e.g.:



.. code-block:: html

    <object width="640" height="480"
      type="application/x-panda3d" data="myapp.p3d"
      onWindowOpen="MyWindowFunction()"
    </object>



You should use the appropriate embedding syntax as described in
:ref:`advanced-object-tags`.

Additional notes
----------------

At each of the above events, certain properties of the plugin object become
defined and available for access by JavaScript. In the following, "plugin" is
assumed to be the DOM object that refers to the embedding <object> element.

After onPluginLoad, you can query certain built-in properties on the plugin:

==================================
plugin.main.status
plugin.main.pluginVersionString
plugin.main.pluginMajorVersion
plugin.main.pluginMinorVersion
plugin.main.pluginSequenceVersion
plugin.main.pluginNumericVersion
plugin.main.pluginDistributor
plugin.main.coreapiHostUrl
plugin.main.coreapiTimestamp
plugin.main.coreapiTimestampString
==================================

You can also call plugin.main.get_system_log() at any point after this to
query the current system log. This is the log file generated by the plugin
system. You can specify an optional numeric parameter; this limits the return
value to only the specified number of bytes at the end of the log.

Note that there appears to be a Firefox bug that sometimes causes the first
reference to plugin.main to return undefined, even though it has actually been
defined by this point. This is especially likely after a page reload (F5)
operation. If this causes you trouble, you may need to work around this with a
JavaScript timeout callback.

After onDownloadBegin, you can query the following properties to monitor the
download:

======================================
plugin.main.numDownloadingPackages
plugin.main.totalDownloadSize
plugin.main.downloadProgress
plugin.main.downloadElapsedSeconds
plugin.main.downloadElapsedFormatted
plugin.main.downloadRemainingSeconds
plugin.main.downloadRemainingFormatted
plugin.main.downloadPackageName
plugin.main.downloadPackageDisplayName
plugin.main.downloadComplete
======================================

After onDownloadNext, downloadPackageName and downloadPackageDisplayName will
be updated with the currently-downloading package. Note that
plugin.main.downloadProgress tracks from 0 .. 1 throughout the entire
download; it doesn't reset for each package.

After onPythonLoad, you can call plugin.main.get_game_log() to query the game
log. This is the output from the application itself. Like get_system_log(),
you can specify an optional numeric parameter to limit the return value to
only the specified number of bytes at the end of the log.
