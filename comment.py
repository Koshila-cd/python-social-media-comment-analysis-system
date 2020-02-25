import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from langdetect import detect
import sys
from nltk.corpus import stopwords

comment = "This movie is awesome. But I don't like the last part"

sentences = []

# language detection
if detect(comment) == 'en':
    sentences = sent_tokenize(comment)
else:
    print("The language is, ", detect(comment))
    sys.exit(1)

# tokenize comment
tokens = []
if len(sentences) > 0:
    for sentence in sentences:
        tokens.append(word_tokenize(sentence))

else:
    tokens = word_tokenize(sentences)

# remove stop words
stop_words=set(stopwords.words("english"))
filtered_comment=[]
for w in tokens:
    for token in w:
        if token not in stop_words:
            filtered_comment.append(token)
print("Tokenized Sentence:",tokens)

# word lemmatization
lem = WordNetLemmatizer()
lemmatized_words=[]
for com in filtered_comment:
    lemmatized_words.append(lem.lemmatize(com, "v"))

print("Filterd Sentence:",filtered_comment)
print("Lemmatized Sentence:",lemmatized_words)

# POS tagging
pos_tagged_words = nltk.pos_tag(lemmatized_words)
print("POS Tagged words:", pos_tagged_words)

comment_nouns = []
for w in pos_tagged_words:
    if w[1] == 'NN' or w[1] == 'NNS' or w[1] == 'NNP' or w[1] == 'NNPS' :
        print(w)
        comment_nouns.append(w)

print(comment_nouns)