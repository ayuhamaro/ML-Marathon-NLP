import jieba
import jieba.posseg as pseg

jieba.set_dictionary('課程練習/dict.txt')

new_words = '教練陪跑計劃 2 n\n百日馬拉松 2 n\n機器學習 2 n\n人工智能 2 n\n翻轉 2 v'
with open('adding.txt', 'w', encoding='utf8') as file:
    file.write(new_words)

jieba.load_userdict('adding.txt')

sentence = '''這是敘述近年來，AI 應用已無所不在，不論在新創或是傳產領域，都可能透過機器學習解決過去難以解決的問題。但目前台灣企業在 AI 導入的腳步仍然緩慢，除了人才嚴重短缺，教育資源無法即時跟上產業變異也是原因之一。因此，我們發起了「 機器學習 百日馬拉松 」教練陪跑計劃，翻轉傳統上課模式，以自主練習為主，幫助你獲得最大學習成效，搶先一步進入 AI 人工智能領域。'''
print("output 精確模式: {}".format('|'.join(jieba.cut(sentence, cut_all=False, HMM=False))))

words = pseg.cut(sentence,)
for word, flag in words:
    print(word, flag)