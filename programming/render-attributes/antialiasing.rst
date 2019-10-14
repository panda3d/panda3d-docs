.. _antialiasing:

Antialiasing
============

Antialiasing
------------

.. only:: cpp

    It is recommended to include:

    .. code-block:: cpp

        #include "antialiasAttrib.h"

The antialias attribute of a node controls what kind of antialiasing is to be
applied to that node. To choose one of the various forms of antialiasing,
invoke one of the following variants:

.. only:: python

    .. code-block:: python

        np.setAntialias(AntialiasAttrib.MNone)
        np.setAntialias(AntialiasAttrib.MPoint)
        np.setAntialias(AntialiasAttrib.MLine)
        np.setAntialias(AntialiasAttrib.MPolygon)
        np.setAntialias(AntialiasAttrib.MMultisample)
        np.setAntialias(AntialiasAttrib.MAuto)

.. only:: cpp

    .. code-block:: cpp

        nodePath.set_antialias(AntialiasAttrib::M_none);
        nodePath.set_antialias(AntialiasAttrib::M_point);
        nodePath.set_antialias(AntialiasAttrib::M_line);
        nodePath.set_antialias(AntialiasAttrib::M_polygon);
        nodePath.set_antialias(AntialiasAttrib::M_multisample);
        nodePath.set_antialias(AntialiasAttrib::M_auto);

In general, when rendering polygonal models, multisample antialiasing looks
best. However, when rendering lines and points, it usually looks better to
choose one of the specialized antialiasing modes. The
``MAuto`` setting automatically
selects the kind that usually works best for the geometry in question. Thus,
if you want to enable antialiasing on the whole scene, just use:

.. only:: python

    .. code-block:: python

        render.setAntialias(AntialiasAttrib.MAuto)

.. only:: cpp

    .. code-block:: cpp

        window->get_render().set_antialias(AntialiasAttrib::M_auto);

In order for multisample antialiasing to work, you have to have multisample
bits available in your framebuffer. To request this, add:

.. code-block:: text

    framebuffer-multisample 1
    multisamples 2

to your Config.prc
file. Note that not all graphics cards have this capability. You may also be
able to request more multisamples, such as 4 or 8, depending on your graphics
card. If your card can provide additional samples, it produces a
higher-quality antialiasing, at a small cost to render time.

The function ``clearAntialias`` can be
used to remove the antialias setting. The function
``setAntialias`` takes an optional
priority parameter, to control attribute overrides.
