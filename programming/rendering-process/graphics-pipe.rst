.. _the-graphics-pipe:

The Graphics Pipe
=================

The :class:`.GraphicsPipe` class is Panda3D's interface to the available 3-D
API's, for instance OpenGL or DirectX. In order to create a window that renders
using a particular API, you must have a GraphicsPipe for that API.

Normally, there is one default graphics pipe created for you automatically when
you import :py:mod:`~direct.directbase.DirectStart`, accessible as
``base.pipe``. For most applications, there is no need to create any additional
graphics pipes.

There are two Config.prc variables that determine the graphics pipe or pipes
that will be available to an application:

load-display
   This variable specifies the first choice for the graphics pipe. It names the
   type of GraphicsPipe that should be attempted first, e.g. pandagl or
   pandadx8. If for some reason a GraphicsPipe of this type cannot be created,
   for instance because of lack of driver support, then Panda3D will fall back
   to the next variable:

aux-display
   This variable can be repeated multiple times, and should list all of the
   available GraphicsPipe implementations. If Panda3D is unable to open a pipe
   of the type named by load-display, then it will walk through the list of
   pipes named by aux-display, in the order they appear in the Config.prc file,
   and try them one at a time until one is successfully opened.

Note that the name specified to each of the above variables, e.g. pandagl,
actually names a Windows DLL or Unix shared-library file. Panda3D will put "lib"
in front of the name and ".dll" or ".so" (according to the operating system)
after the name, and then attempts to import that library. This means that "load-
display pandagl" really means to try to import the file "libpandagl.dll". The
various display DLL's are written so that when they are successfully imported,
they will register support for the kind of GraphicsPipe they implement.

You can create additional graphics pipes, for instance to provide an in-game
interface to switch between OpenGL and DirectX rendering. The easiest way to do
this is to call ``base.makeAllPipes()``. Then you can walk through the list of
GraphicsPipes in ``base.pipeList`` to see all of the available GraphicsPipes
available in particular environment.

When you walk through the GraphicsPipes in base.pipeList, you can call the
following interface methods on each one:

pipe.isValid()
   Returns True if the pipe is available for rendering, False if it can’t be
   used.

pipe.getDisplayWidth()
   Returns the width of the desktop, or the maximum width of any buffer for an
   offscreen-only GraphicsPipe.

pipe.getDisplayHeight()
   Returns the height of the desktop, or the maximum height of any buffer for an
   offscreen-only GraphicsPipe.

pipe.getInterfaceName()
   Returns the name of the API that this GraphicsPipe impements, e.g. “OpenGL”
   or “DirectX8”.

pipe.getType()
   Returns a unique TypeHandle object for each kind of pipe.
