.. _p3d-file-config-settings:

P3D file config settings
========================

.. warning::

   This article describes a deprecated feature as of Panda3D 1.10.0.

You can set certain config settings in a p3d file on the packp3d command line.
These control the way the p3d file may be used or embedded.

Some of these settings can also be set in the
:ref:`HTML object tags <advanced-object-tags>` used when the p3d file is
embedded on a web page. If a config setting is specified in both places, the
HTML page overrides.

================ =================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
Setting          Meaning
================ =================================================================================================================================================================================================================================================================================================================================================================================================================================================================================
auto_start       "1" to launch the app without waiting for the green "play" button
hidden           "1" to avoid opening a Panda3D window
log_basename     Specifies the log file within Panda3D/log to write to for this app
prc_name         Specifies a directory name within Panda3D/prc from which user prc files custom to this app will be loaded
start_dir        Specifies a directory name within Panda3D/start which will be the current directory when this application starts. This is not used if keep_user_env, below, is set "1".
allow_python_dev "1" to allow the user to break into and debug the Python code, with the "-i" option to panda3d. The -D option to packp3d and ppackage is also provided as a convenient way to to set this option.
keep_user_env    "1" if the user's environment variables, and current working directory, should be preserved when running this app. Normally, most environment variables are reset to default values, or cleared altogether. You would normally specify this for a command-line app, where the user may want to preserve his or her environment; for instance, packp3d.p3d itself sets this option. It doesn't make sense to set this for a p3d file that is intended to be run within a web page.
run_origin       The semicolon-separated list of hostnames that are allowed to embed this app in a web page. The default is any hostname. See :ref:`p3d-origin-security`.
script_origin    The semicolon-separated list of hostnames that are allowed to directly call Python methods exposed by this app from JavaScript in a web page. The default is no hostname. See :ref:`p3d-origin-security`.
height           The default size of the window created for the p3d file, when it is run from the desktop (or via the panda3d application). This is not used when the p3d file is embedded in a web page, because in that case the embed will specify the height and width.
                
width           
================ =================================================================================================================================================================================================================================================================================================================================================================================================================================================================================

To specify a config option, use the command-line option
``-c setting=value`` on the packp3d command
line, or use the ``config(setting = 'value')``
function in the pdef file. You can repeat these options to set multiple config
settings on a given file.

All of these config settings are actually stored in the p3d_info.xml file that
is embedded within the p3d multifile. Since they become part of the p3d file
itself, the precise config settings are part of the date that is signed when
you sign a p3d file; thus, changing any of these settings later (without
re-signing) will invalidate your signature. This prevents people from changing
your app's config settings without your approval.
