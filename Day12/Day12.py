#!/usr/bin/env python
# coding: utf-8

# ## 作業目標：搭建一個bag of words模型

# ---

# In[7]:


import pandas as pd
import nltk

nltk.download('punkt')
# nltk.download()
import numpy as np

dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)
corpus = dataset['Review'].values

# ### 從文本中取出所有單字

# In[7]:


whole_words = []
for sentence in corpus:
    tokenized_sentence = nltk.word_tokenize(sentence)
    for word in tokenized_sentence:
        whole_words.append(word)

# ### 移除重複單字
whole_words = set(whole_words)

# In[12]:


print('共有{}個單字'.format(len(whole_words)))

# ### 建立字典使每一個單字有對應數值

# In[18]:


word_index = {}
index_word = {}
n = 0
for word in whole_words:
    """自行填入"""
    print(word_index(word))
# In[10]:


print(word_index)

# In[11]:


print(index_word)


# ## 轉換句子為bag of words型式

# In[34]:


# def _get_bag_of_words_vector(sentence, word_index_dic, whole_words):
#     sentence = sentence
#     '''創建一個vector'''
#     for word in nltk.word_tokenize(sentence):
#         if word in whole_words:
#             '''自行填入'''
#     return vector


# In[35]:


# _get_bag_of_words_vector('Wow... Loved this place.', word_index, whole_words)

# In[ ]:




