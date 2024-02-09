morse= {
 'A': '.-', 'B': '-...', 'C': '-.-.',
 'D': '-..', 'E': '.', 'F': '..-.',
 'G': '--.', 'H': '....', 'I': '..',
 'J': '.---', 'K': '-.-', 'L': '.-..',
 'M': '--', 'N': '-.', 'O': '---',
 'P': '.--.', 'Q': '--.-', 'R': '.-.',
 'S': '...', 'T': '-', 'U': '..-',
 'V': '...-', 'W': '.--', 'X': '-..-',
 'Y': '-.--', 'Z': '--..', '1': '.----',
 '2': '..---', '3': '...--', '4': '....-',
 '5': '.....', '6': '-....', '7': '--...',
 '8': '---..', '9': '----.', '0': '-----',
 '.': '.-.-.-', ',': '--..--', ':': '---...',
 ';': '-.-.-.', '?': '..--..', '!': '-.-.--',
 '"': '.-..-.', "'": '.----.', '+': '.-.-.',
 '-': '-....-', '/': '-..-.', '=': '-...-',
 '_': '..--.-', '$': '...-..-', '@': '.--.-.',
 '&': '.-...', '(': '-.--.', ')': '-.--.-'
}

word = input('Enter a word: ').upper()
while word.find(' ') != -1:
    word = input('You have enter an invalid symbol ' '\nWrite a word without spaces: ')
for letter in word:
    print(morse[letter], end=' ')