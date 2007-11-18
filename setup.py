#!/usr/bin/env python

from distutils.core import setup
import sys

scripts = ['lorem-ipsum-generator']

if 'bdist_wininst' in sys.argv:
	if 'sdist' in sys.argv or 'bdist_rpm' in sys.argv:
		print >> sys.stderr, 'Error: bdist_wininst must be run alone.'
	scripts.append('lorem_ipsum_generator_postinstall.py')

setup(
		name = 'lorem-ipsum-generator',
		version = '0.1.1',
		description = 'Generates random lorem ipsum text',
		long_description = 'Lorem Ipsum Generator provides a GTK+ graphical user interface, and a Python module, that generates random "lorem ipsum" text. The Lorem Ipsum Generator can produce a given quantity of paragraphs or sentences of "lorem ipsum" text.',
		author = 'James Hales',
		author_email = 'jhales.perth@gmail.com',
		license = 'GNU General Public Licence 3.0',
		url = 'http://code.google.com/p/lorem-ipsum-generator/',
		py_modules = ['lipsum'],
		scripts = scripts,
		#scripts = ['lorem-ipsum-generator'],
		data_files = [('share/lorem-ipsum-generator', ['sample.txt', 'dictionary.txt']), ('share/doc/lorem-ipsum-generator', ['README', 'INSTALL', 'COPYING']), ('share/applications', ['lorem-ipsum-generator.desktop'])]
		)

