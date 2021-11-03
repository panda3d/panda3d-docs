.. _subclassing:

Subclassing
===========

Introduction
~~~~~~~~~~~~

Both Python and C++, being object-oriented programming languages, take advantage
of the concept known as "Inheritance", to allow for a class to subclass one or
more other classes. This allows for the creation of a sub-class (or descendent
class) that is said to "inherit" all the attributes of the super class (or
ancestor class), usually with the purpose of expanding upon them.

Subclassing pure-python classes from python or C++ classes from C++ is fairly
straightforward and there's plenty of literature on the subject. The Wikipedia
article on
`inheritance <https://en.wikipedia.org/wiki/Inheritance_(computer_science)>`__
is a good starting point before proceeding to the language-specific
documentation.

Special care however must be taken when creating a Python class that subclasses
from a C++ class, as there are limitations to it.

The Theory
~~~~~~~~~~

The C++ classes do not exactly exist in the Python namespace. They can't;
they're C++ objects, not Python objects. Instead, for each C++ class that must
be available through Python, a wrapper class that has the same name as the C++
class and all of the same methods has been created. When you call one of the
methods on the Python wrapper, it turns around and calls the underlying C++
method of the same name. Thus, it looks like you're actually dealing directly
with the C++ object, even though you're really dealing with a Python object.

When you inherit from a C++ class, you are actually inheriting from the Python
wrapper class. You can't actually inherit from the C++ class itself, since
you're writing a Python class, not a C++ class.

This means that whenever you create an instance of your new inherited class,
you're creating an instance of the C++ class, the Python wrapper, and your
Python inherited class. But then if you pass a pointer of your instance to some
C++ method, all it receives is a pointer to the C++ class.

In the context of Panda, if you create an instance of a new "node" class and
store it in the scene graph, you are really only storing the underlying C++
object in the scene graph--the Python part of the object gets left behind.
This makes sense, because the C++ structures can only store pointers to C++
objects, not Python objects.

So, when you pull the node out of the scene graph later, it creates a new
Python wrapper around it and returns that new wrapper. Now all you have is the
original C++ node--it's not your new node class anymore, it's just the Python
wrapper to the C++ class.

The Practice
~~~~~~~~~~~~

With most C++ classes the only way forward is to create a new C++ subclass and
the related Python wrapper around it. However, there is a work-around for
classes such as PandaNode and NodePath. Both these C++ classes have in fact
been designed with functionality to store and retrieve python objects on them.
Specifically, the methods :meth:`~.NodePath.set_python_tag()`,
:meth:`~.NodePath.get_python_tag()` and :meth:`~.NodePath.has_python_tag()` are
available to respectively store, retrieve and check for the existence of a
pointer to an arbitrary Python object on these C++ objects.

This allows us to subclass from the Python wrapper class around the C++ object
and store, on the C++ object, a pointer to the new sub class.

Let's first see an example of what **doesn't** work:

.. code-block:: python

   import direct.directbase.DirectStart
   from panda3d.core import PandaNode

   # Here we define the new class, subclassing PandaNode
   # and adding a new variable to it.
   class MyNewNode(PandaNode):
       def __init__(self, aName):
           PandaNode.__init__(self, aName)
           self.aVariable = "A value"

   # Here we are creating a new node and we -think-
   # we are placing it in the scene graph:
   myNewNode = MyNewNode("MyNewNode")
   aNodePath = aspect2d.attachNewNode(myNewNode)

   # Here we -attempt- to fetch the stored variable,
   # but we'll get an error because aNodePath.node()
   # returns a PandaNode, not myNewNode!
   print(aNodePath.node().aVariable)

The workaround is for an instance of the new node class to store itself on the
PandaNode, as a Python tag:

.. code-block:: python

   import direct.directbase.DirectStart
   from panda3d.core import PandaNode

   # Here we define the new class, subclassing PandaNode
   # storing its own instance as a python tag and
   # initializing a new variable.
   class MyNewNode(PandaNode):
       def __init__(self, aName):
           PandaNode.__init__(self, aName)
           PandaNode.setPythonTag(self, "subclass", self)
           self.aVariable = "A value"

   # Here we create a new node and we are aware we are
   # placing its -PandaNode- in the scene graph.
   myNewNode = MyNewNode("MyNewNode")
   aNodePath = aspect2d.attachNewNode(myNewNode)

   # Now, first we fetch the panda node:
   thePandaNode = aNodePath.node()

   # then we fetch the instance of MyNewNode stored on it:
   theInstanceOfMyNewNode = thePandaNode.getPythonTag("subclass")

   # and finally we fetch the variable we were
   # interested in all along:
   print(theInstanceOfMyNewNode.aVariable)

In the real world
~~~~~~~~~~~~~~~~~

In a real-world scenario, while dealing with many nodes of arbitrary types,
things get only marginally more difficult. Ultimately you'll want to access
attributes that you know are present on nodes of one or more new subclasses.
For this purpose, once you have a handle to the subclass instance, you can
either test for the type you are expecting (safe but makes the application more
static) or you can test for the presence of the attribute itself (less safe but
creates potentially more dynamic, expandable application).

For example:

.. code-block:: python

   # here we setup the scene
   aNodePath = render.attachNewNode(anInstanceOfMyNewSubclass)
   aPandaNode = aNodePath.node()

   # here we loop over all nodes under render,
   # to find the one we are interested in:
   for child in render.getChildren()
       if child.hasPythonTag("subclass"):
           theInstanceOfASubclass = child.getPythonTag("subclass")

           # here we test for its type, which is safe
           # but doesn't catch subclasses of the subclass
           # or simply other objects that have the same
           # interface and would work just as well:
           if type(theInstanceOfASubclass) == type(MyNewSubclass):
               theInstanceOfASubclass.aVariable = "a new value"
               continue

           # here instead we test for the presence of an
           # attribute, which mean that all compatible
           # objects get modified:
           if hasattr(theInstanceOfASubclass, "aVariable"):
               theInstanceOfASubclass.aVariable = "a new value"
               continue

Conclusion
~~~~~~~~~~

In conclusion we might not be able to truly subclass a C++ class from Python,
but we can certainly get very close to it. There is of course an overhead and
these solutions should not be overused, resorting to pure C++ subclasses where
performance is an issue. But where performance is not -as much- of an issue,
you can probably get a lot of mileage following the examples provided above
and expanding upon them.
