.. _user-pstats-collectors:

User-Defined Collectors
=======================

The PStats client code is designed to be generic enough to allow users to define
their own collectors to time any arbitrary blocks of code (or record additional
non-time-based data), from either the C++ or the Python level.

The general idea is to create a PStatCollector for each separate block of code
you wish to time. The name which is passed to the PStatCollector constructor is
a unique identifier: all collectors that share the same name are deemed to be
the same collector.

Furthermore, the collector's name can be used to define the hierarchical
relationship of each collector with other existing collectors. To do this,
prefix the collector's name with the name of its parent(s), followed by a colon
separator. For instance, ``PStatCollector("Draw:Flip")`` defines a collector
named "Flip", which is a child of the "Draw" collector, defined elsewhere.

You can also define a collector as a child of another collector by giving the
parent collector explicitly followed by the name of the child collector alone,
which is handy for dynamically-defined collectors. For instance,
``PStatCollector(draw, "Flip")`` defines the same collector named above,
assuming that draw is the result of the ``PStatCollector("Draw")`` constructor.

Once you have a collector, simply bracket the region of code you wish to time
with :meth:`collector.start() <.PStatCollector.start>` and
:meth:`collector.stop() <.PStatCollector.stop>`. It is important to ensure that
each call to start() is matched by exactly one call to stop(). If you are
programming in C++, it is highly recommended that you use the
:class:`.PStatTimer` class to make these calls automatically, which guarantees
the correct pairing; the PStatTimer's constructor calls start() and its
destructor calls stop(), so you may simply define a PStatTimer object at the
beginning of the block of code you wish to time. If you are programming in
Python, you must call start() and stop() explicitly.

When you call start() and there was another collector already started, that
previous collector is paused until you call the matching stop() (at which time
the previous collector is resumed). That is, time is accumulated only towards
the collector indicated by the innermost start() .. stop() pair.

Time accumulated towards any collector is also counted towards that collector's
parent, as defined in the collector's constructor (described above).

It is important to understand the difference between collectors nested
implicitly by runtime start/stop invocations, and the static hierarchy implicit
in the collector definition. Time is accumulated in parent collectors according
to the statically-defined parents of the innermost active collector only,
without regard to the runtime stack of paused collectors.

For example, suppose you are in the middle of processing the "Draw" task and
have therefore called start() on the "Draw" collector. While in the middle of
processing this block of code, you call a function that has its own collector
called "Cull:Sort". As soon as you start the new collector, you have paused the
"Draw" collector and are now accumulating time in the "Cull:Sort" collector.
Once this new collector stops, you will automatically return to accumulating
time in the "Draw" collector. The time spent within the nested "Cull:Sort"
collector will be counted towards the "Cull" total time, not the "Draw" total
time.

If you wish to collect the time data for functions, a simple decorator pattern
can be used below, as below:

.. code-block:: python

   from panda3d.core import PStatCollector

   def pstat(func):
       collectorName = "Debug:%s" % func.__name__

       if hasattr(base, 'custom_collectors'):
           if collectorName in base.custom_collectors.keys():
               pstat = base.custom_collectors[collectorName]
           else:
               base.custom_collectors[collectorName] = PStatCollector(collectorName)
               pstat = base.custom_collectors[collectorName]
       else:
           base.custom_collectors = {}
           base.custom_collectors[collectorName] = PStatCollector(collectorName)
           pstat = base.custom_collectors[collectorName]

       def doPstat(*args, **kargs):
           pstat.start()
           returned = func(*args, **kargs)
           pstat.stop()
           return returned

       doPstat.__name__ = func.__name__
       doPstat.__dict__ = func.__dict__
       doPstat.__doc__ = func.__doc__
       return doPstat

To use it, either save the function to a file and import it into the script you
wish to debug. Then use it as a decorator on the function you wish to time. A
collection named Debug will appear in the Pstats server with the function as its
child.

.. code-block:: python

   from pstat_debug import pstat

   @pstat
   def myLongRunFunction():
       """ This function does something long """
