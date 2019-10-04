.. _splash-window-tags:

Splash window tags
==================

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

The following table lists the custom P3D tokens that you may specify within
the <object> element, as described in :ref:`advanced-object-tags`. You can use
these settings to customize the look of the app's embedded frame whenever the
Panda3D window is not being displayed, e.g. before or after launch.

When deploying an application for the desktop, you can specify these tags with
the ``-t tag=value`` flag to pdeploy.

============= ==================================================================================================================================================================================================================================================================================================
Token         Meaning
============= ==================================================================================================================================================================================================================================================================================================
splash_img    The URL of an image to display in the plugin space, anytime before Panda starts running (unless a more specific image, below, overrides)
download_img  The image to display while the p3d file and its required packages are being downloaded
unauth_img    The image to display when the app is unrecognized, and is waiting for the user to click the red "authorize" button
ready_img     The image to display when the app is ready to run, and waiting for the user to click the green "play" button
failed_img    The image to display when the app cannot launch for some reason (e.g. bad URL)
launch_img    The image to display while the app is launching: the time after the user has clicked "play" and before it actually opens its Panda3D window
active_img    The image to display while the app is running (but the app has taken its window out of the frame)
noplugin_img  This is available only if you use the :ref:`RunPanda3D.js <embedding-with-runpanda3d>` method of embedding your p3d file. In this case, this specifies the image to display if the plugin is not installed or cannot be run for some reason.
noplugin_href As above, this is available only if you use the RunPanda3D.js method of embedding your p3d file, and it specifies the URL that the user should be taken to if he or she clicks on the embed region when the plugin is not installed. A good choice, for instance, is https://www.panda3d.org/get .
auth_ready    The three images that define the normally red "authorize" button
             
auth_rollover
             
auth_click   
play_ready    The three images that define the normally green "play" button
             
play_rollover
             
play_click   
fgcolor       The text color of the text that may appear in the window, default is black.
bgcolor       The background color of the window before the app has launched, default is white.
barcolor      The fill color of the loading bar that is shown before the app launches
bar_bgcolor   The background color of the loading bar. If not set, the bgcolor is used.
bar_border    The width of the border around the loading bar, in pixels. Set to 0 to disable the border.
bar_bottom    The number of pixels between the bottom of the window and the bottom edge of the loading bar.
bar_width     Width of the loading bar, in pixels. Alternatively, you may specify it as a percentage of the window width, eg. '60%'
bar_height    Height of the loading bar, in pixels. Alternatively, you may specify it as a percentage of the window height, eg. '5%'
font_family   Specify which font to use for the text that may appear in the splash window. Default is 'Helvetica'.
font_size     The font size, in pixels. Default is 12.
font_style    Changes the slant of the font. Acceptable values are 'normal', 'oblique' and 'italic'.
font_weight   This may be set to 'bold' in order to make the font bold. Some platforms may support a numeric value between 100 and 900 (in increments of 100), where 100 is lightest, 400 is normal, and 900 is black.
============= ==================================================================================================================================================================================================================================================================================================
