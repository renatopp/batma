``batma.iter`` --- Iterators
============================

.. module:: batma.iter
   :synopsis: This module extends the builtin itertool module.


This module extends the python builtin ``itertool`` module.


Functions
---------

.. function:: bounce(iterable)

   Make an iterator returning elements from the ``iterable``. When the iterable 
   is exhausted, the process is repeated in reverse order. This is a shortcut 
   for::

       def bounce(iterable):
           itertools.chain(iterable, reversed(iterable))

   Example::
      
       batma.iter.bounce(['ABC']) # --> A B C C B A


.. function:: cycle_bounce(iterable)

   Its a combination of ``cycle`` and ``bounce`` functions, shortcut for::

       def cycle_bounce(iterable):
           return cycle(bounce(iterable))

   Example::

       batma.iter.cycle_bounce(['ABC']) # --> A B C C B A A B C C B A ...
   


Itertools Builtin Functions
---------------------------

.. function:: cycle(iterable)

   Make an iterator returning elements from the iterable and saving a copy of 
   each. When the iterable is exhausted, return elements from the saved copy. 
   Repeats indefinitely. Example::

       batma.iter.cycle(['ABC']) # --> A B C A B C A B ...

.. function:: chain(*iterable)

   Make an iterator that returns elements from the first iterable until it is 
   exhausted, then proceeds to the next iterable, until all of the iterables 
   are exhausted. Used for treating consecutive sequences as a single sequence. 
   Example::

       batma.iter.chain('ABC', 'DEF') # --> A B C D E F

Consults the full list of iterators in `Itertools documentation <http://docs.python.org/library/itertools.html>`_.