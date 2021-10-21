.. _uber-dogs:

Uber DOGs
=========

The Uber Distributed Object Globals are special objects which are used for game
global objects. These are similar to AI ones but are not dedicated to specific
zones, have a hardcoded doID and with that are directly accessible in the client
without the need for discovering them first like you'd have to do for other DOs.

Compared to other DOs, the DOGs do not store persistent data. Instead, they are
usually used for sending calls to request a server to run specific procedures.
These calls, done through the DOGs, usually also don't require the user to be
authenticated. This way public RPC-like APIs can best be implemented using them
as well as them being a good choice for implementing the client authentication
request logic.

The setup of a generic UD server is similar to that of an AI one. It only
differs in the used abbreviation (UD instead of AI) and the applications
specific implementation. Due to that, check the :ref:`ai-repositories` chapter
for further information.
