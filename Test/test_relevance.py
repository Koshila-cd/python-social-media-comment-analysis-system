import unittest
import main


class TestStringMethods(unittest.TestCase):

    def test_relevance(self):
        category = main.comment_nouns("His trailer shows everything I don't think I'll have to watch after the release")
        self.assertEqual(category, (['trailer', 'show', 'everything', 'release'] [('trailer', 'NN'), ('show', 'NN'), ('everything', 'NN'), ('release', 'NN')], "His trailer shows everything I don't think I'll have to watch after the release"))


if __name__ == '__main__':
    unittest.main()
