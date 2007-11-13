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
import os.path
import re

class generator:
	"""
	Generates random sentences or paragraphs of "lorem ipsum" text, 
	based on the word distribution of a given sample text, and the 
	words in a given dictionary.
	"""

	__punctuation_end_word = ['.', ',', '?', '!']
	__punctuation_end_sentence = ['.', '?', '!']

	def __init__(self, sample_file, dictionary_file):
		"""
		The sample file is used to gather statistical data about the
		word, sentence and paragraph distributions in the text.

		The dictionary file is used as a source of random words, such 
		as the latin "lorem ipsum" words, to produce the output text.

		Sample format:
		Sentences separated by periods, question marks or exclamation
		marks. Commas are counted. All other punctuation should
		ideally be removed. Paragraphs are separated by empty lines.

		Dictionary format:
		Words separated by white space. Words are case-insensitive.
		"""

		self.__generate_dictionary(dictionary_file)
		self.__generate_chains(sample_file)
	
	def __generate_dictionary(self, dictionary_file):
		"""
		Generate a dictionary of words, which are categorised by 
		length, and which can be used in the output lipsum text.
		"""

		words = self.__load_contents(dictionary_file)
		words = words.split()

		dictionary = {}

		for word in words:
			length = len(word)
			
			if not dictionary.has_key(length):
				dictionary[length] = []

			dictionary[length] += [word]

		# TODO:
		# Raise error if there are no words in the
		# dictionary

		self.__dictionary = dictionary
	
	def __generate_chains(self, sample_file):
		"""
		Generate a dictionary of "chains", which are used to 
		randomly create parts of a sentence.
		Also, calculate the mean and standard deviation of
		sentence lengths.
		"""

		words = self.__load_contents(sample_file)

		sentence_split = ''
		for delimiter in self.__punctuation_end_sentence:
			sentence_split += '\\' + delimiter
		sentence_split = '[' + sentence_split + ']'
		sentences = re.split(sentence_split, words)

		paragraphs = words.split('\n\n')
		words = words.split()

		previous = (0,0)
		chains = {}
		end_sentences = []

		for word in words:
			if not chains.has_key(previous):
				chains[previous] = []

			if self.__punctuation_end_word.count(word[-1:]):
				end_word = word[-1:]
				word.rstrip(end_word)
			else:
				end_word = ''
				
			length = len(word) 
			chains[previous] += [(length, end_word)]
			previous = (previous[1], length)

			if self.__punctuation_end_sentence.count(end_word):
				end_sentences += [previous]
		
		self.__chains = chains
		self.__end_sentences = end_sentences

		mu = 0
		sigma = 0

		for sentence in sentences:
			words = len(sentence.split())
			sigma += words**2
			mu += words

		mu /= len(sentences)
		sigma /= len(sentences)
		sigma -= mu**2
		sigma = math.sqrt(sigma)

		self.__sentence_mu = mu
		self.__sentence_sigma = sigma

		mu = 0
		sigma = 0

		for paragraph in paragraphs:
			sentences = len(re.split(sentence_split, paragraph))
			sigma += sentences**2
			mu += sentences

		mu /= len(paragraphs)
		sigma /= len(paragraphs)
		sigma -= mu**2
		sigma = math.sqrt(sigma)

		self.__paragraph_mu = mu
		self.__paragraph_sigma = sigma
	
	def generate_sentence(self, start_with_lorem=False):
		"""
		generate_sentence() -> str

		Generates a single sentence, of variable length.
		"""
		if start_with_lorem:
			sentence = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet,', 'consectetuer', 'adipiscing', 'elit.']
			previous = (10, 4)
		else:
			sentence = []
			previous = ()

			mu = self.__sentence_mu
			sigma = self.__sentence_sigma
			chains = self.__chains
			end_sentences = self.__end_sentences
			dictionary = self.__dictionary

			max_length = int(round(random.normalvariate(mu, sigma)))

			for i in range(len(sentence), max(10, max_length)):
				if chains.has_key(previous):
					chain = random.choice(chains[previous])
					length = chain[0]
					word = random.choice(self.__choose_closest(dictionary, length))
					word = word.lower()

					end_word = chain[1]
					previous = (previous[1], length)

					sentence += [word + end_word]

					if self.__punctuation_end_sentence.count(end_word):
						break
				else:
					previous = random.choice(end_sentences)

			if not self.__punctuation_end_sentence.count(end_word):
				if self.__punctuation_end_word.count(end_word):
					sentence[-1] = sentence[-1].rstrip(end_word) + '.'
				else:
					sentence[-1] = sentence[-1] + '.'


		sentence[0] = sentence[0].capitalize()

		sentence = string.join(sentence)
		return sentence

	def generate_paragraph(self, start_with_lorem=False):
		"""
		generate_paragraph() -> str

		Generates a single paragraph, consisting of a variable number
		of sentences of variable length.
		"""
		if start_with_lorem:
			paragraph = [self.generate_sentence(start_with_lorem=True)]
		else:
			paragraph = []

		mu = self.__paragraph_mu
		sigma = self.__paragraph_sigma
		max_length = int(round(random.normalvariate(mu, sigma)))

		for i in range(len(paragraph), max(max_length, 1)):
			paragraph += [self.generate_sentence()]

		paragraph = string.join(paragraph)
		return paragraph
	
	def __load_contents(self, file_name):
		"""
		Open a file and return its contents.
		"""
		file = open(file_name, 'r')
		contents = file.read()
		file.close()
		return contents

	def __choose_closest(self, dictionary, target_key):
		"""
		For dictionaries with numerical keys, choose the key closest to the
		given number.
		"""

		if (isinstance(dictionary, dict) and isinstance(target_key, int)):
			above = False
			below = False

			for key in dictionary.iterkeys():
				if isinstance(key, int):
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
