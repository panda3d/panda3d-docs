.. _keyboard-support:

Keyboard Support
================

Keyboard events
---------------

Panda3D has keyboard support built-in. Keyboard presses send
:ref:`Events <tasks-and-event-handling>`. Each keyboard key will send an event
when it is first pressed down, when it is released, and one repeatedly while
it is pressed.

The events can be accepted with the following code:

.. only:: python

   .. code-block:: python

      self.accept(<event name>, <function>)
      self.accept(<event name>, <function>, <parameters list>)
      self.acceptOnce(<event name>, <function>)
      self.acceptOnce(<event name>, <function>, <parameters list>)

.. only:: cpp

   .. code-block:: cpp

      framework->define_key(<event name>, <description>, <function>, nullptr);
      framework->define_key(<event name>, <description>, <function>, <data>);

<event name> is a string that labels the event. <function> is a python function
to be called when the event is sent. <parameters list> is a python list of
parameters to use to call <function>.

.. only:: python

   If you're wondering which events are being fired for certain keyboard
   activity, it is advised to call ``base.messenger.toggleVerbose()``. This will
   cause Panda3D to print out all the events that are being sent to the command-
   line prompt. This way, you can find out which keyboard key corresponds to
   which event name.

In general, the keyboard event naming follows the following rules:

1. Keys that type a character are named that character. It is always lowercase,
   even when shift or caps lock is pressed. (Shift and other modifiers are
   explained below.)

   ``"a", "b", "3", "[", etc.`` not ``"A", "B", "#", "{"``

2. The key down event is named for the key.

3. The keyboard autorepeat is named for the key + "-repeat" e.g.

   ``"a-repeat", "2-repeat", "[-repeat"``

4. The key up event is named for the key + "-up" e.g.

   ``"a-up", "2-up", "[-up"``

5. All key events (including "-up") have a corresponding time event labeled

   ``"time-" + <key name>``

Here is an example of time reading in code:

.. code-block:: python

   class ReadKeys(DirectObject.DirectObject):
       def __init__(self):
           self.accept('time-a-repeat', self.printRepeat)

       def printRepeat(self, when):
           print("repeat a", when)

6. Keys that don't type a character are labeled as follows::

   "escape", "f"+"1-12" (e.g. "f1","f2",..."f12"), "print_screen",
   "scroll_lock", "backspace", "insert", "home", "page_up", "num_lock",
   "tab",  "delete", "end", "page_down", "caps_lock", "enter", "arrow_left",
   "arrow_up", "arrow_down", "arrow_right", "shift", "lshift", "rshift",
   "control", "alt", "lcontrol", "lalt", "space", "ralt", "rcontrol"

Note that some key combinations (like ``print_screen`` on Windows) may be
intercepted by the operating system and may therefore not be available. If you
want to be able to catch these keys, you need to find some way to prevent the
system from intercepting the events. (however, "print_screen-up" is still
available in most cases.)

7. Some physical keys are distinguishable from the events that they fire, and
   some are not. The modifier keys distinguish between left and right, but send
   a neutral event as well. (e.g. the left shift key sends both "lshift" and
   "shift" events when pressed) Save for "num_lock", "*", and "+" the numpad
   keys are indistinguishable from the main keyboard counterparts. (e.g. when
   Num Lock is on the both the numpad and keyboard 1 keys send "1")

Here are some examples in code:

.. code-block:: python

   # Calls the function __spam() on the k key event.
   self.accept('k', self.__spam)

   # Calls __spam(eggs, sausage, bacon) on release of the K key.
   self.accept('k-up', self.__spam, [eggs, sausage, bacon,])

   # Exit on pressing the escape button.
   self.accept('escape', sys.exit)

   # Call spamAndEggs when up is pressed and at autorepeat if held.
   self.accept('arrow_up', self.spamAndEggs)
   self.accept('arrow_up-repeat', self.spamAndEggs)

   # Calls when the up arrow key is released.
   self.accept('arrow_up-up', self.spamAndEggs)

.. code-block:: cpp

   // Calls the function __spam(const Event* eventPtr, void* dataPtr) on the k key event.
   framework->define_key("k", "call k", __spam, nullptr);
   framework->define_key("k", "call k", __spam, &data);

   // Call spamAndEggs(const Event* eventPtr, void* dataPtr) when up is pressed
   // and at autorepeat if held.
   framework->define_key("arrow_up", "spam and egg", spamAndEggs, nullptr);
   framework->define_key("arrow_up-repeat", "spam and egg", spamAndEggs, nullptr);

   // Calls when the up arrow key is released
   framework->define_key("arrow_up-up", "spam and egg", spamAndEggs, nullptr);

.. note::

   When the Panda window is minimized or Panda3D loses focus, the "-up" event is
   sent for all currently held keys. Read this forum thread to learn more:
   https://discourse.panda3d.org/t/not-a-bug-solved-bug-with-up-events/4266

Modifier keys
-------------

When a key is pressed while a modifier key is pressed, such as shift, control or
alt, it is not sent in the usual way. Instead, the event name is modified by
prepending the name of the modifier key to the event name, separated by a dash,
in the order "shift", "control", "alt", for example:

``"shift-a" "shift-control-alt-a" "shift-alt-a"``

These compound events don't send a "time-" event. If you need one, use the
"time-" event sent by one of the keys in the combination.

The modifier compound events may optionally be turned off, in which case the "a"
event and the "shift" event will be sent separately:

.. only:: python

   .. code-block:: python

      base.mouseWatcherNode.set_modifier_buttons(ModifierButtons())
      base.buttonThrowers[0].node().set_modifier_buttons(ModifierButtons())

.. only:: cpp

   .. code-block:: cpp

      PT(MouseWatcher) mouse_watcher;
      mouse_watcher = DCAST(MouseWatcher, window->get_mouse().node());

      if (mouse_watcher != nullptr) {
        mouse_watcher->set_modifier_buttons(ModifierButtons());
      }

      ButtonThrower *bt = DCAST(ButtonThrower, window->get_mouse().get_child(0).node());
      if (bt != nullptr) {
        bt->set_modifier_buttons(ModifierButtons());
      }

Polling interface
-----------------

The above interfaces make use of events to cause a method to be called when the
key pressed or released. However, in some situations, it may be more desirable
to instead ask Panda every frame whether or not a certain key is pressed. In
this situation, you can use the polling interface instead, via the
:meth:`~.MouseWatcher.is_button_down()` method on the MouseWatcher node. (The
name of this class is a bit misleading - it listens for keyboard events as
well.)

.. code-block:: python

   forward_speed = 5.0 # units per second
   backward_speed = 2.0
   forward_button = KeyboardButton.ascii_key('w')
   backward_button = KeyboardButton.ascii_key('s')

   def move_task(self, task):
       speed = 0.0

       # Check if the player is holding W or S
       is_down = base.mouseWatcherNode.is_button_down

       if is_down(forward_button):
           speed += forward_speed

       if is_down(backward_button):
           speed -= backward_speed

       # Move the player
       y_delta = speed * globalClock.get_dt()
       self.player.set_y(self.player, y_delta)

Keystroke events
----------------

The interfaces described above are useful for listening for predetermined key
presses, like navigational keys or hot keys, but not for text input. Not only
are there no events for fancy keys in foreign languages, but a single key press
may not necessarily associate with a single letter to be entered in a text
field. This is because some international characters can only be typed using
multiple key presses.

Therefore, Panda3D has a concept of a *keystroke event*, which is used for text
input. Panda3D uses this under the hood for all GUI text entry. If you are
writing your own GUI widgets, it may be desirable for you to catch your own
keystroke events. To do this, it is first necessary to inform Panda3D which
event name should be sent when a keystroke occurs, after which you can accept it
as you would with any other event:

.. code-block:: python

   base.buttonThrowers[0].node().setKeystrokeEvent('keystroke')
   self.accept('keystroke', self.myFunc)

   def myFunc(self, keyname):
       print(keyname)

Raw keyboard events
-------------------

Normally, when you listen for a keyboard event, the user's configured keyboard
layout is taken into account. This may present problems for key bindings that
are determined by *position* on the keyboard. For instance, when using the
popular WASD control scheme for navigating the player, someone who's using an
AZERTY or dvorak keyboard layout may have to bend their fingers in an unnatural
way in order to use this scheme!

In light of this, Panda3D 1.9.0 introduced some features that will help to solve
this problem. The easiest way to fix this problem is to instead refer to the
keys by how they would appear on an ANSI US (QWERTY) keyboard layout. To do
this, you can prepend the ``raw-`` prefix to any key event. This will cause
Panda3D to *ignore* the user's configured keyboard layout, and instead report
the key as if the user had set his keyboard layout to ANSI US. It does this by
interpreting the raw scancode as sent by the hardware, rather than the virtual
key as reported by the operating system. (Note that raw events do not have
prefixes for modifier keys.)

This works for simple cases, but it is often necessary to have more specific
information about the way the keys are mapped in the user's system. For example,
showing "press W to move forward" may be confusing on someone with an AZERTY
layout, in which case it is more appropriate to say "press Z to move forward".
When the application has a configuration screen for the keyboard control scheme,
acquiring more information about the mapping may also be necessary.

This can be done using the :meth:`~.GraphicsWindow.get_keyboard_map()` method on
the GraphicsWindow object, returning a :class:`.ButtonMap` object, which can be
used to find out which virtual key event will be fired for a certain raw
keyboard button:

.. code-block:: python

   # Get the current keyboard layout.
   # This may be a somewhat expensive operation, so don't call
   # it all the time, instead storing the result when possible.
   map = base.win.get_keyboard_map()

   # Use this to print all key mappings
   print(map)

   # Find out which virtual key is associated with the ANSI US "w"
   w_button = map.get_mapped_button("w")

   # Get a textual representation for the button
   w_label = map.get_mapped_button_label("w")
   if w_label:
       # There is none, use the event name instead.
       w_label = str(w_button)
   w_label = w_label.capitalize()

   # Use this label to tell the player which button to press.
   self.tutorial_text = "Press %s to move forward." % (w_label)

   # Poll to check if the button is pressed...
   if base.mouseWatcherNode.is_button_down(w_button):
       print("%s is currently pressed" % (w_label))

   # ...or register event handlers
   self.accept("%s" % (w_button), self.start_moving_forward)
   self.accept("%s-up" % (w_button), self.stop_moving_forward)

The above code example also illustrates the use of the
:meth:`~.ButtonMap.get_mapped_button_label()` function to get a textual
representation for the button, if the operating system provides it. This is most
useful for keys like "shift" or "enter", which may be called differently on
different keyboards or in different languages. However, this is both system-
dependent and locale-dependent. You should not rely on it being present, and if
it is, you should not rely on consistent formatting or capitalization.

Of course, it is always advisable to still add in a configuration screen so that
users can customize key bindings in case they find a particular control scheme
difficult to use.
