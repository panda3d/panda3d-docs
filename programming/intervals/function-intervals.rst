.. _function-intervals:

Function Intervals
==================

.. only:: python

   Function intervals are different from function lerp intervals. While the
   function lerp interval passes data to a function over a period of time, a
   function interval will simply execute a function when called. As such, a
   function interval’s use really appears when combined with sequences and
   parallels. The function interval’s format is simple.

   .. code-block:: python

      intervalName = Func(myFunction)

   You pass the function without parentheses (i.e. you pass
   ``Func``- a function pointer)
   as the parameter. If ``myFunction``
   takes arguments, then pass them as parameters to
   ``Func`` as follows:

   .. code-block:: python

      def myFunction(arg1, arg2):
         # Do something.

      intervalName = Func(myFunction, arg1, arg2)

   Functions cannot be called on their own in sequences and parallels, so it is
   necessary to wrap them in an interval in order to call them. Since function
   intervals have no duration, they complete the moment they are called.

.. only:: cpp

   As FunctionInterval is implemented in Python, this section does not apply to
   C++.
