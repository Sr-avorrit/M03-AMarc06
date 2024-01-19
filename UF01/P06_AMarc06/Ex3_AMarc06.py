res = 0
sentence = input("Enter a sentence: ")
for i in sentence.lower():
    if i != 'a' and i != 'e' and i != 'i' and i != 'o' and i != 'u' and i != ' ':
        res += 1
print(f'The sentence has {res} consonants a on it.')