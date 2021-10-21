.. _egg-syntax:

Egg Syntax
==========

**The Egg Syntax**

This is a condensed version of the Egg Syntax document, incorporating only
syntax definitions in common use. For complete documentation, please see the
`Egg Syntax <https://raw.githubusercontent.com/panda3d/panda3d/master/panda/src/doc/eggSyntax.txt>`__
documentation from the Panda3D source code repository.

General Syntax
--------------

Egg files consist of a series of sequential and hierarchically-nested entries.
In general, the syntax of each entry is::

   <Entry-type> name { contents }

Comment text should be enclosed in quotation marks::

   <Comment> { text }

Local Information Entries
-------------------------

These nodes contain information relevant to the current level of nesting only::

   <Scalar> name { value }

Scalars are attributes of the entry the Scalar is in. Name is the attribute name
with value as the contents of that attribute.

Global Information Entries
--------------------------

These nodes contain information relevant to the file as a whole. They can be
nested along with geometry nodes, but this nesting is irrelevant and the only
significant placement rule is that they should appear before they are
referenced.

Coordinate System
~~~~~~~~~~~~~~~~~

The coordinate system for the file is specified like so::

   <CoordinateSystem> { string }

This entry indicates the coordinate system used in the egg file; the egg loader
will automatically make a conversion if necessary. The following strings are
valid: Y-up, Z-up, Y-up-right, Z-up-right, Y-up-left, or Z-up-left. (Y-up is the
same as Y-up-right, and Z-up is the same as Z-up-right.)

Textures
~~~~~~~~

This describes a texture file that can be referenced later with
``<TRef> { name }``::

   <Texture> name {
     filename
     <Scalar> scalar1 { value1 }
     <Scalar> scalar2 { value2 }
   }

Texture Scalars
^^^^^^^^^^^^^^^

The following attributes are presently implemented for textures:

<Scalar> alpha-file { alpha-filename }
   If this scalar is present, the texture file's alpha channel is read in from
   the named image file (which should contain a grayscale image), and the two
   images are combined into a single two- or four-channel image internally. This
   is useful for loading alpha channels along with image file formats like JPEG
   that don't traditionally support alpha channels.

<Scalar> alpha-file-channel { channel }
   This defines the channel that should be extracted from the file named by
   alpha-file to determine the alpha channel for the resulting channel.  The
   default is 0, which means the grayscale combination of r, g, b.  Otherwise,
   this should be the 1-based channel number, for instance 1, 2, or 3 for r, g,
   or b, respectively, or 4 for the alpha channel of a four-component image.

<Scalar> format { format-definition }
   This defines the load format of the image file.  The format-definition is one
   of:

     RGBA, RGBM, RGBA12, RGBA8, RGBA4,
     RGB, RGB12, RGB8, RGB5, RGB332,
     LUMINANCE_ALPHA,
     RED, GREEN, BLUE, ALPHA, LUMINANCE

   The formats whose names end in digits specifically request a particular texel
   width.  RGB12 and RGBA12 specify 48-bit texels with or without alpha; RGB8
   and RGBA8 specify 32-bit texels, and RGB5 and RGBA4 specify 16-bit texels.
   RGB332 specifies 8-bit texels. The remaining formats are generic and specify
   only the semantic meaning of the channels.  The size of the texels is
   determined by the width of the components in the image file. RGBA is the most
   general; RGB is the same, but without any alpha channel. RGBM is like RGBA,
   except that it requests only one bit of alpha, if the graphics card can
   provide that, to leave more room for the RGB components, which is especially
   important for older 16-bit graphics cards (the "M" stands for "mask", as in a
   cutout).

   The number of components of the image file should match the format specified;
   if it does not, the egg loader will attempt to provide the closest match that
   does.

<Scalar> compression { compression-mode }
   Defines an explicit control over the real-time compression mode applied to
   the texture.  The various options are:

     DEFAULT OFF ON
     FXT1 DXT1 DXT2 DXT3 DXT4 DXT5

   This controls the compression of the texture when it is loaded into graphics
   memory, and has nothing to do with on-disk compression such as JPEG.  If this
   option is omitted or "DEFAULT", then the texture compression is controlled by
   the compressed-textures config variable.  If it is "OFF", texture compression
   is explicitly off for this texture regardless of the setting of the config
   variable; if it is "ON", texture compression is explicitly on, and a default
   compression algorithm supported by the driver is selected.  If any of the
   other options, it names the specific compression algorithm to be used.

<Scalar> wrap { repeat-definition }
   \
<Scalar> wrapu { repeat-definition }
   \
<Scalar> wrapv { repeat-definition }
   \
<Scalar> wrapw { repeat-definition }
   This defines the behavior of the texture image outside of the normal (u,v)
   range 0.0 - 1.0.  It is "REPEAT" to repeat the texture to infinity, "CLAMP"
   not to.  The wrapping behavior may be specified independently for each axis
   via "wrapu" and "wrapv", or it may be specified for both simultaneously via
   "wrap".

   Although less often used, for 3-d textures wrapw may also be specified, and
   it behaves similarly to wrapu and wrapv.

   There are other legal values in addition to REPEAT and CLAMP. The full list
   is:

     CLAMP
     REPEAT
     MIRROR
     MIRROR_ONCE
     BORDER_COLOR

<Scalar> borderr { red-value }
   \
<Scalar> borderg { green-value }
   \
<Scalar> borderb { blue-value }
   \
<Scalar> bordera { alpha-value }
   These define the "border color" of the texture, which is particularly
   important when one of the wrap modes, above, is BORDER_COLOR.

<Scalar> type { texture-type }
   This may be one of the following attributes:

     1D
     2D
     3D
     CUBE_MAP

   The default is "2D", which specifies a normal, 2-d texture.  If any of the
   other types is specified instead, a texture image of the corresponding type
   is loaded.

   If 3D or CUBE_MAP is specified, then a series of texture images must be
   loaded to make up the complete texture; in this case, the texture filename is
   expected to include a sequence of one or more hash mark ("#") characters,
   which will be filled in with the sequence number.  The first image in the
   sequence must be numbered 0, and there must be no gaps in the sequence.  In
   this case, a separate alpha-file designation is ignored; the alpha channel,
   if present, must be included in the same image with the color channel(s).

<Scalar> multiview { flag }
   If this flag is nonzero, the texture is loaded as a multiview texture.  In
   this case, the filename must contain a hash mark ("#") as in the 3D or
   CUBE_MAP case, above, and the different images are loaded into the different
   views of the multiview textures.  If the texture is already a cube map
   texture, the same hash sequence is used for both purposes: the first six
   images define the first view, the next six images define the second view, and
   so on.  If the texture is a 3-D texture, you must also specify num-views,
   below, to tell the loader how many images are loaded for views, and how many
   are loaded for levels.

   A multiview texture is most often used to load stereo textures, where a
   different image is presented to each eye viewing the texture, but other uses
   are possible, such as for texture animation.

<Scalar> num-views { count }
   This is used only when loading a 3-D multiview texture.  It specifies how
   many different views the texture holds; the z height of the texture is then
   implicitly determined as (number of images) / (number of views).

<Scalar> read-mipmaps { flag }
   If this flag is nonzero, then pre-generated mipmap levels will be loaded
   along with the texture.  In this case, the filename should contain a sequence
   of one or more hash mark ("#") characters, which will be filled in with the
   mipmap level number; the texture filename thus determines a series of images,
   one for each mipmap level.  The base texture image is mipmap level 0.

   If this flag is specified in conjunction with a 3D or cube map texture (as
   specified above), then the filename should contain two hash mark sequences,
   separated by a character such as an underscore, hyphen, or dot.  The first
   sequence will be filled in with the mipmap level index, and the second
   sequence will be filled in with the 3D sequence or cube map face.

<Scalar> minfilter { filter-type }
   \
<Scalar> magfilter { filter-type }
   \
<Scalar> magfilteralpha { filter-type }
   \
<Scalar> magfiltercolor { filter-type }
   This specifies the type of filter applied when minimizing or maximizing.
   Filter-type may be one of:

     NEAREST
     LINEAR
     NEAREST_MIPMAP_NEAREST
     LINEAR_MIPMAP_NEAREST
     NEAREST_MIPMAP_LINEAR
     LINEAR_MIPMAP_LINEAR

   There are also some additional filter types that are supported for historical
   reasons, but each of those additional types maps to one of the above.  New
   egg files should use only the above filter types.

<Scalar> anisotropic-degree { degree }
   Enables anisotropic filtering for the texture, and specifies the degree of
   filtering.  If the degree is 0 or 1, anisotropic filtering is disabled.  The
   default is disabled.

<Scalar> envtype { environment-type }
   This specifies the type of texture environment to create; i.e. it controls
   the way in which textures apply to models. Environment-type may be one of:

     MODULATE
     DECAL
     BLEND
     REPLACE
     ADD
     BLEND_COLOR_SCALE
     MODULATE_GLOW
     MODULATE_GLOSS
     NORMAL*
     NORMAL_HEIGHT*
     GLOW*
     GLOSS*
     HEIGHT*
     SELECTOR*

   The default environment type is MODULATE, which means the texture color is
   multiplied with the base polygon (or vertex) color.  This is the most common
   texture environment by far.  Other environment types are more esoteric and
   are especially useful in the presence of multitexture.  In particular, the
   types suffixed by an asterisk (*) require enabling Panda's automatic
   ShaderGenerator.

<Scalar> combine-rgb { combine-mode }
   \
<Scalar> combine-alpha { combine-mode }
   \
<Scalar> combine-rgb-source0 { combine-source }
   \
<Scalar> combine-rgb-operand0 { combine-operand }
   \
<Scalar> combine-rgb-source1 { combine-source }
   \
<Scalar> combine-rgb-operand1 { combine-operand }
   \
<Scalar> combine-rgb-source2 { combine-source }
   \
<Scalar> combine-rgb-operand2 { combine-operand }
   \
<Scalar> combine-alpha-source0 { combine-source }
   \
<Scalar> combine-alpha-operand0 { combine-operand }
   \
<Scalar> combine-alpha-source1 { combine-source }
   \
<Scalar> combine-alpha-operand1 { combine-operand }
   \
<Scalar> combine-alpha-source2 { combine-source }
   \
<Scalar> combine-alpha-operand2 { combine-operand }
   These options replace the envtype and specify the texture combiner mode,
   which is usually used for multitexturing.  This specifies how the texture
   combines with the base color and/or the other textures applied previously.
   You must specify both an rgb and an alpha combine mode.  Some combine-modes
   use one source/operand pair, and some use all three; most use just two.

   ``combine-mode`` may be one of:

     REPLACE
     MODULATE
     ADD
     ADD-SIGNED
     INTERPOLATE
     SUBTRACT
     DOT3-RGB
     DOT3-RGBA

   ``combine-source`` may be one of:

     TEXTURE
     CONSTANT
     PRIMARY-COLOR
     PREVIOUS
     CONSTANT_COLOR_SCALE
     LAST_SAVED_RESULT

   ``combine-operand`` may be one of:

     SRC-COLOR
     ONE-MINUS-SRC-COLOR
     SRC-ALPHA
     ONE-MINUS-SRC-ALPHA

   The default values if any of these are omitted are::

      <Scalar> combine-rgb { modulate }
      <Scalar> combine-alpha { modulate }
      <Scalar> combine-rgb-source0 { previous }
      <Scalar> combine-rgb-operand0 { src-color }
      <Scalar> combine-rgb-source1 { texture }
      <Scalar> combine-rgb-operand1 { src-color }
      <Scalar> combine-rgb-source2 { constant }
      <Scalar> combine-rgb-operand2 { src-alpha }
      <Scalar> combine-alpha-source0 { previous }
      <Scalar> combine-alpha-operand0 { src-alpha }
      <Scalar> combine-alpha-source1 { texture }
      <Scalar> combine-alpha-operand1 { src-alpha }
      <Scalar> combine-alpha-source2 { constant }
      <Scalar> combine-alpha-operand2 { src-alpha }

<Scalar> saved-result { flag }
   If flag is nonzero, then it indicates that this particular texture stage will
   be supplied as the "last_saved_result" source for any future texture stages.

<Scalar> tex-gen { mode }
   This specifies that texture coordinates for the primitives that reference
   this texture should be dynamically computed at runtime, for instance to apply
   a reflection map or some other effect.  The valid values for mode are:

     EYE_SPHERE_MAP (or SPHERE_MAP)
     WORLD_CUBE_MAP
     EYE_CUBE_MAP (or CUBE_MAP)
     WORLD_NORMAL
     EYE_NORMAL
     WORLD_POSITION
     EYE_POSITION
     POINT_SPRITE

<Scalar> stage-name { name }
   Specifies the name of the TextureStage object that is created to render this
   texture.  If this is omitted, a custom TextureStage is created for this
   texture if it is required (e.g. because some other multitexturing parameter
   has been specified), or the system default TextureStage is used if
   multitexturing is not required.

<Scalar> priority { priority-value }
   Specifies an integer sort value to rank this texture in priority among other
   textures that are applied to the same geometry.  This is only used to
   eliminate low-priority textures in case more textures are requested for a
   particular piece of geometry than the graphics hardware can render.

<Scalar> blendr { red-value }
   \
<Scalar> blendg { green-value }
   \
<Scalar> blendb { blue-value }
   \
<Scalar> blenda { alpha-value }
   Specifies a four-component color that is applied with the color in case the
   envtype, above, is "blend", or one of the combine-sources is "constant".

<Scalar> uv-name { name }
   Specifies the name of the texture coordinates that are to be associated with
   this texture.  If this is omitted, the default texture coordinates are used.

<Scalar> rgb-scale { scale }
   \
<Scalar> alpha-scale { scale }
   Specifies an additional scale factor that will scale the r, g, b (or a)
   components after the texture has been applied.  This is only used when a
   combine mode is in effect.  The only legal values are 1, 2, or 4.

<Scalar> alpha { alpha-type }
   This specifies whether and what type of transparency will be performed.
   Alpha-type may be one of:

     OFF
     ON
     BLEND
     BLEND_NO_OCCLUDE
     MS
     MS_MASK
     BINARY
     DUAL

   If alpha-type is OFF, it means not to enable transparency, even if the image
   contains an alpha channel or the format is RGBA.  If alpha-type is ON, it
   means to enable the default transparency, even if the image filename does not
   contain an alpha channel.  If alpha-type is any of the other options, it
   specifies the type of transparency to be enabled.

<Scalar> bin { bin-name }
   This specifies the bin name order of all polygons with this texture applied,
   in the absence of a bin name specified on the polygon itself.  See the
   description for bin under polygon attributes.

<Scalar> draw-order { number }
   This specifies the fixed drawing order of all polygons with this texture
   applied, in the absence of a drawing order specified on the polygon itself.
   See the description for draw-order under polygon attributes.

<Scalar> depth-offset { number }
   \
<Scalar> depth-write { mode }
   \
<Scalar> depth-test { mode }
   Specifies special depth buffer properties of all polygons with this texture
   applied.  See the descriptions for the individual attributes under polygon
   attributes.

<Scalar> quality-level { quality }
   Sets a hint to the renderer about the desired performance / quality tradeoff
   for this particular texture.  This is most useful for the tinydisplay
   software renderer; for normal, hardware-accelerated renderers, this may have
   little or no effect.

   This may be one of:

     DEFAULT
     FASTEST
     NORMAL
     BEST

   "Default" means to use whatever quality level is specified by the global
   ``texture-quality-level`` config variable.

<Transform> { transform-definition }
   This specifies a 2-d or 3-d transformation that is applied to the UV's of a
   surface to generate the texture coordinates.

   The transform syntax is similar to that for groups, except it may define
   either a 2-d 3x3 matrix or a 3-d 4x4 matrix.  (You should use the two-
   dimensional forms if the UV's are two-dimensional, and the three-dimensional
   forms if the UV's are three-dimensional.)

   A two-dimensional transform may be any sequence of zero or more of the
   following.  Transformations are post multiplied in the order they are
   encountered to produce a net transformation matrix. Rotations are
   counterclockwise about the origin in degrees. Matrices, when specified
   explicitly, are row-major.

   ::

      <Translate> { x y }
      <Rotate> { degrees }
      <Scale> { x y }
      <Scale> { s }

       <Matrix3> {
         00 01 02
         10 11 12
         20 21 22
      }

   A three-dimensional transform may be any sequence of zero or more of the
   following.  See the description under <Group>, below, for more information.

   ::

      <Translate> { x y z }
      <RotX> { degrees }
      <RotY> { degrees }
      <RotZ> { degrees }
      <Rotate> { degrees x y z }
      <Scale> { x y z }
      <Scale> { s }

       <Matrix4> {
         00 01 02 03
         10 11 12 13
         20 21 22 23
         30 31 32 33
      }

Materials
~~~~~~~~~

This defines a set of material attributes that may later be referenced with
``<MRef> { name }``::

   <Material> name {
     [scalars]
   }


Material Scalars
^^^^^^^^^^^^^^^^

::

   <Scalar> diffr { number }
   <Scalar> diffg { number }
   <Scalar> diffb { number }
   <Scalar> diffa { number }
   <Scalar> ambr { number }
   <Scalar> ambg { number }
   <Scalar> ambb { number }
   <Scalar> amba { number }
   <Scalar> emitr { number }
   <Scalar> emitg { number }
   <Scalar> emitb { number }
   <Scalar> emita { number }
   <Scalar> specr { number }
   <Scalar> specg { number }
   <Scalar> specb { number }
   <Scalar> speca { number }
   <Scalar> shininess { number }
   <Scalar> local { flag }

Vertex Pool
~~~~~~~~~~~

A vertex pool is a set of vertices. All geometry is created by referring to
vertices by number in a particular vertex pool. There may be one or several
vertex pools in an egg file, but all vertices that make up a single polygon must
come from the same vertex pool. The body of a <VertexPool> entry is simply a
list of one or more <Vertex> entries, as follows:

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
omitted, the vertices are implicitly numbered consecutively beginning at one. If
the number is supplied, the vertices need not be consecutive.

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

::

   <Normal> { x y z [morph-list] }
   <RGBA> { r g b a [morph-list] }
   <UV> [name] { u v [w] [tangent] [binormal] [morph-list] }
   <Dxyz> target { x y z }

Geometry Entries
----------------

Geometry entries reference Vertex pool entries to generate renderable geometry
for Panda to use.

Polygons
~~~~~~~~

A polygon consists of a sequence of vertices from a single vertex pool. Vertices
are identified by pool-name and index number within the pool; indices is a list
of vertex numbers within the given vertex pool. Vertices are listed in
counterclockwise order. Although the vertices must all come from the same vertex
pool, they may have been assigned to arbitrarily many different joints
regardless of joint connectivity (there is no "straddle-polygon" limitation).
See Joints, below.

The polygon syntax is quite verbose, and there isn't any way to specify a set of
attributes that applies to a group of polygons--the attributes list must be
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

::

   <TRef> { texture-name }
   <Texture> { filename }
   <MRef> { material-name }
   <Normal> { x y z [morph-list] }
   <RGBA> { r g b a [morph-list] }
   <BFace> { boolean-value }
   <Scalar> bin { bin-name }
   <Scalar> draw_order { number }
   <Scalar> visibility { hidden | normal }

Grouping Entries
----------------

A <Group> node is the primary means of providing structure to the egg file.
Groups can contain vertex pools and polygons, as well as other groups. The egg
loader translates <Group> nodes directly into PandaNodes in the scene graph
(although the egg loader reserves the right to arbitrarily remove nodes that it
deems unimportant--see the <Model> flag, below to avoid this). In addition, the
following entries can be given specifically within a <Group> node to specify
attributes of the group.

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

::

   <DCS> { boolean-value }
   <DCS> { dcs-type }
   <Model> { boolean-value }
   <Dart> { boolean-value }
   <Switch> { boolean-value }

Group Scalars
~~~~~~~~~~~~~

The following scalars can be defined at the <Group> level::

   <Scalar> fps { frame-rate }
   <Scalar> bin { bin-name }
   <Scalar> draw_order { number }
   <Scalar> visibility { hidden | normal }
   <Scalar> decal { boolean-value }
   <Scalar> decalbase { boolean-value }
   <Scalar> collide-mask { value }
   <Scalar> from-collide-mask { value }
   <Scalar> into-collide-mask { value }
   <Scalar> blend { mode }
   <Scalar> blendop-a { mode }
   <Scalar> blendop-b { mode }
   <Scalar> blendr { red-value }
   <Scalar> blendg { green-value }
   <Scalar> blendb { blue-value }
   <Scalar> blenda { alpha-value }

Other Group Attributes
~~~~~~~~~~~~~~~~~~~~~~

Billboard
^^^^^^^^^

::

   <Billboard> { type }

This entry indicates that all geometry defined at or below this group level is
part of a billboard that will rotate to face the camera. Type is either "axis"
or "point", describing the type of rotation.

Billboards rotate about their local axis. In the case of a Y-up file, the
billboards rotate about the Y axis; in a Z-up file, they rotate about the Z
axis. Point-rotation billboards rotate about the origin.

There is an implicit <Instance> around billboard geometry. This means that the
geometry within a billboard is not specified in world coordinates, but in the
local billboard space. Thus, a vertex drawn at point 0,0,0 will appear to be at
the pivot point of the billboard, not at the origin of the scene.

SwitchCondition
^^^^^^^^^^^^^^^

::

   <SwitchCondition> {
      <Distance> {
         in out [fade] <Vertex> { x y z }
      }
   }

The subtree beginning at this node and below represents a single level of detail
for a particular model. Sibling nodes represent the additional levels of detail.
The geometry at this node will be visible when the point (x, y, z) is closer
than "in" units, but further than "out" units, from the camera. "fade" is
presently ignored.

Tag
^^^

::

   <Tag> key { value }

This attribute defines the indicated tag (as a key/value pair), retrievable via
``NodePath.get_tag()`` and related interfaces, on this node.

Collide
^^^^^^^

::

   <Collide> name { type [flags] }

This entry indicates that geometry defined at this group level is actually an
invisible collision surface, and is not true geometry. The geometry is used to
define the extents of the collision surface. If there is no geometry defined at
this level, then a child is searched for with the same collision type specified,
and its geometry is used to define the extent of the collision surface (unless
the "descend" flag is given; see below).

Valid types so far are:

Plane
   The geometry represents an infinite plane.  The first polygon found in the
   group will define the plane.

Polygon
   The geometry represents a single polygon.  The first polygon is used.

Polyset
   The geometry represents a complex shape made up of several polygons.  This
   collision type should not be overused, as it provides the least optimization
   benefit.

Sphere
   The geometry represents a sphere.  The vertices in the group are averaged
   together to determine the sphere's center and radius.

InvSphere
   The geometry represents an inverse sphere.  This is the same as Sphere, with
   the normal inverted, so that the solid part of an inverse sphere is the
   entire world outside of it.  Note that an inverse sphere is in infinitely
   large solid with a finite hole cut into it.

Tube
   The geometry represents a tube.  This is a cylinder-like shape with
   hemispherical endcaps; it is sometimes called a capsule or a lozenge in other
   packages.  The smallest tube shape that will fit around the vertices is used.

The flags may be any zero or more of:

event
   Throws the name of the <Collide> entry, or the name of the surface if the
   <Collide> entry has no name, as an event whenever an avatar strikes the
   solid.  This is the default if the <Collide> entry has a name.

intangible
   Rather than being a solid collision surface, the defined surface represents a
   boundary.  The name of the surface will be thrown as an event when an avatar
   crosses into the interior, and name-out will be thrown when an avatar exits.

descend
   Instead of creating only one collision object of the given type, each group
   descended from this node that contains geometry will define a new collision
   object of the given type.  The event name, if any, will also be inherited
   from the top node and shared among all the collision objects.

keep
   Don't discard the visible geometry after using it to define a collision
   surface; create both an invisible collision surface and the visible geometry.

level
   Stores a special effective normal with the collision solid that points up,
   regardless of the actual shape or orientation of the solid.  This can be used
   to allow an avatar to stand on a sloping surface without having a tendency to
   slide downward.

ObjectType
^^^^^^^^^^

::

   <ObjectType> { type }

This is a short form to indicate one of several pre-canned sets of attributes.
Type may be any word, and a Config definition will be searched for by the name
"egg-object-type-word", where "word" is the type word. This definition may
contain any arbitrary egg syntax to be parsed in at this group level.

A number of predefined ObjectType definitions are provided:

barrier
   This is equivalent to ``<Collide> { Polyset descend }``.  The geometry
   defined at this root and below defines an invisible collision solid.

trigger
   This is equivalent to ``<Collide> { Polyset descend intangible }``. The
   geometry defined at this root and below defines an invisible trigger surface.

sphere
   Equivalent to ``<Collide> { Sphere descend }``.  The geometry is replaced
   with the smallest collision sphere that will enclose it.  Typically you model
   a sphere in polygons and put this flag on it to create a collision sphere of
   the same size.

tube
   Equivalent to ``<Collide> { Tube descend }``.  As in sphere, above, but the
   geometry is replaced with a collision tube (a capsule). Typically you will
   model a capsule or a cylinder in polygons.

bubble
   Equivalent to ``<Collide> { Sphere keep descend }``.  A collision bubble is
   placed around the geometry, which is otherwise unchanged.

ghost
   Equivalent to ``<Scalar> collide-mask { 0 }``.  It means that the geometry
   beginning at this node and below should never be collided with--characters
   will pass through it.

backstage
   This has no equivalent; it is treated as a special case.  It means that the
   geometry at this node and below should not be translated.  This will normally
   be used on scale references and other modeling tools.

Joint Nodes
-----------

::

   <Joint> name {
     [transform]
     [ref-list]
     [joint-list]
   }


A joint is a highly specialized kind of grouping node. A tree of joints is used
to specify the skeletal structure of an animated character.

A joint may only contain one of three things. It may contain a ``<Transform>``
entry, as above, which defines the joint's unanimated (rest) position; it may
contain lists of assigned vertices or CV's; and it may contain other joints.

A tree of <Joint> nodes only makes sense within a character definition, which is
created by applying the <DART> flag to a group. See <DART>, above.

The vertex assignment is crucial. This is how the geometry of a character is
made to move with the joints. The character's geometry is actually defined
outside the joint tree, and each vertex must be assigned to one or more joints
within the tree.

This is done with zero or more <VertexRef> entries per joint, as the following::

   <VertexRef> { indices [<Scalar> membership { m }] <Ref> { pool-name } }

This is syntactically similar to the way vertices are assigned to polygons. Each
<VertexRef> entry can assign vertices from only one vertex pool (but there may
be many <VertexRef> entries per joint). Indices is a list of vertex numbers from
the specified vertex pool, in an arbitrary order.

The membership scalar is optional. If specified, it is a value between 0.0 and
1.0 that indicates the fraction of dominance this joint has over the vertices.
This is used to implement soft-skinning, so that each vertex may have partial
ownership in several joints.

The <VertexRef> entry may also be given to ordinary <Group> nodes. In this case,
it treats the geometry as if it was parented under the group in the first place.
Non-total membership assignments are meaningless.

Bundle and Table entries
------------------------

A table is a set of animated values for joints. A tree of tables with the same
structure as the corresponding tree of joints must be defined for each character
to be animated. Such a tree is placed under a <Bundle> node, which provides a
handle within Panda to the tree as a whole.

Bundles may only contain tables; tables may contain more tables, bundles, or any
one of the following (<Scalar> entries are optional, and default as shown)::

   <S$Anim> name {
     <Scalar> fps { 24 }
     <V> { values }
   }
