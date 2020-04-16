import unittest
import sentiment_analysis


class TestStringMethods(unittest.TestCase):

    def test_positive_comment(self):
        category = sentiment_analysis.sentiment_analysis("I love this movie")
        self.assertEqual(category, 'p')

    # def test_negative_comment(self):
    #     category = sentiment_analysis.sentiment_analysis("I hate this movie")
    #     self.assertEqual(category, 'n')


if __name__ == '__main__':
    unittest.main()
