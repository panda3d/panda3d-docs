.. _fsm-introduction:

FSM Introduction
================

.. only:: python

   In Panda3D, FSM's are frequently used in game code to automatically handle the
   cleanup logic in game state changes. For instance, suppose you are writing a
   game in which the avatar spends most of his time walking around, but should go
   into swim mode when he enters the water. While he is walking around, you want
   certain animations and sound effects to be playing, and certain game features
   to be active; but while he is swimming, there should be a different set of
   animations, sound effects, and game features (this is just an example, of
   course):

   +-------------------------------------+-------------------------------------+
   | **Walk state**                      | **Swim state**                      |
   |                                     |                                     |
   | -  Should be playing "walk"         | -  Should be playing "swim"         |
   |    animation                        |    animation                        |
   | -  Should hear footsteps sound      | -  Should hear underwater sound     |
   |    effect                           |    effect                           |
   | -  Collision detection with doors   | -  Should have fog on camera        |
   |    should be active                 | -  Should have an air timer running |
   +-------------------------------------+-------------------------------------+

   So, when your avatar switches from walking to swimming, you would need to
   stop the footsteps sound effect, disable the door collisions, start playing
   the "swim" animation, start the underwater sound effect, enable the fog on
   the camera, and start the air timer.

   You could do all this by hand, of course. But using an FSM can make it
   easier. In this simple model, you could define an FSM with two states, "Walk"
   and "Swim". This might be represented graphically like this:

   .. digraph:: transitions

      rankdir=LR
      node [style=rounded, shape=box]

      Walk -> Swim;
      Swim -> Walk;

   To implement this as a Panda3D FSM, you would declare an new class that
   inherits from FSM, and within this class you would define four methods:
   ``enterWalk()``, ``exitWalk()``, ``enterSwim()``, and ``exitSwim()``. This
   might look something like this:

   .. code-block:: python

      from direct.fsm.FSM import FSM

      class AvatarFSM(FSM):
          def __init__(self):#optional because FSM already defines __init__
              #if you do write your own, you *must* call the base __init__ :
              FSM.__init__(self, 'AvatarFSM')
              ##do your init code here

          def enterWalk(self):
              avatar.loop('walk')
              footstepsSound.play()
              enableDoorCollisions()

          def exitWalk(self):
              avatar.stop()
              footstepsSound.stop()
              disableDoorCollisions()

          def enterSwim(self):
              avatar.loop('swim')
              underwaterSound.play()
              render.setFog(underwaterFog)
              startAirTimer()

          def exitSwim(self):
              avatar.stop()
              underwaterSound.stop()
              render.clearFog()
              stopAirTimer()

      myfsm = AvatarFSM()

   Keep in mind this is just an imaginary example, but it should give you an idea
   of what an FSM class looks like.

   Note that each enter method activates everything that is important for its
   particular state, and--this is the important part--the corresponding exit
   method turns off or undoes everything that was turned on by the enter method.
   This means that whenever the FSM leaves a particular state, you can be
   confident that it will completely disable anything it started when it entered
   that state.

   Now to switch from Walk state to Swim state, you would just need to request a
   transition, like this:

   .. code-block:: python

      myfsm.request('Swim')

   This FSM is a
   very simple example. Soon you will find the need for more than two states. For
   instance, you might want to play a transition animation while the avatar is
   moving from Walk state to Swim state and back again, and these can be encoded
   as separate states. There might be a "drowning" animation if the avatar stays
   too long underwater, which again might be another state. Graphically, this now
   looks like this:

   .. digraph:: transitions

      rankdir=LR
      node [style=rounded, shape=box]

      Walk -> Walk2Swim;
      Walk2Swim -> Swim;
      Swim -> Swim2Walk;
      Swim2Walk -> Walk;
      Swim -> Drowning;

      { rank=same; Walk2Swim; Swim2Walk; }

   In a real-world example, you might easily find you have a need for dozens of
   states. This is when using the FSM class to manage all of these transitions
   for you can really make things a lot simpler; if you had to keep all of that
   cleanup code in your head, it can very quickly get out of hand.

.. only:: cpp

   This section does not apply to C++ users.
