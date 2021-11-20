.. _directbutton:

DirectButton
============

DirectButton is a DirectGui object that will respond to the mouse and can
execute an arbitrary function when the user clicks on the object. This is
actually implemented by taking advantage of the "state" system supported by
every DirectGui object.

Each DirectGui object has a predefined number of available "states", and a
current state. This concept of "state" is completely unrelated to Panda's
:ref:`FSM <finite-state-machines>` object. For a DirectGui object, the current
state is simply as an integer number, which is used to select one of a list of
different NodePaths that represent the way the DirectGui object appears in
each state. Each DirectGui object can therefore have a completely different
appearance in each of its states.

Most types of DirectGui objects do not use this state system, and only have
one state, which is state 0. The DirectButton is presently the only predefined
object that has more than one state defined by default. In fact, DirectButton
defines four states, numbered 0 through 3, which are called ready, press,
rollover, and disabled, in that order. Furthermore, the DirectButton
automatically manages its current state into one of these states, according to
the user's interaction with the mouse.

With a DirectButton, then, you have the flexibility to define four completely
different NodePaths, each of which represents the way the button appears in a
different state. Usually, you want to define these such that the ready state is
the way the button looks most of the time, the press state looks like the button
has been depressed, the rollover state is lit up, and the disabled state is
grayed out. In fact, the DirectButton interfaces will set these NodePaths up for
you, if you use the simple forms of the constructor (for instance, if you
specify just a single text string to the ``text`` parameter).

Sometimes you want to have explicit control over the various states, for
instance to display a different text string in each state. To do this, you can
pass a 4-tuple to the text parameter (or to many of the other parameters, such
as relief or geom), where each element of the tuple is the parameter value for
the corresponding state, like this:

.. code-block:: python

   b = DirectButton(text=("OK", "click!", "rolling over", "disabled"))

The above example would create a DirectButton whose label reads "OK" when it is
not being touched, but it will change to a completely different label as the
mouse rolls over it and clicks it.

Another common example is a button you have completely customized by painting
four different texture maps to represent the button in each state. Normally, you
would convert these texture maps into an egg file using ``egg-texture-cards``
like this:

.. code-block:: bash

   egg-texture-cards -o button_maps.egg -p 240,240 button_ready.png button_click.png button_rollover.png button_disabled.png

And then you would load up the that egg file in Panda and apply it to the four
different states like this:

.. code-block:: python

   maps = loader.loadModel('button_maps')
   b = DirectButton(geom=(maps.find('**/button_ready'),
                          maps.find('**/button_click'),
                          maps.find('**/button_rollover'),
                          maps.find('**/button_disabled')))

You can also access one of the state-specific NodePaths after the button has
been created with the interface ``myButton.stateNodePath[stateNumber]``.
Normally, however, you should not need to access these NodePaths directly.

The following are the DirectGui keywords that are specific to a DirectButton.
(These are in addition to the generic DirectGui keywords described on the
:ref:`previous page <directgui>`.)

============== ==================================================== ==========================
Keyword        Definition                                           Value
============== ==================================================== ==========================
command        Command the button performs when clicked             Function
extraArgs      Extra arguments to the function specified in command [Extra Arguments]
commandButtons Which mouse button must be clicked to do the command LMB, MMB, or RMB
rolloverSound  The sound made when the cursor rolls over the button AudioSound instance
clickSound     The sound made when the cursor clicks on the button  AudioSound instance
pressEffect    Whether or not the button sinks in when clicked      <0 or 1>
state          Whether or not the button is disabled                DGG.NORMAL or DGG.DISABLED
============== ==================================================== ==========================

Like any other :ref:`DirectGui <directgui>` widget, you can change any of the
properties by treating the element as a dictionary:

.. code-block:: python

   button["state"] = DGG.DISABLED

Example
-------

.. code-block:: python

   import direct.directbase.DirectStart
   from direct.gui.OnscreenText import OnscreenText
   from direct.gui.DirectGui import *

   from panda3d.core import TextNode

   # Add some text
   bk_text = "This is my Demo"
   textObject = OnscreenText(text=bk_text, pos=(0.95,-0.95), scale=0.07,
                             fg=(1, 0.5, 0.5, 1), align=TextNode.ACenter,
                             mayChange=1)

   # Callback function to set  text
   def setText():
           bk_text = "Button Clicked"
           textObject.setText(bk_text)

   # Add button
   b = DirectButton(text=("OK", "click!", "rolling over", "disabled"),
                    scale=.05, command=setText)

   # Run the tutorial
   base.run()

Note that you will not be able to set the text unless the mayChange flag is 1.
This is an optimization, which is easily missed by newcomers.

When you are positioning your button, keep in mind that the button's vertical
center is located at the base of the text. For example, if you had a button with
the word "Apple", the vertical center would be aligned with the base of the
letter "A".
