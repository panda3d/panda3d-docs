.. _finite-state-machines:

Finite State Machines
=====================

.. only:: python

   A "Finite State Machine" is a concept from computer science. Strictly
   speaking, it means any system that involves a finite number of different
   states, and a mechanism to transition from one state to another.

   In Panda3D, a Finite State Machine, or FSM, is implemented as a Python class.
   To define a new FSM, you should define a Python class that inherits from the
   FSM class. You define the available states by writing appropriate method
   names within the class, which define the actions the FSM takes when it enters
   or leaves certain states. Then you can request your FSM to transition from
   state to state as you need it to.

   You may come across some early Panda3D code that creates an instance of the
   ClassicFSM class. :py:class:`~direct.fsm.ClassicFSM.ClassicFSM` is an earlier
   implementation of the FSM class, and is now considered deprecated. It is no
   longer documented here. We recommend that new code use the FSM class instead,
   which is documented on the following pages.

.. only:: cpp

   This section does not apply to C++ users.

.. toctree::
   :maxdepth: 2

   fsm-introduction
   simple-fsm-usage
   fsm-with-input
   advanced-fsm-tidbits
