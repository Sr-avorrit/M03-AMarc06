word = input("Enter a word to be guessed: ")
answer = '_' * len(word)
temp = word

print(answer)

while answer != word:
    guess = input("Enter a letter: ")
    
    for index, letter in enumerate(temp):
        if letter == guess:
            answer = answer[:index] + guess + answer[index+1:]
            temp = temp[:index] + guess + temp[index+1:]

    print(answer)

print("Congratulations! You have won the game!!!")
