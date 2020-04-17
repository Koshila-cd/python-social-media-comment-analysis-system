from nltk import word_tokenize
import noun_extraction
from owlready2 import *
from nltk.corpus import wordnet
import sentiment_analysis
import named_entity_recognition
from textblob import TextBlob

onto = get_ontology("movie.owl").load()

youTubeDescription = "Happy Zoo Year! The new trailer for Zootopia featuring Shakira’s new single “Try Everything, is here!" \
                     " Watch now and see the film in theatres in 3D March 4! The modern mammal metropolis of Zootopia is a city " \
                     "like no other. Comprised of habitat neighborhoods like ritzy Sahara Square and frigid Tundratown, it’s a melting" \
                     " pot where animals from every environment live together—a place where no matter what you are, from the biggest " \
                     "elephant to the smallest shrew, you can be anything. But when rookie Officer Judy Hopps (voice of Ginnifer Goodwin)" \
                     " arrives, she discovers that being the first bunny on a police force of big, tough animals isn’t so easy. Determined" \
                     " to prove herself, she jumps at the opportunity to crack a case, even if it means partnering with a fast-talking," \
                     " scam-artist fox, Nick Wilde (voice of Jason Bateman), to solve the mystery. Walt Disney Animation Studios’ “Zootopia,”" \
                     " a comedy-adventure directed by Byron Howard and Rich Moore and co-directed by Jared Bush, opens in theaters on March 4," \
                     " 2016. Like Zootopia on Facebook - https://www.facebook.com/DisneyZootopia Follow @DisneyZootopia on Twitter - " \
                     "https://twitter.com/disneyzootopia Follow @DisneyAnimation on Instagram - https://twitter.com/disneyanimation Follow " \
                     "Disney Animation on Tumblr - http://disneyanimation.tumblr.com/ Category Film & Animation"

comment = "is it just me or does this movie have more teens and young adult fans then kid fans?"
comment = "Zootopia is the best animated movie"

star = "*"


def youtube_nouns(description):
    nouns = noun_extraction.extract_nouns(description)
    # Add the nouns extracted from the description into the Ontology
    for n in nouns:
        onto.MovieKeywords(n[0].casefold())
        onto.save(file="movie.owl", format="rdfxml")
        return nouns


def comment_nouns(comment):  # words with missed spellings
    comment = TextBlob(comment).correct().__str__()
    noOfWords = []
    tokens = word_tokenize(comment)
    for t in tokens:
        if t.isalpha():
            noOfWords.append(t)
    mapped = []
    nouns = []

    if len(noOfWords) == 1:
        word1 = star + noOfWords[0]
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
                n1 = star + n
                if onto.search(iri=n1):
                    mapped.append(n)
                else:
                    mapped.__add__(noun_mapping(nouns, mapped))
        else:
            mapped.__add__(noun_mapping(nouns, mapped))
    print("mappedmapped", mapped, nouns, comment)
    return mapped, nouns, comment


def noun_mapping(nouns, mapped):
    for n in nouns:
        noun = star + n[0]
        # print("nnn", n[0])
        # Direct mapping with ontology created for searching for nouns extracted from the YouTube comment
        if onto.search(iri=noun.casefold()):
            # print("cc", noun)
            mapped.append(n[0].casefold())
        else:
            # Semantic mapping
            mapped.__add__(semantic_mapping(n[0].casefold(), mapped))

    # print("mapped", mapped)
    return mapped


def semantic_mapping(word, mapped):
    synonyms = []

    # finding synonyms in wordnet
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            # setting synonyms found from wordnet to array
            synonyms.append(l.name())

    for synonym in set(synonyms):
        s = star + synonym
        if onto.search(iri=s):
            mapped.append(synonym)
    return mapped


def relevance_check(map):
    if len(map[0]) > 0:
        polarity = sentiment_analysis.analyze_sentiment(map[2])
    else:
        polarity = "None"
    return polarity


def toService(comment, description, title):
    onto.MovieNames(title)
    dner = named_entity_recognition.recognition(description)
    if len(dner) > 0:
        for n in dner:
            onto.MovieKeywords(n.casefold())
            onto.save(file="movie.owl", format="rdfxml")

    youtube_nouns(description)

    corrected = TextBlob(comment).correct().__str__()
    print("corrected : ", corrected)
    map = comment_nouns(corrected)
    polarity = relevance_check(map)

    return polarity


# if __name__ == '__main__':
#
#     ######################################################################
#     dner = named_entity_recognition.recognition(youTubeDescription)
#     if len(dner) > 0:
#         for n in dner:
#             # print("dner")
#             onto.MovieKeywords(n.casefold())
#             onto.save(file="movie.owl", format="rdfxml")
#
#     youtube_nouns(youTubeDescription)
#
#     comment = "I liove this monie"
#     # Z < br / > @Z
#     corrected = TextBlob(comment).correct().__str__()
#     # print("corrected : ", corrected)
#     map = comment_nouns(corrected)
#
#     polarity = relevance_check(map)
#     # print("polarity", polarity)
    ######################################################################
