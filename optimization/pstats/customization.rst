.. _pstats-customization:

Customizing the UI
==================

Default Graph Layout
--------------------

By default, when a client connects, the PStats server only opens a single strip
chart window. It can be tedious to reopen the desired graphs every time that you
make a change to the client and wish to re-analyze its performance. Therefore,
it is possible to define which graphs are opened automatically when a client
connects, including the positions these graph windows will have on screen.
To do this, simply open the desired graph windows and move them around as
as desired, and then click "Save Current Layout as Default" in the Graphs menu.
This will cause the server to remember the current layout of the graph windows.
The next time you start a new session and connect a client, all of the
previously saved graph windows will be reopened.

Collector Colors
----------------

While some collectors are assigned colors in the Panda3D source code, other
collectors will receive a randomly generated color. Sometimes, these randomly
generated colors clash with other collectors, making the charts hard to read.
It is possible to specify a custom color for a collector by right-clicking the
label for this collector and choosing "Change Color". The chosen color is
immediately reflected in all charts showing this collector and stored in the
session file if it is written to disk. To make the change apply to future
sessions, use the "Save Current Layout as Default" option to commit it to the
default layout.

Other Optional Collector Properties
-----------------------------------

A more permanent way to specify a color is to modify
panda/src/pstatclient/pStatProperties.cxx, and add a line to the table for your
new collector(s). You can also define additional properties here such as a
suggested initial scale for the graph and, for non-time-based collectors, a unit
name and/or scale factor. The order in which these collectors are listed in this
table is also relevant; they will appear in the same order on the graphs.
The first column should be set to 1 for your new collectors unless you wish them
to be disabled by default. You must recompile the client (but not the server) to
reflect changes to this table.
