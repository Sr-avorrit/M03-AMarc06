play = 'y'
while play == 'y':
    word = input("Enter a word to be guessed: ").lower()
    answer = '_' * len(word)
    temp = word
    errors = 0

    print(answer)

    while answer != word and errors < 5:
        guess = input("Enter a letter: ").lower()
        if guess.lower() not in word:
            errors += 1
            print(f'The leter {guess} is not in the word')
        else:
            for index, letter in enumerate(temp):
                if letter == guess:
                    answer = answer[:index] + guess + answer[index+1:]
                    temp = temp[:index] + guess + temp[index+1:]

        print(answer)
        print(f'You have made {errors} errors')
        if errors == 1:
            print(' O')
        elif errors == 2:
            print(' O')
            print(' |')
        elif errors == 3:
            print(' O')
            print('/|')
        elif errors == 4:
            print(' O')
            print('/|\\')
        elif errors == 5:
            print(' O')
            print('/|\\')
            print('/ \\')


    if errors < 5 :
        print("Congratulations! You have won the game!!!")
    else:
        print("You have lost :(")
    play = ''
    while play != 'y' and play != 'n':
        play = input("do you want to play again? (y/n): ").lower()