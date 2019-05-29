.. _reading-the-html-tokens:

Reading the HTML tokens
=======================

Note: This article describes a deprecated feature as of Panda3D 1.10.0.

As described in :ref:`advanced-object-tags`, you can write Python code to
respond to any arbitrary tokens given in the <object> element. The AppRunner
provides several interfaces for this:

-  base.appRunner.tokens

This is a the raw token data, as a list of (token, value) tuples. Each token
in the <object> element, or in a <param> element within the <object> element,
will appear here, in the order they appear on the web page. You can traverse
this list if you have a token that supports multiple values. However, for most
token values, which only define one value each, it's probably easier to use
one of the following:

-  base.appRunner.getToken()
-  base.appRunner.getTokenInt()
-  base.appRunner.getTokenFloat()
-  base.appRunner.getTokenBool()

These define a simple accessor to query a value defined for a particular
token. They all return None if the token is not defined. The first form,
getToken(), is the simplest, and returns the string value exactly as it
appears on the web page. getTokenInt(), getTokenFloat(), and getTokenBool()
automatically coerce this value into an integer, floating-point number, and
boolean value.
