word = input("Enter a word to be guessed: ")
answer = '_' * len(word)
temp = word
errors = 0

print(answer)

while answer != word and errors < 5:
    guess = input("Enter a letter: ")
    if guess not in word:
        errors += 1
        print(f'The leter {guess} is not in the word')
    else:
        for index, letter in enumerate(temp):
            if letter == guess:
                answer = answer[:index] + guess + answer[index+1:]
                temp = temp[:index] + guess + temp[index+1:]

    print(answer)
    print(f'You have made {errors}')

if errors < 5 :
    print("Congratulations! You have won the game!!!")
else:
    print("You have lost :(")