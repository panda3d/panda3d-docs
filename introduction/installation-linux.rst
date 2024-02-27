.. _installation-linux:

Installing Panda3D in Linux
===========================

The easiest way to install panda is to use the RPM or DEB packages. This is only
possible if your version of Linux is one of the provided versions of Linux. If
not, you will need to :ref:`compile from source <building-from-source>`. If
there is an installer available, download and install the RPM or DEB appropriate
to your version of Linux.

After installing Panda, you should run the sample programs to verify that the
installation is good. To do so, you need to change directory to the Panda
samples directory, select a sample program, change directory to that sample, and
run the sample using Python:

.. code-block:: bash

   $ cd /usr/share/panda3d/samples
   $ ls
   asteroids
   ball-in-maze
   boxing-robots
   bump-mapping
   carousel
   cartoon-shader
   chessboard
   culling
   disco-lights
   distortion
   fireflies
   fractal-plants
   gamepad
   glow-filter
   infinite-tunnel
   looking-and-gripping
   media-player
   motion-trails
   mouse-modes
   music-box
   particles
   procedural-cube
   render-to-texture
   roaming-ralph
   rocket-console
   shader-terrain
   shadows
   solar-system
   $ cd boxing-robots
   $ python3 main.py

**Using an Unsupported Linux Distribution or an Unsupported Python**

Python packages need to be compiled for a particular variant of Python. For
example, a package that works with Python 3.7 will not work with Python 3.8. A
package that works with 32-bit Python will not work with 64-bit Python. A
package that works with UCS2 Python will not work with UCS4 Python. And so
forth. In short, a Python package must be carefully aligned, feature-for-
feature, with one particular Python interpreter. That package will not work with
any other Python interpreter.

Fortunately for you, our prepackaged copies of Panda3D are already carefully
matched. For example, our Panda3D for Ubuntu is already perfectly matched to the
Python interpreter that comes with that version of Ubuntu. So normally, you
don't need to worry about this at all.

If your Linux Distribution is not listed, you will need to build your own copy
of Panda3D. The build process will automatically create a copy of Panda3D which
perfectly matches your Linux Distribution's Python interpreter. This is easy to
do, but it does require a time-consuming compile. On the other hand, trying to
use an RPM or a DEB from some other Distribution is very unlikely to work,
because of this need for an exact feature-for-feature match between the Python
package (Panda3D) and the Python interpreter.

If you are using a copy of Python other than the one that came with the Linux
Distribution, you have a bigger problem. Panda3D's build-scripts automatically
build Panda3D for the system's native Python interpreter, not for some other
Python interpreter. To get Panda3D to build for some other Python interpreter,
you will have to edit the build scripts.

**What to do if you see the Error Message:**

::

   ImportError: No module named direct.directbase.DirectStart

This error means it couldn't find the Python modules -- please make sure you are
running the correct version of Python (probably Python 3.7, that depends on the
Panda3D version) and that the panda3d.pth is located inside the Python
site-packages directory.

**What to do if you see the Error Message:**

::

   ImportError: /usr/lib/panda3d/libpandaexpress.so: undefined symbol: PyUnicodeUCS4_AsWideChar

This could mean that your version of Python is compiled with the flag
``Py_UNICODE_SIZE`` set to ``2``. Please find a Python version compiled with
Py_UNICODE_SIZE set to 4 (which is usually the default). See `this forum topic
<https://discourse.panda3d.org/t/installing-on-ubunutu-7-10/3561/24>`__ for a
more detailed explanation about this problem.  Upgrading to a more recent
version of Python (at least 3.3) may also resolve the problem.
