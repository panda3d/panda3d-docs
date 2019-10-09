.. _log-messages:

Log Messages
============

Panda periodically outputs log messages for debugging purposes. A typical log
message might look like this::

   :util(warning): Adjusting global clock's real time by -3.3 seconds.

The first part of the message, ``util``, is the name of the module that
generated the message. The second part, ``warning``, indicates the severity. The
severity levels are, in decreasing order: fatal, error, warning, info, debug,
and spam. The panda configuration file (Config.prc) contains these directives::

   notify-level warning
   default-directnotify-level warning

Directives like these tell panda which messages to show, and which to suppress.
In the default configuration (shown above), all messages whose severity is
``warning`` or above are shown, all messages whose severity is less are
suppressed.

.. only:: python

   .. note::
      There are two kinds of notifiers: the C++ one and a Pythonic (therefore
      'direct'notify). You can distinguish them by the category name. Where C++
      categories are always lowercase, Python categories are starting with a
      capital letter by convention (e.g. util, and ShowBase). The only
      differences in practice is that you set (all) Python notifiers with the
      prc option ``default-notify-level`` and C++ with ``notify-level``, and
      Pythonic notifiers don't know the *spam* and *fatal* levels.

Sometimes it is interesting and educational to change the configuration to
this:

.. code-block:: text

   notify-level spam
   default-directnotify-level info

If you do this, panda will print out vast amounts of information while it runs.
These informational messages can be useful for debugging. However, there are so
many print-statements that it slows panda down to a crawl. So it may be
desirable to tell panda to narrow it down a little. The way to do that is to
name a particular module in the panda config file. For example, you might do
this:

.. code-block:: text

   notify-level warning
   notify-level-glgsg spam
   default-directnotify-level warning

This tells panda that module "glgsg" should print out everything it can, but
that every other module should only print warnings and errors. By the way,
module ``glgsg`` is a particularly interesting module to investigate. This is
the module that invokes OpenGL. If you tell it to spam you, it will tell you
what it's setting the MODELVIEW and PROJECTION matrices to, and lots of other
interesting information.

Generating your own Log Messages
--------------------------------

You can use the ``Notify`` class to output your own log messages.

In Python this would look something like this:

.. code-block:: python

   from direct.directnotify.DirectNotify import DirectNotify
   (...)
   notify = DirectNotify().newCategory("MyCategory")
   (...)
   notify.warning("Put some informational text here.")

First you create a new notify category, which may be whatever you want, e.g.
"PlayerMovement". It's a convention to have such a notifier for each bigger
class or module. In the last line there is a warning() call, which indicates
that the given text will be only printed if the severity level for this category
is *warning* or *debug*. If the severity isn't set for this particular category,
then the ``default-directnotify-level`` setting is taken.

Redirecting Log Messages to a File
----------------------------------

If you wish, you can redirect all of panda's log messages into a file. The
following snippet will do the trick:

.. code-block:: python

   nout = MultiplexStream()
   Notify.ptr().setOstreamPtr(nout, 0)
   nout.addFile(Filename("out.txt"))

Alternatively you may want to use the notify-output prc option, which expects a
filename as argument::

   notify-output mygame-log.txt
