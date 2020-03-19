import noun_extraction
from owlready2 import *
from nltk.corpus import wordnet
import sentiment_analysis

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

comment = "This Movie is awesome. But I don't like the last part"
# comment = "no no no no"

star = "*"


def youtube_nouns():
    nouns = noun_extraction.extract_nouns(youTubeDescription)
    # Add the nouns extracted from the description into the Ontology
    for n in nouns:
        # onto.MovieKeywords(n[0])
        # onto.save(file="movie.owl", format="rdfxml")
        return nouns


def comment_nouns():  # words with missed spellings
    print("comment_nouns")
    noOfWords = len(comment.split())
    mapped = []
    nouns = noun_extraction.extract_nouns(comment)
    print(nouns)
    if noOfWords == 1:
        word = comment.split()
        word1 = star + word[0] + star
        if onto.search(iri=word1.casefold()):
            mapped.append(word[0].casefold())
            # print("direct map - single word")
        else:
            # Semantic mapping
            mapped.append(semantic_mapping(word1.casefold(), mapped))
    else:
        for n in nouns:
            noun = star + n[0] + star
            # Direct mapping with ontology created for searching for nouns extracted from the YouTube comment
            if onto.search(iri=noun.casefold()):
                mapped.append(n[0].casefold())
                # print("direct map - more words")
            else:
                # Semantic mapping
                mapped.append(semantic_mapping(n[0].casefold(), mapped))
    return mapped, nouns, comment


def semantic_mapping(word, mapped):
    synonyms = []

    # finding synonyms in wordnet
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            # setting synonyms found from wordnet to array
            synonyms.append(l.name())

    for synonym in set(synonyms):
        if onto.search(iri=synonym):
            mapped.append(synonym)
            print("semantic map: ", comment)
    # print("mapped: ", mapped)
    return mapped


def relevance_check(map):
    if len(map[0]) > 0:
        print("relevant")
        polarity = sentiment_analysis.analyze_sentiment(map[2])
    else:
        polarity = "None"
    return polarity

def toService():
    youtube_nouns()
    map = comment_nouns()
    polarity = relevance_check(map)
    return polarity


if __name__ == '__main__':
    youtube_nouns()
    map = comment_nouns()
    print("polarity: ", relevance_check(map))