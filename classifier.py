import main
from nltk.corpus import movie_reviews


description_nouns = []
comment_nouns = []

description_nouns = main.youtube_nouns()
comment_nouns = main.comment_nouns()


if __name__ == '__main__':
    # print("start")
    print("description_nouns", description_nouns)
    print("comment_nouns", comment_nouns)
    # print("end")



