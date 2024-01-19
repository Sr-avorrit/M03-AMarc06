word = input("Enter a word: ")
leters = ''

for i in word:
    if i not in leters:
        leters += i
for leter in leters:
    print(f'the leter {leter} apears {word.lower().count(leter)} times')