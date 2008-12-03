# -*- coding: utf-8 -*-
# Copyright:
#   James Hales, 2007. <jhales.perth@gmail.com>,
#   Zachary Voase, 2008. <zack@biga.mp>
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

from cStringIO import StringIO
import base64
import gzip
import math
import os
import random
import re


NEWLINE = os.linesep


DEFAULT_SAMPLE_COMPRESSED = """
H4sIAFEGLkkC/7Va244ktw1976/QBxTmB/Jk2AlgIAkcBPa7pko7o6Au7SqpAf99SB6SYu
0ukJcYsHdnuqskijw8PKT278dZtlSfV9/ScqzHma7aUt5Km9J87FeZW2m9nCkv9Vmvue4f
qay1vaUfyl7yTg9t27Ecaa0ffc2pfJSGhfyJLV9Xfks/0g7XMdd6pT234/de0rPQT/W9X4
le2vLHTt8t9P8zn62ftez06bG3ck30yjWTIWc661LnvtI7W7/e0k/HXub0e89b+kJ20ZN9
bWeda6FtyjzRHutaeA3esHT64Cytki2/d376Kttb+mdfyXQ5Lq3UYLE8kMpeN9vlWZaS/t
Ovdkzpy0meqPzaq6xTymul9Ru2fPX12VtuRbxBX55zf0s/77KYLXB+HvtMp+j0QN2e5Vwq
vZ/pbfIau+VKr9pymfCCGklBqnPrelg6D4zajpV/1aPxXo22PlOr+1yXvlO4fjwzOTc/2d
1v6bf6yhv7fS0beYdDU9iIRCGoHrlwkLXUL2VfUiN38gL6xFos8uTY42ytNoIQu3l4U4/h
S2RyEdz6A3uNzrQKCDMZPZmJqe7kivoq55k1VF9K/6hZfGRW/PKZL/nRH90llJ1iSGihj/
NZ6a810w6FvPAvWomBcPZ2sqP0GB6At/TXVsmiACJyCMc45f7RC8P4zO+VkSjxmI+T3XZ/
noJFayAVen17PLCohvwt/SOXmWJ80Tm2Z7/sPHiDHLdUDYq+ITAFyDVMa30vJ6HIkjWmJz
+7Fz7lVRakNgySBfa+k//f10y7NIB37TP76tnXV93zOaVPCtNZTvq+LhOiE4zmVDiWenDS
cswGyvQ8li8S+HRRQMvOIYHRAeBfcp+BRwW3pByvaXHw8x3nXOEfWmK8GRH+E79MgHxL/6
ZzjwTdMnHJNZba6/unmXgdS14palf+qI1NYhbKWMERPAnMZfN3OsK+CJPJixNgwX6k5ed+
XmQTXCxn+Tjzqy4Zy6atpqxeeEt/68Ro30sxOIxytFxMjivt9uwnrcvxo5DP9OQJGDN5aO
5TrIklj71v2x8SNkkA92ye575dnLEg/F2QCVYY4CUDiVII3ISlgAL35c0oiT0qx/OsW+Wc
HYGRgCmyyHHYg7Z4HheVk0K+eq9rzZJP5S/Mjnlmm+A3MuRWfdZM0K6ZUomBbBSuhjIOhW
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
"""

DEFAULT_DICT_COMPRESSED = """
H4sIABkJLkkC/z2U667lIAiF//OWVtndTLz0oDaZt5+P9mQShaVFXFxskpQZebeZuqTCsM
tmtn5K0q6xWe1np/ZqXZJaiL5U0rW0gz1vSeid13DUuVUOO7SX3eSoqRdbkmuaU/JobZSB
ZrNxGgtwnEBNzUvXVn8XXLsC7cNS6DvVavjwhGCzxnY42J4OW9sfpCHnnlLSZUdog32xHH
e9ai7A2W1Oiy1MRoV5GV2zlG0xp+ipc6VHL9Gq9iGiAL+8tRKWdovJyiGrPrDHfZxYca9u
hk2Clk/KUJ72H0xQ05A7P0w/GvF91H9v+Og+Dbcfpx5Wa5LPnlnl9HRbSfKNsCnFL5hTQV
m+8HR12H3/4ikppCzlHc6tiLVLvRgUrTOyXisMqOhJ5kN7FM6uifyz5xpSYdzJNhqaNQ1X
jlfKFUvFgHJ7qHPDksQMR41j+OJSkqtN6n7MW9IMqQBnT4+0WFSdO5XYmDPkWs/29lD6nD
RpA7NlGiDCaQO6ofzgIzadnOM8a7RDT2vQsxJl7fqicNTt+CIoBaJKHz3mbu0vei6o9x3Z
fiT+ds8yig0Zng3Rk6tcybnD4gVcWlhrrRps4p6LCNdTU3It15cD4RYwMYttUvm0DGApX8
jUK1ckDzR5Bzga8cZMLhp7PnfhySjM5dZIwOWDKl673gYrgOP8ea8/0cMhgo9/R4/SufEC
dn1QvBHfy3E202lPvidvRruQv0oDPUenFmaLGbFA4i37pL/myBanUANjQIk6oqlO5kkWyH
FP5qeyApAX3ht9uugowlpvNha+CTpUrGhKK5tgyQQUXhBZWXBa8RsSUs9/Sp4C5eHBbFc+
Z52/wAJRKtlL7uSG41sZ30hAAtSY0LqJKKoV32cUrZKRm/eEtd0pugqtTv3uUfe6qNq967
UXlZN/dPUXs0IFAAA=
"""


sample_text_file = gzip.GzipFile(mode='rb',
    fileobj=StringIO(base64.b64decode(DEFAULT_SAMPLE_COMPRESSED)))
DEFAULT_SAMPLE = sample_text_file.read()
sample_text_file.close()

dictionary_text_file = gzip.GzipFile(mode='rb',
    fileobj=StringIO(base64.b64decode(DEFAULT_DICT_COMPRESSED)))
DEFAULT_DICT = dictionary_text_file.read()
dictionary_text_file.close()

class InvalidDictionaryText(Exception):
    def __str__(self):
        return ('Dictionary text must contain one or more white-space '
            'delimited words.')


class InvalidSampleText(Exception):
    def __str__(self):
        return ('Sample text must contain one or more empty-line '
            'delimited paragraphs, and each paragraph must contain one or '
            'more period, question mark, or exclamation mark delimited '
            'sentences.')


class NoDictionary(Exception):
    def __str__(self):
        return ('No words stored in generator. A valid dictionary text must '
            'be supplied.')


class NoChains(Exception):
    def __str__(self):
        return ('No chains stored in generator. A valid sample text must be '
            'supplied.')

class Generator(object):
    """
    Generates random strings of "lorem ipsum" text, based on the word 
    distribution of a given sample text, using the words in a given 
    dictionary.
    """

    # Configuration variables
    __delimiters_sentences  = ['.', '?', '!']
    __delimiters_words      = [','] + __delimiters_sentences

    # Markov chain statistics (generated)
    __chains                = {}
    __chains_starts         = []
    __chains_dictionary     = {}

    # Sentence / paragraph statistics
    __sentence_mean         = 0
    __sentence_sigma        = 0
    __paragraph_mean        = 0
    __paragraph_sigma       = 0
    
    def __init__(self, sample=DEFAULT_SAMPLE, dictionary=DEFAULT_DICT):
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
        
        self.set_dictionary(dictionary)
        self.set_sample(sample)

    def set_sentence_mean(self, mean):
        """
        Sets the mean length of the randomly generated sentences. 
        Quantities are in number of words.
        """

        if mean < 0:
            raise ValueError('Mean sentence length must be non-negative.')

        self.__sentence_mean = mean
    
    def set_sentence_sigma(self, sigma):
        """
        Sets the standard deviation of the lengths of the randomly 
        generated sentences. Quantities are in number of words.
        """
        if sigma < 0:
            raise ValueError('Standard deviation of sentence length must be non-negative.')

        self.__sentence_sigma = sigma
    
    def set_paragraph_mean(self, mean):
        """
        Sets the mean length of the randomly generated paragraphs. 
        Quantities are in number of sentences.
        """
        
        if mean < 0:
            raise ValueError('Mean paragraph length must be non-negative.')

        self.__paragraph_mean = mean

    def set_paragraph_sigma(self, sigma):
        """
        Sets the standard deviation of the lengths of the randomly
        generated sentences. Quantities are in number of sentences.
        """
        
        if sigma < 0:
            raise ValueError('Standard deviation of paragraph length must be non-negative.')

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

        if len(dictionary) > 0:
            self.__chains_dictionary = dictionary
        else:
            raise InvalidDictionaryText

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
        chains_starts = [previous]

        for word in words:
            if not chains.has_key(previous):
                chains[previous] = []

            # If the word ends in a "word delimiter", strip it of
            # the character and record it
            if word[-1] in self.__delimiters_words:
                word_delimiter = word[-1]
                word = word.rstrip(word_delimiter)
            else:
                word_delimiter = ''

            chains.setdefault(previous, []).append(
                    (len(word), word_delimiter))
            previous = (previous[1], len(word))

            # If the word ends in a "sentence delimiter", record it
            if word_delimiter in self.__delimiters_sentences:
                chains_starts += [previous]

        if len(chains) > 0 and len(chains_starts) > 0:
            self.__chains = chains
            self.__chains_starts = chains_starts
        else:
            raise InvalidSampleText

    def reset_statistics(self):
        self.__sentence_mean = self.__generated_sentence_mean
        self.__sentence_sigma = self.__generated_sentence_sigma
        self.__paragraph_mean = self.__generated_paragraph_mean
        self.__paragraph_sigma = self.__generated_paragraph_sigma
    
    def __save_generated_statistics(self):
        self.__generated_sentence_mean = self.__sentence_mean
        self.__generated_sentence_sigma = self.__sentence_sigma
        self.__generated_paragraph_mean = self.__paragraph_mean
        self.__generated_paragraph_sigma = self.__paragraph_sigma

    def __generate_statistics(self, sample):
        self.__generate_sentence_statistics(sample)
        self.__generate_paragraph_statistics(sample)
        self.__save_generated_statistics()

    def __split_sentences(self, text):
        sentence_split = ''
        for delimiter in self.__delimiters_sentences:
            sentence_split += '\\' + delimiter
        sentence_split = '[' + sentence_split + ']'
        text = re.split(sentence_split, text)
        return text


    def __generate_sentence_statistics(self, sample):
        # Split the sample into a list of sentences
        sentences = self.__split_sentences(sample)

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

        if n > 0:
            mean /= n
            sigma /= n
            sigma -= mean**2
            sigma = math.sqrt(sigma)
            self.__sentence_mean = mean
            self.__sentence_sigma = sigma
        else:
            raise InvalidSampleText
    
    def __generate_paragraph_statistics(self, sample):
        # Split the sample into a list of paragraphs
        sample = sample.replace('\r\n', '\n')
        sample = sample.replace('\r', '\n')
        sample = sample.replace('\n', NEWLINE)
        paragraphs = sample.split(NEWLINE * 2)

        # Analyse paragraphs
        mean = 0.0
        sigma = 0.0
        n = 0

        for paragraph in paragraphs:
            sentences = self.__split_sentences(paragraph)
            sentences = sum([1 for sentence in sentences if len(sentence.strip()) > 0])
            if sentences > 0:
                sigma += sentences**2
                mean += sentences
                n += 1

        if n > 0:
            mean /= n
            sigma /= n
            sigma -= mean**2
            sigma = math.sqrt(sigma)
            self.__paragraph_mean = mean
            self.__paragraph_sigma = sigma
        else:
            raise InvalidSampleText
    
    def generate_sentence(self, start_with_lorem=False):
        """
        Generates a single sentence, of random length.

        If start_with_lorem=True, then the sentence will begin with the
        standard "Lorem ipsum..." first sentence.
        """

        if len(self.__chains) == 0 or len(self.__chains_starts) == 0:
            raise NoChains

        if len(self.__chains_dictionary) == 0:
            raise NoDictionary

        # Determine randomly the length of the sentence
        sentence_length = random.normalvariate(self.__sentence_mean, self.__sentence_sigma)
        sentence_length = max(int(round(sentence_length)), 1)

        sentence = []
        previous = ()

        # Generate a sentence from the "chains"
        word_delimiter = '' # Defined here in case while loop doesn't run

        # Start with "Lorem ipsum..."
        if start_with_lorem:
            lorem = "lorem ipsum dolor sit amet, consecteteur adipiscing elit".split()
            sentence += lorem[:sentence_length]
            last_char = sentence[-1][-1]
            if last_char not in self.__delimiters_sentences:
                word_delimiter = last_char

        while len(sentence) < sentence_length:
            while (not self.__chains.has_key(previous)):
                previous = random.choice(self.__chains_starts)

            chain = random.choice(self.__chains[previous])

            word_length = chain[0]
            
            if chain[1] in self.__delimiters_sentences:
                word_delimiter = ''
            else:
                word_delimiter = chain[1]

            word = random.choice(self.__choose_closest_key(self.__chains_dictionary, word_length))
            word = word.lower()

            previous = (previous[1], word_length)

            sentence += [word + word_delimiter]

        # Finish the sentence off with capitalisation, a period and 
        # form it into a string
        if word_delimiter not in self.__delimiters_sentences:
            if word_delimiter in self.__delimiters_words:
                sentence[-1] = sentence[-1].rstrip(word_delimiter) + '.'
            else:
                sentence[-1] = sentence[-1] + '.'

        sentence[0] = sentence[0].capitalize()
        sentence = ' '.join(sentence)

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
        paragraph = ' '.join(paragraph)
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

class MarkupGenerator(Generator):
    """
    Generates random strings of "lorem ipsum" text, based on the word 
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

        text = between_paragraphs.join(text)
        return text
    
    def __generate_markup_sentences(self, begin_sentence, end_sentence, between_sentences, quantity, start_with_lorem=False):
        text = []

        while len(text) < quantity:
            sentence = self.generate_sentence(
                    start_with_lorem = (start_with_lorem and len(text) == 0)
                    )
            sentence = begin_sentence + sentence + end_sentence
            text += [sentence]

        text = between_sentences.join(text)
        return text

    def generate_html_paragraphs(self, quantity, start_with_lorem=False):
        """
        Generates a quantity of paragraphs, with each paragraph 
        surrounded by HTML pararaph tags.
        """
        return self.__generate_markup_paragraphs(
                begin_paragraph     = '<p>' + NEWLINE + '\t',
                end_paragraph       = NEWLINE + '</p>',
                between_paragraphs  = NEWLINE,
                quantity            = quantity,
                start_with_lorem    = start_with_lorem
                )
    
    def generate_text_paragraphs(self, quantity, start_with_lorem=False):
        """
        Generates a quantity of paragraphs, separated by empty lines.
        """
        return self.__generate_markup_paragraphs(
                begin_paragraph     = '',
                end_paragraph       = '',
                between_paragraphs  = NEWLINE * 2,
                quantity            = quantity,
                start_with_lorem    = start_with_lorem
                )
    
    def generate_html_sentence_list(self, quantity, start_with_lorem=False):
        """Generates a quantity of sentences surrounded by HTML 'li' tags."""
        output = self.__generate_markup_sentences(
                begin_sentence      = '\t<li>' + NEWLINE + '\t\t',
                end_sentence        = NEWLINE + '\t</li>',
                between_sentences   = NEWLINE,
                quantity            = quantity,
                start_with_lorem    = start_with_lorem
                )

        return ('<ul>' + NEWLINE + output + NEWLINE + '</ul>')
    
    def generate_html_paragraph_list(self, quantity, start_with_lorem=False):
        """Generates a quantity of paragraphs surrounded by HTML 'li' tags."""
        output = self.__generate_markup_paragraphs(
                begin_paragraph     = '\t<li>' + NEWLINE + '\t\t', 
                end_paragraph       = NEWLINE + '\t</li>',
                between_paragraphs  = NEWLINE,
                quantity            = quantity,
                start_with_lorem    = start_with_lorem
                )
        return ('<ul>' + NEWLINE + output + NEWLINE + '</ul>')

    def generate_html_sentences(self, quantity, start_with_lorem = False):
        return self.__generate_markup_sentences(
                begin_sentence      = '<p>' + NEWLINE + '\t',
                end_sentence        = NEWLINE + '</p>',
                between_sentences   = NEWLINE,
                quantity            = quantity,
                start_with_lorem    = start_with_lorem
                )
    
    def generate_text_sentences(self, quantity, start_with_lorem=False):
        """
        Generates a quantity of sentences.
        """
        return self.__generate_markup_sentences(
                begin_sentence      = '',
                end_sentence        = '',
                between_sentences   = ' ',
                quantity            = quantity,
                start_with_lorem    = start_with_lorem
                )
