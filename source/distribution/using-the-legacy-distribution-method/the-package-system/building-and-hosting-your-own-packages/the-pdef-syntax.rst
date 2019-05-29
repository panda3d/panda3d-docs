.. _the-pdef-syntax:

The pdef syntax
===============

Note: This article describes a deprecated feature as of Panda3D 1.10.0.

A package definition looks something like a Python class definition:


.. code-block:: python

    class mypackage(package):
        file('neededfile.dll')
        module('my.python.module')
        dir('/c/my/root_dir')



In fact, you can put any Python syntax you like into a pdef file, and it will
be executed by ppackage. A pdef file is really just a special kind of Python
program. The class syntax shown above is just the convention by which packages
are declared.

The above sample generates a package called "mypackage", which contains the
file neededfile.dll and the Python module my/python/module.py, as well as all
files that those two files reference in turn; it also includes all of the
contents of c:\my\root_dir .

More details of the pdef syntax will be provided soon. In the meantime, you
can also examine the file direct/src/p3d/panda3d.pdef, for a sample file that
produces the panda3d package itself (as well as some related packages).

You can also examine the file direct/src/p3d/Packager.py; any method of
Packager named do_foo() produces a package function you can call named foo().
For instance, there is a Packager.do_file() method that accepts a Filename (as
well as other optional parameters); this method is called when file() appears
within a class definition in a pdef file.

Sometimes the files and modules you wish to include are not on the path, and
thus can not be found. To see what is on the path is when your pdef file is
run, you can use this at the top of your pdef file:


.. code-block:: python

    import sys
    print sys.path



Often when building packages, it's useful to have the working directory on the
path, but it may be missing. It can be added with:


.. code-block:: python

    import sys
    sys.path.insert(0,'') #add the working directory as the first entry in sys.path



When making p3d packages, you use p3d instead of package for the class. An
example p3d could be as follows:


.. code-block:: python

    import sys
    # add the working directory to the path so local files and modules can be found
    sys.path.insert(0,'') 
    
    class MyP3D(p3d):
        require('morepy','panda3d','somePackage') # include some other packages
            
        config( 
            version="0.0", 
            display_name="MyP3D") 
        
        module('core.*') # include the python package core, and its submodules
        dir('data',newDir='data') # include a folder called data
        mainModule('main') # include and set the main module that runs when the p3d is run
        file('events.txt') # include a text file



Generally what ppackage is pretty good about finding what modules are imported
and automatically including them, but there are cases where this fails and
explicitly specifying something like "module('api.*.*')" is useful.

As of Panda3D 1.7.1, you can specify an optional 'required' parameter to the
file() or module() function call. By setting it to true, you can indicate that
this file is vital to the package. Basically, when the file is missing and the
required flag is set, it will refuse to build the package (rather than just
emitting a warning).

You can put loops, if statements (based on os.name for example) and other flow
control inside packages, but calling functions outside of them that add files
and modules and such will not work.
