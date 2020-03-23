import wikipedia
import noun_extraction
from gensim import corpora, models
from nltk.tokenize import sent_tokenize, word_tokenize
# wikipedia.set_lang("en")
#
# movie = wikipedia.page("Film")
trailer = wikipedia.page("Trailer promotion")
#
# print(trailer.content)
# wiki_nouns = noun_extraction.extract_nouns(trailer.content)
# print(wiki_nouns)
list_of_tokenss = sent_tokenize(trailer.content)

list_of_list_of_tokens = []
for sent in list_of_tokenss:
    list_of_list_of_tokens.append(word_tokenize(sent))

dictionary_LDA = corpora.Dictionary(list_of_list_of_tokens)
dictionary_LDA.filter_extremes(no_below=3)
corpus = [dictionary_LDA.doc2bow(list_of_tokens) for list_of_tokens in list_of_list_of_tokens]
print(corpus)
# num_topics = 20
# %time lda_model = models.LdaModel(corpus, num_topics=num_topics, \
#                                   id2word=dictionary_LDA, \
#                                   passes=4, alpha=[0.01]*num_topics, \
#                                   eta=[0.01]*len(dictionary_LDA.keys()))

