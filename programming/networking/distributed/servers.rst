.. _servers:

Servers
=======

In a distributed networking system, there are multiple types of servers like the
state server, AI server, database server and so on. Each server type has a
specific task and all servers will work closely together in the end.

The system is very flexible. It can be built to run from a single application
instance up to a multi machine multi application setup for large scale networked
games.

A very simple example of a server that would manage the basic state and AI
server would instantiate the Server Repository and the AI Repository parts as
shown in the next sections.
