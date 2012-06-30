``batma.util`` --- Utilities
============================

.. module:: batma.util
   :synopsis: Module for utility functions.

:file: ``batma/util.py``

Module for utility functions.

Decorators
----------

.. function:: singleton(cls)

   Singleton decorator. Example::

       @batma.util.singleton
       class MySingletonClass(object): pass


.. function:: classproperty(property)

   Decorator to make class properties. Example::

       class Vector2(object):
           @batma.util.classproperty
           @classmethod
           def One(cls):
               return Vector2(1, 1)

       vector = Vector2.One


Functions
---------

.. function:: frange(start, stop=None, step=1.0)
   
   A range function, that does accept float increments. Example::

       batma.util.frange(5)          # --> [0.0, 1.0, 2.0, 3.0, 4.0]
       batma.util.frange(5, 10)      # --> [5.0, 6.0, 7.0, 8.0, 9.0]
       batma.util.frange(5, 6, 0.2)  # --> [5.0, 5.2, 5.4, 5.6, 5.8]


.. function:: xfrange(start, stop=None, step=1.0)

   A xrange function, that does accept float increments. Example::

       batma.util.xfrange(5)         # --> [0.0, 1.0, 2.0, 3.0, 4.0]
       batma.util.xfrange(5, 10)     # --> [5.0, 6.0, 7.0, 8.0, 9.0]
       batma.util.xfrange(5, 6, 0.2) # --> [5.0, 5.2, 5.4, 5.6, 5.8]


.. function:: is_iterable(value)

   Verify if a ``value`` is an iterable. Example::

       batma.util.is_iterable([])        # --> True
       batma.util.is_iterable('asdf')    # --> True
       batma.util.is_iterable(2)         # --> False




