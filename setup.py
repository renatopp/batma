# -*- coding: utf-8 -*-

__author__ = 'Renato de Pontes Pereira'
__author_email__ = 'renato.ppontes@gmail.com'
__version__ = '0.0.1-beta'
__date__ = '2011 09 25'

try:
    import setuptools
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

from setuptools import setup, find_packages

f = open('README.rst','rU')
long_description = f.read()
f.close()

setup(
    name = 'batma',
    version = __version__,
    author = __author__,
    license='MIT License',
    description = '2D game engine inspired on XNA and cocos2d',
    long_description=long_description,
    url = 'http://renatopp.com/batma',
    download_url = 'https://github.com/renatopp/batma',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        ('Topic :: Software Development :: Libraries :: Python Modules'),
        ('Topic :: Games/Entertainment'),
    ],
    keywords='2d game engine opengl batma cocos2d xna pyglet',
    packages = find_packages(),
    install_requires=['pyglet>=1.1.4',],
    )