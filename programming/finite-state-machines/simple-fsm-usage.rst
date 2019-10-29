.. _simple-fsm-usage:

Simple FSM Usage
================

.. only:: python

   A Panda3D FSM is implemented by defining a new Python class which inherits
   from the class :py:class:`direct.fsm.FSM.FSM` (normally imported as simply
   FSM), and defining the appropriate enter and exit methods on the class.

   FSM states are represented by name strings, which should not contain spaces
   or punctuation marks; by Panda3D convention, state names should begin with a
   capital letter. An FSM is always in exactly one state a time; the name of the
   current state in stored in ``fsm.state``. When it transitions from one state
   to another, it first calls ``exitOldState()``, and then it calls
   ``enterNewState()``, where OldState is the name of the previous state, and
   NewState is the name of the state it is entering. While it is making this
   transition, the FSM is not technically in either state, and ``fsm.state``
   will be None--but you can find both old and new state names in
   ``fsm.oldState`` and ``fsm.newState``, respectively.

   To define a possible state for an FSM, you only need to define an
   ``enterStateName()`` and/or ``exitStateName()`` method on your class, where
   StateName is the name of the state you would like to define. The
   ``enterStateName()`` method should perform all the necessary action for
   entering your new state, and the corresponding ``exitStateName()`` method
   should generally undo everything that was done in ``enterStateName()``, so
   that the world is returned to a neutral state.

   An FSM starts and finishes in the state named "Off". When the FSM is created,
   it is already in "Off"; and when you destroy it (by calling
   :py:meth:`fsm.cleanup() <direct.fsm.FSM.FSM.cleanup>`), it automatically
   transitions back to "Off".

   To request an FSM to transition explicitly to a new state, use the call
   :py:meth:`fsm.request('StateName') <direct.fsm.FSM.FSM.request>`, where
   StateName is the state you would like it to transition to.

   Arguments to enterStateName methods
   -----------------------------------

   Normally, both ``enterStateName()`` and ``exitStateName()`` take no arguments
   (other than self). However, if your FSM requires some information before it
   can transition to a particular state, you can define any arguments you like
   to the enterStateName method for that state; these arguments should be passed
   in to the ``request()`` call, following the state name.

   .. code-block:: python

      from direct.fsm.FSM import FSM

      class AvatarFSM(FSM):

          def enterWalk(self, speed, doorMask):
              avatar.setPlayRate(speed, 'walk')
              avatar.loop('walk')
              footstepsSound.play()
              enableDoorCollisions(doorMask)

          def exitWalk(self):
              avatar.stop()
              footstepsSound.stop()
              disableDoorCollisions()

      myfsm = AvatarFSM('myAvatar')
      myfsm.request('Walk', 1.0, BitMask32.bit(2))

   Note that the exitStateName method must always take no arguments.

   Allowed and disallowed state transitions
   ----------------------------------------

   By default, every state transition request is allowed: the call
   ``fsm.request('StateName')`` will always succeed, and the the FSM will be
   left in the new state. You may wish to make your FSM more robust by
   disallowing certain transitions that you don't want to happen.

   For instance, consider the example FSM described previously, which had the
   following state diagram:

   .. digraph:: transitions

      rankdir=LR
      node [style=rounded, shape=box]

      Walk -> Walk2Swim;
      Walk2Swim -> Swim;
      Swim -> Swim2Walk;
      Swim2Walk -> Walk;
      Swim -> Drowning;

      { rank=same; Walk2Swim; Swim2Walk; }

   In this diagram, the arrows represent legal transitions. It is legal to
   transition from 'Walk' to 'Walk2Swim', but not from 'Walk' to 'Swim2Walk'. If
   you were to request the FSM to enter state 'Swim2Walk' while it is currently
   in state 'Walk', that's a bug; you might prefer to have the FSM throw an
   exception, so you can find this bug.

   To enforce this, you can store ``self.defaultTransitions`` in the FSM's
   ``__init__()`` method. This should be a map of allowed transitions from each
   state. That is, each key of the map is a state name; for that key, the value
   is a list of allowed transitions from the indicated state. Any transition not
   listed in defaultTransitions is considered invalid. For example:

   .. code-block:: python

      class AvatarFSM(FSM):

          def __init__(self):
              FSM.__init__(self, 'myAvatar')
              self.defaultTransitions = {
                  'Walk' : [ 'Walk2Swim' ],
                  'Walk2Swim' : [ 'Swim' ],
                  'Swim' : [ 'Swim2Walk', 'Drowning' ],
                  'Swim2Walk' : [ 'Walk' ],
                  'Drowning' : [ ],
              }

   If you do not assign anything to ``self.defaultTransitions()``, then all
   transitions are legal. However, if you do assign a map like the above, then
   requesting a transition that is not listed in the map will raise the
   exception :py:exc:`FSM.RequestDenied <direct.fsm.FSM.RequestDenied>`.

.. only:: cpp

   This section does not apply to C++ users.
