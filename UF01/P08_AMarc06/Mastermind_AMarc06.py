import random as r
digits = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

print("Benvingut/a a l'Mastermind!\nHas de endevinar un nombre de 4 xifres diferents")
code = digits[r.randrange(0, 10)]
while len(code) < 4:
    num = digits[r.randrange(0, 10)]
    if num not in code:
        code += num
guess = ''
while len(guess) != 4 or not guess.isnumeric():
    guess = input("¿Que codi proposes ?: ")
while guess != code:
    match = 0
    near = 0
    for i in guess:
        if i in code and guess.index(i) == code.index(i):
            match += 1
        elif i in code and guess.index(i) != code.index(i):
            near += 1
    print(f'La teva proposta ({guess}) té {match} encerts i {near} coincidències.')
    guess = input("Proposa un altre codi: ")
    while len(guess) != 4 or not guess.isnumeric():
        guess = input("Proposa un altre codi: ")
print('Felicitats, has endevinat el codi!')
print(code)
