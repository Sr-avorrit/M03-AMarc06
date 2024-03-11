
eventos = [
    ["Boda Roja", "Riverrun", "300 AC", ["Jon Snow", "Daenerys Targaryen"]],
]

casas = [
    ["Stark", "Winter is Coming", ["Jon Snovv"]],
    ["Targaryen", "Fire and Blood", ["Daenerys Targaryen"]],
]
personajes = [
    ["Jon Snow", "Stark", 30],
    [" Daenerys Targaryen", "Targaryen", 25],
]

print('''                                                                                                       
┓ ┏•         •   ┏┓     •    
┃┃┃┓┏┓╋┏┓┏┓  ┓┏  ┃ ┏┓┏┳┓┓┏┓┏┓
┗┻┛┗┛┗┗┗ ┛   ┗┛  ┗┛┗┛┛┗┗┗┛┗┗┫
                            ┛''')
op = 0
while op != 7:
    op = 0
    while op not in range(1, 8):
        print('\nMenu:\n'
              '1. Afegir Personatges.\n'
              '2. Afegir cases.\n'
              '3. Afegir esdeveniment.\n'
              '4. Associar personatges a cases i viceversa.\n'
              '5. Registre de Participants a Esdeveniments.\n'
              '6. Visualització d\'informació\n'
              '7. Sortir')
        op = int(input('\nSeleciona una opcio: '))
        if op not in range(1, 8):
            print('\nERROR: Opcio Invalida\n')
    match op:
        case 1:
            personajes.append([input('Nom del personatge: '), '', int(input('Edad del personatge: '))])
        case 2:
            casas.append([input('Nom de la Casa: '), input('Lema de la Casa: '), []])
        case 3:
            eventos.append([input('Nom Esdeveniment: '), input('Lloc Esdeveniment: '), input('Data Esdeveniment: '), []])
        case 4:
            nom = input('Nom Personatge: ')
            casa = input('Nom Casa: ')
            if nom not in [x[0] for x in personajes] or casa not in [x[0] for x in casas]:
                print('ERROR: El personatge i/o la casa introduida no existeix.')
            else:
                if input(f'Estas segur que vols asociar el personatge a la casa (y/n): ').lower() == 'y':
                    for i in range(len(personajes)):
                        if personajes[i][0] == nom:
                            personajes[i][1] = casa
                    for i in range(len(casas)):
                        if casas[i][0] == casa:
                            casas[i][2].append(nom)
                    print('La asociacio s\'ha realitzat amb exit')
        case 5:
            nom = input('Nom Personatge: ')
            esdev = input('Nom Casa: ')
            if nom not in [x[0] for x in personajes] or esdev not in [x[0] for x in eventos]:
                print('ERROR: El personatge i/o l\'esdeveniment introduit no existeix.')
            else:
                for i in range(len(eventos)):
                    if eventos[i][0] == esdev:
                        eventos[i][3].append(nom)
                    print('e el personatge ha estat registrat com a participant a l\'esdeveniment.')
        case 6:
            match = input('Cerca: ')
            found = [x for x in personajes if match.lower() in x[0].lower()]
            for i in found:
                print(f'Nom: {i[0]}, Casa: {i[1]}, Edad: {i[2]}')




def descompte(preu, per):
    return preu*(1-(per/100))


# print(descompte(int(input('Insert price: ')), int(input('Insert Percentage: '))))


def llegeix0a10():
    a = int(input('Enter a number between 0 and 10: '))
    if a not in range(0, 11):
        return llegeix0a10()
    else:
        return a


# print(llegeix0a10())
