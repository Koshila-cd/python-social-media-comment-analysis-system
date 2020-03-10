from owlready2 import *
import pandas as pd
import noun_extraction

onto = get_ontology("/data")
mg = pd.read_csv('data/Movie-genres.csv', index_col=0)
mn = pd.read_csv('data/Movie-names.csv', index_col=0)
ms = pd.read_csv('data/Movie-stars.csv', index_col=0)
md = pd.read_csv('data/Movie-directors.csv', index_col=0)
mr = pd.read_csv('data/Movie-reviews.csv', index_col=0)
msn = pd.read_csv('data/Movie-stage-names.csv', index_col=0)
ma = pd.read_csv('data/Movie-awards.csv', index_col=0)

# Movie Names
class MovieNames(Thing):
    namespace = onto


for label, row in mn.iterrows():
    MovieNames(label)


# Movie Keywords
class MovieKeywords(Thing):
    namespace = onto


for label, row in mr.iterrows():
    nouns = noun_extraction.extract_nouns(label)
    for n in nouns:
        MovieKeywords(n[0])


# Movie Awards
class MovieAwards(Thing):
    namespace = onto


for label, row in ma.iterrows():
    MovieAwards(label)


# Movie Stars
class MovieStars(Thing):
    namespace = onto


for label, row in ms.iterrows():
    MovieStars(label)


# Movie Directors
class MovieDirectors(Thing):
    namespace = onto


for label, row in md.iterrows():
    MovieDirectors(label)


# Movie Genres
class MovieGenres(Thing):
    namespace = onto


for label, row in mg.iterrows():
    MovieGenres(label)


# Movie Character Names
class MovieCharacterNames(Thing):
    namespace = onto


# Movie Stage Names
class MovieStageNames(Thing):
    namespace = onto


for label, row in msn.iterrows():
    MovieStageNames(label)

# onto.save(file="movie.owl", format="rdfxml")

# print(list(onto.classes()))
# g = 0
# for i in MovieKeywords.instances():
#     print(i)
#     print(g + 1)
#     g = g + 1