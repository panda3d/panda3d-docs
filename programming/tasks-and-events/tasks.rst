.. _tasks:

Tasks
=====

Tasks are special functions that are called once each frame while your
application executes. They are similar in concept to threads. However, in
Panda3D, tasks are not generally separate threads; instead, all tasks are run
cooperatively, one at a time, within the main thread. This design simplifies
game programming considerably by removing the requirement to protect critical
sections of code from mutual access. (See :ref:`task-chains` in the next section
if you really want to use threading.)

.. only:: python

   When you start Panda3D by initializing ShowBase, a handful of tasks are
   created by default, but you are free to add as many additional tasks as you
   like.

.. only:: cpp

   When you start Panda3D by initializing WindowFramework, a handful of tasks
   are created by default, but you are free to add as many additional tasks as
   you like.

The Task Function
-----------------

A task is defined with a function or class method; this function is the main
entry point for the task and will be called once per frame while the task is
running. By default, the function receives one parameter, which is the task
object; the task object carries information about the task itself, such as the
amount of time that the task has been running.

Your task function should return when it has finished processing for the frame.
Because all tasks are run in the same thread, you must not spend too much time
processing any one task function; the entire application will be locked up until
the function returns.

.. only:: python

   The task function may return either ``Task.cont`` to indicate that the task
   should be called again next frame, or ``Task.done`` to indicate that it
   should not be called again. If it returns None (which is to say, it does not
   return anything), then the default behavior is to stop.

   You can check how long your task has been running by checking ``task.time``
   in your task function. You can also check how many times the task function
   has been run by using ``task.frame``.

   The below example imports the Task module and shows a function used as task.

   .. code-block:: python

      from direct.task import Task

      # This task runs for two seconds, then prints done
      def exampleTask(task):
          if task.time < 2.0:
              return Task.cont

          print('Done')
          return Task.done

.. only:: cpp

   The task function may return either ``AsyncTask::DS_cont`` to indicate that
   the task should be called again next frame, or ``AsyncTask::DS_done`` to
   indicate that it should not be called again.

   You can check how long your task has been running by checking
   ``task->get_elapsed_time()`` in your task function. You can also check how
   many times the task function has been run by using
   ``task->get_elapsed_frames()``.

   .. code-block:: cpp

      #include "asyncTaskManager.h"

      // This task runs for two seconds, then prints done
      AsyncTask::DoneStatus example_task(GenericAsyncTask *task, void *data) {
        if (task->get_elapsed_time() < 2.0) {
          return AsyncTask::DS_cont;
        }
        cout << "Done" << endl;
        return AsyncTask::DS_done;
      }

Task Return Values
------------------

The value returned from a task affects how the task manager handles that task
going forward.

.. only:: python

   ============== =======================================================================
   Variable       Purpose
   ============== =======================================================================
   ``Task.done``  Specifies that a task is finished and removes it from the task manager.
   ``Task.cont``  Perform the task again next frame.
   ``Task.again`` Perform the task again, using the same delay as initially specified.
   ============== =======================================================================

.. only:: cpp

   ======================= =======================================================================
   Variable                Purpose
   ======================= =======================================================================
   ``AsyncTask::DS_done``  Specifies that a task is finished and removes it from the task manager.
   ``AsyncTask::DS_cont``  Perform the task again next frame.
   ``AsyncTask::DS_again`` Perform the task again, using the same delay as initially specified.
   ======================= =======================================================================

The Do-Later Task
-----------------

.. only:: cpp

   If you have used Panda3D in Python, you might be familiar with the Python
   function ``taskMgr.doMethodLater()``, which lets you schedule a task to be
   started after a certain delay. This isn't needed in C++, because you can set
   a delay on a task directly with ``task->set_delay()``. An example will be
   provided below in the task manager section.

.. only:: python

   A useful special kind of task is the do-later: this is similar to a task, but
   rather than being called every frame it will be called only once, after a
   certain amount of time (in seconds) has elapsed. You can, of course,
   implement a do-later task with a regular task that simply does nothing until
   a certain amount of time has elapsed (as in the above example), but using a
   do-later is a much more efficient way to achieve the same thing, especially
   if you will have many such tasks waiting around.

   .. code-block:: python

      taskMgr.doMethodLater(delayTime, myFunction, 'Task Name')

   In this example myFunction must accept a task variable. If you wish to use a
   function that does not accept a task variable:

   .. code-block:: python

      taskMgr.doMethodLater(delayTime, myFunction, 'Task Name', extraArgs = [variables])

   Note: if you wish to call a function which takes no variables simply pass
   ``extraArgs = []``

   Do-Later tasks can be repeated from the task function by returning
   ``Task.again``. You can also change the delay of the Do-Later task by
   changing ``task.delayTime``, but changing this will not have any effect on
   the task's actual delay time until the next time it gets added to the do-
   later list, for instance by returning ``Task.again``.

   .. code-block:: python

      # This task increments itself so that the delay between task executions
      # gradually increases over time. If you do not change task.delayTime
      # the task will simply repeat itself every 2 seconds
      def myFunction(task):
          print("Delay: %s" % task.delayTime)
          print("Frame: %s" % task.frame)
          task.delayTime += 1
          return task.again

      myTask = taskMgr.doMethodLater(2, myFunction, 'tickTask')

   If you wish to change the delayTime outside of the task function itself, and
   have it make an immediate effect, you can remove and re-add the task by hand,
   for instance:

   .. code-block:: python

      taskMgr.remove(task)
      task.delayTime += 1
      taskMgr.add(task)

   There is a read-only public member ``task.wakeTime`` which stores the time at
   which the task should wake up, should you desire to query this.

The Task Object
---------------

The ``task`` object is passed into all task functions. There are several members
accessible in the func object, among which:

.. only:: python

   ============== ======================================================================================================================================================================================
   Member         Returns
   ============== ======================================================================================================================================================================================
   ``task.time``  A float that indicates how long this task function has been running since the first execution of the function. The timer is running even when the task function is not being executed.
   ``task.frame`` An integer that counts the number of elapsed frames since this function was added. Count may start from 0 or 1.
   ``task.id``    An integer that gives the unique id assigned to this task by the Task Manager.
   ``task.name``  The task name assigned to the task function.
   ============== ======================================================================================================================================================================================

.. only:: cpp

   ============================== ======================================================================================================================================================================================
   Member                         Returns
   ============================== ======================================================================================================================================================================================
   ``task->get_elapsed_time()``   A float that indicates how long this task function has been running since the first execution of the function. The timer is running even when the task function is not being executed.
   ``task->get_elapsed_frames()`` An integer that counts the number of elapsed frames since this function was added. Count may start from 0 or 1.
   ``task->get_task_id()``        An integer that gives the unique id assigned to this task by the Task Manager.
   ``task->get_name()``           The task name assigned to the task function.
   ============================== ======================================================================================================================================================================================

To remove the task and stop it from executing from outside the task function,
call ``task.remove()``.

The Task Manager
----------------

.. only:: python

   All tasks are handled through the global Task Manager object, called
   ``taskMgr`` in Panda3D.

.. only:: cpp

   All tasks are handled through the Task Manager object. Here we assume that
   you  have obtained a reference to it and stored it in a variable called
   ``task_mgr``, for example:

   .. code-block:: cpp

      PT(AsyncTaskManager) task_mgr = AsyncTaskManager::get_global_ptr();


The Task Manager keeps a list of all currently-running tasks.

.. only:: python

   To add your task function to the task list, call ``taskMgr.add()`` with your
   function and an arbitrary name for the task. ``taskMgr.add()`` returns a Task
   which can be used to remove the task later on.

   .. code-block:: python

      taskMgr.add(exampleTask, 'MyTaskName')

   You can add extra arguments to the call through the ``extraArgs`` parameter.
   When you do this, the task parameter is no longer sent to your function  by
   default. If you still want it, make sure to set ``appendTask=True``, which
   makes the task the last argument sent to the function.

   .. code-block:: python

      taskMgr.add(exampleTask, 'MyTaskName', extraArgs=[a,b,c], appendTask=True)

.. only:: cpp

   To add a task to the Task Manager, first create a task object by indicating
   your function and an arbitrary name, and then add it to the task list by
   calling ``task_mgr->add()`` with a pointer to your task.

   .. code-block:: cpp

      PT(GenericAsyncTask) task;
      task = new GenericAsyncTask("MyTaskName", &example_task, nullptr);

      task_mgr->add(task);

   You can add an arbitrary argument to the call through the third parameter.

Although normally each task is given a unique name, you may also create multiple
different tasks with the same name. This can be convenient for locating or
removing many task functions at the same time.  Each task remains independent of
the others, even if they have the same name; this means that a task function
returning a "done" status will not affect any other task functions.

.. only:: python

   To remove the task and stop it from executing, call ``taskMgr.remove()``. You
   can pass in either the name of the task, or the task object (which was
   returned by ``taskMgr.add()``, above).

   .. code-block:: python

      taskMgr.remove('MyTaskName')

.. only:: cpp

   To remove the task and stop it from executing, you can call
   ``task->remove()``.

   .. code-block:: cpp

      task->remove();

   A useful task method is ``task->set_delay()``; it causes your task to be
   called after a certain amount of time (in seconds). You can, of course,
   implement this kind of functionality with an underlayed task that simply does
   nothing until a certain amount of time has elapsed (as in the above example),
   but using this method is a much more efficient way to achieve the same thing,
   especially if you will have many such tasks waiting around. Note that you
   need to set the delay before you add the task to the Task Manager, otherwise
   the call won't have an effect.

   .. code-block:: cpp

      task->set_delay (60);
      task_mgr->add(task);

   Similarly, if you wish to change the delay time of a task, you have to remove
   the task and re-add it by hand. For instance:

   .. code-block:: cpp

      task->remove();
      task->set_delay(10);
      task_mgr->add(task);

   You can also alter the delay of the task inside the task function, but you
   will have to return AsyncTask::DS_again afterwards so that it takes effect.

.. only:: python

   You may add a cleanup function to the task function with the uponDeath
   parameter. Similar to task functions, the uponDeath function has a task
   object as a parameter. The cleanup function is called whenever the task
   finishes, for instance by ``return Task.done``, or when it is explicitly
   removed via ``taskMgr.remove()``.

   .. code-block:: python

      taskMgr.add(exampleTask, 'TaskName', uponDeath=cleanupFunc)

.. only:: cpp

   You may add a cleanup function to the task with the
   ``task->set_upon_death()`` function. Similar to task functions, this function
   receives a function pointer as a parameter. The cleanup function is called
   whenever the task finishes, for instance by ``return AsyncTask::DS_done;``,
   or when it is explicitly removed via a ``task->remove()`` call.

   .. code-block:: cpp

      task->set_upon_death(&cleanupFunc);

To control order in which tasks are executed, you can use sort or priority
argument. If you use only sort or only priority, tasks given lesser value will
execute sooner.

.. only:: python

   .. code-block:: python

      taskMgr.add(task2, "second", sort=2)
      taskMgr.add(task1, "first", sort=1)

   or

   .. code-block:: python

      taskMgr.add(task2, "second", priority=2)
      taskMgr.add(task1, "first", priority=1)

   In both cases, task1 given name "first" will be executed before task2
   ("second").

If you use both sort and priority arguments, tasks with lower sort value will be
executed first. However, if there are several tasks which have same sort value,
but different priority value then that tasks are going to be executed in a way
that ones with HIGHER priority value will be executed first.

.. only:: python

   To clarify it a bit, here is code sample, tasks are named in order in which
   they are executed.

   .. code-block:: python

      taskMgr.add(task1, "first", sort=1, priority=2)
      taskMgr.add(task2, "second", sort=1, priority=1)
      taskMgr.add(task3, "third", sort=2, priority=1)
      taskMgr.add(task4, "fourth", sort=3, priority=13)
      taskMgr.add(task5, "fifth", sort=3, priority=4)

   To print the list of tasks currently running, simply print out ``taskMgr``.
   Among your own tasks, you may see the following system tasks listed:

   dataloop
      Processes the keyboard and mouse inputs

   tkloop
      Processes Tk GUI events

   eventManager
      Processes events generated by C++ code, such as collision events

   igloop
      Draws the scene

   There also is graphical interface for managing tasks. This is very useful for
   having a look at the tasks while your application is running.

   .. code-block:: python

      taskMgr.popupControls()

.. only:: cpp

   To print the list of tasks currently running, simply call
   ``task_mgr->write(cout);``.

Task timing
-----------

.. only:: python

   To see the specific timing information for each task when you print taskMgr,
   add the following line to your Config.prc file::

      task-timer-verbose #t

   (see :ref:`the-configuration-file` for config syntax)

Examples
--------

.. only:: python

   uponDeath

   .. code-block:: python

      taskAccumulator = 0

      def cleanUp(task):
          global taskAccumulator
          print("Task func has accumulated %d" % taskAccumulator)
          # Reset the accumulator
          taskAccumulator = 0

      # A task that runs forever
      def taskFunc(task):
          global taskAccumulator
          taskAccumulator += 1
          return task.cont

      def taskStop(task):
          taskMgr.remove('Accumulator')

      # Add the taskFunc function with an uponDeath argument
      taskMgr.add(taskFunc, 'Accumulator', uponDeath=cleanUp)
      # Stops the task 2 seconds later
      taskMgr.doMethodLater(2, taskStop, 'Task Stop')

.. only:: cpp

   set_upon_death()

   .. code-block:: cpp

      int task_accumulator = 0;

      void clean_up(GenericAsyncTask *task, bool clean_exit, void *user_data) {
        cout << "Task func has accumulated " << task_accumulator << endl;
        //  Reset the accumulator
        task_accumulator = 0;
      }

      // A task that runs forever
      AsyncTask::DoneStatus task_func(GenericAsyncTask *task, void *data) {
        task_accumulator++;
        return AsyncTask::DS_cont;
      }

      AsyncTask::DoneStatus task_stop(GenericAsyncTask *task, void *data) {
        ((GenericAsyncTask *)data)->remove();
        return AsyncTask::DS_done;
      }

      // Note that we skip the initialization and finalization of
      // the application for the sake of simplifying the example.
      int main(int argc, char *argv[]) {
        /* Insert here your app initialization code */
        /* ... */

        AsyncTaskManager *task_mgr = AsyncTaskManager::get_global_ptr();

        PT(GenericAsyncTask) task, stopper_task;

        // Add the task_func function with an upon_death callback
        task = new GenericAsyncTask("Accumulator", &task_func, nullptr);
        task->set_upon_death(&clean_up);
        task_mgr->add(task);

        // Adds another task to stop the main task 2 seconds later
        stopper_task = new GenericAsyncTask("Task stopper", &task_stop, task);
        stopper_task->set_delay(2);
        task_mgr->add(stopper_task);

        /* Insert here your app finalization code */
        /* ... */
      }
