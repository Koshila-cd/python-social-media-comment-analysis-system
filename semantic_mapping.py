from sense2vec import Sense2Vec
from nltk.corpus import wordnet

def semantic_map(noun):
    synonyms = []

    for syn in wordnet.synsets(noun[0]):
        for l in syn.lemmas():
            synonyms.append(l.name())

    print(set(synonyms))
    map = True

    return bool(map)