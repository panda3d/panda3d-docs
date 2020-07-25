.. _dc-definition-files:

Distributed Class Definition
============================

The .dc file defines what distributed objects, and their functions, are
communicated across the network.

A direct.dc file is shipped with the engine and placed in the
direct/distributed/ path, which defines the necessary functionality for the
distributed objects bundled with Panda3D. You may want to copy this file to a
more convenient location related to your game to simplify the loading with the
lists used in the repositories shown before.

The syntax is a mix of C++ and python.

A simple example of such a dc file may look as follows.

.. code-block:: cpp

   import DGameObject/AI
   import AIDGameObject/AI

   struct gameDataModel {
     string value_a;
     uint8 value_b;
     int8 value_c/100;
   }

   dclass DGameObject: DistributedObject {
     sendGameData(gameDataModel data) p2p;
   };

   dclass AIDGameObject: DistributedObject {
     setAnounceGenerate(string helloMsg) broadcast ram;
     messageRoundtripToAI(gameDataModel data) p2p;
     messageRoundtripToClient(gameDataModel data) p2p;
   }

Keywords
--------

Keywords define the circumstances for propagating the data. They must be defined
at the start of the file.

Possible keywords are shown below:

.. code-block:: cpp

   keyword required;
   keyword broadcast;
   keyword ram;
   keyword p2p;
   keyword clsend;

The keywords are used for the following

required
   The parameters must be defined when generate() is called.

broadcast
   By default only the owner of the object will receive update messages. With
   the broadcast tag all copies of the object will receive the message. This
   will be the most frequently used tag in most cases, leave it off when you
   only want the owner of the object to receive a message such as a private
   chat, receiving gold, etc.

ram
   Normally the values sent over the wire will only be received by the
   interested clients, but a new client will not receive previously sent values.
   This is useful for things like chat. The values passed with a ram keyword
   will persist in memory and new clients will receive messages previously sent.
   This will be useful for things like position or names. Methods using this
   keyword have to define respective get* and set* methods to gather and set the
   value when re-sending it over the network.

p2p
   Only the owner of the object will receive updates for this method. The
   clsend keyword is implicitly included with this keyword.

clsend
   Normally only the owner of the object is allowed to send updates. With this
   keyword, the method can be updated by any client.

The required statement at the end of a field determines that this field has to
be set at the generation of the object. These fields have to be called set* as a
convention as in the python representation of that class the set gets taken away
at generation time and will be replaced with a get to call the set value with
the get functions return value.

For example, taking the dc representation of an Avatar class as defined here…

.. code-block:: cpp

   import Avatar
   dclass Avatar {
     setName(string n) required;
   }

…we get this Python class:

.. code-block:: python

   class Avatar:
       def getName(self):
           return self.name

       def setName(self, name):
           self.name = name

       def d_setName(self, name):
           self.sendUpdate("setName", [name])

       def b_setName(self, name):
           self.setName(name)
           self.d_setName(name)

Note if, for example, the name value gets changed locally after generation of
the DO, it doesn't automatically change the value of the DO on the server. This
has to be done manually. Though, calling the distributed versions of these
functions (as defined in the dc file) will automatically call the corresponding
functions of the representing python class on the client.

Python Imports
--------------

.. code-block:: cpp

   from direct.distributed import DistributedObject/AI
   from direct.distributed import TimeManager/AI
   from direct.distributed import DistributedNode/AI
   from direct.distributed import DistributedSmoothNode/AI

Any Python objects to be mapped for distributed networking should be imported
here. A modified python syntax is used. In the first line DistributedObject.py
and DistributedObjectAI.py will be mapped.

The /AI can also be used for module/filenames like this.

.. code-block:: cpp

   from someManager.DSomeManager/AI import DSomeManager/AI

This will import the DSomeManager class from ``someManager.DSomeManager.py``
and DSomeManagerAI from ``someManager.DsomeManagerAI.py``.

Variables
---------

1. int8, int16, int32, and int64: Signed integer values and bit size
2. uint8, uint16, uint32, and uint64: For unsigned integers
3. float64: A C double, for floating point numbers
4. string: An arbitrary string up to 64k in length. Obviously bandwidth
   intensive so avoid for frequent communication
5. char: Same as int8 but will be realized as a character
6. blob: String but arbitrary byte sequence usually not intended for print or
   something encoded that is too complicated for the normal dc system
7. Structures can also be identified as well.

Hint on floats: There only exists float64. For single precision floating point
numbers you can use integers like:

.. code-block:: cpp

   int16 foo/100

To conserve bandwidth when passing small float values it is possible to convert
them into ints by multiplying them by the given value and dividing them again.
int16 / 10 gives single-point precision for values between -3276.7 to 3276.7.
int16 / 100 will give two-point precision for values between -327.67 and 327.67.

Structs
-------

.. code-block:: cpp

   struct BarrierData {
     uint16 context;
     string name;
     uint32 avIds[];
   };

You can define C-style structs in addition to the dclass (defined below). This
is really the same thing as a dclass, except it can be embedded in a message
rather than created as an object in its own right. The struct may or may not
correspond with a Python class of the same name. If the struct does have a
Python representation, an instance of that class is created and passed in to
functions that receive this kind of parameter; otherwise, a tuple with all of
the fields is passed instead.

Arrays
------

Each variable can be an array by appending [#] on the end of a value where # is
the size of the array. You can also leave the value between the columns empty
and it will become a dynamic array. So it could look like this for a fixed:

.. code-block:: cpp

   int8[16] foo

and a dynamic array:

.. code-block:: cpp

   int8[] foo

Allowed range and list of ranges

If you want to only have a specified range of numbers that is allowed to be send
or set on a value, you can use it like this:

.. code-block:: cpp

   dclass Foo{
     setHam(int16(1-1000,2001-3000))
   }

This will only allow numbers from 1-1000 and 2001-3000. This can also be used in
array declarations.

dclass
------

.. code-block:: cpp

   dclass DistributedNode: DistributedObject {

Here the methods to be mapped in :class:`.DistributedNode` and
:class:`.DistributedNodeAI` are defined. Note that this inherits the definition
of DistributedObject. Multiple inheritance is also allowed.

.. code-block:: cpp

   setX(int16 / 10) broadcast ram;
   setY(int16 / 10) broadcast ram;
   setZ(int16 / 10) broadcast ram;

Here are three function definitions. When a DistributedNode receives a message
with the name "setX", :meth:`.DistributedNode.setX()` will be called and the
values passed to the function.

Syntax:
functionName(container variable1 <, container variable 2,...>) <parameters>;

.. code-block:: python

   setH(int16 % 360 / 10) broadcast ram;
   setP(int16 % 360 / 10) broadcast ram;
   setR(int16 % 360 / 10) broadcast ram;

   setPos: setX, setY, setZ;
   setHpr: setH, setP, setR;
   setPosHpr: setX, setY, setZ, setH, setP, setR;
   setXY: setX, setY;
   setXZ: setX, setZ;
   setXYH: setX, setY, setH;
   setXYZH: setX, setY, setZ, setH;

These messages are composed of previously defined messages. The message "setPos"
will contain the message "setX", "setY", "setZ" and their appropriate values.
