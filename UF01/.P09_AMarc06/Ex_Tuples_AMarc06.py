import random as ran

menu = (
    'Character Creation',
    'Attribute Modification',
    'Adventurer Group',
    'Search in the Group',
    'Group Statistics',
    'Sort by Level',
    'Simulated Combat',
    'Heal all the characters',
    'Return to your silly human world',
)
functions = (
    'characterCreation()',
    'attributeModification()',
    'adventurerGroup()',
    'findOnGroup()',
    'groupStatics()',
    'levelSort()',
    'combatSimulation()',
    'heallCharacters()',
)
race = (
    'Elf',
    'Giant',
    'Dwarf',
    'Human',
    'God',
    'Demon',
    'Angel',
    'Orc',
)
rol = (
    'Wizard',
    'Warrior',
    'Healer',
    'Seller',
    'Adventurer',
    'Archer',
)
modifyAtributes = (
    'Increase character level',
    'Change class',
)
places = (
    'clif',
    'combat arena',
    'death plain',
    'old dungeon',
)

characters = [('Tor', 0, 0, 8, 100), ('Ra', 2, 4, 10, 100)]
group = []

def characterCreation():
    global characters
    print('\nIt looks like you want to add a character.\nTo do this you will have to go '
          'to the adventurer registration building.\nSee you son in our tavern.')
    print('\nHi traveler, welcome to the adventurer register I\'m Alis, and'
          ' I\'m going to gide you through the process of creating a new character.')
    name = input('What\'s your character\'s name?\n> ')
    print(f'Magnific, nice to meet you {name}')
    print('To which class deos your character belong?')
    clas = selection(rol)
    print('\nTo which race your character belong to?')
    rac = selection(race)
    print(f'\nThat\'s awesome, its the first time in the las 100 years that I meet a {race[rac]} that is a {rol[clas]}.')
    level = ran.randint(1, 10)
    print(f'Our magical system now will determine your character level, lets see what\'s the result is.\n'
          f'According to the scan your level is {level}')
    print(f'Lets recap, your name is {name}, you are a {rol[clas]} from the village of the {race[rac]}s, '
          f'and level {level}')
    print(f'\nCongratulations {name} the {rol[clas]} your character has ben added to our system, '
          f'we hope to se you again hear soon.')
    characters.append((name, clas, rac, level, 100))
    print('And remember the tavern is a grate place to gain information about what to do next.\n'
          '\nHi traveler, long time not seeing you.\nWhat brings you here today?\n')
    

def selection(vari):
    print('\nSelect:')
    for option in vari:
        if type(option) == tuple:
            print(f'{vari.index(option) + 1}: {option[0]}')
        else:
            print(f'{vari.index(option) + 1}: {option}')
    try:
        option = int(input('> '))
        if option in range(len(vari)+1):
            return option-1
        else:
            print(f'ERROR: Invalid option. Enter a integer in the range 1 to {len(vari)}')
            selection()
    except ValueError:
        print('ERROR: Invalid input type. Enter a integer')
        selection()


def atributeModificationSelection(cha):
    print('\nSelect:')
    for option in modifyAtributes:
        print(f'{modifyAtributes.index(option) + 1}: {option}')
    try:
        option = int(input('> '))
        if option in range(len(modifyAtributes)+1):
            a, b, c, d = characters[cha]
            characters.pop(cha)
            match option:
                case 1:
                    d += 1
                case 2:
                    b = selection(rol)
            characters.insert(cha, (a, b, c, d))
            num = findNameGroup(a)
            group.pop(num)
            characters.insert(num, (a, b, c, d))
            print(f'{a}, now you are a {rol[b]} from the kingdom of {race[c]} and a power of level {d}')
        else:
            print(f'ERROR: Invalid option. Enter a integer in the range 1 to {len(menu)}')
            atributeModificationSelection()
    except ValueError:
        print('ERROR: Invalid input type. Enter a integer')
        atributeModificationSelection()


def attributeModification():
    print('\nSo you want to modify soe ones attributes, I can do this for you.\n'
          'Please, who\'s attributes do you want to change?')
    cha = selection(characters)
    print(f'So you wan to modify som attributes of {characters[cha][0]}.')
    print('What would you like to modify?')
    atributeModificationSelection(cha)
    print(f'Well, we have finished modifying the attributes of {characters[cha][0]}.\n'
          f'What would you like to do next?')


def numSel(max):
    try:
        option = int(input('> '))
        if option <= max:
            return option
        else:
            print(f'ERROR: Invalid option. Enter a integer in the range 1 to {max}')
            numSel(max)
    except ValueError:
        print('ERROR: Invalid input type. Enter a integer')
        numSel(max)


def adventurerGroup():
    chara = characters
    for ch in chara:
        if ch in group:
            chara.remove(ch)
    print(f'\nIt locs like you want to form a group.\n'
          f'To do this you must go to the adventurers hall\n\n'
          f'Welcome to the adventurers hall, I\'m Jinx and im going to guide you throw this proces.\n')
    if len(characters) == 0:
        print('It looks like you don\'t have enough friends to make a group.\n'
              'The minimum number is 1.\n'
              'If you wan to add characters you can go to the tavern and ask Ozgar.\n'
              'See you here son.')
    else:
        print('So traveler, how many friends would you like to add to yor group?\n'
              'Remember you can\'t add more friends than characters you have created.')
        num = numSel(len(chara))
        print('Now we can start adding your friends to your group')
        for i in range(num):
            cha = selection(chara)
            group.append(chara[cha])
            chara.remove(chara[cha])
        print('Your friends have been added to your group.\n'
              'Here you have a summary of your actual group.\n'
              '\nIn your group we cand find:')
        for i in group:
            print(f'{i[0]} the {race[i[2]]} {rol[i[1]]} of level {i[3]}')
        print('\nReturn here when you find new friends to add to your group traveler.\n'
              'Now you can go rest to the tavern.')

def findNameGroup(nam):
    if nam.lower() in [i[0].lower() for i in group]:
        return [i[0].lower() for i in group].index(nam.lower())
    else:
        return -1

def findOnGroup():
    print('Well, it seams you don\'t know your friends well.\n'
          'But dont worry, i can help you findig the persons in your group.'
          'You only have to give my their name.')
    nam = input('Which is it\'s name of your friend?\n\n> ')
    inde = findNameGroup(nam)
    if inde != -1:
        print(f'Well it sems that your friend {group[inde][0]} is a {race[group[inde][2]]} '
              f'of the ordr of the {rol[group[inde][1]]}s and level {group[inde][3]}')
    else:
        print('I\'t seams you don\'t know your fellows names.\n'
              'You are one of the worst team leaders I have ever seen.')
        if ran.randint(1, 10) == 10:
            print('You can make us a favor and go find a dragon to kill you')
    print('What else can I do for you?')


def groupStatics():
    suma = 0
    amount = 0
    print('\nI can do this for you, jast give me a second.')
    for i in group:
        suma += i[3]
        amount += 1
    print(f'The average level of your party is {suma/amount}')
    if ran.randint(1, 10) == 10:
        print('You can make us a favor and go find a dragon to kill you')
    print(f'What else can i do for you?')


def combatSimulation():
    turn = True
    a = 0
    b = 0
    charac = characters.copy()
    round = 0
    for ch in charac:
        if ch[4] == 0:
            charac.remove(ch)
    print(f'\nYou wan to perform a combat?\n'
          f'You have guts traveler. To do so you must go to the {places[ran.randint(0, len(places)-1)]}.\n'
          f'Be careful wile traveling to the combat location, you might find some dragons.\n'
          f'Se you here soon with a victory.\n\n'
          f'You come from far away just for combating?'
          f'That\'s grate.')
    if len(characters) < 2:
        print('But it seams theres no enough people to perform a combat.\n'
              'I suggest you to return to the village and find some new adventurers in Ozgar tavern.\n'
              'Return when you are redy.')
    else:
        if len(charac) < 2:
            print('There are not enough healthy persons, please go to the '
                  'tavern and take a rest before tacking a combat.')
        else:
            while a == b:
                a = ran.randint(0, len(charac)-1)
                b = ran.randint(0, len(charac)-1)
            indexes = characters.index(charac[a]), characters.index(charac[b])
            a = list(charac[a])
            b = list(charac[b])
            print(f'It seams the combat will be between '
                  f'{a[0]} the {rol[a[1]]} {race[a[2]]}  '
                  f'and {b[0]} the {rol[b[1]]} {race[b[2]]}\n\n'
                  f'The rules are simple.\n'
                  f'The first one to loss all the health points is the losser.\n\n'
                  f'Lets start this awsome combat!!!')
            while bool(a[4] and b[4]):
                round += 1
                print(f'\nRound number {round}.')
                damage = ran.randint(1, 100)
                if turn:
                    if damage == 11 and a[4] < 120:
                        healing = ran.randint(1, 10)
                        if rol.index('Healer') == a[1]:
                            healing *= 1+0.1*a[3]
                        print(f'{a[0]} heal himself and gain {healing} healing points.')
                        a[4] += healing
                    else:
                        damage = ran.randint(1, 10)
                        if rol.index('Healer') == a[1]:
                            damage *= 0.1*a[3]
                        else:
                            damage *= 1+0.1*a[3]
                        print(f'{a[0]} attack {b[0]} and make a total damage of {damage} healing points.')
                        b[4] -= damage
                    turn = False
                else:
                    healing = ran.randint(1, 10)
                    if rol.index('Healer') == b[1] and b[4] < 120:
                        healing *= 1 + 0.1 * b[3]
                        print(f'{b[0]} heal himself and gain {healing} healing points.')
                        b[4] += healing
                    else:
                        damage = ran.randint(1, 10)
                        if rol.index('Healer') == b[1]:
                            damage *= 0.1 * b[3]
                        else:
                            damage *= 1 + 0.1 * b[3]
                        print(f'{b[0]} attack {a[0]} and make a total damage of {damage} healing points.')
                        a[4] -= damage
                    turn = True
                a[4] = 0 if a[4] < 0 else a[4]
                b[4] = 0 if b[4] < 0 else b[4]
            print(f'\nThe winner of the combat is {a[0] if a[4] > 0 else b[0]}')
            print(f'You can now go to the tavern to have a beverage and rest.')
            for i in reversed(sorted(list(indexes))):
                characters.pop(i)
            characters.append(tuple(a))
            characters.append(tuple(b))


def levelSort():
    print('Ok, Now I\'m going to show you the members of your group ordered by their level.')
    for i in sorted(group, key=lambda x: x[3]):
        print(f'{i[0]} the {race[i[2]]} {rol[i[1]]} of level {i[3]}')
    if ran.randint(1, 10) == 10:
        print('Will you still bothering me?\nGo do something somewhere else.')
    print('Is there any ting else i can do for you?')


def optionSelection():
    print('\nSelect:')
    for option in menu:
        print(f'{menu.index(option) + 1}: {option}')
    try:
        option = int(input('> '))
        if option in range(len(menu)+1):
            if option == len(menu):
                return option
            else:
                eval(functions[option-1])
        else:
            print(f'ERROR: Invalid option. Enter a integer in the range 1 to {len(menu)}')
            optionSelection()
    except ValueError:
        print('ERROR: Invalid input type. Enter a integer')
        optionSelection()


def heallCharacters():
    print('\nYou traveler need your friends to rest a little to heal their wounds.\n'
          'After a little of rest and drinking mead everyone has gained all their health points again.')
    for chara in characters:
        if chara[4] < 100:
            characters.remove(chara)
            chara = list(chara)
            chara[4] = 100
            characters.append(tuple(chara))


op = 0
print('\nWelcome to the tavern of Ozgar traveler.\n'
      'I\'m Onis the innkeeper what would you like to do today?')
op = optionSelection()
while op != len(menu):
    op = optionSelection()
print('\nHave a nice trip traveler we hope to see you here son.\n'
      'And remember in your puny world there are not dragons and magical creatures.\n'
      'If some time you feel magic is missing in your live,'
      ' you can always return here.')
