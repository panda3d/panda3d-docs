.. _distributing-as-a-self-contained-installer:

Distributing as a self-contained installer
==========================================

Note: This article describes a deprecated feature as of Panda3D 1.10.0.

It is possible to distribute your p3d file as a fully self-contained
application. You can use your p3d file to generate a custom installer, and
distribute this installer to your users. The installer will produce a
fully-self-contained application that doesn't require the user to install the
Panda3D plugin separately. The user never needs to know that he/she is running
Panda3D at all.

This can be done using the
``pdeploy`` utility. It has the
ability generate a graphical installer for every known platform, so you will
never need to boot a different operating system just to generate an installer
for that platform. However, note that pdeploy requires an internet connection
to run.

For information about command-line options, you can invoke:


.. code-block:: bash

    pdeploy -h

This will print the
help text for pdeploy, along with information about every supported
command-line option.

Generating an installer
-----------------------

You can create a graphical installer for your game using a command similar to:


.. code-block:: bash

    pdeploy -s -N "My Cool Game" -v 1.0.0 myCoolGame.p3d installer

This will create
various subdirectories in the current directory, one for every platform,
containing graphical installers that install your game. (You can specify a
custom output directory with the -o option.) The Panda3D libraries are not
packed with the installer, but they will be automatically downloaded when the
game is ran for the first time.

The -s option ensures a self-contained installer is created that does not
require an internet connection to run. The resulting installers will also
contain the Panda3D libraries and will be larger. In case you want to produce
much lighter installers that do not contain the Panda3D libraries themselves,
simply omit the -s option. In this case, the game will automatically download
the latest stable version of the Panda3D libraries and install it into the
user's cache directory on launch (only the first time, though, or when there
are updates available).

By default, pdeploy will generate an installer for every known platform. You
can also specify a custom set of platforms, by adding the -P option followed
by the platform name. You may repeat -P as many times as necessary. To
generate an installer only for the current platform, use the -c option. If -c
is provided, any -P options are ignored.

You can also let pdeploy pass custom tokens to the application, as described
in :ref:`advanced-object-tags` and :ref:`splash-window-tags`. You can simply
pass tokens to pdeploy using the -t token=value option, and you may repeat the
-t option as many times as you need.

In Panda3D versions 1.8 and above, you can let pdeploy generate a custom icon
for the installed game. Use and repeat the -i option to pass several image
files of different square sizes, which will be combined into a single icon
file by pdeploy. To support all platforms, it is recommended to supply images
of the sizes 16x16, 32x32, 48x48, 128x128, 256x256, and 512x512, but you may
omit the latter two or three sizes if you cannot provide images in that
resolution. It is recommended to use .png images for correct transparency.

When running the resulting game, the window will be placed in the center of
the screen, unless explicitly overridden in the application. You can pass a
custom height and width for the window using the 'width' and 'height' tokens.

Note: Even though most of the informational command-line arguments are
optional, it is highly recommended to specify as many of them as possible, to
provide the most accurate description for your application.

Example
~~~~~~~

This fictional example shows how to use pdeploy and commonly-used options.
(You may want to omit the -P options to generate for every platform.) This is
a single command, line breaks are merely added to avoid this manual page from
stretching. 

.. code-block:: bash

    pdeploy -s -n coolgame -N "My Cool Game" -v 1.0.0 -a com.cool_company -A "Cool Company"
    -e packager@cool_company.com -l "Modified BSD License"
    -L bsd.txt -t width=800 -t height=600
    -i icon16.png -i icon32.png -i icon48.png -i icon128.png 
    -P linux_amd64 -P win32 -P osx_i386 coolGame.p3d installer



Generating a launcher executable
--------------------------------

Instead of a graphical installer, pdeploy also has the ability to generate a
standalone launcher executable. It works similar to tools like py2exe, but is
designed to embed .p3d games. This will not require a Panda3D installation to
run - instead, when running it, it will automatically download and install the
Panda3D libraries. The pdeploy command-line looks like this:


.. code-block:: bash

    pdeploy myCoolGame.p3d standalone

Like when generating an
installer, you can use the -c and P options to specify a custom set of
platforms to generate for, -o to specify a custom output directory, and -t to
pass custom tokens.

Note that the resulting executable will have some dependencies, such as the
X11 libraries on Unix, and the Visual C++ 2008 runtime on Windows. It will not
run if those libraries are not present on the system. You should use the
"installer" option, as explained above, for a fully self-contained installer
that contains the dependent libraries.
