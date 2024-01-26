dict = {}
sentence = input('Enter a sentence: ').lower()
words = sentence.split(' ')
dict = dict.fromkeys(words, 0)
for word in words:
    dict[word] += 1
print(dict)