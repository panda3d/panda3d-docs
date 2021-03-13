.. _configuring-panda3d:

Configuring Panda3D
===================

In the etc subdirectory, you will find a configuration file Config.prc. This
controls several of Panda's configuration options - does it use OpenGL or
DirectX, how much debugging output does it print, and so forth. The following
table lists several of the most commonly-used variables.

For a full documentation about Panda3D's configuration system, click
`here <https://raw.githubusercontent.com/panda3d/panda3d/release/1.10.x/panda/src/doc/howto.use_config.txt>`__
to view the original documentation file.

To know about accessing config variables from within your code, please see
:ref:`accessing-config-vars-in-a-program`.

To get a more complete list of variables, see the
:ref:`list of all config variables <list-of-all-config-variables>`.

====================== ================ ================== ========================================================================================================================================================
Variable               Values           Default            Details
====================== ================ ================== ========================================================================================================================================================
load-display           pandagl          pandagl            Specifies which graphics GSG to use for rendering (OpenGL, Direct3D 8/9 or TinyPanda software rendering)

                       pandadx9

                       pandadx8

                       p3tinydisplay
aux-display            pandagl          pandagl            Specifies which graphics GSG to use if the GSG specified in load-display fails; May be specified multiple times to create multiple fallbacks.

                       pandadx9

                       pandadx8

                       p3tinydisplay
win-size               Number of pixels 640 480            Specifies the size of the Panda3D window
win-origin             Pixel offsets    50 50              Specifies the offset of the Panda3D window
window-title           Window title     Panda              Specifies the title of the Panda3D window
fullscreen             true             false              Enables full-screen mode (true or false)

                       false
undecorated            true             false              Removes border from window (true or false)

                       false
cursor-hidden          true             false              Hides mouse cursor (true or false)

                       false
sync-video             true             true               Limits the frame rate to monitor's capabilities

                       false
show-frame-rate-meter  true             false              Shows the frame rate (in frames per second) at the upper right corner of the screen (true or false)

                       false
notify-level-[package] fatal            info               Sets notification levels for various Panda3D packages to control the amount of information printed during execution (fatal being least, spam being most)

                       error

                       warning

                       info

                       debug

                       spam
model-path             Path string      see config file    Adds specified path to the list of paths searched when loading a model
audio-library-name     p3openal_audio   p3openal_audio     Loads the appropriate audio library

                       p3fmod_audio

                       p3miles_audio

                       null
want-directtools       true             true               Enables directtools, a suite of interactive object/camera manipulation tools

                       false            line commented out
want-tk                true             true               Enables support for using Tkinter/PMW (Python's wrappers around Tk)

                       false            line commented out
====================== ================ ================== ========================================================================================================================================================
