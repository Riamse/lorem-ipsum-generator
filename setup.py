#!/usr/bin/env python

from setuptools import setup
import sys


setup(
		name = 'lorem-ipsum-generator',
		version = 'trunk'
		description = 'Generates random lorem ipsum text',
		long_description = 'Lorem Ipsum Generator provides a GTK+ graphical user interface, and a Python module, that generates random "lorem ipsum" text. The Lorem Ipsum Generator can produce a given quantity of paragraphs or sentences of "lorem ipsum" text.',
		author = 'James Hales',
		author_email = 'jhales.perth@gmail.com',
		license = 'BSD License',
		url = 'http://code.google.com/p/lorem-ipsum-generator/',
		py_modules = ['lipsum'],
        scripts = ['lipsum', 'lipsum_postinstall.py'],
		data_files = [('share/lipsum', ['sample.txt', 'dictionary.txt']), ('share/doc/lorem-ipsum-generator', ['README', 'INSTALL', 'COPYING']), ('share/applications', ['lipsum.desktop'])]
		)

