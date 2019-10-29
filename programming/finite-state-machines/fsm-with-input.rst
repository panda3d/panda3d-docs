.. _fsm-with-input:

FSM with input
==============

.. only:: python

   Another common use for FSM's is to provide an abstraction for AI state. For
   this purpose, you would like to supply an "input" string to the FSM and let
   the FSM decide which state it should transition to rather than explicitly
   specifying the target state name. Consider the following FSM state diagram:

   .. digraph:: transitions

      rankdir=TB
      node [style=rounded, shape=box]

      North -> West [ label="  left" ];
      West -> South [ label="  left" ];
      South -> East [ label="  left", constraint=false ];
      East -> North [ label="  left", constraint=false ];

      North:n -> North:n [ label="straight" ];
      West:s -> West:s [ label="straight" ];
      South:s -> South:s [ label="straight" ];
      East:n -> East:n [ label="straight" ];

      { rank=same; West; South }
      { rank=same; North; East }

   Here the text next to an arrow represents the "input" string given to the FSM,
   and the direction of the arrow represents the state transition that should be
   made for that particular input string, from the indicated starting state.

   In this example, we have encoded a simple FSM that determines which compass
   direction a character will be facing after either turning left or continuing
   straight. The input will be either "left" or "straight", and the result is a
   transition to a new state that represents the new compass direction, based on
   the previous compass direction. If we request "left" from state North, the
   FSM transitions to state West. On the other hand, if we request "left" from
   state South, the FSM transitions to state East. If we request "straight" from
   any state, the FSM should remain in its current state.

   To implement this in Panda3D, we define a number of **filter functions**, one
   for each state. The purpose of this function is to decide what state to
   transition to next, if any, on receipt of a particular input.

   A filter function is created by defining a python method named
   ``filterStateName()``, where StateName is the name of the FSM state to which
   this filter function applies. The filterStateName method receives two
   parameters, a string and a tuple of arguments (the arguments contain the
   optional additional arguments that might have been passed to the
   ``fsm.request()`` call; it's usually an empty tuple). The filter function
   should return the name of the state to transition to. If the transition
   should be disallowed, the filter function can either return None to quietly
   ignore it, or it can raise an exception. For example:

   .. code-block:: python

      class CompassDir(FSM):

          def filterNorth(self, request, args):
              if request == 'straight':
                  return 'North'
              elif request == 'left':
                  return 'West'
              else:
                  return None

          def filterWest(self, request, args):
              if request == 'straight':
                  return 'West'
              elif request == 'left':
                  return 'South'
              else:
                  return None

          def filterSouth(self, request, args):
              if request == 'straight':
                  return 'South'
              elif request == 'left':
                  return 'East'
              else:
                  return None

          def filterEast(self, request, args):
              if request == 'straight':
                  return 'East'
              elif request == 'left':
                  return 'North'
              else:
                  return None

   Note that input strings, by convention, should begin with a lowercase letter,
   as opposed to state names, which should begin with an uppercase letter. This
   allows you to make the distinction between requesting a state directly, and
   feeding a particular input string to an FSM. To feed input to this FSM, you
   would use the ``request()`` call, just as before:

   .. code-block:: python

      myfsm.request('left') # or myfsm.request_left()
      myfsm.request('left')
      myfsm.request('straight') # or myfsm.request_straight()
      myfsm.request('left')

   If the FSM had been in state North originally, after the above sequence of
   operations it would now be in state East.

   The defaultFilter method
   ------------------------

   Although defining a series of individual filter methods gives you the most
   flexibility, for many FSM's you may not need this much explicit control. For
   these cases, you can simply define a defaultFilter method that does
   everything you need. If a particular ``filterStateName()`` method does not
   exist, then the FSM will call the method named ``defaultFilter()`` instead;
   you can put any logic here that handles the general case.

   For instance, we could have defined the above FSM using just the
   defaultFilter method, and a lookup table:

   .. code-block:: python

      class CompassDir(FSM):
          nextState = {
              ('North', 'straight') : 'North',
              ('North', 'left') : 'West',
              ('West', 'straight') : 'West',
              ('West', 'left') : 'South',
              ('South', 'straight') : 'South',
              ('South', 'left') : 'East',
              ('East', 'straight') : 'East',
              ('East', 'left') : 'North',
          }

          def defaultFilter(self, request, args):
              key = (self.state, request)
              return self.nextState.get(key)

   The base FSM class defines a :py:meth:`~direct.fsm.FSM.FSM.defaultFilter()`
   method that implements the default FSM transition rules (that is, allow all
   direct-to-state (uppercase) transition requests unless
   ``self.defaultTransitions`` is defined; in either case, quietly ignore input
   (lowercase) requests).

   In practice, you can mix- and-match the use of the defaultFilter method and
   your own custom methods. The defaultFilter method will be called only if a
   particular state's custom filter method does not exist. If a particular
   state's filterStateName method is defined, that method will be called upon a
   new request; it can do any custom logic you require (and it can call up to
   the defaultFilter method if you like).

.. only:: cpp

   This section does not apply to C++ users.
