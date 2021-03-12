import pandas as pd
import nltk
#nltk.download()
import numpy as np

dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)
corpus = dataset['Review'].values

whole_words = []
for sentence in corpus:
    tokenized_sentence = nltk.word_tokenize(sentence)
    for word in tokenized_sentence:
        whole_words.append(word)

whole_words = set(whole_words)
print('共有{}個單字'.format(len(whole_words)))

word_index = {}
index_word = {}
n = 0
for word in whole_words:
    word_index[word] = n
    index_word[n] = word
    n+=1

print(word_index)
print(index_word)


def _get_bag_of_words_vector(sentence, word_index_dic, whole_words):
    sentence = sentence
    vector = np.zeros(len(whole_words))
    for word in nltk.word_tokenize(sentence):
        if word in whole_words:
            vector[word_index[word]]+=1
    return vector


vector = _get_bag_of_words_vector('Wow... Loved this place.', word_index, whole_words)
print(vector)

