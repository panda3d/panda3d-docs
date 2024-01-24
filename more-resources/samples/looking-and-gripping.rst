.. _looking-and-gripping:

Sample Programs: Looking and Gripping
=====================================

To run a sample program, you need to install Panda3D.
If you're a Windows user, you'll find the sample programs in your start menu.
If you're a Linux user, you'll find the sample programs in /usr/share/panda3d.

.. rubric:: Screenshots

.. image:: screenshot-sample-programs-looking-and-gripping.png
   :height: 392

.. rubric:: Explanation

This tutorial will cover how you can manipulate actor joints in Panda. Joints
are essentially bones used by a 3D package (Maya, 3D Studio, XSI, etc) to
deform a character. The model is bound to these joints and moving these joints
will cause the model to deform. For example, rotating the shoulder joint will
move the arms, rotating the leg joints will bend the legs. In Panda, these
joints are normally not accessible. However, by controlling them with
controlJoint, you can manipulate the orientation of that joint in Panda
independent of its preloaded animations. You could even use a model without
premade animations and manipulate the joints manually in Panda.

Specifically in this tutorial, we will take control of the neck joint of a
humanoid character and rotate that joint to always face the mouse cursor. This
will in turn make the head of the character "look" at the mouse cursor. We
will also expose the hand joint using exposeJoint and use its positional data
to "attach" objects that the character can hold. By using exposeJoint, the
object will stay in the character's hand even if the hand is moving through an
animation.

.. note::
   Models with joints will differ greatly from each other depending on how they
   were made and who made them. You may find that a certain model's joints are
   not oriented logically or practically. Also beware that joints may have
   limits on how far they can twist. Going beyond a joints limits may cause
   strange and unwanted deformations.

.. rubric:: Back to the List of Sample Programs:

:ref:`samples`
