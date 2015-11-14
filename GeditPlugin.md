# Gedit plugin #

The [command-line interface](CommandLineInterface.md) for Lorem Ipsum Generator can be used with the [External Tools plugin](http://library.gnome.org/users/gedit/stable/gedit-external-tools-plugin.html.en) in Gedit to insert random sentences or paragraphs into documents in Gedit.

## Lipsum sentence ##

**Description:** Print a lorem ipsum sentence.

**Command:**
```
#!/bin/sh
lorem-ipsum-generator -s 1
```

**Input:** Nothing

**Output:** Insert at cursor position

**Applicability:** All documents

## Lipsum paragraph ##

**Description:** Print a lorem ipsum paragraph.

**Command:**
```
#!/bin/sh
lorem-ipsum-generator -p 1
```

**Input:** Nothing

**Output:** Insert at cursor position

**Applicability:** All documents

## Multiple Lipsum sentences ##

**Description:** Write a number of sentences in the current document and select that number. This will replace the number with that many lorem ipsum sentences.

**Command:**
```
#!/bin/sh
read SENTENCES
lorem-ipsum-generator -s $SENTENCES
```

**Input:** Current selection

**Output:** Replace current selection

**Applicability:** All documents

## Multiple Lipsum paragraphs ##

**Description:** Write a number of paragraphs in the current document and select that number. This will replace the number with that many lorem ipsum paragraphs.

**Command:**
```
#!/bin/sh
read PARAGRAPHS
lorem-ipsum-generator -p $PARAGRAPHS
```

**Input:** Current selection

**Output:** Replace current selection

**Applicability:** All documents