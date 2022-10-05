.. _pstats-thread-profiling:

Thread Profiling
================

If the client has multiple threads that generate PStats data, the PStats server
can open up graphs for these threads as well. Each separate thread is considered
unrelated to the main thread, and may have the same or an independent
frame rate. Each separate thread will be given its own pulldown menu to create
graphs associated with that thread; these auxiliary thread menus will appear on
the menu bar following the Graphs menu, which represents the main thread.

The Timeline view is particularly useful for profiling with multiple threads.
It shows the collectors for the different threads underneath each other,
allowing you to spot synchronization issues.

You can enable further thread profiling features by putting this in Config.prc::

   pstats-thread-profiling true

This will enable additional collectors showing context switches and other
synchronization events. This feature is still experimental.
