.. _searching-the-scene-graph:

Searching the Scene Graph
=========================

It is often useful to get a handle to a particular node deep within the scene
graph, especially to get a sub-part of a model that was loaded from a single
file. There are a number of methods dedicated to finding entrenched nodes and
returning the NodePaths.

First, and most useful, is the :meth:`~.NodePath.ls()` command:

.. only:: python

   .. code-block:: python

      myNodePath.ls()

.. only:: cpp

   .. code-block:: cpp

      myNodePath.ls();

This simply lists all of the children of the indicated NodePath, along with all
of their children, and so on until the entire subgraph is printed out. It also
lists the transforms and :ref:`render-attributes` that are on each node. This is
an especially useful command for when you're running interactively with Python;
it's a good way to check that the scene graph is what you think it should be.

The two methods :meth:`~.NodePath.find` and :meth:`~.NodePath.find_all_matches`
will return a :class:`~.NodePath` and a :class:`~.NodePathCollection`
respectively. These methods require a path string as an argument. Searches can
be based on name or type. In its simplest form this path consists of a series of
node names separated by slashes, like a directory pathname. When creating the
string each component may optionally consist of one of the following special
names, instead of a node name.

============== =======================================================
``*``          Matches exactly one node of any name
``**``         Matches any sequence of zero or more nodes
``+typename``  Matches any node that is or derives from the given type
``-typename``  Matches any node that is the given type exactly
``=tag``       Matches any node that has the indicated tag
``=tag=value`` Matches any node whose tag matches the indicated value
============== =======================================================

Furthermore, a node name may itself contain standard filename globbing
characters, like \*, ?, and [a-z], that will be accepted as a partial match. (In
fact, the '*' special name may be seen as just a special case of this.) The
globbing characters may not be used with the typename matches or with tag
matches, but they may be used to match a tag's value in the =tag=value syntax.

The special characters "@@", appearing at the beginning of a node name, indicate
a stashed node. Normally, stashed nodes are not returned by a find (but see the
special flags, below), but a stashed node may be found if it is explicitly named
with its leading @@ characters. By extension, "@@*" may be used to identify any
stashed node.

Examples:

``"room//graph"`` will look for a node named "graph", which is a child of an
unnamed node, which is a child of a node named "room", which is a child of the
starting path.

``"**/red*"`` will look for any node anywhere in the tree (below the starting
path) with a name that begins with "red".

``"**/+PartBundleNode/**/head"`` will look for a node named "head", somewhere
below a PartBundleNode anywhere in the tree.

The argument may also be followed by one or more optional control flags. To use
a control flag, add a semicolon after the argument, followed by at least one of
the special flags with no extra spaces or punctuation.

====== =========================================================================
``-h`` Do not return hidden nodes
``+h`` Return hidden nodes
``-s`` Do not return stashed nodes unless explicitly referenced with @@
``+s`` Return stashed nodes even without any explicit @@ characters
``-i`` Node name comparisons are not case insensitive: case must match exactly
``+i`` Node name comparisons are case insensitive: case is not important. This
       affects matches against the node name only; node type and tag strings are
       always case sensitive
====== =========================================================================

The default flags are ``+h-s-i``.

The :meth:`~.NodePath.find` method searches for a single node that
matches the path string given. If there are multiple matches, the method returns
the shortest match. If it finds no match, it will return an empty NodePath. On
the other hand, :meth:`~.NodePath.find_all_matches` will return all
NodePaths found, shortest first.

.. only:: python

   .. code-block:: python

      myNodePath.find("<Path>")
      myNodePath.findAllMatches("<Path>")

.. only:: cpp

   .. code-block:: cpp

      myNodePath.find("<Path>");
      myNodePath.find_all_matches("<Path>");

Some examples:

.. only:: python

   .. code-block:: python

      myNodePath.find("house/door")

.. only:: cpp

   .. code-block:: cpp

      myNodePath.find("house/door");

This will look for a node named "door", which is a child of a node named
"house", which is a child of the starting path.

.. only:: python

   .. code-block:: python

      myNodePath.find("**/red*")

.. only:: cpp

   .. code-block:: cpp

      myNodePath.find("**/red*");

This will look for any node anywhere in the tree (below the starting path) with
a name that begins with "red".

.. only:: python

   .. code-block:: python

      shipNP.findAllMatches("**/=type=weaponMount")

.. only:: cpp

   .. code-block:: cpp

      shipNP.findAllMatches("**/=type=weaponMount");

This will search shipNP recursively using tag/value. Tag name is "type" and
tag value is "weaponMount". All matches found will be returned.

In addition there are also the methods :meth:`~.NodePath.get_parent()` and
:meth:`~.NodePath.get_children()`. :meth:`~.NodePath.get_parent()` returns the
NodePath of the parent node. :meth:`~.NodePath.get_children()` returns the
children of the current node as a :class:`~.NodePathCollection`.

.. only:: python

   The NodePathCollection can be treated like any Python sequence:

   .. code-block:: python

      for child in myNodePath.getChildren():
          print(child)

.. only:: cpp

   .. code-block:: cpp

      NodePathCollection children = myNodePath.get_children();
      for (int i = 0; i < children.size(); ++i) {
          std::cout << children[i] << "\n";
      }

For more information and a complete list of NodePath functions please see the
:class:`~.NodePath` page in the API Reference.
