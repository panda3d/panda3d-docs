.. _pipeline-tips:

Pipeline Tips
=============

This section isn't totally related to Panda3D. However, these are a few good
pointers on how to keep the 'art to programmer' pipeline running smoothly.

How artists can help programmers with the pipeline
--------------------------------------------------

**"Keep renaming to a minimum, preferably with good names to start with, and
especially for parts or joints that the programmer will have to manipulate."**

Programmers generally deal with objects by their names, not with a graphical
tool like artists. Every time a name changes, a programmer has to make the
change in his or her code, and often has to hunt through the egg to try and
figure out what the name has changed to. In a large model, this can be very
time-consuming. If you do have to change a name, make sure to let the
programmer know when you give him or her the new model.

**"Check your model in pview before handing it off."**

The biggest delays in the pipeline come from the back and forth iterations
between artist and programmer. A quick check with pview will often find
missing textures, backward facing polygons, incorrect normals, mis-tagged
collision solids, and a host of other problems.

**"Build models with good hierarchy, and don't change the hierarchy
unnecessarily."**

A well organized hierarchy can make a model much easier for a programmer to
work with, and can also have a significant effect on rendering performance.
For rendering purposes, good hierarchies group objects that are close to each
other together, and don't have more than a few hundred to a few thousand
triangles (depending on the target hardware) in each node. (Low-end hardware
performs better with only a few hundred triangles per node; high-end hardware
performs better with several thousand triangles per node.)

**"Put groups of objects that the programmer will have to deal with in a
special way under a single node."**

For instance, if there's a section of an environment that will be hidden
during some point in the game, put that entire section under a single node.
The programmer might also like certain classes of collision solids to be under
a single node.

**"Don't use lossy compression (i.e. jpeg) for textures."**

Although jpegs save space on disk, they also degrade your beautiful textures!
If textures have to be manipulated later (i.e. downgraded), this degradation
will only be compounded. Every time you edit and resave a jpeg, the image
quality gets worse. Jpegs may need to be used in the finished product, but
it's always best to make this conversion the last step in the process, not the
first one. I recommend using the png format, which provides lossless
compression and full support for all color depths as well as alpha.

**"If there's any chance that an object will be broken apart and used as
separate pieces, give each piece a separate texture map."**

Nothing hurts worse than having to remap an object after its been painted, or
wasting huge swaths of texture space.

**"If parts of an object are semi-transparent, make sure those pieces are
separate parts in the hierarchy."**

Rendering semi-transparent objects is a little tricky. Each object with
transparency needs to be sorted back-to-front each frame by the rendering
engine. If things aren't going quite as planned, a programmer might need to
get a handle on a transparent part in order to manipulate its render order.

**"If a semi-transparent object is very large, or you can see through multiple
layers (like a glass sphere), break it up into separate pieces."**

Objects with multiple layers of transparency won't render correctly depending
on which angle they're being view from, because some of the polygons will be
drawn before others, and if it's all one object, the rendering engine can't
sort them back-to-front.

**"Use quads, and higher-order polygons, for collision solids when possible,
rather than triangles. But make sure your quads are planar."**

In general, dividing a quad into two triangles doubles the time it takes to
test a collision with it, so it is better to model collision polygons with
quads when possible. The same goes for five-sided and higher-order polygons as
well. However, there are two important requirements: (1) the collision
polygons must be convex, not concave, and (2) they must be perfectly flat (all
of the vertices must lie exactly in the same plane). If either of these is not
met, Panda will triangulate the polygon anyway.

Things that don't matter as much, but will give programmers warm-fuzzies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**"Use a consistent naming scheme."**

Programmers live in a world where names and naming conventions are incredibly
important. Nothing makes them happier than when the names of art assets fit in
well with their code. Common naming conventions are: mixedCaseNames,
CapitalizedMixedCaseNames, names_with_underscores, names-with-hyphens. Pick
one and stick with it.

**"Don't misspell things."**
