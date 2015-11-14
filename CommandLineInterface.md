## Command-line interface ##

As of version 0.3 there is now a command-line interface to the Lorem Ipsum Generator.

By default, calling `lorem-ipsum-generator` with no command-line arguments will open the GUI. Calling `lorem-ipsum-generator` with the `-p` or `-s` arguments will generate paragraphs or sentences of text and print it to the terminal, without loading the GUI. Providing any command-line arguments in addition to the `--gui` option will apply the effects of the arguments and then load the GUI. Providing the `-p` or `-s` arguments in addition to the `--gui` option will load the GUI and then generate the specified number of paragraphs or sentences.

### Examples ###

  * To generate paragraphs
```
lorem-ipsum-generator -p 5
```
  * To generate sentences
```
lorem-ipsum-generator -s 5
```
  * To send default settings to the GUI
```
lorem-ipsum-generator --sample mysample.txt -p 5 -f html-li -g
```
  * To get help on command-line arguments
```
lorem-ipsum-generator --help
```

### Command-line arguments ###

Here is a list of the command-line arguments, as listed by the `--help` option:

```
Usage: lorem-ipsum-generator [options]

Options:
  -h, --help            show this help message and exit
  -p NUM, --paragraphs=NUM
                        generate NUM paragraphs
  -s NUM, --sentences=NUM
                        generate NUM sentences
  --sample=FILE         use FILE as the sample text
  --dictionary=FILE     use FILE as the dictionary text
  --sentence-mean=NUM   set the mean sentence length to NUM
  --paragraph-mean=NUM  set the mean paragraph length to NUM
  --sentence-sigma=NUM  set the standard deviation sentence length to NUM
  --paragraph-sigma=NUM
                        set the standard deviation paragraph length to NUM
  -l, --lorem           start with "Lorem ipsum dolor..."
  -f FORMAT, --format=FORMAT
                        produce format in plain, html-p, or html-li format
  -g, --gui             force GUI to start
```