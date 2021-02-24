import json
import re
from collections import Counter, namedtuple

documents = []


def ngram(documents, N=2):
    # 建立儲存預測字, 所有ngram詞頻字典, 所有字詞(分母)
    ngram_prediction = dict()
    total_grams = list()
    words = list()
    Word = namedtuple('Word', ['word', 'prob'])  # 使用namedtuple來儲存預測字詞與對應機率

    for doc in documents:
        # 在每個文章加上起始(<start>)與結束符號(<end>)
        split_words = ['<s>'] + list(doc) + ['</s>']
        # 計算分子
        [total_grams.append(tuple(split_words[i:i+N])) for i in range(len(split_words)-N+1)]
        # 計算分母
        [words.append(tuple(split_words[i:i+N-1])) for i in range(len(split_words)-N+2)]

    # 計算分子詞頻
    total_word_counter = Counter(total_grams)
    # 計算分母詞頻
    word_counter = Counter(words)
    # 計算所有N-gram預測字詞的機率
    for key in total_word_counter:
        word = ''.join(key[:N-1])
        if word not in ngram_prediction:
            ngram_prediction.update({word: set()})

        next_word_prob = total_word_counter[key] / word_counter[key[:N-1]]

        w = Word(key[-1], f'{next_word_prob}')
        ngram_prediction[word].add(w)

    return ngram_prediction


with open('./WebNews.json', 'r', encoding='utf-8') as f:
    news_data = json.loads(f.read())
    corpus_list = list(d['detailcontent'] for d in news_data)
    corpus_list = list(''.join(re.findall(r'^<.*?>$|[\u4E00-\u9FA50-9]', article)) for article in corpus_list)

four_gram_pred = ngram(corpus_list, 4)

text = '鄭文燦'
next_words = four_gram_pred[text]
next_words = sorted(next_words, key=lambda x: x[1], reverse=True)
for next_word in next_words:
    print('next word: {}, probability: {}'.format(next_word.word, next_word.prob))
