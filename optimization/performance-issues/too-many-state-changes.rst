.. _too-many-state-changes:

Too Many State Changes
======================

The state of an object is the sum of its color, material, light, fog, and other
attributes. It can be expensive, for a variety of reasons, to have too many
different states in your scene. It is better if many objects share the same
state.

One example is a model that consists of various parts, each with its own texture
and UV map. A texture is a kind of state change, so this will not be very
efficient. A better way to do this is to combine all the textures of the
different parts into a single larger texture, and use the UV map to reference
different parts of the same texture. This way, Panda only needs to send only a
single texture state change to the graphics card, rather than one for each part.

If different parts of the model all have their own state, this will additionally
prevent Panda from being able to flatten these parts of the model together, as
explained in :ref:`too-many-meshes`.
