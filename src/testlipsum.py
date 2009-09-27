import unittest
import lipsum
import math

class TestGenerator(unittest.TestCase):
    def setUp(self):
        self.sample = """
        One two three four five six. Seven eight nine ten eleven twelve.

        Thirteen fourteen fifteen sixteen. Seventeen eighteen nineteen twenty.
        """
        self.dictionary = "a bb ccc dddd eeeee ffffff ggggggg hhhhhhhh iiiiiiiii jjjjjjjjjj kkkkkkkkkkk llllllllllll".split()
        self.generator = lipsum.Generator(self.sample, self.dictionary)

    def test_mean(self):
        self.assertEquals(lipsum._mean([1, 2, 3, 4]), 2.5)
        self.assertEquals(lipsum._mean([6, 6, 4, 4]), 5)

    def test_mean_empty(self):
        self.assertEquals(lipsum._mean([]), 0)

    def test_variance(self):
        self.assertEquals(lipsum._variance([6, 6, 4, 4]), 1)
        self.assertEquals(lipsum._variance([1, 2, 3, 4]), 1.25)

    def test_variance_empty(self):
        self.assertEquals(lipsum._variance([]), 0)

    def test_sigma(self):
        self.assertEquals(lipsum._sigma([6, 6, 4, 4]), 1)
        self.assertEquals(lipsum._sigma([1, 2, 3, 4]), math.sqrt(1.25))

    def test_sigma_empty(self):
        self.assertEquals(lipsum._sigma([]), 0)

    def test_split_sentences(self):
        self.assertEquals(lipsum._split_sentences("Hello. Hi."), ["Hello", "Hi"])
        self.assertEquals(lipsum._split_sentences(self.sample), 
                ["One two three four five six", 
                    "Seven eight nine ten eleven twelve", 
                    "Thirteen fourteen fifteen sixteen", 
                    "Seventeen eighteen nineteen twenty"])

    def test_split_sentences_empty(self):
        self.assertEquals(lipsum._split_sentences(""), [])

    def test_split_sentences_trailing(self):
        self.assertEquals(lipsum._split_sentences("Hello. Hi. Hello"), 
                ["Hello", "Hi", "Hello"])
        self.assertEquals(lipsum._split_sentences("  Hello. Hi. Hello  "), 
                ["Hello", "Hi", "Hello"])
        self.assertEquals(lipsum._split_sentences("..  Hello... Hi.... Hello  "), 
                ["Hello", "Hi", "Hello"])

    def test_split_paragraphs(self):
        self.assertEquals(lipsum._split_paragraphs(self.sample), 
                ["One two three four five six. Seven eight nine ten eleven twelve.",
                    "Thirteen fourteen fifteen sixteen. Seventeen eighteen nineteen twenty."])

    def test_split_paragraphs_empty(self):
        self.assertEquals(lipsum._split_paragraphs(""), [])

    def test_split_paragraphs_trailing(self):
        self.assertEquals(lipsum._split_paragraphs("Hello\n\nHi"), ["Hello", "Hi"])
        self.assertEquals(lipsum._split_paragraphs("Hello\n\nHi\n"), ["Hello", "Hi"])
        self.assertEquals(lipsum._split_paragraphs("Hello\n\nHi\n\n"), ["Hello", "Hi"])
        self.assertEquals(lipsum._split_paragraphs("Hello\n\nHi\n\n\n"), ["Hello", "Hi"])
        self.assertEquals(lipsum._split_paragraphs("Hello\n\nHi\n\n\n\n\n\n"), ["Hello", "Hi"])
        self.assertEquals(lipsum._split_paragraphs("\nHello\n\nHi"), ["Hello", "Hi"])
        self.assertEquals(lipsum._split_paragraphs("\n\nHello\n\nHi"), ["Hello", "Hi"])
        self.assertEquals(lipsum._split_paragraphs("\n\n\nHello\n\nHi"), ["Hello", "Hi"])
        self.assertEquals(lipsum._split_paragraphs("\n\n\n\n\n\nHello\n\nHi"), ["Hello", "Hi"])

    def test_split_words(self):
        self.assertEquals(lipsum._split_words("One two three four"), 
                ["One", "two", "three", "four"])
        self.assertEquals(lipsum._split_words("  One    two  three  four   "), 
                ["One", "two", "three", "four"])

    def test_choose_closest(self):
        self.assertEquals(lipsum._choose_closest([1,2,3,4], 1), 1)
        self.assertEquals(lipsum._choose_closest([1,2,3,4], 4), 4)
        self.assertEquals(lipsum._choose_closest([1,2,3,4], 20), 4)
        self.assertEquals(lipsum._choose_closest([1,2,3,4], -10), 1)
        self.assertEquals(lipsum._choose_closest([1,4], 2), 1)
        self.assertEquals(lipsum._choose_closest([1,4], 3), 4)
        self.assertEquals(lipsum._choose_closest([1,3], 2), 1)
        self.assertEquals(lipsum._choose_closest([3,1], 2), 3)
        self.assertEquals(lipsum._choose_closest([1], 200), 1)

    def test_split_words_empty(self):
        self.assertEquals(lipsum._split_words(""), [])

    def test_sentence_mean(self):
        self.assertEquals(self.generator.sentence_mean, 5)

    def test_set_sentence_mean(self):
        self.generator.sentence_mean = 4
        self.assertEquals(self.generator.sentence_mean, 4)

    def test_paragraph_mean(self):
        self.assertEquals(self.generator.paragraph_mean, 2)

    def test_set_paragraph_mean(self):
        self.generator.paragraph_mean = 4
        self.assertEquals(self.generator.paragraph_mean, 4)

    def test_sentence_sigma(self):
        self.assertEquals(self.generator.sentence_sigma, 1)

    def test_set_sentence_sigma(self):
        self.generator.sentence_sigma = 4
        self.assertEquals(self.generator.sentence_sigma, 4)

    def test_paragraph_sigma(self):
        self.assertEquals(self.generator.paragraph_sigma, 0)

    def test_set_paragraph_sigma(self):
        self.generator.paragraph_sigma = 4
        self.assertEquals(self.generator.paragraph_sigma, 4)

    def test_sample(self):
        self.assertEquals(self.generator.sample, self.sample)

    def test_dictionary(self):
        self.assertEquals(set(self.generator.dictionary), set(self.dictionary))

    def test_dictionary(self):
        newdict = ["a", "b", "c"]
        self.generator.dictionary = newdict
        self.assertEquals(set(self.generator.dictionary), set(newdict))

    def test_init_no_sample(self):
        self.assertRaises(lipsum.InvalidSampleError, lipsum.Generator, "", self.dictionary)
        self.assertRaises(lipsum.InvalidSampleError, lipsum.Generator, " ", self.dictionary)
        self.assertRaises(lipsum.InvalidSampleError, lipsum.Generator, "\n\n", self.dictionary)
        self.assertRaises(lipsum.InvalidSampleError, lipsum.Generator, "   \n\n   ", self.dictionary)
        self.assertRaises(lipsum.InvalidSampleError, lipsum.Generator, ". .\n\n .", self.dictionary)

    def test_init_no_dict(self):
        self.assertRaises(lipsum.InvalidDictionaryError, lipsum.Generator, self.sample, [])

if __name__ == '__main__':
    unittest.main()
