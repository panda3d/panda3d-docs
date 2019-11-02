.. _using-intervals-to-move-the-panda:

Using Intervals to move the Panda
=================================

Intervals and Sequences
-----------------------

:ref:`intervals`
~~~~~~~~~~~~~~~~

*Intervals* are tasks that change a property from one value to another over a
specified period of time. Starting an interval effectively starts a background
process that modifies the property over the specified period of time.

:ref:`Sequences <sequences-and-parallels>`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Sequences*, sometimes called *MetaIntervals*, are a type of interval that
contains other intervals.  Playing a sequence will cause each contained interval
to execute in sequence, one after the other.

The Program
-----------

Update the Code
~~~~~~~~~~~~~~~

The next step is to cause the panda to actually move back and forth. Update the
code to the following:

.. only:: python

   .. literalinclude:: using-intervals-to-move-the-panda.py
      :language: python
      :linenos:

.. only:: cpp

   .. literalinclude:: using-intervals-to-move-the-panda.cxx
      :language: cpp
      :linenos:

When the ``pandaPosInterval1`` interval is started, it will gradually adjust the
position of the panda from (0, 10, 0) to (0, -10, 0) over a period of 13
seconds. Similarly, when the ``pandaHprInterval1`` interval is started, the
heading of the panda will rotate 180 degrees over a period of 3 seconds.

The ``pandaPace`` sequence above causes the panda to move in a straight line,
turn, move in the opposite straight line, and finally turn again. The code
``pandaPace.loop()`` causes the Sequence to be started in looping mode.

Run the Program
~~~~~~~~~~~~~~~

The result of all this is to cause the panda to pace back and forth from one
tree to the other.
