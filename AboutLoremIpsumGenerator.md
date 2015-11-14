# About "lorem ipsum" text #

"Lorem ipsum" text is jumbled, latin text, conventionally used as dummy text to test the appearance of designs that incorporate large amounts of text. Examples include books, magazines and web pages.

The motivation is that meaningful, English text is distracting when testing designs. By using latin, this distraction is eliminated (for people who don't know latin) and designers can focus on the appearance of the design as a whole, and on the typography that is used in the page.

"Lorem ipsum" text also has the advantage that it has a similar word distribution to regular English text. This means that, when looking at the design as a whole, it will look similar to how it would if actual content were used. The text does not produce distracting patterns in white-space, as would be produced if repeating text such as "test test test" were used.

Using generated, random "lorem ipsum" text reinforces the last mentioned benefit. As the generated text is random, it allows for an arbitrary amount of text to be produced without relying on repetition.

_More information:_ [Lorem ipsum (Wikipedia)](http://en.wikipedia.org/wiki/Lorem_ipsum)

# How the program generates random "lorem ipsum" text #

The Lorem Ipsum Generator produces its text based on the analysis of a sample file.

Markov chains are used to generate sentences with a word length distribution similar to the sample file.

A Markov chain is a process where the next decision to be made is based solely on the result of the last decision. In the Lorem Ipsum Generator, sentences are built word at a time, and this can be interpreted as a series of decisions (which word to choose). Words are chosen based on their length only, and which word is chosen depends on the last two words chosen.

The decision is based on probability. The probability that a word of a certain length is chosen, given the length of the last two words chosen, is equal to the probability that a word of the same length appears in the sample text, given that the two words before it are the same length as the last two words chosen in the Markov chain process.

The Lorem Ipsum Generator chooses latin words from a separate dictionary file, and substitutes in these words based on their lengths, and the lengths chosen as part of the Markov chain. The Lorem Ipsum Generator also takes note of periods, question marks, exclamation marks and commas in the sample text, inserting these as part of the Markov Chain algorithm.

The use of Markov chains in the Lorem Ipsum Generator was inspired by the Mark V. Shaney program. This program produces seemingly grammatically correct sentences (in real English, as opposed to jumbled latin), based on a sample file. There is an amusing story surrounding the Mark V. Shaney program.

To generate sentences and paragraphs of "lorem ipsum" text, the Lorem Ipsum Generator uses normally distributed random variables to limit the lengths of sentences and paragraphs. The distribution of these variables depends on the mean and standard deviation of the sentence and paragraph lengths in the sample text (where sentence length is defined as the number of words in a sentence, and paragraph length as the number of sentences in a paragraph).

_More information:_ [Markov chain (Wikipedia)](http://en.wikipedia.org/wiki/Markov_chain), [Mark V. Shaney (Wikipedia)](http://en.wikipedia.org/wiki/Mark_V_Shaney)