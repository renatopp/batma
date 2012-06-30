``batma.Camera``
================

:file: ``batma/core/camera.py``

.. class:: batma.Camera

   Represents a 2D camera on the game. The camera is limited in positioning and
   anchoring. Moving the camera will move all GameObjects on the screen, except
   the ones with ``static`` setted as True. By default all :class:`Text` objects
   are statics.


Variables
---------

.. data:: camera.rect

   A :class:`Rect` object. 

.. data:: camera.x

   The camera position at the horizontal axis.

.. data:: camera.y

   The camera position at the vertical axis.

.. data:: camera.position

   Shortcut for the (:data:`x`, :data:`y`) variables.

.. data:: camera.anchor_x

   Camera anchor at the horizontal axis.

.. data:: camera.anchor_y

   Camera anchor at the vertical axis.

.. data:: camera.anchor

   Shortcut for the (:data:`anchor_x`, :data:`anchor_y`) variables. 

.. data:: camera.anchor_name

   READ ONLY. 

   Get the anchor name: ``topleft``, ``topright``, ``bottomleft``, 
   ``bottomright``, ``center`` or ``custom``.


Methods
-------

.. function:: camera.__init__(position=None, anchor='center')

   Constructor. By default all cameras are initialized with anchor in center 
   and position at the center of the screen.

.. function:: camera.reapply_anchor()

   Re-calculate the :data:`anchor` based on :data:`anchor_name` and 
   :data:`rect`.