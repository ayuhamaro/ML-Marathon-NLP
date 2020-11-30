

#isnumeric(), isdigit(), isdecimal() 各有幾個
test_string = ['5.9', '30', '½', '³', '⑬']


def spam(s, isnumeric_count, isdigit_count, isdecimal_count):
    for attr in ['isnumeric', 'isdecimal', 'isdigit']:
        if attr == 'isnumeric':
            if getattr(s, attr)():
                isnumeric_count += 1
        elif attr == 'isdecimal':
            if getattr(s, attr)():
                isdecimal_count += 1
        elif attr == 'isdigit':
            if getattr(s, attr)():
                isdigit_count += 1
    return isnumeric_count, isdigit_count, isdecimal_count


isnumeric_count = 0
isdigit_count = 0
isdecimal_count = 0

for string_item in test_string:
    isnumeric_count, isdigit_count, isdecimal_count = spam(string_item, isnumeric_count, isdigit_count, isdecimal_count)

print('isnumeric_count: {}'.format(isnumeric_count))
print('isdigit_count: {}'.format(isdigit_count))
print('isdecimal_count: {}'.format(isdecimal_count))


#運用formatting 技巧 output
accuracy = 98.129393
recall = 94.879583
precision = 96.294821

print('Accuracy: {:.2f}%, Recall: {:.2f}%, Precision: {:.2f}%'.format(accuracy, recall, precision))

accuracy = 0.98129393
recall = 0.94879583
precision = 0.96294821

print('Accuracy: {:.2%}, Recall: {:.2%}, Precision: {:.2%}'.format(accuracy, recall, precision))


#依照只是轉換number output format
number = 3.1415926

print('{:.2e}'.format(number))
print('{:.2%}'.format(number))
print('{:0<10f}'.format(number))