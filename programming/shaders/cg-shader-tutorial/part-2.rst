.. _cg-tutorial-part-2:

Cg Tutorial Part 2
==================

.. caution::

   Support for Cg shaders will be deprecated in an upcoming version of Panda3D.

Cg Tutorial Part 2: The Simplest Shader
---------------------------------------

In this part of the tutorial, we will introduce the barest shader possible and
then modify the python application to load this shader to verify that it
works. How would we know that it works? Well, this shader is so simple that it
basically makes our application useless and all we will see is a black screen.

The Shader
----------

.. code-block:: glsl

   //Cg
   /* lesson2.sha */

   void vshader(
       out float4 l_position : POSITION)
   {
       l_position = float4(0.0, 0.0, 0.0, 1.0);
   }

   void fshader(
       out float4 o_color : COLOR)
   {
       o_color = float4(1.0, 0.0, 1.0, 1.0);
   }

We'll only go through the basics of this shader for now. Also note that not
everything in this tutorial is a Cg requirement, some of the things such as
variable names are Panda3D requirements.

The first important thing in this shader is the first line, the ``//Cg``
comment. Removing it will cause the shader to fail compilation. This is a panda
requirement, telling the engine that the shader being loaded is a Cg shader.
Second, you see two functions; vshader and fshader. These are the respective
entry points for the vertex and fragment shaders.

The only requirements for a vertex shader is that it has to generate a
position. In Panda, objects move in three dimensions so having an output of 3
positions should be enough but on reading the vertex shader you can see that
its output is a float4. A float4 is an array of four float values, so what
possible use is the fourth value to the vertex shader? With this fourth value,
you can do some fancy stuff that you cannot do with a float3. In later
examples we will multiply the output with a float4 matrix, in other words 16
float values. A float3 cannot be multiplied by a float4 matrix. You can think
of the fourth value in the same way as the fourth component in an RGBA color,
the alpha component. Its not often necessary but it allows you to do
interesting things.

In this vertex shader, the only thing that we are doing is assigning the
variable l_position a constant float4. In C/C++/C# you cannot assign arrays to
arrays the way we do it here, but in Cg this is possible for fixed sized
arrays. The l_position variable can be renamed into anything you like, as long
as it is prefixed with l\_ and it has the "POSITION" keyword attached.

Why do we have to write "out" in front of l_position? In C/C++/C# every
function has at most one return value but shaders often need to return more
than one value. The NVIDIA guys added an "in" keyword and an "out" keyword to
Cg. "out" means that it is a return value. "in" means that is an input value.
This basic shader has no inputs at all and this is one of the main reasons it
cannot produce any useful results. Here we only output l_position but in later
examples we will have more then one output value.

The "POSITION" keyword is a hint for the GPU. The GPU then knows that is
should assign l_position to an internal POSITION register (register is a
simplification, this term might not be precise). This tells the GPU that it
will later have to draw the output of POSITION on the screen. Currently the
GPU does not know what color the pixels will have but it can calculate a
position on the screen for every given POSITION. The GPU itself is not as
smart as one might think, we need to do some not so simple math first to help
the GPU calculate the correct position on the screen.

More or less everything that was said about the vertex shader is true for the
fragment shader. The minimum requirement is that a fragment shader has to
create a color, to do this we have to assign a float4 to o_color. Again, you
can name this anything you like, but this time it needs to be prefixed with
o\_ and have the "COLOR" keyword attached.

Here the GPU needs the keyword "COLOR" for o_color. This is hint for the GPU
that we would like to assign a float4 to the color buffer of your screen. As
you may know, the range of a color component is 0 - 255 for R, G and B. That
is a fact the GPU knows and it translates the floating point values to
integers. The advantage of writing shaders in floating point is that if 48 bit
color displays become common, we do not have to change our shader and neither
would we have to change our shader if we only have a 16 bit color depth.

The Python Script
-----------------

The only thing we will change in our panda script is to load our shader file
and assign the shader on our root node. Run the script and you will see a
black screen, so theres no point in providing a screenshot for this one!

.. code-block:: python

   #Lesson2.py

   import sys
   import direct.directbase.DirectStart

   base.setBackgroundColor(0.0, 0.0, 0.0)
   base.disableMouse()

   base.camLens.setNearFar(1.0, 50.0)
   base.camLens.setFov(45.0)

   camera.setPos(0.0, -20.0, 10.0)
   camera.lookAt(0.0, 0.0, 0.0)

   root = render.attachNewNode("Root")

   modelCube = loader.loadModel("cube.egg")

   cubes = []
   for x in [-3.0, 0.0, 3.0]:
       cube = modelCube.copyTo(root)
       cube.setPos(x, 0.0, 0.0)
       cubes += [ cube ]

   # Load the shader from the file.
   shader = loader.loadShader("lesson2.sha")
   # Assign the shader to work on the root node
   # If you remove the line below, you will see
   # that panda is actually rendering our scene.
   root.setShader(shader)

   base.accept("escape", sys.exit)
   base.accept("o", base.oobe)

   def move(x, y, z):
       root.setX(root.getX() + x)
       root.setY(root.getY() + y)
       root.setZ(root.getZ() + z)

   base.accept("d", move, [1.0, 0.0, 0.0])
   base.accept("a", move, [-1.0, 0.0, 0.0])
   base.accept("w", move, [0.0, 1.0, 0.0])
   base.accept("s", move, [0.0, -1.0, 0.0])
   base.accept("e", move, [0.0, 0.0, 1.0])
   base.accept("q", move, [0.0, 0.0, -1.0])

   base.run()

Modifying the Shader
--------------------

Let's modify the shader to get some idea of what we can do in Cg. We still
won't be producing any output yet but it will give you a good overview of how
to write in Cg.

First lets see what happens when we try to use a float3 as the shader output.
Try changing the vertex shader to the sample below and then running the panda
script. Examine the console output carefully.

.. code-block:: glsl

   void vshader(
       out float4 l_position : POSITION)
   {
       l_position = float3(0.0, 0.0, 0.0, 1.0);
   }

Now this next vertex shader does exactly the same thing as the original shader
but shows how you can assign fixed length arrays to other fixed length arrays
in Cg.

.. code-block:: glsl

   void vshader(
       out float4 l_position : POSITION)
   {
       float4 zero = float4(0.0, 0.0, 0.0, 1.0);
       l_position = zero;
   }

Finally lets do some useless maths in the vertex shader. Also note how you can
assign a value to l_position more than once. You should try making your own
modifications to the shader and see if it can compile

.. code-block:: glsl

   void vshader(
       out float4 l_position : POSITION)
   {
       float4 zero = float4(0.0, 0.0, 0.0, 1.0);
       zero = zero * float4(1.0, 2.0, 3.0, 4.0);
       zero = zero * 5.0;
       l_position = zero;
       l_position = float4(0.0, 0.0, 0.0, 1.0);
   }

After modifying the vertex shader, try to modify the fragment shader on your
own. In the next tutorial, we will improve the shader's usefulness.

:ref:`Part 3: The Simplest Possible Useful Shader <cg-tutorial-part-3>`
