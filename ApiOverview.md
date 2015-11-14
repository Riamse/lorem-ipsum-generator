# API Overview #

You can generate "lorem ipsum" text from Python applications by importing the `lipsum` module.

```
import lipsum
```

This provides two classes: a low-level class, `Generator` for generating sentences and paragraphs, and a subclass of this, `MarkupGenerator` that produces text in some useful formats.

The main methods for the `Generator` are the `generate_sentence` and `generate_paragraph` methods, which are self-explanatory.

```
g = lipsum.Generator()
g.generate_sentence()
g.generate_paragraph()
g.generate_paragraph(start_with_lorem=True)
```

The `Generator` also provides attributes for altering the sample text and dictionary used by the generator. The sample text is a string (ideally of a reasonable length and format), and the dictionary is a list of words.

```
g.sample = "I was working on the proof of one of my poems all the morning, and took out a comma. In the afternoon I put it back again."
g.dictionary = ["foo", "bar", "skub", "zort", "wacka"]
```

These can alternatively be set at the initialisation of the `Generator`.

```
g = lipsum.Generator("...", [...])
```

Further, there are attributes for modifying the mean and standard deviation of the lengths of sentences and paragraphs that are produced, which are helpful when you want finer control over the lengths of sentences and paragraphs.

Sentence lengths are measured in words. Paragraph lengths are measured in sentences. The mean and standard deviation (sigma) are as though they were parameters to normally distributed random variables (which they are).

```
g.sentence_mean = 10
g.sentence_sigma = 5.4
g.paragraph_mean = 3.5
g.paragraph_sigma = 2
```

If you decide you want to revert back to the old values, there is a function to reset these values to those that were initially calculated from the sample text.

```
g.reset_statistics()
```

The `MarkupGenerator` is the same in all respects, except that it provides a few extra methods for generating text in various formats.

```
m = lipsum.MarkupGenerator()
m.generate_paragraphs_plain(5)
m.generate_sentences_html_li(10)
```

Full details can be found in the pydoc documentation:

```
help(lipsum)
```

As of version 0.3, the API is still in flux. It may not be very Pythonic, and there may be areas which can be improved drastically to make it more useful in other applications. Suggestions are welcomed in the Issue tracker.