text = input("Enter a text: ")
char_1 = input("Witch character would you like to replace: ")
char_2 = input(f'With which character do you want to replace the character {char_1}: ')

text = text.replace(char_1.lower(), char_2.lower()).replace(char_1.upper(), char_2.upper())

print(text)