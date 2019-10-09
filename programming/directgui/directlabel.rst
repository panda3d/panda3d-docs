.. _directlabel:

DirectLabel
===========

Labels are like buttons, but they do not respond to mouse-clicks. This means a
DirectLabel is basically just a text string, and in that respect is similar to
:ref:`onscreentext`, except that the DirectLabel integrates better with the
rest of the DirectGUI system (and the constructor accepts more DirectGUI-like
options).

If you are making a text label to appear on a DirectFrame or in conjunction
with DirectGUI somehow, you should probably use a DirectLabel. For all other
uses of text, you would probably be better off using :ref:`onscreentext` or a
making a plain :ref:`text-node` instead.

DirectLabel's only unique keyword can be used if you want to create a label
with multiple states. If you set the value of activeState to a nonexistent
state, the label will disappear, since the default state is undefined.

=========== ========================================= ======
Keyword     Definition                                Value
=========== ========================================= ======
activeState The “active” or normal state of the label Number
=========== ========================================= ======
