import service

description_nouns = []
comment_nouns = []

description_nouns = service.youtube_nouns()
comment_nouns = service.comment_nouns()

print(description_nouns)


if __name__ == '__main__':
    print("start")
    print("description_nouns", description_nouns)
    print("comment_nouns", comment_nouns)
    print("end")



