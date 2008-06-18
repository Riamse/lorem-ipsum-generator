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

	# Configuration variables
	__delimiters_sentences 		= ['.', '?', '!']
	__delimiters_words 		= [','] + __delimiters_sentences

	# Markov chain statistics (generated)
	__chains 			= []
	__chains_starts	 	= []
	__chains_dictionary		= []

	# Sentence / paragraph statistics
	__sentence_mean 		= 0
	__sentence_sigma 		= 0
	__paragraph_mean 		= 0
	__paragraph_sigma 		= 0

	def set_sentence_mean(self, mean):
		"""
		Sets the mean length of the randomly generated sentences. 
		Quantities are in number of words.
		"""
		self.__sentence_mean = mean
	
	def set_sentence_sigma(self, sigma):
		"""
		Sets the standard deviation of the lengths of the randomly 
		generated sentences. Quantities are in number of words.
		"""
		self.__sentence_sigma = sigma
	
	def set_paragraph_mean(self, mean):
		"""
		Sets the mean length of the randomly generated paragraphs. 
		Quantities are in number of sentences.
		"""
		self.__paragraph_mean = mean

	def set_paragraph_sigma(self, sigma):
		"""
		Sets the standard deviation of the lengths of the randomly
		generated sentences. Quantities are in number of sentences.
		"""
		self.__paragraph_sigma = sigma

	def get_sentence_mean(self):
		return self.__sentence_mean

	def get_sentence_sigma(self):
		return self.__sentence_sigma

	def get_paragraph_mean(self):
		return self.__paragraph_mean

	def get_paragraph_sigma(self):
		return self.__paragraph_sigma
	
	def set_dictionary(self, dictionary):
		"""
		Sets the dictionary of words used to generate output. Accepts
		a string containing case-insensitive, white-space delimited 
		words.
		"""

		words = dictionary.split()
		self.__generate_dictionary(words)
	
	def __generate_dictionary(self, words):
		dictionary = {}
		for word in words:
			word = word.lower()
			length = len(word)

			if not dictionary.has_key(length):
				dictionary[length] = []

			dictionary[length] += [word]

		self.__chains_dictionary = dictionary

	def set_sample(self, sample):
		"""
		Sets the sample text to calculate the word distribution to
		be used by the generated lorem ipsum text. 
		
		Sentences in the supplied string are separated by periods, 
		question marks or exclamation makrs.  Commas are included in
		the generated lorem ipsum text according to their distribution 
		in the sample text. All other punctuation marks should ideally 
		be removed, or else they will be counted as parts of words. 
		Paragraphs are separated by empty lines.
		"""

		self.__generate_chains(sample)
		self.__generate_statistics(sample)
	
	def __generate_chains(self, sample):
		words = sample.split()

		previous = (0, 0)
		chains = {}
		chains_starts = []

		for word in words:
			if not chains.has_key(previous):
				chains[previous] = []

			# If the word ends in a "word delimiter", strip it of
			# the character and record it
			if self.__delimiters_words.count(word[-1:]):
				word_delimiter = word[-1:]
				word = word.rstrip(word_delimiter)
			else:
				word_delimiter = ''

			length = len(word)
			chains[previous] += [(length, word_delimiter)]
			previous = (previous[1], length)

			# If the word ends in a "sentence delimiter", record it
			if self.__delimiters_sentences.count(word_delimiter):
				chains_starts += [previous]

		self.__chains = chains
		self.__chains_starts = chains_starts

	def __generate_statistics(self, sample):
		self.__generate_sentence_statistics(sample)
		self.__generate_paragraph_statistics(sample)

	def __sentence_split(self):
		sentence_split = ''
		for delimiter in self.__delimiters_sentences:
			sentence_split += '\\' + delimiter
		sentence_split = '[' + sentence_split + ']'
		return sentence_split


	def __generate_sentence_statistics(self, sample):
		# Form a regular expression to split the sample into sentences
		# Split the sample into a list of sentences
		sentences = re.split(self.__sentence_split(), sample)

		# Analyse sentences
		mean = 0.0
		sigma = 0.0
		n = 0

		for sentence in sentences:
			words = len(sentence.split())
			if words > 0:
				sigma += words**2
				mean += words
				n += 1

		mean /= n
		sigma /= n
		sigma -= mean**2
		sigma = math.sqrt(sigma)

		self.__sentence_mean = mean
		self.__sentence_sigma = sigma
	
	def __generate_paragraph_statistics(self, sample):
		# Split the sample into a list of paragraphs
		paragraphs = sample.split('\n\n')

		# Analyse paragraphs
		mean = 0.0
		sigma = 0.0
		n = 0

		for paragraph in paragraphs:
			sentences = len(re.split(self.__sentence_split(), paragraph))
			if sentences > 0:
				sigma += sentences**2
				mean += sentences
				n += 1

		mean /= n
		sigma /= n
		sigma -= mean**2
		sigma = math.sqrt(sigma)

		self.__paragraph_mean = mean
		self.__paragraph_sigma = sigma

	def __init__(self, sample=None, dictionary=None):
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
		if not dictionary == None:
			self.set_dictionary(dictionary)
		if not sample == None:
			self.set_sample(sample)
	
	def generate_sentence(self, start_with_lorem=False):
		"""
		Generates a single sentence, of random length.

		If start_with_lorem=True, then the sentence will begin with the
		standard "Lorem ipsum..." first sentence.
		"""

		# Determine randomly the length of the sentence
		sentence_length = random.normalvariate(self.__sentence_mean, self.__sentence_sigma)
		sentence_length = max(int(round(sentence_length)), 1)

		# Initialise variables being used
		sentence = []
		previous = ()

		# Start with "Lorem ipsum..." if start_with_lorem is True
		if start_with_lorem:
			lorem = "lorem ipsum dolor sit amet, consecteteur adipiscing elit".split()
			sentence += lorem
		
		# Otherwise generate a sentence from the "chains"
		word_delimiter = '' # Defined here in case while loop doesn't run

		while len(sentence) < sentence_length:
			while (not self.__chains.has_key(previous)):
				previous = random.choice(self.__chains_starts)

			chain = random.choice(self.__chains[previous])

			word_length = chain[0]
			
			if self.__delimiters_sentences.count(chain[1]):
				word_delimiter = ''
			else:
				word_delimiter = chain[1]

			word = random.choice(self.__choose_closest_key(self.__chains_dictionary, word_length))
			word = word.lower()

			previous = (previous[1], word_length)

			sentence += [word + word_delimiter]

		# Finish the sentence off with capitalisation, a period and 
		# form it into a string
		if not self.__delimiters_sentences.count(word_delimiter):
			if self.__delimiters_words.count(word_delimiter):
				sentence[-1] = sentence[-1].rstrip(word_delimiter) + '.'
			else:
				sentence[-1] = sentence[-1] + '.'

		sentence[0] = sentence[0].capitalize()
		sentence = string.join(sentence)

		return sentence
	
	def generate_paragraph(self, start_with_lorem=False):
		"""
		Generates a single lorem ipsum paragraph, of random length.

		If start_with_lorem=True, then the sentence will begin with the
		standard "Lorem ipsum..." first sentence.
		"""

		paragraph = []

		# Determine randomly the length of the paragraph
		paragraph_length = random.normalvariate(self.__paragraph_mean, self.__paragraph_sigma)
		paragraph_length = max(int(round(paragraph_length)), 1)

		# Generate the paragraph
		while len(paragraph) < paragraph_length:
			sentence = self.generate_sentence(
					start_with_lorem = (start_with_lorem and len(paragraph) == 0)
					)
			paragraph += [sentence]

		# Finish the paragraph off
		paragraph = string.join(paragraph)
		return paragraph
	
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
	"""
	Generates random strings of "lorem ipsum" text,	based on the word 
	distribution of a given sample text, using the words in a given 
	dictionary.

	Provides a number of methods for producing "lorem ipsum" text with
	varying formats.
	"""
	def __generate_markup_paragraphs(self, begin_paragraph, end_paragraph, between_paragraphs, quantity, start_with_lorem=False):
		text = []

		while len(text) < quantity:
			paragraph = self.generate_paragraph(
					start_with_lorem = (start_with_lorem and len(text) == 0)
					)
			paragraph = begin_paragraph + paragraph + end_paragraph
			text += [paragraph]

		text = string.join(text, between_paragraphs)
		return text

	def generate_html_paragraphs(self, quantity, start_with_lorem=False):
		"""
		Generates a quantity of paragraphs, with each paragraph 
		surrounded by HTML pararaph tags.
		"""
		return self.__generate_markup_paragraphs(
				begin_paragraph 	= '<p>\n\t',
				end_paragraph 		= '\n</p>',
				between_paragraphs	= '\n',
				quantity		= quantity,
				start_with_lorem 	= start_with_lorem
				)
	
	def generate_text_paragraphs(self, quantity, start_with_lorem=False):
		"""
		Generates a quantity of paragraphs, separated by empty lines.
		"""
		output =  self.__generate_markup_paragraphs(
				begin_paragraph 	= '',
				end_paragraph 		= '',
				between_paragraphs	= '\n\n',
				quantity		= quantity,
				start_with_lorem 	= start_with_lorem
				)
		return output
	
	def generate_text_sentences(self, quantity, start_with_lorem=False):
		"""
		Generates a quantity of sentences.
		"""
		text = []

		while len(text) < quantity:
			sentence = self.generate_sentence(
					start_with_lorem = (start_with_lorem and len(text) == 0)
					)
			text += [sentence]

		text = string.join(text, ' ')
		return text
	
