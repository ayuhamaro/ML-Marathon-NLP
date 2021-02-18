import numpy as np
from ckiptagger import WS, POS, NER, construct_dictionary

sentence_list = [
    "傅達仁今將執行安樂死，卻突然爆出自己20年前遭緯來體育台封殺，他不懂自己哪裡得罪到電視台。",
    "美國參議院針對今天總統布什所提名的勞工部長趙小蘭展開認可聽證會，預料她將會很順利通過參議院支持，成為該國有史以來第一位的華裔女性內閣成員。",
    "",
    "土地公有政策?？還是土地婆有政策。.",
    "… 你確定嗎… 不要再騙了……",
    "最多容納59,000個人,或5.9萬人,再多就不行了.這是環評的結論.",
    "科長說:1,坪數對人數為1:3。2,可以再增加。",
]

word_to_weight = {
    "年前": 1
}
dictionary1 = construct_dictionary(word_to_weight)

ws = WS("./data") #建構斷詞

word_sentence_list = ws(
    sentence_list,
    sentence_segmentation = True, # To consider delimiters
    segment_delimiter_set = {",", "。", ":", "?", "!", ";"},
    coerce_dictionary = dictionary1) # This is the defualt set of delimiters
print(word_sentence_list)


pos = POS("./data")

pos_sentence_list = pos(word_sentence_list)
print(pos_sentence_list)


ner = NER("./data")

entity_sentence_list = ner(word_sentence_list, pos_sentence_list)
print(entity_sentence_list)


def combine_wandp(word_s, word_p):
    assert len(word_s) == len(word_p)
    result = ''
    for j, word in enumerate(word_s):
        result += '%s(%s)　'%(word, word_p[j])
    return result


for i, sentence in enumerate(sentence_list):
    print(f'Input sentence: \n {sentence}')
    print('\n')

    print(f'Segmentation with PoS: \n')
    print(combine_wandp(word_sentence_list[i], pos_sentence_list[i]))

    print('\n')
    print('Named Entity Recognition:')
    for n in sorted(entity_sentence_list[i]):
        print(n)
    print('\n')
