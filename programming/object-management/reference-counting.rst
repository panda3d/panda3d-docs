.. _reference-counting:

Reference Counting
==================

Reference Counts
----------------

To manage the lifetime of objects, Panda3D has a reference counting system for
many objects. This means that for every object that uses this mechanism, a
reference count is kept which counts the number of references exist to that
object. Every time a new reference is made (eg. assigned to a new variable), the
reference count is increased. When the reference count reaches zero, the object
is deleted.

This is similar to Python's reference counting system, and in fact, the two
systems interact when Panda3D is used with Python. However, since an object's
lifetime may persist beyond the lifetime of an object in Python, Python's own
reference counting system alone is not sufficient.

.. only:: python

   Since this system is entirely integrated with Python's own reference counting
   system, you generally do not need to be concerned with the details of this
   system. This page only exists for advanced users who need to manipulate the
   reference count for low-level integration with C++ code.

The class that manages the reference count is :class:`.ReferenceCount`. To see
if a class is reference counted, check if it inherits from ReferenceCount.
C++ classes that are reference counted inherit from either
:class:`.ReferenceCount` or :class:`.TypedReferenceCount` (if use of the typing
system is desired), or another class that itself inherits from
:class:`.ReferenceCount`.

Managing Reference Counts
-------------------------

There are several ways that the reference count can be manipulated in code.
To get the number of references to an object, use the
:meth:`~.ReferenceCount.get_ref_count()` method.

The reference counted can be incremented and decremented manually using the
:meth:`~.ReferenceCount.ref()` and :meth:`~.ReferenceCount.unref()` methods, but
be careful! This messes up Panda's internal bookkeeping, and will likely cause
crashes and memory leaks. Do not do this unless you know exactly what you're
doing!

.. only:: cpp

   Smart Pointers
   ~~~~~~~~~~~~~~

   To correctly track references in C++ code, Panda3D needs to know whenever a
   new reference to the class is created. Therefore, Panda3D defines a template
   class ``PointerTo<T>`` which is just like the ordinary pointer ``T*``, except
   that the reference count is incremented when it is created or assigned, and
   decremented when it goes out of scope. There is a convenience macro ``PT(T)``
   to save typing.

   There is also a macro ``ConstPointerTo<T>``, shortened to ``CPT(T)``, which
   manages a pointer to a const object. This is similar to ``const T*`` in C++;
   the pointer can still be reassigned, but the object may not be modified.

   This is a usage example:

   .. code-block:: cpp

      PT(TextNode) node = new TextNode("title");

      node->set_text("I am a reference counted TextNode!");

   A ``PointerTo`` is functionally equivalent to a regular pointer, and it can
   cast implicitly to the appropriate pointer type. You can use ``ptr.p()`` to
   explicitly retrieve the underlying plain pointer.

   When they aren't necessary
   ~~~~~~~~~~~~~~~~~~~~~~~~~~

   Although it is safest to use ``PT(T)`` to refer to an object in all cases,
   in some cases it is not strictly necessary and may be more efficient not to.

   This can only be done, however, when you are **absolutely sure** that the
   reference count cannot decrease to zero during the time you might be using
   that reference. In particular, a getter or setter of a class storing a
   ``PointerTo`` need not take or return a ``PointerTo`` since the class object
   itself already holds a reference count.

   The following code example highlights a case where it is not necessary:

   .. code-block:: cpp

      PT(TextNode) node;
      node = new TextNode("title");

      use_text_node(node);

      void use_text_node(TextNode *node) {
        node->do_something();
      }

   One crucial example where the return value of a function has to be a
   ``PointerTo`` is where the function may return a new instance of the object:

   .. code-block:: cpp

      PT(TextNode) make_text_node() {
        return new TextNode("title");
      }

      PT(TextNode) node = make_text_node();

   Managing Reference Count
   ------------------------

   Although it is recommended to use ``PointerTo`` for all references, it is
   possible to manage the reference count manually using the ``ref()`` and
   ``unref()`` methods, as already stated above.

   This can not always work as an alternative, though, since an object returned
   from a function that returns a ``PointerTo`` may be destructed before you get
   a chance to call ``ref()`` to save it! This is why it's recommended to always
   use ``PointerTo`` except in very rare, low-level cases.

   .. warning::

     The :meth:`~.ReferenceCount.unref()` method should *not* be used if it may
     cause the reference count to reach zero. This is because a member function
     cannot destruct the object it is called on, so this will leak memory.
     Instead, you should use the ``unref_delete(pt)`` macro to decrease the
     reference count unless you are absolutely sure that it will not reach zero.

   Weak Pointer
   ------------

   A weak pointer stores a reference to an object without incrementing its
   reference count. In this respect it is just like a regular C++ pointer,
   except that weak pointers have extra advantages: they can know when the
   underlying object has been destructed.

   Weak pointers are implemented by ``WeakPointerTo<T>`` and
   ``WeakConstPointerTo<T>``, abbreviated to ``WPT(T)`` and ``WCPT(T)``,
   respectively. They work just like regular pointers, but be careful not to
   dereference it if it may have already been deleted! To see if it has been
   deleted, call ``ptr.was_deleted()``. The only thread safe way to access its
   value is to call ``ptr.lock()``, which returns ``nullptr`` if the pointer has
   been deleted (or is about to be), and otherwise returns a regular
   reference-counted PointerTo that ensures you can access it for as long as you
   hold it. This is a common idiom to access a weak pointer:

   .. code-block:: cpp

      if (auto ptr = weak_ptr.lock()) {
        // Safely use ptr in here.
      } else {
        // The pointer has been deleted.
      }

   Circular References
   -------------------

   When designing your class hierarchy, you should be particularly wary of
   circular references. This happens when object A stores a reference to object
   B, but object B also stores a reference to object A. Since each object will
   always retain a reference to the other object, the reference count will never
   reach zero and memory leaks may ensue.

   One way to solve this problem is to store a regular, non-reference counted
   pointer to object A in object B, and let object A unset the reference to
   itself in its destructor. This is not a general solution, however, and the
   most optimal solution depends on the specific situation.

   Stack Allocation
   ----------------

   In some rare cases, it is desirable to create a temporary instance of the
   object on the stack. To achieve this, it is necessary to call
   :cpp:func:`~ReferenceCount::local_object()` on the object directly after
   allocation:

   .. code-block:: cpp

      Texture tex;
      tex.local_object();

   However, this should only be used for very temporary objects, since reference
   counted objects are not meant to be passed by value. Other code may assume it
   is safe to store a reference to it, causing the application to crash after
   the object goes out of scope.
