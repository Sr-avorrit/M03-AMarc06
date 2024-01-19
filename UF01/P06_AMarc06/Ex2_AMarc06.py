res = 0
sentence = input("Enter a sentence: ")
for i in sentence.lower():
    if i == 'a':
        res += 1
print(f'The sentence has {res} leters a on it.')