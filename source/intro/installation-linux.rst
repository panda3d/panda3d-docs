.. _installation-linux:

Installing Panda3D in Linux
===========================

The Installation Process - Linux
--------------------------------


The easiest way to install panda is to use the RPM or DEB packages. This is
only possible if your version of Linux is one of the provided versions of
Linux. If not, you will need to
:ref:`compile from source <building-from-source>`. If there is an installer
available, download and install the RPM or DEB appropriate to your version of
Linux.

After installing Panda, you should run the sample programs to verify that the
installation is good. To do so, you need to change directory to the Panda
samples directory, select a sample program, change directory to that sample,
and run the sample using Python:

::
    $ cd /usr/share/panda3d/samples
    $ ls
    Asteroids
    Ball-in-Maze
    Boxing-Robots
    Carousel
    Cartoon-Shader
    Chessboard
    Disco-Lights
    Fireflies
    Fractal-Plants
    Glow-Filter
    GUI
    Infinite-Tunnel
    Looking-and-Gripping
    Media-Player
    Motion-Trails
    Music-Box
    Normal-Mapping
    Particles
    Procedural-Cube
    Roaming-Ralph
    Shadows
    Solar-System
    Teapot-on-TV
    Texture-Swapping
    $ cd Boxing-Robots
    $ python Tut-Boxing-Robots.py


**Using an Unsupported Linux Distribution or an Unsupported Python**

Python packages need to be compiled for a particular variant of Python. For
example, a package that works with Python 2.4 will not work with Python 2.5. A
package that works with 32-bit Python will not work with 64-bit Python. A
package that works with UCS2 Python will not work with UCS4 Python. And so
forth. In short, a Python package must be carefully aligned,
feature-for-feature, with one particular Python interpreter. That package will
not work with any other Python interpreter.

Fortunately for you, our prepackaged copies of Panda3D are already carefully
matched. For example, our Panda3D for Ubuntu is already perfectly matched to
the Python interpreter that comes with that version of Ubuntu. So normally,
you don't need to worry about this at all.

If your Linux Distribution is not listed, you will need to build your own copy
of Panda3D. The build process will automatically create a copy of Panda3D
which perfectly matches your Linux Distribution's Python interpreter. This is
easy to do, but it does require a time-consuming compile. On the other hand,
trying to use an RPM or a DEB from some other Distribution is very unlikely to
work, because of this need for an exact feature-for-feature match between the
Python package (Panda3D) and the Python interpreter.

If you are using a copy of Python other than the one that came with the Linux
Distribution, you have a bigger problem. Panda3D's build-scripts automatically
build Panda3D for the system's native Python interpreter, not for some other
Python interpreter. To get Panda3D to build for some other Python interpreter,
you will have to edit the build scripts.

**What to do if you see the Error Message:**

If you see this error:

::
    display(error): The application requested hardware acceleration, but your OpenGL
    display(error): driver, GDI Generic, only supports software rendering.
    display(error): You need to install a hardware-accelerated OpenGL driver, or,
    display(error): if you actually *want* to use a software renderer, then
    display(error): alter the hardware/software configuration in your Config.prc file.
    display(error): Window wouldn't open; abandoning window.


This error is fairly self-explanatory: it means your video drivers are
inadequate. Obtain better drivers.

**What to do if you see the Error Message:**
``ImportError: No module named direct.directbase.DirectStart``

This error means it couldn't find the Python modules -- please make sure you
are running the correct version of Python (probably Python 2.7, that depends
on the Panda3D version) and that the panda3d.pth is located inside the Python
site-packages directory.

**What to do if you see the Error Message:**
``ImportError: /usr/lib/panda3d/libpandaexpress.so: undefined symbol: PyUnicodeUCS4_AsWideChar``

This could mean that your version of Python is compiled with the flag
``Py_UNICODE_SIZE`` set to
``2``. Please find a Python
version compiled with Py_UNICODE_SIZE set to 4 (which is usually the default).
See `this forum
topic <https://www.panda3d.org/forums/viewtopic.php?t=3904#20510>`__ for a
more detailed explanation about this problem.
