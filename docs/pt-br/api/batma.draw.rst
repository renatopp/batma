``batma.draw`` --- Drawing Primitives
=====================================

.. module:: batma.draw
   :synopsis: Module for drawing shapes.

:file: ``batma/graphics/draw.py``

Draw several shapes. Most of the primitives take a ``width`` argument to 
represent the size of stroke around the edge of the shape. If a width of 0 is 
passed the function will actually solid fill the entire shape.

All shapes use the ``batma.engine.default_color`` by default if the agurment is 
None.


Functions
---------

.. function:: rect(rect, color=None, width=0)

   Draws a rectangular shape. The given Rect is the area of the rectangle.


.. function:: polygon(points, color=None, width=0)

   Draws a polygonal shape. The pointlist argument is the vertices of the 
   polygon. For aapolygon, use aalines with the 'closed' parameter.


.. function:: circle(pos, radius, color=None, width=0)

   Draws a circular shape. The pos argument is the center of the circle, and 
   radius is the size.


.. function:: ellipse(rect, color=None, width=0)

   Draws an elliptical shape. The given rectangle is the area that the circle 
   will fill.     


.. function:: arc(rect, start_angle, stop_angle, color=None, width=1)

   Draws an elliptical arc. The rect argument is the area that the ellipse will 
   fill. The two angle arguments are the initial and final angle in radians, 
   with the zero on the right.


.. function:: line(start_pos, end_pos, color=None, width=1)

   Draw a straight line segment. There are no endcaps, the ends are squared off 
   for thick lines.


.. function:: lines(points, closed, color=None, width=1)

   Draw a sequence of lines. The pointlist argument is a series of points that 
   are connected by a line. If the closed argument is true an additional line 
   segment is drawn between the first and last points.

   This does not draw any endcaps or miter joints. Lines with sharp corners and 
   wide line widths can have improper looking corners.


.. function:: aaline(start_pos, end_pos, color=None, blend=1)

   Draws an anti-aliased line. This will respect the clipping rectangle. A 
   bounding box of the affected area is returned returned as a rectangle. If 
   blend is true, the shades will be be blended with existing pixel shades 
   instead of overwriting them. This function accepts floating point values 
   for the end points.


.. function:: aalines(points, closed, color=None, blend=1)

   Draws a sequence. You must pass at least two points in the sequence of 
   points. The closed argument is a simple boolean and if true, a line will be 
   draw between the first and last points. The boolean blend argument set to 
   true will blend the shades with existing shades instead of overwriting them. 
   This function accepts floating point values for the end points.

