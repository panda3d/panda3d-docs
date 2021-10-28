.. _multi-part-actors:

Multi-Part Actors
=================

It is possible to assemble a character model out of several separate pieces
(separate models). If this is the case, then the pieces must contain bones that
can be attached to each other. For example, if you have a robot consisting of a
set of legs and a swappable torso, and if you want to glue them together at the
waist, then the legs model should contain a bone "waist", and the torso model
should also contain a bone "waist". You can then attach them together:

.. code-block:: python

   nodePath = Actor.Actor(
       {
           'legs':'RobotLegs.egg',
           'torso':'RobotTorso1.egg',
       }, {
           'legs':{'dance':'RobotLegs-Dance.egg'},
           'torso':{'dance':'RobotTorso1-Dance.egg'},
       })
   nodePath.attach('torso','legs','waist')

Multi-part actors are fairly complicated. Each part is loaded from a separate
egg file, and each part has its own set of animations that are applied to it.
For each animation you want to play, you will need to have a corresponding egg
file for each part.

In the Actor constructor, you specify the list of model files with a dictionary
of part name to egg file, as shown above. The list of animation files is more
complicated; it's a dictionary of dictionaries. The outer dictionary maps part
names to animation dictionaries. Each animation dictionary maps animation name
to animation egg file for the corresponding part.

Here's another example:

.. code-block:: python

   myactor = Actor(
       # part dictionary
       {
           "head": "char/dogMM/dogMM_Shorts-head-mod",
           "torso": "char/dogMM/dogMM_Shorts-torso-mod",
           "legs": "char/dogMM/dogMM_Shorts-legs-mod"
       },
       # dictionary of anim dictionaries
       {
           "head": {
               "walk": "char/dogMM/dogMM_Shorts-head-walk",
               "run": "char/dogMM/dogMM_Shorts-head-run",
           },
           "torso": {
               "walk": "char/dogMM/dogMM_Shorts-torso-walk",
               "run": "char/dogMM/dogMM_Shorts-torso-run",
           },
           "legs": {
               "walk":"char/dogMM/dogMM_Shorts-legs-walk",
               "run":"char/dogMM/dogMM_Shorts-legs-run",
           },
       })

In addition multipart actor parts need to be connected together in a meaningful
fashion:

.. code-block:: python

   myactor.attach("head", "torso", "joint-head")
   myactor.attach("torso", "legs", "joint-hips")

The :py:meth:`~direct.actor.Actor.Actor.attach()` call names two parts, and
reparents the part named by the first parameter onto the part named by the
second parameter, at the node named by the third parameter, which should be an
exposed joint (that is, a joint in the part named by the second parameter).
You must have already exposed the joint before this call, either with the
egg- optchar command line tool, or by calling
:py:meth:`actor.exposeJoint() <direct.actor.Actor.Actor.exposeJoint>` at
runtime.

After calling :py:meth:`~direct.actor.Actor.Actor.attach()`, the stacked part
will inherit the animation from the attachment joint, by virtue of the scene
graph relationship.

Animation
---------

You can animate the parts as normal animations, but you need to supply the
partname, like this:

.. code-block:: python

   myactor.play('Animation Name', 'Part Name')

If you want to use AnimControl, as explained in
:ref:`this section <actor-animations>`, you must supply the part name as second
parameter in :py:meth:`~direct.actor.Actor.Actor.getAnimControl()`:

.. code-block:: python

   # you can see you just need to call
   # actor.getAnimControl('Animation Name', 'Part Name')
   # to get access to the AnimControl of that part.

   ac = actor.getAnimControl('Animation Name', 'Part Name')
   ac.isPlaying() # Returns a boolean whether the animation is playing or not
   ac.getFrame() # Returns the current frame number
   ac.getFrameRate() # Returns the speed of the animation, in frames per second
   ac.getFullFframe() # Returns a floating-point frame number.
   ac.getFullFrame() # Returns an integer frame number.
   ac.getNextFrame() # Returns the number of the next frame on the queue.
   ac.getNumFrames() # Returns the total number of frames
   ac.getPlayRate() # Returns the playrate. explained further below
   ac.loop() # Starts playing the animation in a loop
   ac.play() # Starts playing the animation
   ac.pose(frame) # Poses at frame frame
   ac.setPlayRate(rate) # Sets the playrate.  explained further below
   ac.stop() # Stops the animation

   # Note: the numbers returned by getFullFrame and getFullFframe keep counting
   # and may exceed the total number of frames.
