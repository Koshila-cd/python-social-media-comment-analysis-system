from nltk import ngrams
from nltk.tokenize import word_tokenize
from nltk import classify
from nltk import NaiveBayesClassifier
import string
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk.corpus import movie_reviews
import pandas as pd

pr = pd.read_csv('data/pos-reviews-youtube.csv', index_col=0)
nr = pd.read_csv('data/neg-reviews-youtube.csv', index_col=0)

positive_review_file = movie_reviews.fileids('pos')[0]
documents = []

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        # documents.append((list(movie_reviews.words(fileid)), category))
        documents.append((movie_reviews.words(fileid), category))

# for label, row in pr.iterrows():
#     tokens = fyp.extract_nouns(label)
#     for t in tokens:
#         documents.append((t, 'pos'))
#
# for label, row in nr.iterrows():
#     tokens = fyp.extract_nouns(label)
#     for t in tokens:
#         documents.append((t, 'neg'))
# print(len(documents))  # Output: 2000

# shuffle the document list
from random import shuffle

shuffle(documents)
all_words = [word.lower() for word in movie_reviews.words()]

all_words_frequency = FreqDist(all_words)

stopwords_english = stopwords.words('english')
# create a new list of words by removing stopwords from all_words
all_words_without_stopwords = [word for word in all_words if word not in stopwords_english]

# create a new list of words by removing punctuation from all_words
all_words_without_punctuation = [word for word in all_words if word not in string.punctuation]

# Let's name the new list as all_words_clean
# because we clean stopwords and punctuations from the word list

# all_words_clean = []
# for word in all_words:
#     if word not in stopwords_english and word not in string.punctuation:
#         all_words_clean.append(word)
#
# all_words_frequency = FreqDist(all_words_clean)
#
# # get 2000 frequently occuring words
# most_common_words = all_words_frequency.most_common(2000)
#
# # the most common words list's elements are in the form of tuple
# # get only the first element of each tuple of the word list
# word_features = [item[0] for item in most_common_words]


# def document_features(document):
#     # "set" function will remove repeated/duplicate tokens in the given list
#     document_words = set(document)
#     features = {}
#     for word in word_features:
#         features['contains(%s)' % word] = (word in document_words)
#     return features


# get the first negative movie review file
# movie_review_file = movie_reviews.fileids('neg')[0]
#
# feature_set = [(document_features(doc), category) for (doc, category) in documents]
#
# test_set = feature_set[:400]
# train_set = feature_set[400:]
# classifier = NaiveBayesClassifier.train(train_set)
#
# accuracy = classify.accuracy(classifier, test_set)
# print(accuracy)  # Output: 0.77
#
# custom_review = "I hated the film. It was a disaster. Poor direction, bad acting."
# custom_review_tokens = word_tokenize(custom_review)
# custom_review_set = document_features(custom_review_tokens)
# print(classifier.classify(custom_review_set))  # Output: neg
# Negative review correctly classified as negative

# probability result
# prob_result = classifier.prob_classify(custom_review_set)
#
# custom_review = "It was a wonderful and amazing movie. I loved it. Best direction, good acting."
# custom_review_tokens = word_tokenize(custom_review)
# custom_review_set = document_features(custom_review_tokens)
#
# print(classifier.classify(custom_review_set))  # Output: neg
# Positive review is classified as negative
# We need to improve our feature set for more accurate prediction

# probability result
# prob_result = classifier.prob_classify(custom_review_set)

# show 5 most informative features
pos_reviews = []
for fileid in movie_reviews.fileids('pos'):
    words = movie_reviews.words(fileid)
    pos_reviews.append(words)

neg_reviews = []
for fileid in movie_reviews.fileids('neg'):
    words = movie_reviews.words(fileid)
    neg_reviews.append(words)

stopwords_english = stopwords.words('english')


# feature extractor function
def bag_of_words(words):
    words_clean = []

    for word in words:
        word = word.lower()
        if word not in stopwords_english and word not in string.punctuation:
            words_clean.append(word)

    words_dictionary = dict([word, True] for word in words_clean)

    return words_dictionary


# positive reviews feature set
pos_reviews_set = []
for words in pos_reviews:
    pos_reviews_set.append((bag_of_words(words), 'pos'))

# negative reviews feature set
neg_reviews_set = []
for words in neg_reviews:
    neg_reviews_set.append((bag_of_words(words), 'neg'))

# radomize pos_reviews_set and neg_reviews_set
# doing so will output different accuracy result everytime we run the program
from random import shuffle

shuffle(pos_reviews_set)
shuffle(neg_reviews_set)

test_set = pos_reviews_set[:200] + neg_reviews_set[:200]
train_set = pos_reviews_set[200:] + neg_reviews_set[200:]

# classifier = NaiveBayesClassifier.train(train_set)

# accuracy = classify.accuracy(classifier, test_set)
#
# custom_review = "I hated the film. It was a disaster. Poor direction, bad acting."
# custom_review_tokens = word_tokenize(custom_review)
# custom_review_set = bag_of_words(custom_review_tokens)
# print(classifier.classify(custom_review_set))  # Output: neg
# Negative review correctly classified as negative

# probability result
# prob_result = classifier.prob_classify(custom_review_set)
#
# custom_review = "It was a wonderful and amazing movie. I loved it. Best direction, good acting."
# custom_review_tokens = word_tokenize(custom_review)
# custom_review_set = bag_of_words(custom_review_tokens)
# print(classifier.classify(custom_review_set))
# Positive review correctly classified as positive

# probability result
# prob_result = classifier.prob_classify(custom_review_set)

stopwords_english = stopwords.words('english')


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


from nltk.tokenize import word_tokenize

text = "It was a very good movie."
words = word_tokenize(text.lower())

# working with cleaning words
# i.e. removing stopwords and punctuation
words_clean = clean_words(words, stopwords_english)

# cleaning words is find for unigrams
# but this can omit important words for bigrams
# for example, stopwords like very, over, under, so, etc. are important for bigrams
# we create a new stopwords list specifically for bigrams by omitting such important words
important_words = ['above', 'below', 'off', 'over', 'under', 'more', 'most', 'such', 'no', 'nor', 'not', 'only', 'so',
                   'than', 'too', 'very', 'just', 'but']

stopwords_english_for_bigrams = set(stopwords_english) - set(important_words)

words_clean_for_bigrams = clean_words(words, stopwords_english_for_bigrams)

# We will use general stopwords for unigrams
# And special stopwords list for bigrams
unigram_features = bag_of_words(words_clean)

bigram_features = bag_of_ngrams(words_clean_for_bigrams)

# combine both unigram and bigram features
all_features = unigram_features.copy()
all_features.update(bigram_features)


# let's define a new function that extracts all features
# i.e. that extracts both unigram and bigrams features
def bag_of_all_words(words, n=2):
    words_clean = clean_words(words, stopwords_english)
    words_clean_for_bigrams = clean_words(words, stopwords_english_for_bigrams)

    unigram_features = bag_of_words(words_clean)
    bigram_features = bag_of_ngrams(words_clean_for_bigrams)

    all_features = unigram_features.copy()
    all_features.update(bigram_features)

    return all_features


pos_reviews = []
for fileid in movie_reviews.fileids('pos'):
    words = movie_reviews.words(fileid)
    pos_reviews.append(words)

neg_reviews = []
for fileid in movie_reviews.fileids('neg'):
    words = movie_reviews.words(fileid)
    neg_reviews.append(words)

# positive reviews feature set
pos_reviews_set = []
for words in pos_reviews:
    pos_reviews_set.append((bag_of_all_words(words), 'pos'))

# negative reviews feature set
neg_reviews_set = []
for words in neg_reviews:
    neg_reviews_set.append((bag_of_all_words(words), 'neg'))

classifier = NaiveBayesClassifier.train(train_set)

accuracy = classify.accuracy(classifier, test_set)

custom_review = "I hated the film. It was a disaster. Poor direction, bad acting."
custom_review_tokens = word_tokenize(custom_review)
custom_review_set = bag_of_all_words(custom_review_tokens)
print(classifier.classify(custom_review_set))  # Output: neg
# Negative review correctly classified as negative

# probability result
prob_result = classifier.prob_classify(custom_review_set)

custom_review = "this is not crazy"
custom_review_tokens = word_tokenize(custom_review)
custom_review_set = bag_of_all_words(custom_review_tokens)

print(classifier.classify(custom_review_set))  # Output: pos
# Positive review correctly classified as positive

# probability result
prob_result = classifier.prob_classify(custom_review_set)

custom_review = "I hate this movie"
custom_review_tokens = word_tokenize(custom_review)
custom_review_set = bag_of_all_words(custom_review_tokens)

print("new comment sentiment : ", classifier.classify(custom_review_set))
