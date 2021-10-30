.. _removing-custom-class-instances:

Removing Custom Class Instances
===============================

The following text was taken from the Panda3D 1.6 Game Engine Beginner's Guide
available from Packt Publishing with the author's permission. The text refers to
a "custom class", which is a python class that is not part of the Panda3D SDK.
Here is an example of a custom class:

.. code-block:: python

   class MyClass:
       def __init__(self):
           myVar1 = 10
           myVar2 = 20
       def myMethod(self):
           return (self.myVar1, self.myVar2)

From Panda3D 1.6 Game Engine Beginner's Guide:

Python will automatically garbage collect a custom class instance when all the
references to that instance are removed. In theory, this makes garbage
collection as simple as cleaning up those references, but because there are so
many different places and reasons for these references garbage collection can
quickly grow complicated. Following these steps will help to ensure that a
custom class instance is properly garbage collected.

1. Call :meth:`~.NodePath.remove_node()` on all NodePaths in the scene graph –
   The first step is to clear out the NodePaths that the custom class has added
   to the scene graph. If this step isn’t accomplished, it won’t necessarily
   prevent the custom class instance from being garbage collected, but it could.
   Even if the custom class instance is still garbage collected the scene graph
   itself will retain references to the NodePaths that haven’t been cleared out
   and they will remain in the scene graph. There is one exception to this rule:
   when a parent NodePath has :meth:`~.NodePath.remove_node` called on it that
   ultimately result in the removal of its child NodePaths, so long as nothing
   else retains a reference to them. However, relying on this behavior is an
   easy way to make mistakes so it’s better to manually remove all of the
   NodePaths a custom class adds to the scene graph.

2. Call :py:meth:`~direct.actor.Actor.Actor.delete()` on all Actors – Just
   calling :meth:`~.NodePath.remove_node()` on an Actor isn’t enough. Calling
   :py:meth:`~direct.actor.Actor.Actor.delete()` will remove ties to animations,
   exposed joints, and so on to ensure that all the extra components of the
   Actor are removed from memory as well.

3. Set all Intervals, Sequences, and Parallels equal to None – It’s very common
   for Intervals, Sequences, and Parallels to retain references to something in
   the class and prevent the class instance from being cleaned up. To be safe,
   it’s best to remove the references to these Intervals so that they get
   cleaned up themselves and any references they have to the class are removed.

4. Detach all 3D sounds connected to class NodePaths – 3D sounds won’t actually
   retain references to the custom class, but if the NodePaths they are attached
   to are removed with :meth:`~.NodePath.remove_node()` and the sounds aren’t
   detached, they’ll generate an error and crash the program when they try to
   access the removed NodePaths. Play it safe and detach the sounds.

5. End all tasks running in the class – The task manager will retain a reference
   to the class instance so long as the class instance has a task running, so
   set up all of the tasks in the custom class to end themselves with return
   task.done. This is the most reliable way to stop them and clear the reference
   to the custom class in the task manager.

6. If the custom class inherits from DirectObject, call ``self.ignoreAll()``–
   Panda3D’s message system will also retain a reference to the custom class if
   it is set up to receive messages. To be on the safe side, every class that
   inherits from DirectObject and will be deleted during run time should call
   ``self.ignoreAll()`` to tell the message system that the class is no longer
   listening to messages. That will remove the reference.

7. Remove all direct references to the custom class instance – Naturally, the
   custom class instance won’t get cleaned up if something is referencing it
   directly, either through a circular self reference, or because it was created
   as a “child” of another class and that other class has a reference to it
   stored as a variable. All of these references need to be removed. This also
   includes references to the custom class instance placed in PythonTags.

The ``__del__`` method is a good way to test if a custom class is being garbage
collected. The ``__del__`` method is similar to the ``__init__`` method in that
we don’t call it ourselves; it gets called when something happens. ``__init__``
is called when a new instance of the class is created; ``__del__`` is called
when an instance of the class is garbage collected. It’s a pretty common thought
to want to put some important clean up steps in the ``__del__`` method itself,
but this isn’t wise. In fact, it’s best not to have a ``__del__`` method in any
of our classes in the final product because the ``__del__`` method can actually
hinder proper garbage collection. A better usage is to put a simple print
statement in the ``__del__`` method that will serve as a notifier that Python
has garbage collected the custom class instance. For example:

.. code-block:: python

   def __del__(self):
       print("Instance of Custom Class Alpha Removed")

Once we've confirmed that our custom class is being garbage collected properly,
we can remove the ``__del__`` method.
