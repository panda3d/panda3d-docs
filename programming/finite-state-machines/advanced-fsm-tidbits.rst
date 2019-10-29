.. _advanced-fsm-tidbits:

Advanced FSM Tidbits
====================

.. only:: python

   request vs. demand
   ------------------

   As stated previously, you normally request an FSM to change its state by
   calling either ``fsm.request('NewState', arg1, arg2, ...)``, or
   ``fsm.request('inputString', arg1, arg2, ...)``, where arg1, arg2, ...
   represent optional arguments to the destination state's enter function (or to
   the filter function). The call to ``request()`` will either succeed or fail,
   according to what the filter function for the current state does. If it
   succeeds, it will return the tuple ``('NewState', arg1, arg2)``, indicating
   the new state it has transitioned to. If it fails, it will simply return None
   (unless the filter function was written to throw an exception on failure).

   If you request an FSM to make a transition, and the request fails, you might
   consider this an error condition, and you might prefer to have your code to
   stop right away rather than continuing. In this case, you should call
   :py:meth:`fsm.demand() <direct.fsm.FSM.FSM.demand>` instead. The syntax is
   the same as that for ``request()``, but instead of returning None on failure,
   it will always raise an exception if the state transition is denied. There is
   no return value from ``demand()``; if it returns, the transition was
   accepted.

   FSM.AlreadyInTransition
   -----------------------

   An FSM is always in exactly one state, except while it is in the process of
   transitioning between states (that is, while it is calling the exitStateName
   method for the previous state, followed by the enterStateName method for the
   new state). During this time, the FSM is not considered in either state, and
   if you query ``fsm.state`` it will contain None.

   During this transition time, it is not legal to call ``fsm.request()`` to
   request a new state. If you try to do this, the FSM will raise the exception
   :py:exc:`FSM.AlreadyInTransition <direct.fsm.FSM.AlreadyInTransition>`.
   This is a particularly common error if some cleanup code that is called from
   the exitStateName method has a side-effect that triggers a transition to a
   new state.

   However, there's a simple solution to this problem: call ``fsm.demand()``
   instead. Unlike ``request()``, ``demand()`` can be called while the FSM is
   currently in transition. When this happens, the FSM will queue up the demand,
   and will carry it out as soon as it has fully transitioned into its new
   state.

   forceTransition()
   -----------------

   There is also a method
   :py:meth:`fsm.forceTransition() <direct.fsm.FSM.FSM.forceTransition>`.
   This is similar to ``demand()`` in that it never fails and does not have a
   return value, but it's different in that it completely bypasses the filter
   function. You should therefore only pass an uppercase state name (along with
   any optional arguments) to forceTransition, never a lowercase input string.
   The FSM will always transition to the named state, even if it wouldn't
   otherwise be allowed. Thus, ``forceTransition()`` can be useful in special
   cases to skip to another state that's not necessarily connected to the
   current state (for instance, to handle emergency cleanup when an exception
   occurs). Be careful that you don't overuse ``forceTransition()``, though;
   consider whether ``demand()`` would be a better choice. If you find yourself
   making lots of calls to ``forceTransition()``, it may be that your filter
   functions (or your defaultTransitions) are poorly written and are
   disallowing what should be legitimate state transitions.

   Filtering the optional arguments
   --------------------------------

   The filterStateName method receives two parameters: the string request, and a
   tuple, which contains the additional arguments passed to the request (or
   demand) call. It then normally returns the state name the FSM should
   transition to, or it returns None to indicate the transition is denied.

   However, the filter function can also return a tuple. If it returns a tuple,
   it should be of the form ``('StateName', arg1, arg2, ...)``, where arg1,
   arg2, ... represent the optional arguments that should be passed to the
   enterStateName method. Usually, these are the same arguments that were passed
   to the filterStateName method (in this case, you can generate the return
   value tuple with the python syntax ``('StateName',) + args``).

   The returned arguments are not necessarily the same as the ones passed in,
   however. The filter function is free to check, modify, or rearrange any of
   them; or it might even make up a completely new set of arguments. In this
   way, the filter function can filter not only the state transitions
   themselves, but also the set of data passed along with the request.

.. only:: cpp

   This section does not apply to C++ users.
