#
# Copyright James Hales, 2007. <jhales.perth@gmail.com>
#
# This file is part of the Lorem Ipsum Generator.
# 
# The Lorem Ipsum Generator is free software: you can redistribute it 
# and/or modify it under the terms of the GNU General Public License 
# as published by the Free Software Foundation, either version 3 of 
# the License, or (at your option) any later version.
# 
# The Lorem Ipsum generator is distributed in the hope that it will 
# be useful, but WITHOUT ANY WARRANTY; without even the implied 
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with the Lorem Ipsum Generator.  If not, 
# see <http://www.gnu.org/licenses/>.

import math
import random
import string
import re

class generator(object):
	"""
	Generates random strings of "lorem ipsum" text,	based on the word 
	distribution of a given sample text, using the words in a given 
	dictionary.
	"""

	__word_delimiters = ['.', ',', '?', '!']
	__sentence_delimiters = ['.', '?', '!']

	# Public methods

	def generate_sentence(self, start_with_lorem=False, sentence_mean=None, sentence_stddev=None):
		"""
		Generates a single sentence, of random length.

		If start_with_lorem=True, then the sentence will begin with the
		standard "Lorem ipsum..." first sentence.
		"""

		# Initialise variables being used
		sentence = []
		previous = ()

		chains = self.__chains
		sentence_delimiting_words = self.__sentence_delimiting_words
		dictionary = self.__dictionary
		word_delimiter = ''

		# Determine randomly the length of the sentence
		try:
			sentence_length = random.normalvariate(sentence_mean, sentence_stddev)
		except:
			sentence_length = random.normalvariate(self.__sentence_mean, self.__sentence_stddev)

		sentence_length = max(int(round(sentence_length)), 1)

		# Just return "Lorem ipsum..." if start_with_lorem is True
		if start_with_lorem:
			lorem = "lorem ipsum dolor sit amet, consecteteur adipiscing elit".split()
			sentence += lorem
		
		# Otherwise generate a sentence from the "chains"
		while len(sentence) < sentence_length:
			while not chains.has_key(previous):
				previous = random.choice(sentence_delimiting_words)

			chain = random.choice(chains[previous])

			word_length = chain[0]
			
			if self.__sentence_delimiters.count(chain[1]):
				word_delimiter = ''
			else:
				word_delimiter = chain[1]

			word = random.choice(self.__choose_closest_key(dictionary, word_length))
			word = word.lower()

			previous = (previous[1], word_length)

			sentence += [word + word_delimiter]

		# Finish the sentence off with capitalisation, a period and 
		# form it into a string
		if not self.__sentence_delimiters.count(word_delimiter):
			if self.__word_delimiters.count(word_delimiter):
				sentence[-1] = sentence[-1].rstrip(word_delimiter) + '.'
			else:
				sentence[-1] = sentence[-1] + '.'

		sentence[0] = sentence[0].capitalize()
		sentence = string.join(sentence)

		return sentence


	def generate_paragraph(self, start_with_lorem=False, paragraph_mean=None, paragraph_stddev=None, sentence_mean=None, sentence_stddev=None):
		"""
		Generates a single lorem ipsum paragraph, of random length.
		"""

		paragraph = []

		# Determine randomly the length of the paragraph
		try:
			paragraph_length = random.normalvariate(paragraph_mean, paragraph_stddev)
		except:
			paragraph_length = random.normalvariate(self.__paragraph_mean, self.__paragraph_stddev)

		paragraph_length = max(int(round(paragraph_length)), 1)

		# Generate the paragraph
		while len(paragraph) < paragraph_length:
			sentence = self.generate_sentence(
					start_with_lorem = (start_with_lorem and len(paragraph) == 0),
					sentence_mean = sentence_mean, 
					sentence_stddev = sentence_stddev
					)
			paragraph += [sentence]

		# Finish the paragraph off
		paragraph = string.join(paragraph)
		return paragraph
	
	# Private methods
	def __init__(self, sample, dictionary):
		"""
		Initialises a lorem ipsum generator by performing ahead of time 
		the calculations required by all "generations".

		Requires two strings containing a sample text and a dictionary 
		text.

		Sample text:
		The sample text is used to calculate the word distribution to
		be used by the generated lorem ipsum text. Sentences are 
		separated by periods, question marks or exclamation makrs. 
		Commas are included in the generated lorem ipsum text according 
		to their distribution in the sample text. All other punctuation 
		marks should ideally be removed, or else they will be counted 
		as parts of words. Paragraphs are separated by empty lines.

		Dictionary text:
		The dictionary text is used as the list of words to use in the
		generated lorem ipsum text. Words are separated by white space,
		and are case-insensitive.
		"""

		self.__generate_dictionary(dictionary)
		self.__generate_chains(sample)
		self.__generate_statistics(sample)
	
	def __generate_chains(self, sample):
		"""
		Generate a dictionary of "chains", which are used to randomly
		create parts of a sentence.

		Accepts a string containing the sample text.
		"""

		words = sample.split()

		# Calculate the "chains"
		previous = (0, 0)
		chains = {}
		sentence_delimiting_words = []

		for word in words:
			# Compile a list of what can come after a pair of words
			# with lengths matching the two words previously 
			# analysed -- list the word length, and the punctuation,
			# e.g. commas, periods, etc. that come after the word
			if not chains.has_key(previous):
				chains[previous] = []

			if self.__word_delimiters.count(word[-1:]):
				word_delimiter = word[-1:]
				word.rstrip(word_delimiter)
			else:
				word_delimiter = ''

			length = len(word)
			chains[previous] += [(length, word_delimiter)]
			previous = (previous[1], length)

			if self.__sentence_delimiters.count(word_delimiter):
				sentence_delimiting_words += [previous]

		self.__chains = chains
		self.__sentence_delimiting_words = sentence_delimiting_words
	
	def __generate_dictionary(self, dictionary):
		"""
		Generate a dictionary of words used to generate the lorem ipsum
		text.

		Accepts a string containing the dictionary text.
		"""

		words = dictionary.split()

		dictionary = {}

		for word in words:
			word = word.lower()
			length = len(word)

			if not dictionary.has_key(length):
				dictionary[length] = []

			dictionary[length] += [word]

		self.__dictionary = dictionary
	
	def __generate_statistics(self, sample):
		"""
		Calculate the mean and standard deviations of sentence and
		paragraph lengths in the sample text.

		Accepts a string containing the sample text.
		"""

		# Form a regular expression to split the sample into sentences
		sentence_split = ''
		for delimiter in self.__sentence_delimiters:
			sentence_split += '\\' + delimiter
		sentence_split = '[' + sentence_split + ']'

		# TODO: There has to be a general-purpose statistics module 
		# that I can use to calculate means and standard deviations

		# Split the sample into a list of sentences
		sentences = re.split(sentence_split, sample)

		# Analyse sentences
		mean = 0
		stddev = 0

		for sentence in sentences:
			words = len(sentence.split())
			stddev += words**2
			mean += words

		mean /= len(sentences)
		stddev /= len(sentences)
		stddev -= mean**2
		stddev = math.sqrt(stddev)

		self.__sentence_mean = mean
		self.__sentence_stddev = stddev

		# Split the sample into a list of paragraphs
		paragraphs = sample.split('\n\n')

		# Analyse paragraphs
		mean = 0
		stddev = 0

		for paragraph in paragraphs:
			sentences = len(re.split(sentence_split, paragraph))
			stddev += sentences**2
			mean += sentences

		mean /= len(paragraphs)
		stddev /= len(paragraphs)
		stddev -= mean**2
		stddev = math.sqrt(stddev)

		self.__paragraph_mean = mean
		self.__paragraph_stddev = stddev
	
	def __choose_closest_key(self, dictionary, target_key):
		"""
		For dictionaries with numerical or otherwise ordered keys, 
		choose the key closest to the given number.
		"""

		above = False
		below = False
		
		for key in dictionary.iterkeys():
			above = key
			if target_key < key:
				if below == False:
					below = above
				break
			below = key

		if abs(above - target_key) < abs(below - target_key):
			return dictionary[above]
		else:
			return dictionary[below]

class markupgenerator(generator):
	def __generate_markup_paragraphs(self, begin_paragraph, end_paragraph, between_paragraphs, quantity, start_with_lorem=False, paragraph_mean=None, paragraph_stddev=None, sentence_mean=None, sentence_stddev=None):
		text = []

		while len(text) < quantity:
			paragraph = self.generate_paragraph(
					start_with_lorem = (start_with_lorem and len(text) == 0), 
					sentence_mean = sentence_mean,
					sentence_stddev = sentence_stddev,
					paragraph_mean = paragraph_mean,
					paragraph_stddev = sentence_stddev
					)
			paragraph = begin_paragraph + paragraph + end_paragraph
			text += [paragraph]

		text = string.join(text, between_paragraphs)
		return text

	def generate_html_paragraphs(self, quantity, start_with_lorem=False, paragraph_mean=None, paragraph_stddev=None, sentence_mean=None, sentence_stddev=None):
		return self.__generate_markup_paragraphs(
				begin_paragraph 	= '<p>\n\t',
				end_paragraph 		= '\n</p>',
				between_paragraphs	= '\n',
				quantity		= quantity,
				start_with_lorem 	= start_with_lorem,
				sentence_mean 		= sentence_mean,
				sentence_stddev 	= sentence_stddev,
				paragraph_mean 		= paragraph_mean,
				paragraph_stddev 	= sentence_stddev
				)
	
	def generate_text_paragraphs(self, quantity, start_with_lorem=False, paragraph_mean=None, paragraph_stddev=None, sentence_mean=None, sentence_stddev=None):
		return self.__generate_markup_paragraphs(
				begin_paragraph 	= '',
				end_paragraph 		= '',
				between_paragraphs	= '\n\n',
				quantity		= quantity,
				start_with_lorem 	= start_with_lorem,
				sentence_mean 		= sentence_mean,
				sentence_stddev 	= sentence_stddev,
				paragraph_mean 		= paragraph_mean,
				paragraph_stddev 	= sentence_stddev
				)
	
	def generate_text_sentences(self, quantity, start_with_lorem=False, sentence_mean=None, sentence_stddev=None):
		text = []

		while len(text) < quantity:
			sentence = self.generate_sentence(
					start_with_lorem = (start_with_lorem and len(text) == 0),
					sentence_mean = sentence_mean,
					sentence_stddev = sentence_stddev
					)
			text += [sentence]

		text = string.join(text, ' ')
		return text
