.. _task-chains:

Task Chains
===========

When you add tasks to the TaskManager, you are actually adding them to the
default Task Chain. The TaskManager maintains one or more task chains; each
chain is a list of tasks that are available to be executed.

You are free to create additional task chains as you see the need. Normally,
though, there is no reason to have more than the default task chain, unless you
wish to take advantage of threaded tasks: each task chain has the option of
being serviced by one or more sub-threads, which allows the tasks on that chain
to run in parallel with (or at a lower priority than) the main tasks.

Note that threading is an advanced topic, and the use of threading inherently
comes with risks. In particular, it is easy to introduce race conditions or
deadlocks in code that involves multiple threads. You are responsible for
protecting critical sections of your code from mutual access with proper use of
synchronization primitives, such as provided by Panda's Mutex and ConditionVar
classes, and for Python users, the :py:mod:`direct.stdpy.threading` module. For
the purposes of this discussion, we will assume that you are already familiar
with the proper use of synchronization primitives in threading.

Note also that Panda may be compiled with a special threading mode (called
"simple threads") that is designed to be low overhead, but which is
fundamentally incompatible with true threads as provided by the system library.
Thus, in any Panda application, you must always use Panda's synchronization
primitives, and not the system-provided ones; and you must use Panda's thread
primitives and not call into the system thread library directly, or you will
risk a terrible crash. That is, you should use Panda's Thread and Mutex
classes (or for Python users, the :py:mod:`direct.stdpy.threading` module), and
not any system thread or mutex implementation. See :ref:`threading` for more.

Defining task chains
--------------------

To set up a new task chain, you simply call:

.. only:: cpp

   .. code-block:: cpp

      AsyncTaskManager *task_mgr = AsyncTaskManager::get_global_ptr();
      AsyncTaskChain *chain = task_mgr->make_task_chain("chain_name");

   Each task chain must have a unique name. If you pass a name to
   make_task_chain() that has already been used, it will return the same pointer
   that was returned previously.

   Once you have a task chain pointer, you may then set parameters on that
   instance to configure the chain according to your needs.

.. only:: python

   .. code-block:: python

      taskMgr.setupTaskChain('chain_name', numThreads = None, tickClock = None,
                             threadPriority = None, frameBudget = None,
                             frameSync = None, timeslicePriority = None)

   Task chains are identified by their unique name. Repeated calls to
   setupTaskChain() with the same task chain name will reconfigure the same task
   chain.

The task chain parameters are:

.. only:: python

   numThreads
      Specifies the number of threads that will service this task chain. The
      default is zero, which means the task chain will be handled by the main
      thread. If you set this to 1, then a single thread will be spawned to
      handle all of the tasks in the chain one at a time, in the normal order.
      If you set this to some number higher than 1, then multiple threads will
      be spawned to handle the tasks on the chain. In this case, some of the
      tasks may be run in parallel with each other, and task ordering is
      difficult to guarantee.

   tickClock
      If this is true, then this task chain will be responsible for ticking the
      global clock each frame (and thereby incrementing the frame counter).
      There should be just one task chain responsible for ticking the clock, and
      usually it is the default task chain.

   threadPriority
      This specifies the priority level to assign to threads on this task chain.
      It may be one of TP_low, TP_normal, TP_high, or TP_urgent. This is passed
      to the underlying threading system to control the way the threads are
      scheduled. It only has meaning for a threaded task chain, of course.

   frameBudget
      This is the maximum amount of time (in seconds) to allow this task chain
      to run per frame. Set it to -1 to mean no limit (the default). It's not
      directly related to threadPriority.

   frameSync
      Set this true to force the task chain to sync to the clock. When this flag
      is false, the default, the task chain will finish all of its tasks and
      then immediately start from the first task again, regardless of the clock
      frame. When it is true, the task chain will finish all of its tasks and
      then wait for the clock to tick to the next frame before resuming the
      first task. This only makes sense for threaded tasks chains; non-threaded
      task chains are automatically synchronous.

   timeslicePriority
      This is false in the default mode, in which each task runs exactly once
      each frame, round-robin style, regardless of the task's priority value.
      Set it to true to change the meaning of priority so that certain tasks are
      run less often, in proportion to their time used and to their priority
      value. See :meth:`.AsyncTaskChain.set_timeslice_priority()` for more.

.. only:: cpp

   set_num_threads()
      Specifies the number of threads that will service this task chain. The
      default is zero, which means the task chain will be handled by the main
      thread. If you set this to 1, then a single thread will be spawned to
      handle all of the tasks in the chain one at a time, in the normal order.
      If you set this to some number higher than 1, then multiple threads will
      be spawned to handle the tasks on the chain. In this case, some of the
      tasks may be run in parallel with each other, and task ordering is
      difficult to guarantee.

   set_tick_clock()
      If this is true, then this task chain will be responsible for ticking the
      global clock each frame (and thereby incrementing the frame counter).
      There should be just one task chain responsible for ticking the clock, and
      usually it is the default task chain.

   set_thread_priority()
      This specifies the priority level to assign to threads on this task chain.
      It may be one of TP_low, TP_normal, TP_high, or TP_urgent. This is passed
      to the underlying threading system to control the way the threads are
      scheduled. It only has meaning for a threaded task chain, of course.

   set_frame_budget()
      This is the maximum amount of time (in seconds) to allow this task chain
      to run per frame. Set it to -1 to mean no limit (the default). It's not
      directly related to threadPriority.

   set_frame_sync()
      Set this true to force the task chain to sync to the clock. When this flag
      is false, the default, the task chain will finish all of its tasks and
      then immediately start from the first task again, regardless of the clock
      frame. When it is true, the task chain will finish all of its tasks and
      then wait for the clock to tick to the next frame before resuming the
      first task. This only makes sense for threaded tasks chains; non-threaded
      task chains are automatically synchronous.

   set_timeslice_priority()
      This is false in the default mode, in which each task runs exactly once
      each frame, round-robin style, regardless of the task's priority value.
      Set it to true to change the meaning of priority so that certain tasks are
      run less often, in proportion to their time used and to their priority
      value. See :meth:`.AsyncTaskChain::set_timeslice_priority()` for more.

Using task chains
-----------------

.. only:: python

   You may add any tasks to the task chain of your choosing with the optional
   taskChain parameter to :py:meth:`taskMgr.add()` or
   :py:meth:`taskMgr.doMethodLater()`. This parameter should receive the name of
   the task chain to add the task to; this is the 'chain_name' you specified in
   the above call to :py:meth:`taskMgr.setupTaskChain()`. For example:

   .. code-block:: python

      taskMgr.add(self.myTaskFunc, 'myTaskName', taskChain = 'myChain')

.. only:: cpp

   You may add any tasks to the task chain of your choosing by using
   :meth:`AsyncTask::set_task_chain()`. This method should receive the string
   name of the task chain to add the task to; this is the "chain_name" you
   specified in the above call to :meth:`task_mgr->make_task_chain()
   <AsyncTaskManager::make_task_chain>`. For example:

   .. code-block:: cpp

      PT(AsyncTask) task = new GenericAsyncTask("myTaskName");
      task->set_function(my_task_func);
      task->set_task_chain("myChain");
      task_mgr->add(task);
