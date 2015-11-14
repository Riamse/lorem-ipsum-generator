# Advanced features #

![http://lorem-ipsum-generator.googlecode.com/files/Screenshot-Lorem%20ipsum%20generator-0.2.1-advanced.png](http://lorem-ipsum-generator.googlecode.com/files/Screenshot-Lorem%20ipsum%20generator-0.2.1-advanced.png)

## Overview ##

  * **Sample text** - a text file containing sample text. This is analysed and the word, sentence and paragraph length distributions are used to create similar-looking "lorem ipsum" text
  * **Dictionary text** - a text file containing a list of alternative words to generate text with.
  * **Sentence length** - the mean and standard deviation of sentence lengths in words. The generated text has sentence lengths determined by a normally distributed random variable, according to the mean and standard deviation listed here. This is updated to reflect the sample text when a new sample text is chosen.
  * **Paragraph length** - the mean and standard deviation of paragraph lengths in words. The generated text has paragraph lengths determined by a normally distributed random variable, according to the mean and standard deviation listed here. This is updated to reflect the sample text when a new sample text is chosen.
  * **Reset statistics** - resets the sentence and paragraph length values to their values as determined from the sample text.

## Sample texts and dictionaries ##

**Note:** While some attempts have been made to catch errors stemming from invalid or unexpected sample and dictionary texts, it is possible than unchecked errors will occur with unusual files. Heed the following advice for sample and dictionary text formats:

  * **Sample texts** must contain one or more empty-line delimited paragraphs, and each paragraph must contain one or more period, question mark, or exclamation mark delimited sentences.
  * **Dictionary texts** must contain contain one or more white-space delimited words.