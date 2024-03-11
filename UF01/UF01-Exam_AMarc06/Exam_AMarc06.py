import random as ran

ubicacions= {
   'Bosc Korok': {
       'objectes': ['espasa reial', 'arc korok', 'boomerang', 'corda'],
       'menjars': ['poció de vida', 'bolets', 'fruita del bosc', 'poma'],
       'enemics': {'keese':30, 'bokoblin':15},
   },
   'Castell de Hyrule': {
       'objectes': ['espasa reial', 'ballesta reial', 'clau'],
       'menjars': ['peix del llac', 'poció real', 'poma', 'bolets'],
       'enemics': {'guardià':5, 'moblin':10, 'keese':30},
   },
   'Llac Hylia': {
       'objectes': ['escut', 'clau', 'arc reial'],
       'menjars': ['poció de vida', 'peix del llac','poma'],
       'enemics': {'lizalfos':15, 'hinox':2},
   },
   'Poblat Orni': {
       'objectes': ['espasa Orni', 'corda'],
       'menjars': ['fruita del bosc','bolets', 'poma'],
       'enemics': {'keese':25, 'bokoblin':20},
   },
   'Ciutat Gerudo': {
       'objectes': ['daga Gerudo', 'boomerang'],
       'menjars': ['poció de vida', 'plàtans', 'poma'],
       'enemics': {'lizalfos':18, 'guardià':2, 'moldora':2},
   },
}

menjars = {
   'poció de vida': 30,
   'fruita del bosc': 15,
   'plàtans': 10,
   'peix del llac': 25,
   'poció real': 40,
   'poma': 5,
   'bolets':20
}

enemics={
   'bokoblin': -30,
   'moblin': -20,
   'guardià': -60,
   'keese': -10,
   'lizalfos': -20,
   'hinox': -40,
   'moldora': -50
}
objectes={
   'daga':'arma',
   'boomerang':'arma',
   'espasa':'arma',
   'escut':'protecció',
   'clau':'desbloquejar',
   'corda':'escalar',
   'arc':'arma',
}

invenari = {}

vida = 100
op = 0

while vida > 0 and op != len(ubicacions.keys())+1:
    while op not in range(1, len(list(ubicacions.keys()))+2):
        print('\nOn vols anar?')
        for i in ubicacions.keys():
            print(f'{list(ubicacions.keys()).index(i)+1}. {i}')
        print(f'{len(ubicacions.keys())+1}. Sortir')
        op = int(input('\nSeleciona ubicació: '))
    if op != len(ubicacions.keys())+1:
        ub = list(ubicacions.keys())[op-1]
        obj = ubicacions[ub]['objectes'][ran.randint(0, len(ubicacions[ub]['objectes'])-1)]
        men = ubicacions[ub]['menjars'][ran.randint(0, len(ubicacions[ub]['menjars'])-1)]
        ene = ubicacions[ub]['enemics']
        ene = list(ene.keys())[ran.randint(0, len(list(ene.keys()))-1)]
        print(f'Link ha trobat un {obj} (objecte), un {men} (menjar) i un {ene} (enemic).\n')
        if len(invenari) == 0:
            invenari['ubicacions'] = {ub: 1}
            invenari['objectes'] = {obj: 1}
            invenari['menjars'] = {men: 1}
            invenari['enemics'] = {ene: 1}
        else:
            if ub not in invenari['ubicacions'].keys():
                invenari['ubicacions'][ub] = 1
            else:
                invenari['ubicacions'][ub] += 1
            if obj not in invenari['objectes'].keys():
                invenari['objectes'][obj] = 1
            else:
                invenari['objectes'][obj] += 1
            if obj not in invenari['menjars'].keys():
                invenari['menjars'][men] = 1
            else:
                invenari['menjars'][men] += 1
            if obj not in invenari['menjars'].keys():
                invenari['enemics'][ene] = 1
            else:
                invenari['enemics'][ene] += 1
        select = (input('Que vols escollir el menjar(m) o el objecte(o): '))
        while select.lower() not in ['m', 'o']:
            select = (input('Que vols escollir el menjar(m) o el objecte(o): '))
        if select.lower() == 'm':
            vida += menjars[men]
        else:
            if objectes[obj.split(' ')[0]] != 'arma':
                vida += enemics[ene]
            else:
                ubicacions[ub]['enemics'][ene] -= 1
        op = 0
print('\n'+'=' * 30 + 'INVENTARI' + '=' * 30)
if len(invenari) != 0:
    print('-UBICACIONS: ', end='')
    for i in invenari['ubicacions'].items():
        print(f'{i[0]} ({i[1]})', end=', ')
    print('\n-MENJARS: ', end='')
    for i in invenari['menjars'].items():
        print(f'{i[0]} ({i[1]})', end=', ')
    print('\n-ENEMICS: ', end='')
    for i in invenari['enemics'].items():
        print(f'{i[0]} ({i[1]})', end=', ')
    print('\n-OBJECTES: ', end='')
    for i in invenari['objectes'].items():
        print(f'{i[0]} ({i[1]})', end=', ')
    print('\n' + '=' * len('=' * 30 + 'INVENTARI' + '=' * 30))
else:
    print('-UBICACIONS: ')
    print('-MENJARS: ')
    print('-ENEMICS: ')
    print('-OBJECTES: ')
    print(''+'='*len('='*30+'INVENTARI'+'='*30))
print('\n'+'-'*16+' UBICACIONS '+'-'*16)
for i in ubicacions:
    print(f'{i.upper():20}{'Enemics':14}{'Quantitat':>10}')
    for j in ubicacions[i]['enemics']:
        print(f'{'':20}{j:14}{ubicacions[i]['enemics'][j]:>10}')
    print()
print('-'*len('-'*16+' UBICACIONS '+'-'*16))
