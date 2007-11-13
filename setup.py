#!/usr/bin/env python

from distutils.core import setup

setup(
		name = 'lorem-ipsum-generator',
		version = '0.1',
		description = 'Generates random lorem ipsum text',
		author = 'James Hales',
		author_email = 'jhales.perth@gmail.com',
		url = 'http://code.google.com/p/lorem-ipsum-generator/',
		py_modules = ['lipsum'],
		scripts = ['lorem-ipsum-generator'],
		data_files = [('share/lorem-ipsum-generator/', ['sample.txt', 'dictionary.txt']), ('share/doc/lorem-ipsum-generator', ['README', 'INSTALL', 'COPYING']), ('share/applications/', ['lorem-ipsum-generator.desktop'])]
		)

