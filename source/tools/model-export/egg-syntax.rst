.. _egg-syntax:

Egg Syntax
==========

**The Egg Syntax**

This is a condensed version of the Egg Syntax document, incorporating only
syntax definitions in common use. For complete documentation, please see the
`Egg
Syntax <https://raw.githubusercontent.com/panda3d/panda3d/master/panda/src/doc/eggSyntax.txt>`__
documentation from the Panda3D source code repository.

\__TOC_\_

General Syntax
--------------

Egg files consist of a series of sequential and hierarchically-nested entries.
In general, the syntax of each entry is:

`` <Entry-type> name { contents }``

Comment text should be enclosed in quotation marks:

`` <Comment> { text }``

Local Information Entries
-------------------------

These nodes contain information relevant to the current level of nesting only.

`` <Scalar> name { value }``

Scalars are attributes of the entry the Scalar is in. Name is the attribute
name with value as the contents of that attribute.

Global Information Entries
--------------------------

These nodes contain information relevant to the file as a whole. They can be
nested along with geometry nodes, but this nesting is irrelevant and the only
significant placement rule is that they should appear before they are
referenced.

Coordinate System
~~~~~~~~~~~~~~~~~

`` <CoordinateSystem> { string }``

This entry indicates the coordinate system used in the egg file; the egg
loader will automatically make a conversion if necessary. The following
strings are valid: Y-up, Z-up, Y-up-right, Z-up-right, Y-up-left, or
Z-up-left. (Y-up is the same as Y-up-right, and Z-up is the same as
Z-up-right.)

Textures
~~~~~~~~

This describes a texture file that can be referenced later with <TRef> { name
}.

::
    <Texture> name {
      filename
      [scalars]
    }


Texture Scalars
^^^^^^^^^^^^^^^

This is not a complete list of texture attributes. Please refer to the full
document for all scalars and their value definitions

| `` <Scalar> alpha-file { alpha-filename }``
| `` <Scalar> alpha-file-channel { channel }``
| `` <Scalar> format { format-definition }``
| `` <Scalar> type { texture-type }``
| `` <Scalar> envtype { environment-type }``
| `` <Scalar> tex-gen { mode }``
| `` <Scalar> stage-name { name }``
| `` <Scalar> uv-name { name }``
| `` <Scalar> rgb-scale { scale }``
| `` <Scalar> alpha-scale { scale }``
| `` <Scalar> alpha { alpha-type }``
| `` <Transform> { transform-definition }``

Materials
~~~~~~~~~

This defines a set of material attributes that may later be referenced with
<MRef> { name }.

::
    <Material> name {
      [scalars]
    }


Material Scalars
^^^^^^^^^^^^^^^^

| `` <Scalar> diffr { number }``
| `` <Scalar> diffg { number }``
| `` <Scalar> diffb { number }``
| `` <Scalar> diffa { number }``
| `` <Scalar> ambr { number }``
| `` <Scalar> ambg { number }``
| `` <Scalar> ambb { number }``
| `` <Scalar> amba { number }``
| `` <Scalar> emitr { number }``
| `` <Scalar> emitg { number }``
| `` <Scalar> emitb { number }``
| `` <Scalar> emita { number }``
| `` <Scalar> specr { number }``
| `` <Scalar> specg { number }``
| `` <Scalar> specb { number }``
| `` <Scalar> speca { number }``
| `` <Scalar> shininess { number }``
| `` <Scalar> local { flag }``

Vertex Pool
~~~~~~~~~~~

A vertex pool is a set of vertices. All geometry is created by referring to
vertices by number in a particular vertex pool. There may be one or several
vertex pools in an egg file, but all vertices that make up a single polygon
must come from the same vertex pool. The body of a <VertexPool> entry is
simply a list of one or more <Vertex> entries, as follows:

::
    <VertexPool> name {
      <Vertex> number1 {
      }
      <Vertex> numer2 {
      }
      ...
    }


Vertices
^^^^^^^^

A <Vertex> entry is only valid within a vertex pool definition. The number is
the index by which this vertex will be referenced. It is optional; if it is
omitted, the vertices are implicitly numbered consecutively beginning at one.
If the number is supplied, the vertices need not be consecutive.

The vertex's coordinates are always given in world space, regardless of any
transforms before the vertex pool or before the referencing geometry. If the
vertex is referenced by geometry under a transform, the egg loader will do an
inverse transform to move the vertex into the proper coordinate space without
changing its position in world space. One exception is geometry under an
<Instance> node; in this case the vertex coordinates are given in the space of
the <Instance> node. (Another exception is a <DynamicVertexPool>; see below.)

::
    <Vertex> number {
        x y z [w]
        [attributes]
      }


Vertex Attributes
'''''''''''''''''

| `` <Normal> { x y z [morph-list] }``
| `` <RGBA> { r g b a [morph-list] }``
| `` <UV> [name] { u v [w] [tangent] [binormal] [morph-list] }``
| `` <Dxyz> target { x y z }``

Geometry Entries
----------------

Geometry entries reference Vertex pool entries to generate renderable geometry
for Panda to use.

Polygons
~~~~~~~~

A polygon consists of a sequence of vertices from a single vertex pool.
Vertices are identified by pool-name and index number within the pool; indices
is a list of vertex numbers within the given vertex pool. Vertices are listed
in counterclockwise order. Although the vertices must all come from the same
vertex pool, they may have been assigned to arbitrarily many different joints
regardless of joint connectivity (there is no "straddle-polygon" limitation).
See Joints, below.

The polygon syntax is quite verbose, and there isn't any way to specify a set
of attributes that applies to a group of polygons--the attributes list must be
repeated for each polygon. This is why egg files tend to be very large.

::
    <Polygon> name { 
        [attributes] 
        <VertexRef> { 
            indices 
            <Ref> { pool-name } 
        } 
    }


Polygon Attributes
^^^^^^^^^^^^^^^^^^

| `` <TRef> { texture-name }``
| `` <Texture> { filename }``
| `` <MRef> { material-name }``
| `` <Normal> { x y z [morph-list] }``
| `` <RGBA> { r g b a [morph-list] }``
| `` <BFace> { boolean-value }``
| `` <Scalar> bin { bin-name }``
| `` <Scalar> draw_order { number }``
| `` <Scalar> visibility { hidden | normal }``

Grouping Entries
----------------

A <Group> node is the primary means of providing structure to the egg file.
Groups can contain vertex pools and polygons, as well as other groups. The egg
loader translates <Group> nodes directly into PandaNodes in the scene graph
(although the egg loader reserves the right to arbitrarily remove nodes that
it deems unimportant--see the <Model> flag, below to avoid this). In addition,
the following entries can be given specifically within a <Group> node to
specify attributes of the group.

::
    <Group> name {
      [attributes]
      [scalars]
      [SwitchCondition]
      [Tag]
      [Collide]
      [ObjectType]
    }


Grouping Attributes
~~~~~~~~~~~~~~~~~~~

| `` <DCS> { boolean-value }``
| `` <DCS> { dcs-type }``
| `` <Model> { boolean-value }``
| `` <Dart> { boolean-value }``
| `` <Switch> { boolean-value }``

Group Scalars
~~~~~~~~~~~~~

| `` <Scalar> fps { frame-rate }``
| `` <Scalar> bin { bin-name }``
| `` <Scalar> draw_order { number }``
| `` <Scalar> visibility { hidden | normal }``
| `` <Scalar> decal { boolean-value }``
| `` <Scalar> decalbase { boolean-value }``
| `` <Scalar> collide-mask { value }``
| `` <Scalar> from-collide-mask { value }``
| `` <Scalar> into-collide-mask { value }``
| `` <Scalar> blend { mode }``
| `` <Scalar> blendop-a { mode }``
| `` <Scalar> blendop-b { mode }``
| `` <Scalar> blendr { red-value }``
| `` <Scalar> blendg { green-value }``
| `` <Scalar> blendb { blue-value }``
| `` <Scalar> blenda { alpha-value }``

Other Group Attributes
~~~~~~~~~~~~~~~~~~~~~~

Billboard
^^^^^^^^^

`` <Billboard> { type }``

This entry indicates that all geometry defined at or below this group level is
part of a billboard that will rotate to face the camera. Type is either "axis"
or "point", describing the type of rotation.

Billboards rotate about their local axis. In the case of a Y-up file, the
billboards rotate about the Y axis; in a Z-up file, they rotate about the Z
axis. Point-rotation billboards rotate about the origin.

There is an implicit <Instance> around billboard geometry. This means that the
geometry within a billboard is not specified in world coordinates, but in the
local billboard space. Thus, a vertex drawn at point 0,0,0 will appear to be
at the pivot point of the billboard, not at the origin of the scene.

SwitchCondition
^^^^^^^^^^^^^^^

| `` <SwitchCondition> {``
| ``    <Distance> { ``
| ``       in out [fade] <Vertex> { x y z }``
| ``    }``
| `` }``

The subtree beginning at this node and below represents a single level of
detail for a particular model. Sibling nodes represent the additional levels
of detail. The geometry at this node will be visible when the point (x, y, z)
is closer than "in" units, but further than "out" units, from the camera.
"fade" is presently ignored.

Tag
^^^

`` <Tag> key { value }``

This attribute defines the indicated tag (as a key/value pair), retrievable
via NodePath::get_tag() and related interfaces, on this node.

Collide
^^^^^^^

`` <Collide> name { type [flags] }``

This entry indicates that geometry defined at this group level is actually an
invisible collision surface, and is not true geometry. The geometry is used to
define the extents of the collision surface. If there is no geometry defined
at this level, then a child is searched for with the same collision type
specified, and its geometry is used to define the extent of the collision
surface (unless the "descend" flag is given; see below).

``   Valid types so far are:``

| ``   Plane``
| ``   ``
| ``     The geometry represents an infinite plane.  The first polygon``
| ``     found in the group will define the plane.``

``   Polygon``

| ``     The geometry represents a single polygon.  The first polygon is``
| ``     used.``

``   Polyset``

| ``     The geometry represents a complex shape made up of several``
| ``     polygons.  This collision type should not be overused, as it``
| ``     provides the least optimization benefit.``

``   Sphere``

| ``     The geometry represents a sphere.  The vertices in the group are``
| ``     averaged together to determine the sphere's center and radius.``

``   InvSphere``

| ``     The geometry represents an inverse sphere.  This is the same as``
| ``     Sphere, with the normal inverted, so that the solid part of an``
| ``     inverse sphere is the entire world outside of it.  Note that an``
| ``     inverse sphere is in infinitely large solid with a finite hole``
| ``     cut into it.``

``   Tube``

| ``     The geometry represents a tube.  This is a cylinder-like shape``
| ``     with hemispherical endcaps; it is sometimes called a capsule or``
| ``     a lozenge in other packages.  The smallest tube shape that will``
| ``     fit around the vertices is used.``

``   The flags may be any zero or more of:``

``   event``

| ``     Throws the name of the <Collide> entry, or the name of the``
| ``     surface if the <Collide> entry has no name, as an event whenever``
| ``     an avatar strikes the solid.  This is the default if the``
| ``     <Collide> entry has a name.``

``   intangible``

| ``     Rather than being a solid collision surface, the defined surface``
| ``     represents a boundary.  The name of the surface will be thrown``
| ``     as an event when an avatar crosses into the interior, and``
| ``     name-out will be thrown when an avatar exits.``

``   descend``

| ``     Instead of creating only one collision object of the given type,``
| ``     each group descended from this node that contains geometry will``
| ``     define a new collision object of the given type.  The event``
| ``     name, if any, will also be inherited from the top node and``
| ``     shared among all the collision objects.``

| ``   keep``
| ``     Don't discard the visible geometry after using it to define a``
| ``     collision surface; create both an invisible collision surface``
| ``     and the visible geometry.``

``   level``

| ``     Stores a special effective normal with the collision solid that``
| ``     points up, regardless of the actual shape or orientation of the``
| ``     solid.  This can be used to allow an avatar to stand on a``
| ``     sloping surface without having a tendency to slide downward.``

ObjectType
^^^^^^^^^^

`` <ObjectType> { type }``

This is a short form to indicate one of several pre-canned sets of attributes.
Type may be any word, and a Config definition will be searched for by the name
"egg-object-type-word", where "word" is the type word. This definition may
contain any arbitrary egg syntax to be parsed in at this group level.

``   A number of predefined ObjectType definitions are provided:``

``   barrier``

| ``     This is equivalent to <Collide> { Polyset descend }.  The``
| ``     geometry defined at this root and below defines an invisible``
| ``     collision solid.``

``   trigger``

| ``     This is equivalent to <Collide> { Polyset descend intangible }.``
| ``     The geometry defined at this root and below defines an invisible``
| ``     trigger surface.``

``   sphere``

| ``     Equivalent to <Collide> { Sphere descend }.  The geometry is``
| ``     replaced with the smallest collision sphere that will enclose``
| ``     it.  Typically you model a sphere in polygons and put this flag``
| ``     on it to create a collision sphere of the same size.``

``   tube``

| ``     Equivalent to <Collide> { Tube descend }.  As in sphere, above,``
| ``     but the geometry is replaced with a collision tube (a capsule).``
| ``     Typically you will model a capsule or a cylinder in polygons.``

``   bubble``

| ``     Equivalent to <Collide> { Sphere keep descend }.  A collision``
| ``     bubble is placed around the geometry, which is otherwise``
| ``     unchanged.``

``   ghost``

| ``     Equivalent to <Scalar> collide-mask { 0 }.  It means that the``
| ``     geometry beginning at this node and below should never be``
| ``     collided with--characters will pass through it.``

``   backstage``

| ``     This has no equivalent; it is treated as a special case.  It``
| ``     means that the geometry at this node and below should not be``
| ``     translated.  This will normally be used on scale references and``
| ``     other modeling tools.``

| ``   There may also be additional predefined egg object types not``
| ``   listed here; see the *.pp files that are installed into the etc``
| ``   directory for a complete list.``

| `` <Transform> { transform-definition }``
| `` <VertexRef> { indices <Ref> { pool-name } }``

Joint Nodes
-----------

::
    <Joint> name {
      [transform]
      [ref-list]
      [joint-list]
    }


A joint is a highly specialized kind of grouping node. A tree of joints is
used to specify the skeletal structure of an animated character.

A joint may only contain one of three things. It may contain a
``<Transform>`` entry, as above, which
defines the joint's unanimated (rest) position; it may contain lists of
assigned vertices or CV's; and it may contain other joints.

A tree of <Joint> nodes only makes sense within a character definition, which
is created by applying the <DART> flag to a group. See <DART>, above.

The vertex assignment is crucial. This is how the geometry of a character is
made to move with the joints. The character's geometry is actually defined
outside the joint tree, and each vertex must be assigned to one or more joints
within the tree.

This is done with zero or more <VertexRef> entries per joint, as the
following:

`` <VertexRef> { indices [<Scalar> membership { m }] <Ref> { pool-name } }``

This is syntactically similar to the way vertices are assigned to polygons.
Each <VertexRef> entry can assign vertices from only one vertex pool (but
there may be many <VertexRef> entries per joint). Indices is a list of vertex
numbers from the specified vertex pool, in an arbitrary order.

The membership scalar is optional. If specified, it is a value between 0.0 and
1.0 that indicates the fraction of dominance this joint has over the vertices.
This is used to implement soft-skinning, so that each vertex may have partial
ownership in several joints.

The <VertexRef> entry may also be given to ordinary <Group> nodes. In this
case, it treats the geometry as if it was parented under the group in the
first place. Non-total membership assignments are meaningless.

Bundle and Table entries
------------------------

A table is a set of animated values for joints. A tree of tables with the same
structure as the corresponding tree of joints must be defined for each
character to be animated. Such a tree is placed under a <Bundle> node, which
provides a handle within Panda to the tree as a whole.

Bundles may only contain tables; tables may contain more tables, bundles, or
any one of the following (<Scalar> entries are optional, and default as
shown):

::
    <S$Anim> name { 
      <Scalar> fps { 24 }
      <V> { values }
    }

