import unittest
import noun_extraction


class TestStringMethods(unittest.TestCase):

    def test_nouns(self):
        tokens = noun_extraction.extract_nouns("I love this movie")
        self.assertEqual(tokens, [('movie', 'NN')])


if __name__ == '__main__':
    unittest.main()
