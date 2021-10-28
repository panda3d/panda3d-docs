.. _meshdrawer:

MeshDrawer
==========

:class:`.MeshDrawer` is a class with which you can draw geometry every frame as
fast as possible.  Common cases where you might want to use it include:
projectiles such as bullets, trails, and laser beams; and UI elements such as
health bars, labels, icons, and motion lines.

You create a MeshDrawer like this:

.. only:: python

   .. code-block:: python

      generator = MeshDrawer()
      generator.setBudget(1000)
      generatorNode = generator.getRoot()
      generatorNode.reparentTo(render)

.. only:: cpp

   .. code-block:: cpp

      #include "meshDrawer.h"
      ...
      MeshDrawer generator = MeshDrawer();
      generator.set_budget(1000);
      NodePath generatorNode = generator.get_root();
      generatorNode.reparent_to(window->get_render());

Basically this creates a MeshDrawer that will draw at most 1000 triangles or
500 billboarded quads on screen. Then it gets the root node inside the
MeshDrawer that has the geom that will be morphed into any thing you like.

You might also disable depth write, enable transparency, set two sided, add a
texture and re parent the geom to a fixed bin and render without lights. What
this code does is outside the mesh drawer and is done strictly to the node and
you probably had to do this to the special FX node's you have any ways.

.. only:: python

   .. code-block:: python

      generatorNode.setDepthWrite(False)
      generatorNode.setTransparency(True)
      generatorNode.setTwoSided(True)
      generatorNode.setTexture(loader.loadTexture("radarplate.png"))
      generatorNode.setBin("fixed",0)
      generatorNode.setLightOff(True)

.. only:: cpp

   .. code-block:: cpp

      generatorNode.set_depth_write(false);
      generatorNode.set_transparency(TransparencyAttrib::M_alpha);
      generatorNode.set_two_sided(true);
      generatorNode.set_texture(TexturePool::load_texture("radarplate.png"));
      generatorNode.set_bin("fixed",0);
      generatorNode.set_light_off();

The MeshDrawer is used in kind of an old style draw loop. I recommend creating
a specific task for MeshDrawer so that you can see how much time it eats up
using pstats. To the begin call you need to pass the render and base.cam so
that mesh drawer can figure out correct facing for billboards. A lot of FX
require billboards so it makes sense to precompute some of this facing stuff
at the start.

.. only:: python

   .. code-block:: python

      def drawtask(task):
          generator.begin(base.cam,render)

          ... your draw code ...

          generator.end()
          return task.cont

      taskMgr.add(drawtask, "meshdrawer task")

.. only:: cpp

   .. code-block:: cpp

      void drawTask() {
        // You'll need access to the window and the generator
        // Call this method in your update or use a task.
        generator.begin(window->get_camera_group(), window->get_render());

        ... your draw code ...

        generator.end()
      }

See the :class:`~panda3d.core.MeshDrawer` page in the API Reference to see a
complete overview of the available methods.

Many of the calls take a frame of Vec4() type. The frame is the
Vec4(x,y,width,height) coordinates inside the texture. Frame of Vec4(0,0,1,1)
would be the entire texture while Vec4(0,0,.5.5) would be NW quarter of the
texture. Note that the Vec4 coordinates starts counting from the bottom left,
counting to the top right. If you had a 16x16 plate, the 15th field in the
11th row would be: Vec4(14.0/16,5.0/16,1.0/16,1.0/16.)

This is use full to create palletized textures and show only small parts of
the texture per billboard. For instance you might have a images of the entire
forest in one texture and only render the trees you want by specifying their
UV cords.

MeshDrawer works by using calls similar to Panda3D's animation system and
basically creates a buffer of undefined vertices which is then morphed into
the shape you specify. Triangles which don't get used are turned into micro
(0,0,0) triangles so that they will not be visible. Then those vertices are
shipped to the GPU every frame, it's good to keep a low count of triangles in
this buffer. This is also why the begin and end are needed to mark the vertex
as being edited and then submit them back to Panda3D when finished.

You can also take a look at :class:`~panda3d.core.MeshDrawer2D`.

It follows a similar pattern as MeshDrawer but has stuff that is useful to
draw in 2d. Major differences is that its begin() takes no arguments and it
deals mostly with rectangles and borders around them. It also has a setClip
function which clips rectangles as they are drawn. This is very useful to draw
rectangles that appear to be inside other rectangles and be clipped by their
parents. It has only the low level abstraction on which you would have to
build your own UI components, or you can take a look at TreeGUI.
