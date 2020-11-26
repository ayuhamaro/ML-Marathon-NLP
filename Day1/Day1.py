import pandas as pd

#讀入所需文件
dataset = pd.read_csv(r'Restaurant_Reviews.tsv', sep='\t')
all_review = dataset['Review'].values
#print(all_review)


#計算有多少個句子是以 . 結尾
n = 0
for sentence in all_review:
    if sentence.endswith('.'):
        n += 1
#print('共有 {} 個句子是以 . 結尾'.format(n))


#將所有. 換成 ,
for sentence_number in range(len(all_review)):
    all_review[sentence_number] = all_review[sentence_number].replace('.', ',')
#print(all_review)


#將所有sentence 中的第一個 the 置換成 The
for sentence_number in range(len(all_review)):
    input_sentence = all_review[sentence_number]
    if 'the' in input_sentence:
        location = input_sentence.find('the')
        input_sentence = ''.join((input_sentence[:location],'T',input_sentence[location+1:]))
        all_review[sentence_number] = input_sentence
#print(all_review)


#將偶數句子全部轉換為大寫，基數句子全部轉換為小寫
for sentence_number in range(len(all_review)):
    if sentence_number % 2 == 0:
        all_review[sentence_number] = all_review[sentence_number].upper()
    else:
        all_review[sentence_number] = all_review[sentence_number].lower()
#print(all_review)


#將所有句子合併在一起，並以' / ' 為間隔
print('/'.join(all_review))