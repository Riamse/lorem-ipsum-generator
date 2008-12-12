#!/usr/bin/env python
import lipsum
from sys import prefix
from os.path import abspath,exists
from optparse import OptionParser

def load_contents(file):
    file = open(file, 'r')
    contents = file.read()
    file.close()
    return contents

# Parse options
parser = OptionParser()
parser.add_option("-p", "--paragraphs", dest="paragraphs", help="generate NUM paragraphs", metavar="NUM", type="int")
parser.add_option("-s", "--sentences", dest="sentences", help="generate NUM sentences", metavar="NUM", type="int")
parser.add_option("--sample", dest="sample_path", help="use FILE as the sample text", metavar="FILE")
parser.add_option("--dictionary", dest="dictionary_path", help="use FILE as the dictionary text", metavar="FILE")
parser.add_option("--sentence_mean", dest="sentence_mean", help="set the mean sentence length to NUM", metavar="NUM", type="float")
parser.add_option("--paragraph_mean", dest="paragraph_mean", help="set the mean paragraph length to NUM", metavar="NUM", type="float")
parser.add_option("--sentence_sigma", dest="sentence_sigma", help="set the standard deviation sentence length to NUM", metavar="NUM", type="float")
parser.add_option("--paragraph_sigma", dest="paragraph_sigma", help="set the standard deviation paragraph length to NUM", metavar="NUM", type="float")
parser.add_option("-l", "--lorem", dest="lorem", action="store_true", help="start with \"Lorem ipsum dolor...\"")
parser.add_option("-f", "--format", metavar="FORMAT", dest="format", action="store", help="optionally produce formatted output", choices=("plain", "html-p", "html-li"))

(options, args) = parser.parse_args()

# Initialise generator
generator = lipsum.MarkupGenerator()

# Set the sample and dictionary texts
if options.sample_path:
    generator.sample = load_contents(options.sample_path)

if options.dictionary_path:
    generator.dictionary = load_contents(options.dictionary_path)

# Set statistics
if options.sentence_mean:
    generator.sentence_mean = options.sentence_mean
if options.paragraph_mean:
    generator.paragraph_mean = options.paragraph_mean
if options.sentence_sigma:
    generator.sentence_sigma = options.sentence_sigma
if options.paragraph_sigma:
    generator.paragraph_sigma = options.paragraph_sigma

output = ""

# Generate paragraphs?
if options.paragraphs:
    if options.format == "html-p":
        output = generator.generate_paragraphs_html_p(options.paragraphs, options.lorem)
    elif options.format == "html-li":
        output = generator.generate_paragraphs_html_li(options.paragraphs, options.lorem)
    else:
        output = generator.generate_paragraphs_plain(options.paragraphs, options.lorem)
# Generate sentences?
elif options.sentences:
    if options.format == "html-p":
        output = generator.generate_sentences_html_p(options.sentences, options.lorem)
    elif options.format == "html-li":
        output = generator.generate_sentences_html_li(options.sentences, options.lorem)
    else:
        output = generator.generate_sentences_plain(options.sentences, options.lorem)

print output
