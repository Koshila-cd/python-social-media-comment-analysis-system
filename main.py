from nltk import word_tokenize
import noun_extraction
from owlready2 import *
from nltk.corpus import wordnet
import sentiment_analysis
import named_entity_recognition

onto = get_ontology("movie.owl").load()

slash = "/"


def youtube_nouns(description):
    nouns = noun_extraction.extract_nouns(description)
    # Add the nouns extracted from the description into the Ontology
    for n in nouns:
        onto.MovieKeywords(n[0].casefold())
        onto.save(file="movie.owl", format="rdfxml")
        return nouns


def comment_nouns(comment):
    noOfWords = []
    tokens = word_tokenize(comment)
    # remove punctuation in tokens
    for t in tokens:
        if t.isalpha():
            noOfWords.append(t)
    mapped = []
    nouns = []

    # procedure for single word comments
    if len(noOfWords) == 1:
        word1 = slash + noOfWords[0]
        if onto.search(iri=word1.casefold()):
            mapped.append(noOfWords[0].casefold())
        else:
            # Semantic mapping
            mapped.__add__(semantic_mapping(noOfWords[0].casefold(), mapped))
    else:
        nouns = noun_extraction.extract_nouns(comment)
        cner = named_entity_recognition.recognition(comment)
        if len(cner) > 0:
            # Direct mapping with ontology created for searching for nouns extracted from the YouTube comment
            for n in cner:
                n1 = slash + n
                if onto.search(iri=n1):
                    mapped.append(n)
                else:
                    mapped.__add__(noun_mapping(nouns, mapped))
        else:
            mapped.__add__(noun_mapping(nouns, mapped))
    print("Nouns: ", nouns)
    print("Mapped: ", mapped)
    return mapped, nouns, comment


def noun_mapping(nouns, mapped):
    for n in nouns:
        noun = slash + n[0]
        # Direct mapping with ontology created for searching for nouns extracted from the YouTube comment
        if onto.search(iri=noun.casefold()):
            # print("noun mapping: ", n)
            mapped.append(n[0].casefold())
        else:
            # Semantic mapping
            mapped.__add__(semantic_mapping(n[0].casefold(), mapped))

    return mapped


def semantic_mapping(word, mapped):
    syns = []

    # finding synsets in wordnet
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            # setting words in synsets found from wordnet to array
            syns.append(l.name())

    for syn1 in set(syns):
        s = slash + syn1
        if onto.search(iri=s):
            mapped.append(syn1)
    return mapped


def relevance_check(map):
    if len(map[0]) > 0:
        # sentiment analysis
        polarity = sentiment_analysis.analyze_sentiment(map[2])
        print("relevant comment")
    else:
        polarity = "None"
        print("irrelevant comment")
    return polarity


def toService(comment, description, title):
    onto.MovieNames(title.casefold())
    # recognize named-entities in description
    dner = named_entity_recognition.recognition(description)
    if len(dner) > 0:
        for n in dner:
            # save description details in Ontology
            onto.MovieKeywords(n.casefold())
            onto.save(file="movie.owl", format="rdfxml")

    print("comment: ", comment)
    map = comment_nouns(comment)
    polarity = relevance_check(map)

    return polarity

if __name__ == '__main__':
    ######################################################################

    comment = "We're shaking...It's an earthquake"

    map = comment_nouns(comment)

    polarity = relevance_check(map)
    print("polarity", polarity)
    ######################################################################
