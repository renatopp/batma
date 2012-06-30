``batma.Engine``
================

:file: ``batma/core/engine.py``

.. class:: batma.Engine

   (SINGLETON)


Methods
-------

.. function:: engine.apply_config(game, *args, **kwargs)
   
   Apply new configuration to engine, in this method the engine sets the 
   :data:`batma.game` global and create a new :class:`Camera` to 
   :data:`batma.camera`. All arguments (except ``game``) are passed to 
   :data:`batma.display` in it :func:`display.apply_config`.


.. function:: engine.start()

   Start the engine. This method initializes the display (:func:`display.init`)
   and run the game. :func:`engine.start` is called automatically by 
   :func:`batma.run` function.


.. function:: engine.pause()

   Pause the engine. When this method is called, both the :func:`game.update`
   and :func:`game.draw` are not executed.


.. function:: engine.resume()

   Resume the paused engine.


.. function:: engine.stop()

   Stop the engine and end the game.


.. function:: engine.is_running()

   Return ``True`` if engine is not paused.