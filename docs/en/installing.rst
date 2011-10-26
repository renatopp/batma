====================
Installing the Batma
====================

------------
Requirements
------------

- Python 2.7 *~duh~* (not tested in 2.6 or lower)
  (http://www.python.org)

- Pyglet 1.1.4
  (http://pyglet.org/)


------------
Installation
------------

Installing using easy_install
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Via **easy_install** is the easiest way to install the Batma, it will install pyglet too if it's not found in system::

    easy_install batma


Installing using setup.py
^^^^^^^^^^^^^^^^^^^^^^^^^

Download the latest package [LINK HEHE!], extract to some directory and run::

    python setup.py install


Installing the hard way
^^^^^^^^^^^^^^^^^^^^^^^

Download the latest package [LINK HEHE!], extract to some directory and set the python path:

**Windows-only**::

    set PYTHONPATH c:\path\to\batma\;%PYTHONPATH%

**Linux, Mac OS X or Windows under cygwin**::
    
    set PYTHONPATH /path/to/batma/:$PYTHONPATH
    export PYTHONPATH


------------------
Testing your Batma
------------------

If everything went ok, just open a terminal (or cmd in windows), type::

    $ python -c "import batma"

If nothing happens, means that is ok! lol


