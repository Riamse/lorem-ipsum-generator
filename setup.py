#!/usr/bin/env python

from setuptools import setup, find_packages
import sys


setup(
		name = 'lorem-ipsum-generator',
		version = '0.3',
		description = 'Generates random lorem ipsum text',
		long_description = 'Lorem Ipsum Generator provides a GTK+ graphical user interface, and a Python module, that generates random "lorem ipsum" text. The Lorem Ipsum Generator can produce a given quantity of paragraphs or sentences of "lorem ipsum" text.',
		author = 'James Hales',
		author_email = 'jhales.perth@gmail.com',
		license = 'BSD License',
		url = 'http://code.google.com/p/lorem-ipsum-generator/',
		py_modules = ['lipsum'],
        scripts = ['src/lorem-ipsum-generator', 'src/.lorem_ipsum_generator_postinstall.py'],
		data_files = [('share/doc/lorem-ipsum-generator', ['README', 'INSTALL', 'COPYING']), ('share/applications', ['data/lorem-ipsum-generator.desktop'])],
        packages = find_packages('src'),
        package_dir = {'' : 'src'},
        package_data = {
            'lipsum': ['data/lipsum.xml', 'data/sample.txt', 'data/dictionary.txt'],
            }
		)

