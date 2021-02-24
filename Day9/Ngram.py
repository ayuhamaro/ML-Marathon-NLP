import urllib, requests
import re
import random
import collections
from nltk import ngrams


books = {'Pride and Prejudice': '1342',
         'Huckleberry Fin': '76',
         'Sherlock Holmes': '1661'}

book = books['Pride and Prejudice']


url_template = f'https://www.gutenberg.org/cache/epub/{book}/pg{book}.txt'
response = requests.get(url_template)
txt = response.text

words = re.split('[^A-Za-z]+', txt.lower())
words = [x for x in words if x != ''] # 移除空字串


#使用NLTK API搭建Bigram
bigram_frequency = ngrams(words, n=4)

#使用collectins套件計算詞頻
bigram_frequency = collections.Counter(bigram_frequency)

print(bigram_frequency)