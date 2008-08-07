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
parser.add_option("--sample", dest="sample", help="use FILE as the sample text", metavar="FILE")
parser.add_option("--dictionary", dest="dictionary", help="use FILE as the dictionary text", metavar="FILE")
parser.add_option("--sentence_mean", dest="sentence_mean", help="set the mean sentence length to NUM", metavar="NUM", type="float")
parser.add_option("--paragraph_mean", dest="paragraph_mean", help="set the mean paragraph length to NUM", metavar="NUM", type="float")
parser.add_option("--sentence_sigma", dest="sentence_sigma", help="set the standard deviation sentence length to NUM", metavar="NUM", type="float")
parser.add_option("--paragraph_sigma", dest="paragraph_sigma", help="set the standard deviation paragraph length to NUM", metavar="NUM", type="float")
parser.add_option("-t", "--html", dest="html", action="store_true", help="include HTML paragraph tags")
parser.add_option("-l", "--lorem", dest="lorem", action="store_true", help="start with \"Lorem ipsum dolor...\"")

(options, args) = parser.parse_args()

# Initialise generator
generator = lipsum.markupgenerator()

# Set the sample and dictionary texts
sample_path = options.sample
dictionary_path = options.dictionary
for pre in ['./', prefix + '/share/lorem-ipsum-generator/']:
    trial = abspath(pre + 'sample.txt')
    if not sample_path and exists(trial):
        sample_path = trial
    trial = abspath(pre + 'dictionary.txt')
    if not dictionary_path and exists(trial):
        dictionary_path = trial

sample = load_contents(sample_path)
generator.set_sample(sample)

dictionary = load_contents(dictionary_path)
generator.set_dictionary(dictionary)

# Set statistics
if options.sentence_mean != None:
    generator.set_sentence_mean(options.sentence_mean)
if options.paragraph_mean != None:
    generator.set_paragraph_mean(options.paragraph_mean)
if options.sentence_sigma != None:
    generator.set_sentence_sigma(options.sentence_sigma)
if options.paragraph_sigma != None:
    generator.set_paragraph_sigma(options.paragraph_sigma)

output = ""

# Generate paragraphs?
if options.paragraphs != None:
    if options.html != None:
        output = generator.generate_html_paragraphs(options.paragraphs, options.lorem)
    else:
        output = generator.generate_text_paragraphs(options.paragraphs, options.lorem)
# Generate sentences?
elif options.sentences != None:
    output = generator.generate_text_sentences(options.sentences, options.lorem)

print output
