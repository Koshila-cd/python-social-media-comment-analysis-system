import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from textblob import TextBlob


def extract_nouns(text):
    # text = TextBlob(text).correct().__str__()
    sentences = sent_tokenize(text)

    # tokenize comment
    tokens = []
    if len(sentences) > 0:
        for sentence in sentences:
            tokens.append(word_tokenize(sentence))

    else:
        tokens = word_tokenize(sentences)

    # remove stop words
    stop_words = set(stopwords.words("english"))
    filtered_comment = []
    for w in tokens:
        for token in w:
            if token not in stop_words:
                filtered_comment.append(token)

    # word lemmatization
    lem = WordNetLemmatizer()
    lemmatized_words = []
    for com in filtered_comment:
        lemmatized_words.append(lem.lemmatize(com, "v"))

    # select only letters from alphabet
    remove_punc = []
    for l in lemmatized_words:
        if l.isalpha():
            remove_punc.append(l)

    # POS tagging
    pos_tagged_words = nltk.pos_tag(remove_punc)

    text_nouns = []
    for w in pos_tagged_words:
        if w[1] == 'NN' or w[1] == 'NNS' or w[1] == 'NNP':
            text_nouns.append(w)

    return text_nouns


if __name__ == '__main__':
    text = "This movie is awesome. But I don't like the last part!!!"
    extract_nouns(text)
