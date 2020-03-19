# Panda3D Documentation

This repository contains the source code for the documentation of the
[Panda3D](https://www.panda3d.org/) game engine.

The resulting documentation can be found at: https://docs.panda3d.org/

## Building the Documentation

The documentation is built upon [Sphinx](https://www.sphinx-doc.org/en/master/),
and several extensions are required.  The easiest way to install Sphinx and the
extensions into an existing Python installation is using pip:
```
pip install -r requirements.txt
```

You can then build the manual in the desired format.  For example, you can build
it in the HTML format by executing this command in your command prompt:
```
make html
```

If the command was successful, the resulting documentation can be found in the
`_build/html` folder.  Other formats are also possible, such as `make latexpdf`
for producing a .pdf file.  Consult the Sphinx manual for other options.

On Windows, if you receive an error like the following:
```
The 'sphinx-build' command was not found. Make sure you have Sphinx
installed, then set the SPHINXBUILD environment variable to point
to the full path of the 'sphinx-build' executable. Alternatively you
may add the Sphinx directory to PATH.
```

It may be the case that your Python Scripts folder is not on the PATH.  The
easiest way to deal with this is by setting your SPHINXBUILD variable something
like so (adjust for the location of your Python build):

```
set SPHINXBUILD=C:\Panda3D-1.10.6-x64\python\python.exe -m sphinx
```

## Editing the Documentation

To make changes, simply edit the .rst files in a code editor and rerun the
`make html` command to rebuild only the files that have changed.

To propose changes, push the changes to a local branch on a fork of the GitHub
repository and open a Pull Request.  For more information on how to do this,
refer to this guide:

https://opensource.guide/how-to-contribute/#opening-a-pull-request

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
