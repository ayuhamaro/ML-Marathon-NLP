import numpy as np
import pandas as pd


# 為何需要使用馬可夫假設來簡化語言模型的計算?
# 如果不加以簡化，只能以句子或片語做比較，這樣會造成過擬合，需要非常大量的語料資料


words = ['i', 'want', 'to', 'eat', 'chinese', 'food', 'lunch', 'spend']
word_cnts = np.array([2533, 927, 2417, 746, 158, 1093, 341, 278]).reshape(1, -1)
df_word_cnts = pd.DataFrame(word_cnts, columns=words)
print(df_word_cnts)


bigram_word_cnts = [[5, 827, 0, 9, 0, 0, 0, 2], [2, 0, 608, 1, 6, 6, 5, 1], [2, 0, 4, 686, 2, 0, 6, 211],
                    [0, 0, 2, 0, 16, 2, 42, 0], [1, 0, 0, 0, 0, 82, 1, 0], [15, 0, 15, 0, 1, 4, 0, 0],
                    [2, 0, 0, 0, 0, 1, 0, 0], [1, 0, 1, 0, 0, 0, 0, 0]]

df_bigram_word_cnts = pd.DataFrame(bigram_word_cnts, columns=words, index=words)
print(df_bigram_word_cnts)


word_cnts_array = [2533, 927, 2417, 746, 158, 1093, 341, 278]

for i in range(len(bigram_word_cnts)):
    for j in range(len(bigram_word_cnts[i])):
        bigram_word_cnts[i][j] = round(bigram_word_cnts[i][j] / word_cnts_array[i], 6)

df_bigram_word_cnts = pd.DataFrame(bigram_word_cnts, columns=words, index=words)
print(df_bigram_word_cnts)


# 請根據已給的機率與所計算出的機率(df_bigram_prob), 試著判斷下列兩個句子哪個較為合理
# p(want|i) = 0.32649
# p(i|want) = 0.002157
# 因此 i want english food 較合理