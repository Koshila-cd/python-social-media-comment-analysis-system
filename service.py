import noun_extraction
from owlready2 import *

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

comment = "This movie is awesome. But I don't like the last part"


def youtube_nouns():
    nouns = noun_extraction.extract_nouns(youTubeDescription)
    # Add the nouns extracted from the description into the Ontology
    # for n in nouns:
        # onto.MovieKeywords(n[0])
    # onto.save(file="movie.owl", format="rdfxml")
    return nouns

star = "*"
def comment_nouns():
    nouns = noun_extraction.extract_nouns(comment)
    for n in nouns:
        print(n[0])
        iri1 = star + n[0] + star
        # Direct mapping with ontology created for searching for nouns extracted from the YouTube comment
        if onto.search(iri = iri1):
            print("relevant")
    return nouns


if __name__ == '__main__':
    youtube_nouns()
    comment_nouns()
