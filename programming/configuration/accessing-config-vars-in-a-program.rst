.. _accessing-config-vars-in-a-program:

Accessing Config Vars in a Program
==================================

Panda3D uses a :ref:`configuration file <configuring-panda3d>` named
Config.prc. Panda3D supplies functions to easily read values out of
Config.prc, and to alter their values in memory (the modified values are not
written back out to disk). The ability to read and alter configuration settings
procedurally has two major uses:

#. Storing your own configuration data.
#. Tweaking Panda3D's behavior.

"Storing your own configuration data" means that your game might have its own
settings that need to be stored. Rather than writing your own configuration
file parser, you might consider adding your configuration data to the panda
configuration file instead.

Suppose hypothetically that you are writing an online game, and your online
game connects to a server. You need a configuration file to tell you the name
of the server. Open up the "Config.prc" file and add the following line at the
end of the file.

.. code-block:: text

   my-game-server panda3dgame.com

Note
that I invented the variable name "my-game-server" out of thin air. This
variable is not recognized by Panda3D in any way. Therefore, this line has no
effect on the engine whatsoever.

To manipulate this variable procedurally, use code not unlike the following,
which creates an object of class :class:`.ConfigVariableString` and then
manipulates it using the methods :meth:`~.ConfigVariableString.set_value()` and
:meth:`~.ConfigVariableString.get_value()`.

.. only:: python

   .. code-block:: python

      from panda3d.core import ConfigVariableString

      myGameServer = ConfigVariableString('my-game-server', '127.0.0.1')
      print('Server specified in config file: ', myGameServer.getValue())

      # Allow the user to change servers on the command-line.
      if (sys.argv[1] == '--server'):
          myGameServer.setValue(sys.argv[2])
      print('Server that we will use: ', myGameServer.getValue())

The second parameter to the ConfigVariableString constructor is the default
value that should be returned, in case the line "my-game-server" does not
appear in any Config.prc file. There is also an optional third parameter,
which is a description of the purpose of the variable.

.. only:: python

   This string will be displayed when the user executes the command
   ``print(cvMgr)``.

The types of configuration variable are:

ConfigVariableString
ConfigVariableInt
ConfigVariableBool
ConfigVariableColor
ConfigVariableDouble
ConfigVariableFilename
ConfigVariableList
ConfigVariableSearchPath

Most of these follow the same form as ConfigVariableString, above, except that
the value is of the indicated type, rather than a string. The two exceptions are
ConfigVariableList and ConfigVariableSearchPath. These types of variables do not
accept a default value to the constructor since the default value in both cases
is always the empty list or search path.

.. only:: python

   To display the current value of a particular variable interactively (for a
   string-type variable in this example), type the following:

   .. code-block:: python

      print(ConfigVariableString("my-game-server"))

Panda3D will automatically load any PRC files it finds in its standard config
directory at start-up.

.. only:: python

   You can view a list of the files it has actually loaded with the following
   command:

   .. code-block:: python

      print(cpMgr)

   It is helpful
   to do this to ensure that you are editing the correct Config.prc file.

Sometimes, it is desirable to load an additional configuration file from disk,
by giving an explicit filename. To do so, use :func:`.load_prc_file()`. Note
that :ref:`filename-syntax` uses a forward slash even under Windows.

.. only:: python

   .. code-block:: python

      from panda3d.core import loadPrcFile

      loadPrcFile("config/Config.prc")

.. only:: cpp

   .. code-block:: cpp

      #include "load_prc_file.h"

      load_prc_file("config/Config.prc");

The filename you specify is searched for along the model-path, in the same way
that an Egg or Bam file is searched for when you use
:py:meth:`loader.loadModel() <direct.showbase.Loader.Loader.loadModel>`.

.. only:: python

   You should load your own PRC file before instantiating ShowBase.  Changing
   certain configuration variables later on may not affect the
   window/environment that has already been created.

.. only:: cpp

   You should load your own PRC file before opening the window.  Changing
   certain configuration variables later on may not affect the
   window/environment that has already been created.

You can also use :func:`.load_prc_file_data()` to load a string that you define
in your code, as if it were the contents read from a disk file. The
:func:`.load_prc_file_data()` call requires two parameters. The first parameter
is an arbitrary string name to assign to this "file" (and it can be the empty
string if you don't care), while the second parameter is the contents of the
file itself. This second parameter should contain newlines between variable
definitions if you want to set the value of more than one variable.

For example, let's say that Panda3D's configuration file contains this line:

.. code-block:: text

   fullscreen #f

By default, Panda3D programs will run in a window, not fullscreen. However, if
you do this, then by the time you instantiate ShowBase, you will have changed
the fullscreen-flag to true, and your program will run in fullscreen.

.. only:: python

   .. code-block:: python

      from panda3d.core import loadPrcFileData

      loadPrcFileData('', 'fullscreen true')

.. only:: cpp

   .. code-block:: cpp

      #include "load_prc_file.h"

      load_prc_file_data("", "fullscreen true");

There are other ways to go to fullscreen. This is not necessarily the most
straightforward approach, but it illustrates the point.

You can get a more complete list of available config variables at runtime,
with the :meth:`~.ConfigVariableManager.list_variables()` method:

.. only:: python

   .. code-block:: python

      cvMgr = ConfigVariableManager.getGlobalPtr()
      cvMgr.listVariables()

.. only:: cpp

   .. code-block:: cpp

      ConfigVariableManager::get_global_ptr()->list_variables();

For a more complete documentation about Panda3D's configuration system, view
the `original documentation
file <https://raw.githubusercontent.com/panda3d/panda3d/master/panda/src/doc/howto.use_config.txt>`__.
