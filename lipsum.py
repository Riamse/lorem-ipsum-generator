from cStringIO import StringIO
import base64
import gzip
import math
import os
import random
import re

# Delimiters that mark ends of sentences
DELIMITERS_SENTENCES = ['.', '?', '!']

# Delimiters which do not form parts of words (i.e. "hello," is the word
# "hello" with a comma next to it)
DELIMITERS_WORDS = [','] + DELIMITERS_SENTENCES

NEWLINE = os.linesep

# Contains a reasonable default sample text
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

# Contains a reasonable default latin dictionary
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
DEFAULT_DICT = dictionary_text_file.read().split()
dictionary_text_file.close()

def split_paragraphs(text):
    """
    Splits a piece of text into paragraphs, separated by empty lines.
    """
    lines = text.splitlines()
    paragraphs = [[]]
    for line in lines:
        if len(line.strip()) > 0:
            paragraphs[-1] += [line]
        elif len(paragraphs[-1]) > 0:
            paragraphs.append([])
    paragraphs = map(' '.join, paragraphs)
    return paragraphs

def split_sentences(text):
    """
    Splits a piece of text into sentences, separated by periods, question 
    marks and exclamation marks.
    """
    sentence_split = ''
    for delimiter in DELIMITERS_SENTENCES:
        sentence_split += '\\' + delimiter
    sentence_split = '[' + sentence_split + ']'
    sentences = re.split(sentence_split, text)
    return sentences

def split_words(text):
    """
    Splits a piece of text into words, separated by whitespace.
    """
    return text.split()

def mean(values):
    return sum(values) / float(len(values))

def variance(values):
    squared = map(lambda x : x**2, values)
    return mean(squared) - mean(values)**2

def sigma(values):
    return math.sqrt(variance(values))

def choose_closest(values, target):
    """
    Find the number in the list of values that is closest to the target.
    """
    closest = values[0]
    for value in values:
        if abs(target - value) < abs(target - closest):
            closest = value

    return closest

def get_word_info(word):
    longest = (word, "")

    for delimiter in DELIMITERS_WORDS:
        if len(delimiter) > len(longest[1]) and word.endswith(delimiter):
            word = word.rpartition(delimiter)
            longest = (word[0], word[1])

    return (len(longest[0]), longest[1])


class InvalidDictionaryTextError(Exception):
    def __str__(self):
        return ('Dictionary text must contain one or more white-space '
            'delimited words.')


class InvalidSampleTextError(Exception):
    def __str__(self):
        return ('Sample text must contain one or more empty-line '
            'delimited paragraphs, and each paragraph must contain one or '
            'more period, question mark, or exclamation mark delimited '
            'sentences.')


class NoDictionaryError(Exception):
    def __str__(self):
        return ('No words stored in generator. A valid dictionary text must '
            'be supplied.')


class NoChainsError(Exception):
    def __str__(self):
        return ('No chains stored in generator. A valid sample text must be '
            'supplied.')


class Generator(object):
    """
    Generates random strings of "lorem ipsum" text, based on the word
    distribution of a given sample text, using the words in a given
    dictionary.
    """

    # Words that can be used in the generated output
    # Maps a word-length to a list of words of that length
    __words = {}

    # Chains of three words that appear in the sample text
    # Maps a pair of word-lengths to a third word-length and an optional 
    # piece of trailing punctuation (for example, a period, comma, etc.)
    __chains = {}

    # Pairs of word-lengths that can appear at the beginning of sentences
    __starts = []

    # Sample that the generated text is based on
    __sample = ""

    # Statistics for sentence and paragraph generation
    __sentence_mean = 0
    __sentence_sigma = 0
    __paragraph_mean = 0
    __paragraph_sigma = 0

    # Last calculated statistics, in case they are overwritten by user
    __generated_sentence_mean = 0
    __generated_sentence_sigma = 0
    __generated_paragraph_mean = 0
    __generated_paragraph_sigma = 0

    def __init__(self, sample=DEFAULT_SAMPLE, dictionary=DEFAULT_DICT):
        """
        Initialises a lorem ipsum generator by performing ahead of time
        the calculations required by all "generations".

        Requires two strings containing a sample text and a dictionary
        """
        self.sample = sample
        self.dictionary = dictionary

    def __set_sentence_mean(self, mean):
        if mean < 0:
            raise ValueError('Mean sentence length must be non-negative.')
        self.__sentence_mean = mean

    def __set_sentence_sigma(self, sigma):
        if sigma < 0:
            raise ValueError('Standard deviation of sentence length must be '
                'non-negative.')
        self.__sentence_sigma = sigma

    def __set_paragraph_mean(self, mean):
        if mean < 0:
            raise ValueError('Mean paragraph length must be non-negative.')
        self.__paragraph_mean = mean

    def __set_paragraph_sigma(self, sigma):
        if sigma < 0:
            raise ValueError('Standard deviation of paragraph length must be '
                'non-negative.')
        self.__paragraph_sigma = sigma

    def __get_sentence_mean(self):
        """
        A non-negative value determining the mean sentence length (in words)
        of generated sentences. Is changed to match the sample text when the
        sample text is updated.
        """
        return self.__sentence_mean

    def __get_sentence_sigma(self):
        """
        A non-negative value determining the standard deviation of sentence
        lengths (in words) of generated sentences. Is changed to match the
        sample text when the sample text is updated.
        """
        return self.__sentence_sigma

    def __get_paragraph_mean(self):
        """
        A non-negative value determining the mean paragraph length (in
        sentences) of generated sentences. Is changed to match the sample text
        when the sample text is updated.
        """
        return self.__paragraph_mean

    def __get_paragraph_sigma(self):
        """
        A non-negative value determining the standard deviation of paragraph
        lengths (in sentences) of generated sentences. Is changed to match the
        sample text when the sample text is updated.
        """
        return self.__paragraph_sigma

    sentence_mean = property(__get_sentence_mean, __set_sentence_mean)
    sentence_sigma = property(__get_sentence_sigma, __set_sentence_sigma)
    paragraph_mean = property(__get_paragraph_mean, __set_paragraph_mean)
    paragraph_sigma = property(__get_paragraph_sigma, __set_paragraph_sigma)

    def __get_sample(self):
        return self.__sample

    def __set_sample(self, sample):
        """
        Sets the generator to be based on a new sample text.
        """
        self.__sample = sample
        self.__generate_chains(sample)
        self.__generate_statistics(sample)

    def __generate_chains(self, sample):
        """
        Generates the __chains and __starts values required for sentence generation.
        """
        words = split_words(sample)
        word_info = map(get_word_info, words)

        previous = (0, 0)
        chains = {}
        starts = [previous]

        for pair in word_info:
            chains.setdefault(previous, []).append(pair)
            if pair[1] in DELIMITERS_SENTENCES:
                starts.append(previous)
            previous = (previous[1], pair[0])

        if len(chains) > 0:
            self.__chains = chains
            self.__starts = starts
        else:
            raise ValueError("Could not generate chains from sample text.")

    def __generate_statistics(self, sample):
        """
        Calculates the mean and standard deviation of sentence and paragraph lengths.
        """
        self.__generate_sentence_statistics(sample)
        self.__generate_paragraph_statistics(sample)
        self.reset_statistics()

    def __generate_sentence_statistics(self, sample):
        """
        Calculates the mean and standard deviation of the lengths of sentences 
        (in words) in a sample text.
        """
        sentences = filter(lambda s : len(s.strip()) > 0, split_sentences(sample))
        sentence_lengths = map(len, map(split_words, sentences))
        self.__generated_sentence_mean = mean(sentence_lengths)
        self.__generated_sentence_sigma = sigma(sentence_lengths)

    def __generate_paragraph_statistics(self, sample):
        """
        Calculates the mean and standard deviation of the lengths of paragraphs
        (in sentences) in a sample text.
        """
        paragraphs = filter(lambda s : len(s.strip()) > 0, split_paragraphs(sample))
        paragraph_lengths = map(len, map(split_sentences, paragraphs))
        self.__generated_paragraph_mean = mean(paragraph_lengths)
        self.__generated_paragraph_sigma = sigma(paragraph_lengths)

    def reset_statistics(self):
        """
        Returns the values of sentence_mean, sentence_sigma, paragraph_mean,
        and paragraph_sigma to their values as calculated from the sample
        text.
        """
        self.sentence_mean = self.__generated_sentence_mean
        self.sentence_sigma = self.__generated_sentence_sigma
        self.paragraph_mean = self.__generated_paragraph_mean
        self.paragraph_sigma = self.__generated_paragraph_sigma


    def __set_dictionary(self, dictionary):
        """
        Sets the generator to use a given selection of words for generating 
        sentences with.
        """
        words = {}

        for word in dictionary:
            try:
                word = str(word)
                words.setdefault(len(word), set()).add(word)
            except TypeError:
                continue

        if len(words) > 0:
            self.__words = words

    def __get_dictionary(self):
        dictionary = []

        for length, words in self.__words.items():
            for word in words:
                dictionary.append(word)

        return dictionary

    sample = property(__get_sample, __set_sample)
    dictionary = property(__get_dictionary, __set_dictionary)

    def generate_sentence(self, start_with_lorem=False):
        """
        Generates a single sentence, of random length.

        If start_with_lorem=True, then the sentence will begin with the
        standard "Lorem ipsum..." first sentence.
        """
        if len(self.__chains) == 0 or len(self.__starts) == 0:
            raise NoChainsError

        if len(self.__words) == 0:
            raise NoDictionaryError

        # The length of the sentence is a normally distributed random variable.
        sentence_length = random.normalvariate(self.sentence_mean, \
            self.sentence_sigma)
        sentence_length = max(int(round(sentence_length)), 1)

        sentence = []
        previous = ()

        word_delimiter = '' # Defined here in case while loop doesn't run

        # Start the sentence with "Lorem ipsum...", if desired
        if start_with_lorem:
            lorem = "lorem ipsum dolor sit amet, consecteteur adipiscing elit"
            lorem = lorem.split()
            sentence += lorem[:sentence_length]
            last_char = sentence[-1][-1]
            if last_char in DELIMITERS_WORDS:
                word_delimiter = last_char

        # Generate a sentence from the "chains"
        while len(sentence) < sentence_length:
            # If the current starting point is invalid, choose another randomly
            while (not self.__chains.has_key(previous)):
                previous = random.choice(self.__starts)

            # Choose the next "chain" to go to. This determines the next word
            # length we'll use, and whether there is e.g. a comma at the end of
            # the word.
            chain = random.choice(self.__chains[previous])
            word_length = chain[0]

            # If the word delimiter contained in the chain is also a sentence
            # delimiter, then we don't include it because we don't want the
            # sentence to end prematurely (we want the length to match the
            # sentence_length value).
            if chain[1] in DELIMITERS_SENTENCES:
                word_delimiter = ''
            else:
                word_delimiter = chain[1]

            # Choose a word randomly that matches (or closely matches) the
            # length we're after.
            closest_length = choose_closest(
                    self.__words.keys(),
                    word_length)
            word = random.choice(list(self.__words[closest_length]))

            sentence += [word + word_delimiter]
            previous = (previous[1], word_length)

        # Finish the sentence off with capitalisation, a period and
        # form it into a string
        sentence = ' '.join(sentence)
        sentence = sentence.capitalize()
        sentence = sentence.rstrip(word_delimiter) + '.'

        return sentence

    def generate_paragraph(self, start_with_lorem=False):
        """
        Generates a single lorem ipsum paragraph, of random length.

        If start_with_lorem=True, then the paragraph will begin with the
        standard "Lorem ipsum..." first sentence.
        """
        paragraph = []

        # The length of the paragraph is a normally distributed random variable.
        paragraph_length = random.normalvariate(self.paragraph_mean, \
            self.paragraph_sigma)
        paragraph_length = max(int(round(paragraph_length)), 1)

        # Construct a paragraph from a number of sentences.
        while len(paragraph) < paragraph_length:
            sentence = self.generate_sentence(
                start_with_lorem = (start_with_lorem and len(paragraph) == 0)
                )
            paragraph += [sentence]

        # Form the paragraph into a string.
        paragraph = ' '.join(paragraph)

        return paragraph


class MarkupGenerator(Generator):
    """
    Generates random strings of "lorem ipsum" text, based on the word
    distribution of a given sample text, using the words in a given
    dictionary.

    Provides a number of methods for producing "lorem ipsum" text with
    varying formats.
    """
    def __generate_markup(self, begin, end, between, quantity,
        start_with_lorem, function):
        """
        Generates multiple pieces of text, with begin before each piece, end
        after each piece, and between between each piece. Accepts a function
        that returns a string.
        """
        text = []

        while len(text) < quantity:
            part = function(
                    start_with_lorem = (start_with_lorem and len(text) == 0)
                    )
            part = begin + part + end
            text += [part]

        text = between.join(text)
        return text

    def __generate_markup_paragraphs(self, begin_paragraph, end_paragraph,
        between_paragraphs, quantity, start_with_lorem=False):
        return self.__generate_markup(
                begin_paragraph,
                end_paragraph,
                between_paragraphs,
                quantity,
                start_with_lorem,
                self.generate_paragraph)

    def __generate_markup_sentences(self, begin_sentence, end_sentence,
        between_sentences, quantity, start_with_lorem=False):
        return self.__generate_markup(
                begin_sentence,
                end_sentence,
                between_sentences,
                quantity,
                start_with_lorem,
                self.generate_sentence)

    def generate_paragraphs_plain(self, quantity, start_with_lorem=False):
        """Generates a number of paragraphs, separated by empty lines."""
        return self.__generate_markup_paragraphs(
                begin_paragraph='',
                end_paragraph='',
                between_paragraphs=NEWLINE * 2,
                quantity=quantity,
                start_with_lorem=start_with_lorem
                )

    def generate_sentences_plain(self, quantity, start_with_lorem=False):
        """Generates a number of sentences."""
        return self.__generate_markup_sentences(
                begin_sentence='',
                end_sentence='',
                between_sentences=' ',
                quantity=quantity,
                start_with_lorem=start_with_lorem
                )

    def generate_paragraphs_html_p(self, quantity, start_with_lorem=False):
        """
        Generates a number of paragraphs, with each paragraph
        surrounded by HTML pararaph tags.
        """
        return self.__generate_markup_paragraphs(
                begin_paragraph='<p>' + NEWLINE + '\t',
                end_paragraph=NEWLINE + '</p>',
                between_paragraphs=NEWLINE,
                quantity=quantity,
                start_with_lorem=start_with_lorem
                )

    def generate_sentences_html_p(self, quantity, start_with_lorem=False):
        """
        Generates a number of sentences, with each sentence
        surrounded by HTML pararaph tags.
        """
        return self.__generate_markup_sentences(
                begin_sentence='<p>' + NEWLINE + '\t',
                end_sentence=NEWLINE + '</p>',
                between_sentences=NEWLINE,
                quantity=quantity,
                start_with_lorem=start_with_lorem
                )

    def generate_paragraphs_html_li(self, quantity, start_with_lorem=False):
        """Generates a number of paragraphs, separated by empty lines."""
        output = self.__generate_markup_paragraphs(
                begin_paragraph='\t<li>\n\t\t',
                end_paragraph='\n\t</li>',
                between_paragraphs=NEWLINE,
                quantity=quantity,
                start_with_lorem=start_with_lorem
                )
        return ('<ul>' + NEWLINE + output + NEWLINE + '</ul>')

    def generate_sentences_html_li(self, quantity, start_with_lorem=False):
        """Generates a number of sentences surrounded by HTML 'li' tags."""
        output = self.__generate_markup_sentences(
                begin_sentence='\t<li>' + NEWLINE + '\t\t',
                end_sentence=NEWLINE + '\t</li>',
                between_sentences=NEWLINE,
                quantity=quantity,
                start_with_lorem=start_with_lorem
                )
        return ('<ul>' + NEWLINE + output + NEWLINE + '</ul>')
