from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk import classify
from nltk import NaiveBayesClassifier
from nltk.corpus import movie_reviews
from nltk import ngrams
from nltk.corpus import stopwords
import string
import pandas as pd
import noun_extraction
from random import shuffle

pr = pd.read_csv('data/pos-reviews-youtube.csv', index_col=0)
nr = pd.read_csv('data/neg-reviews-youtube.csv', index_col=0)
stopwords_english = stopwords.words('english')


# def analyze_sentiment(comment):
#     blob1 = TextBlob(comment)
#     p = blob1.sentiment.polarity
#     print("score: ", p)
#     polarity = sentiment_category(p)
#     print("category: ", polarity)
#     return polarity
#
#
# def sentiment_category(score):
#     category = 'x'
#     print("score", score)
#     if score > 0.0:
#         category = 'p'
#
#     if score < 0.0:
#         category = 'n'
#
#     return category


# clean words, i.e. remove stopwords and punctuation
def clean_words(words, stopwords_english):
    words_clean = []
    for word in words:
        word = word.lower()
        if word not in stopwords_english and word not in string.punctuation:
            words_clean.append(word)
    return words_clean


# feature extractor function for unigram
def bag_of_words(words):
    words_dictionary = dict([word, True] for word in words)
    return words_dictionary


# feature extractor function for ngrams (bigram)
def bag_of_ngrams(words, n=2):
    words_ng = []
    for item in iter(ngrams(words, n)):
        words_ng.append(item)
    words_dictionary = dict([word, True] for word in words_ng)
    return words_dictionary


# let's define a new function that extracts all features
# i.e. that extracts both unigram and bigrams features
def bag_of_all_words(words, n=2):
    words_clean = clean_words(words, stopwords_english)
    words_clean_for_bigrams = clean_words(words, stopwords_english_for_bigrams())

    unigram_features = bag_of_words(words_clean)
    bigram_features = bag_of_ngrams(words_clean_for_bigrams)

    all_features = unigram_features.copy()
    all_features.update(bigram_features)

    return all_features


def stopwords_english_for_bigrams():
    important_words = ['above', 'below', 'off', 'over', 'under', 'more', 'most', 'such', 'no', 'nor', 'not', 'only',
                       'so',
                       'than', 'too', 'very', 'just', 'but']

    return set(stopwords_english) - set(important_words)


def sentiment_analysis(text):
    # cleaning words is find for unigrams
    # but this can omit important words for bigrams
    # for example, stopwords like very, over, under, so, etc. are important for bigrams
    # we create a new stopwords list specifically for bigrams by omitting such important words

    pos_reviews = []
    neg_reviews = []

    for fileid in movie_reviews.fileids('pos'):
        words = movie_reviews.words(fileid)
        pos_reviews.append(words)

    for fileid in movie_reviews.fileids('neg'):
        words = movie_reviews.words(fileid)
        neg_reviews.append(words)

    for label, row in pr.iterrows():
        print(label)
        tokens = noun_extraction.extract_nouns(label)
        for t in tokens:
            pos_reviews.append(t)

    for label, row in nr.iterrows():
        tokens = noun_extraction.extract_nouns(label)
        for t in tokens:
            neg_reviews.append(t)
    # 0.8325 0.755
    # before 0.7875 now 0.805
    # positive reviews feature set
    pos_reviews_set = []
    for words in pos_reviews:
        pos_reviews_set.append((bag_of_all_words(words), 'pos'))

    # negative reviews feature set
    neg_reviews_set = []
    for words in neg_reviews:
        neg_reviews_set.append((bag_of_all_words(words), 'neg'))

    # print(len(pos_reviews_set), len(neg_reviews_set))  # Output: (1000, 1000)

    # radomize pos_reviews_set and neg_reviews_set
    # doing so will output different accuracy result everytime we run the program
    # shuffle(pos_reviews_set)
    # shuffle(neg_reviews_set)

    test_set = pos_reviews_set[:200] + neg_reviews_set[:200]
    train_set = pos_reviews_set[200:] + neg_reviews_set[200:]

    print(len(test_set), len(train_set))  # Output: (400, 1600)

    classifier = NaiveBayesClassifier.train(train_set)

    accuracy = classify.accuracy(classifier, test_set)
    print(accuracy)  # Output: 0.8325

    custom_review_tokens = word_tokenize(text)
    custom_review_set = bag_of_all_words(custom_review_tokens)

    # print("new comment sentiment ::: ",classifier.classify(custom_review_set))
    polarity = category(classifier.classify(custom_review_set))
    return polarity


def category(score):
    category = 'x'
    print("score", score)
    if score == 'pos':
        category = 'p'

    if score == 'neg':
        category = 'n'

    return category


if __name__ == '__main__':
    comment = "LOVE IT (just watched it)."
    sentiment_analysis(comment)
    # analyze_sentiment(comment)
