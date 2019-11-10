# Panda3D Engine Documentation

This repository contains a work-in-progress conversion from the old Mediawiki format to a new Sphinx-based site. This should make it much easier for people to contribute to the documentation, and will also allow us to have the manual and API reference in one place.

Since this new format is still quite rough around the edges, Panda3D's main website will still be linking to the old manual.

The documentation can be found at: https://docs.panda3d.org/

## To-do List
- [x] Base conversion utilizing [the panda-sphinx repository](https://github.com/Moguri/panda-sphinx)
- [x] Manual fixes for formatting issues
- [ ] Welcome page (index.rst)
- [x] Move API Reference from Doxygen to Sphinx
- [ ] Spellcheck/proofread

## Building The Documentation
```
pip install -r requirements.txt
make html
```

## Coding Style

When editing the documentation, please try to conform to the following
guidelines:

* Running text should be wrapped to an 80-character ruler. Many editors have
  a feature to do this automatically (eg. Alt+Q in Sublime Text).
  Code may exceed this, as long as it follows our code guidelines for the
  respective language, with a strict limit of 86 characters relative to the base
  indent of the code block (LaTeX starts wrapping code beyond that).
* Please configure your editor to strip extra spaces at the end of a line.
* Use a single blank newline at the end of each file.
* Indentation for ReStructuredText should be 3 spaces, except code blocks,
  which need to be indented to 4 spaces for Python code and 2 for C++.
* The manual exists mostly to explain concepts and should not become a cookbook
  for code examples.  However, in a few cases it is helpful to have a complete
  code example listed.  In this case, put it in a separate .py file and refer to
  it using a `.. literalinclude::` block.
* When choosing a location for a new manual page, keep the filename concise, and
  try to avoid creating redundancy in the path. For example, prefer
  `bullet/tutorial.rst` over `the-bullet-integration/bullet-tutorial.rst`.
* Page titles should be underlined with `===`, sections with `---`, and finally,
  sub-sections with `^^^`, and the underline should be as wide as the title.
* You can link to a class in the API reference using ``:class:`.NodePath` `` and
  to a method with ``:meth:`.NodePath.reparentTo()` `` if you want to include
  the class prefix, or ``:meth:`~.NodePath.reparentTo()` `` if you just want to
  show the name of the method, like `reparentTo()`.  You can use custom text as
  well, like ``:meth:`myNodePath.reparentTo(render) <.NodePath.reparentTo>` ``.
* See the [Python guide](https://devguide.python.org/documenting/#style-guide)
  for more information.
