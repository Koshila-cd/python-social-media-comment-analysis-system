import unittest
import sentiment_analysis


class TestStringMethods(unittest.TestCase):

    def test_positive_comment(self):
        category = sentiment_analysis.analyze_sentiment("I love this movie")
        self.assertEqual(category, 'p')

    def test_negative_comment(self):
        category = sentiment_analysis.analyze_sentiment("I hate this movie")
        self.assertEqual(category, 'n')


if __name__ == '__main__':
    unittest.main()