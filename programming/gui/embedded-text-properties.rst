.. _embedded-text-properties:

Embedded Text Properties
========================

It's possible to change text properties in the middle of a paragraph. To do
this, you must first define the different kinds of text properties you might
want to change to, and give each one a name; then you can embed special
characters in your text string to switch these predefined text properties in
and out.

Defining your text properties
-----------------------------

You can create any number of :class:`.TextProperties` objects. Each of these can
store a different set of text properties, any of the text properties that you
can set directly on a :class:`.TextNode`. These include the per-character
attributes such as font, color, shadow, and slant, as well as per-line
formatting properties such as alignment and wordwrap.

.. code-block:: python

   tpRed = TextProperties()
   tpRed.setTextColor(1, 0, 0, 1)
   tpSlant = TextProperties()
   tpSlant.setSlant(0.3)
   tpRoman = TextProperties()
   tpRoman.setFont(cmr12)

You can set as many or as few different attributes on any one TextProperties
object as you like. Only the attributes you specify will be applied to the text
string; any attributes you don't mention will remain unchanged when you apply
the TextProperties. In the above example, applying the tpRed structure to a
particular text string will only change the text color to red; other properties,
such as slant, shadow, and font, will remain whatever they were previously.
Similarly for tpSlant, which only changes the slant, and tpRoman, which only
changes the font.

Registering the new TextProperties objects
------------------------------------------

You will need a pointer to the global :class:`.TextPropertiesManager` object:

.. code-block:: python

   tpMgr = TextPropertiesManager.getGlobalPtr()

After you have created your TextProperties objects, you must register each one
with the TextPropertiesManager, under a unique name:

.. code-block:: python

   tpMgr.setProperties("red", tpRed)
   tpMgr.setProperties("slant", tpSlant)
   tpMgr.setProperties("roman", tpRoman)

Referencing the TextProperties in text strings
----------------------------------------------

Now you're ready to put the special characters in your text string to activate
these mode changes. To do this, you will use the special character '\\1', or the
ASCII 0x01 character. You use the \\1 character twice, as a kind of quotation
mark before and after the name you have used above to register your
TextProperties object, e.g. '\\1red\\1' to activate tpRed, or '\\1slant\\1' to
activate tpSlant.

The sequence '\\1red\\1' acts as a push operation. It applies tpRed to the
current text properties, but also remembers the previous properties. To go back
to the previous properties, use the character '\\2' by itself. You can nest
property changes like this; each '\\2' will undo the most recent '\\1name\\1'
that is still in effect.

The following text string:

.. code-block:: python

   text.setText("Every day in \1slant\1every way\2 I'm \1red\1getting "
                "\1roman\1better \1slant\1and\2 better.\2\2")

Looks like this:

.. image:: text-attrib.png

You can use these special characters in any Panda construct that generates text,
including TextNode, OnscreenText, and any DirectGui object.
