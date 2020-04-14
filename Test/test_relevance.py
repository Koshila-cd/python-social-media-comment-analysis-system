import unittest
import main


class TestStringMethods(unittest.TestCase):

    def test_relevance(self):
        category = main.comment_nouns("I love this movie")
        # self.assertEqual(category, ['movie'], [('movie', 'NN')], 'I love this movie')


if __name__ == '__main__':
    unittest.main()
