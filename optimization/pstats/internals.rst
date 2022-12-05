.. _pstats-internals:

PStats Internals
================

The PStats code is divided into two main parts: the client code and the server
code.

The PStats Client
-----------------

The client code is in panda/src/pstatclient, and is available to run in every
Panda client unless it is compiled out. (It will be compiled out when building
for Release in CMake or when passing ``--optimize 4`` to makepanda, unless
DO_PSTATS is also explicitly set to non-empty.)

The client code is designed for minimal runtime overhead when it is compiled in
but not enabled (that is, when the client is not in contact with a PStats
server), as well as when it is enabled (when the client is in contact with a
PStats server). It is also designed for zero runtime overhead when it is
compiled out.

There is one global :class:`.PStatClient` class object, which manages all of the
communications on the client side. Each :class:`.PStatCollector` is simply an
index into an array stored within the :class:`.PStatClient` object, although the
interface is intended to hide this detail from the programmer.

Initially, before the :class:`.PStatClient` has established a connection, calls
to :meth:`~.PStatCollector.start()` and :meth:`~.PStatCollector.stop()` simply
return immediately.

When you call :meth:`.PStatClient.connect()`, the client attempts to contact the
PStatServer via a TCP connection to the hostname and port named in the
pstats-host and pstats-port Config.prc variables, respectively. (The default
hostname and port are localhost and 5185.) You can also pass in a specific
hostname and/or port to the :meth:`~.PStatClient.connect()` call. Upon
successful connection and handshake with the server, the :class:`.PStatClient`
sends a list of the available collectors, along with their names, colors, and
hierarchical relationships, on the TCP channel.

Once connected, each call to :meth:`~.PStatCollector.start()` and
:meth:`~.PStatCollector.stop()` adds a collector number and timestamp to an
array maintained by the PStatClient. At the end of each frame, the PStatClient
boils this array into a datagram for shipping to the server.
Each :meth:`~.PStatCollector.start()` and :meth:`~.PStatCollector.stop()` event
requires 6 bytes; if the resulting datagram will fit within a UDP packet (1K
bytes, or about 84 start/stop pairs), it is sent via UDP; otherwise, it is sent
on the TCP channel. (Some fraction of the packets that are eligible for UDP,
from 0% to 100%, may be sent via TCP instead; you can specify this with the
``pstats-tcp-ratio`` Config.prc variable.)

Also, to prevent flooding the network and/or overwhelming the PStats server,
only so many frames of data will be sent per second. This parameter is
controlled by the ``pstats-max-rate`` Config.prc variable and is set to 30 by
default. (If the packets are larger than 1K, the max transmission rate is also
automatically reduced further in proportion.) If the frame rate is higher than
this limit, some frames will simply not be transmitted. The server is designed
to cope with missing frames and will assume missing frames are similar to their
neighbors.

Finally, to prevent an excessive backlog building up if there is too much data
for the transmission to handle, Panda3D will only queue up a certain number of
frames of data at a time. This is determined by the value of the
``pstats-max-queue-size`` variable. If the backlog of frames to send is greater
than this value, subsequent frames are dropped. Note that each thread sends its
own frame, so you need to make sure this value is at least as large to
accommodate all the threads sending data at once.

The server does all the work of analyzing the data after that. The client's next
job is simply to clear its array and prepare itself for the next frame.

The PStats Server
-----------------

The generic server code is in pandatool/src/pstatserver, and the GUI-specific
server code is in pandatool/src/gtk-stats and pandatool/src/win-stats, for Unix
and Windows, respectively. (There is also an OS-independent text-stats
subdirectory, which builds a trivial PStats server that presents a scrolling-
text interface. This is mainly useful as a proof of technology rather than as a
usable tool, but it does have an option to output the data in JSON format so
that it can be analyzed by a third-party application, if the PStats server is
not available for this platform.)

The GUI-specific code is the part that manages the interaction with the user via
the creation of windows and the handling of mouse input, etc.; most of the real
work of interpreting the data is done in the generic code in the pstatserver
directory.

The PStatServer owns all of the connections, and uses network sockets to
communicate with the clients. It listens on the specified port for new
connections, using the pstats-port Config.prc variable to determine the port
number (this is the same variable that specifies the port to the client),
although this can be overridden by using the ``-p`` option on the command-line.
Usually you can leave this at its default value of 5185, but there may be some
cases in which that port is already in use on a particular machine (for
instance, maybe someone else is running another PStats server on another display
of the same machine).

Once a connection is received, it creates a PStatMonitor class (this class is
specialized for each of the different GUI variants) that handles all the data
for this particular connection. A PStatMonitor is also created when a session
is loaded from a file.

The work of digesting the data from the client is performed by the PStatView
class, which analyzes the pattern of start and stop timestamps, along with the
relationship data of the various collectors, and boils it down into a list of
the amount of time spent in each collector per frame.

Finally, a PStatStripChart, PStatFlameGraph, PStatTimeline or PStatPianoRoll
class object defines the actual graph output of colored lines and bars; the
generic versions of these include virtual functions to do the actual drawing
(the GUI specializations of these redefine these methods to make the appropriate
calls).
