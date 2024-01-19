import os
# Language code extracted from ISO 639-2/T for English and Catalan and ISO 639-1 for Spanish
eng = {
    '': {
        0: 'Enter the article code',
        1: 'The code must be formed by 3 numbers',
        2: 'The code must be unic',
        3: 'Enter a price for the product',
        4: 'Enter the amount of stock of the product',
        5: 'The stock must be a numerical value',
        6: 'ARTICLES LIST',
        7: {
            0: 'Ref. Num.',
            1: 'Name',
            2: 'Type',
            3: 'Material',
            4: 'Price',
            5: 'Stock',
            6: 'Position'
        },
        8: 'ARTICLE MODIFICATION',
        9: 'Which position product do you what to modify the stock',
        10: 'Stock modified!',
        11: 'You Must enter a numeric value',
        12: 'Value out of range',
        13: 'Value an code does not match',
        14: 'Product not found',
        15: 'Pres Enter to continue',
        16: 'FIND PRODUCT',
        17: 'ARTICLE'
    },

    'A': {
        'title': 'PRINCIPAL MENU',
        0: {
            'A': 'Add article to wherehouse',
            'B': 'List articles',
            'C': 'Modify article',
            'D': 'Find article by ref. number',
            'E': 'Quit'
        },
        'question': 'Select an option',
        'error': 'Invalid option',
    },
    'AA': {
        'title': 'PRODUCT MENU',
        0: {
            'A': 'Screws',
            'B': 'Paint',
            'C': 'Go back'
        },
        'question': 'Select an option',
        'error': 'Invalid option',
    },
    'AAA': {
        'title': 'TYPE MENU',
        0: {
            'A': 'With hexagonal head',
            'B': 'Nickel plated',
            'C': 'With screw for wood',
            'D': 'Go back'
        },
        'question': 'Select an option',
        'error': 'Invalid option',
    },
    'AAAA': {
            'title': 'MATERIAL MENU',
            0: {
                'A': 'Stainless Steel',
                'B': 'For wood',
                'C': 'Go back'
            },
            'question': 'Select an option',
            'error': 'Invalid option',
        },
    'AAB': {
        'title': 'TYPE MENU',
        0: {
            'A': 'Plain',
            'B': 'Decorative',
            'C': 'Temple',
            'D': 'Economic',
            'E': 'Go back'
        },
        'question': 'Select an option',
        'error': 'Invalid option',
    },
    'AABA': {
            'title': 'MATERIAL MENU',
            0: {
                'A': 'Acrylic Paint',
                'B': 'Plastic Paint',
                'C': 'Go back'
            },
            'question': 'Select an option',
            'error': 'Invalid option',}

}
es = {
    '': {
            0: 'Entrar código del producto',
            1: 'El código debe estar formado por 3 números',
            2: 'El código debe ser único',
            3: 'Introduce el precio del producto',
            4: 'Introduce la cantidad de productos en stock',
            5: 'El stock debe ser un valor numérico',
            6: 'LISTA DE ARTÍCULOS',
            7: {
                0: 'Num. de Ref.',
                1: 'Nombre',
                2: 'Tipo',
                3: 'Material',
                4: 'Precio',
                5: 'Stock',
                6: 'Posición'
            },
            8: 'MODIFICACIÓN DE ARTÍCULO',
            9: '¿Qué posición del producto quieres cambiar?',
            10: '¡Stock modificado!',
            11: 'Debes introducir un valor numérico',
            12: 'Valor fuera de rango',
            13: 'La posición y el código no coinciden',
            14: 'El producto no se ha encontrado',
            15: 'Presiona Enter para continuar',
            16: 'BUSCAR PRODUCTO',
            17: 'ARTÍCULO'
        },
    'A': {
        'title': 'MENÚ PRINCIPAL',
        0: {
            'A': 'Agregar producto',
            'B': 'Lista de artículos',
            'C': 'Modificar artículo',
            'D': 'Buscar artículo',
            'E': 'Salir'
        },
        'question': 'Selecciona una opción',
        'error': 'Opción no válida',
    },
    'AA': {
        'title': 'MENÚ DE PRODUCTO',
        0: {
            'A': 'Tornillo',
            'B': 'Pintura',
            'C': 'Volver atrás'
        },
        'question': 'Selecciona una opción',
        'error': 'Opción no válida',
    },
    'AAA': {
        'title': 'MENÚ DE TIPO',
        0: {
            'A': 'Con cabeza hexagonal',
            'B': 'Niquelado',
            'C': 'Rosca para madera',
            'D': 'Volver atrás'
        },
        'question': 'Selecciona una opción',
        'error': 'Opción no válida',
    },
    'AAAA': {
        'title': 'MENÚ DE MATERIAL',
        0: {
            'A': 'Acero Inoxidable',
            'B': 'Para Madera',
            'C': 'Volver atrás'
        },
        'question': 'Selecciona una opción',
        'error': 'Opción no válida',
    },
    'AAB': {
        'title': 'MENÚ DE TIPO',
        0: {
            'A': 'Liso',
            'B': 'Decorativo',
            'C': 'Temple',
            'D': 'Económico',
            'E': 'Volver atrás'
        },
        'question': 'Selecciona una opción',
        'error': 'Opción no válida',
    },
    'AABA': {
        'title': 'MENÚ MATERIAL',
        0: {
            'A': 'Pintura Acrílica',
            'B': 'Pintura Plástica',
            'C': 'Volver atrás'
        },
        'question': 'Selecciona una opción',
        'error': 'Opción no válida',
    }
}
cat = {
    '': {
        0: 'Entrar codi del producte',
        1: 'El codi ha de estar format per 3 numeros',
        2: 'El codi a de ser unic',
        3: 'Entre el preu del producte',
        4: 'Entra la quantitat de productes en stock',
        5: 'El stcok ha de ser un valor numeric',
        6: 'LLISTE DE ARTICLES',
        7: {
            0: 'Num. de Ref.',
            1: 'Nom',
            2: 'Tipus',
            3: 'Material',
            4: 'Preu',
            5: 'Stock',
            6: 'Posicio'
        },
        8: 'MODIFICACIO DE ARTICLE',
        9: 'Quina posicio del producte vols caviar',
        10: 'Stock modificat!',
        11: 'Has de entrar un valor numeric',
        12: 'Valor fora de rang',
        13: 'La posicio i el codi no coincideixen',
        14: 'El producte no s ha trobat',
        15: 'Preme Enter per a continuar',
        16: 'CERCA PRODUCTE',
        17: 'ARTICLE'
    },

    'A': {
        'title': 'MENU PRINCIPAL',
        0: {
            'A': 'Afegir producte',
            'B': 'Llista articles',
            'C': 'Modifica article',
            'D': 'Cerca article',
            'E': 'Surt'
        },
        'question': 'Seleciona una opcio',
        'error': 'Opcio no valida',
    },
    'AA': {
        'title': 'MENU DE PRODUCTE',
        0: {
            'A': 'Cargol',
            'B': 'Pintura',
            'C': 'Anar enrera'
        },
        'question': 'Seleciona una opcio',
        'error': 'Opcio no valida',
    },
    'AAA': {
        'title': 'MENU DE TIPUS',
        0: {
            'A': 'Amb cap hexagonal',
            'B': 'Niquelat',
            'C': 'Rosca per a fusta',
            'D': 'Anar Enrera'
        },
        'question': 'Seleciona una opcio',
        'error': 'Opcio no valida',
    },
    'AAAA': {
            'title': 'MENU DE MATERIAL',
            0: {
                'A': 'Acer Inoxidable',
                'B': 'Per Fusta',
                'C': 'Anar enrera'
            },
            'question': 'Seleciona una opcio',
        'error': 'Opcio no valida',
        },
    'AAB': {
        'title': 'MENU DE TIPUS',
        0: {
            'A': 'Llisa',
            'B': 'Decorativa',
            'C': 'Temple',
            'D': 'Economica',
            'E': 'Anar enrera'
        },
        'question': 'Seleciona una opcio',
        'error': 'Opcio no valida',
    },
    'AABA': {
            'title': 'MENU MATERIAL',
            0: {
                'A': 'Pintura Acrilica',
                'B': 'Pintura Plastica',
                'C': 'Anar Enrera'
            },
            'question': 'Seleciona una opcio',
            'error': 'Opcio no valida',
    }
}

current = 'A'
products = {}
products = {
    '123': {'name': 'Screws', 'type': 'With hexagonal head', 'material': 'Stainless Steel', 'price': '12.45', 'stock': '54'},
    '456': {'name': 'Screws', 'type': 'Decorative', 'material': '', 'price': '34.2', 'stock': '12'}
}

def langsel(lang):
    global menu
    match lang:
        case 'A':
            menu = eng.copy()
        case 'B':
            menu = cat.copy()
        case 'C':
            menu = es.copy()
        case default:
            print('ERROR: Invalid option')
            lang = input('> ').upper()
            langsel(lang)


def printMenu():
    global current
    if current in list(menu.keys()):
        print(f'{menu[current]['title']:^30}')
        for option, description in menu[current][0].items():
            print(f'{option}) {description}')
        choice = input(f'\n{menu[current]['question']}: ').upper()
        while choice not in menu[current][0].keys():
            choice = input(f'\n{menu[current]['error']}\n{menu[current]['question']}: ').upper()
        if choice == list(menu[current][0].keys())[-1]:
            current = current[:-1]
        else:
            current += choice
    else:
        if current[:2] == 'AA':
            addProduct()
        elif current[:2] == 'AB':
            listProduct()
        elif current[:2] == 'AC':
            modifyProduct()
        else:
            getProduct()
        current = 'A'


def addProduct():
    global current
    option = ''
    code = input(f'{menu[''][0]}: ')
    while (len(code) != 3 and code.isnumeric()) or code in list(products.keys()):
        if not (len(code) == 3 and code.isnumeric()):
            print(f'{menu[''][1]}')
        else:
            print(f'{menu[''][2]}')
        code = input(f'{menu[''][0]}: ')
    products[code] = {}
    for op in current:
        option += op
        if option in list(menu.keys()) and option != 'A':
            if len(option) == 2:
                products[code]['name'] = menu[option][0][option[1:]]
            if len(option) == 3:
                products[code]['type'] = menu[option][0][option[2:]]
                products[code]['material'] = ''
            if len(option) == 4:
                products[code]['material'] = menu[option][0][option[3:]]
    products[code]['price'] = input(f'{menu[''][3]}: ')
    products[code]['stock'] = input(f'{menu[''][4]}: ')
    while not products[code]['stock'].isnumeric():
        print(f'{menu[''][5]}')
        products[code]['stock'] = input(f'{menu[''][4]}: ')


def listProduct():
    list = f'{menu[''][7][0]:20}{menu[''][7][1]:15}{menu[''][7][2]:25}{menu[''][7][3]:20}{menu[''][7][4]:10}{menu[''][7][5]:{len(menu[''][7][5])}}'
    for i in range(round(len(list)/2)-round(len(menu[''][6])/2)):
        print('=', end='')
    print(menu[''][8], end='')
    for i in range(round(len(list)/2)-round(len(menu[''][6]))-1):
        print('=', end='')
    print('\n', list, sep='')
    for i in range(len(list)+1):
        print('=', end='')
    print('')
    for ref, product in products.items():
        print(f'{ref:20}{product['name']:15}{product['type']:25}{product['material']:20}{product['price']:10}{product['stock']:{len(menu[''][7][5])}}')


def modifyProduct():
    listMenu = f'{menu[''][7][6]:15}{menu[''][7][0]:20}{menu[''][7][1]:20}{menu[''][7][2]:25}{menu[''][7][3]:15}'
    for i in range(round(len(listMenu) / 2) - round(len(menu[''][6]) / 2)):
        print('=', end='')
    print(menu[''][6], end='')
    for i in range(round(len(listMenu) / 2) - round(len(menu[''][6]) / 2)-2):
        print('=', end='')
    print('\n', listMenu, sep='')
    for i in range(len(listMenu)):
        print('=', end='')
    print('')
    for i in range(len(products)):
        codes = list(products.items())
        code, info = codes[i]
        print(f'{i:<15}{code:20}{info['name']:20}{info['type']:25}{info['material']:15}')
    position = input(f'{menu[''][9]}: ')
    while int(position) > len(products) or int(position) < 0:
        print(menu[''][12])
        position = input(f'{menu[''][9]}: ')
    code = input(f'{menu[''][0]}: ')
    while code != list(products.keys())[int(position)]:
        print(menu[''][13])
        code = input(f'{menu[''][0]}: ')
    products[code]['stock'] = input(f'{menu[''][4]}: ')
    while not products[code]['stock'].isnumeric():
        print(f'{menu[''][5]}')
        products[code]['stock'] = input(f'{menu[''][4]}: ')
    print(menu[''][10])


def getProduct():
    for i in range(20):
        print('=', end='')
    print(menu[''][16], end='')
    for i in range(20):
        print('=', end='')
    print('')
    for i in range(len(menu[''][16])+40):
        print('=', end='')
    print('')
    code = input(f'{menu[''][0]}: ')
    while len(code) != 3 and code.isnumeric():
        print(f'{menu[''][1]}')
        code = input(f'{menu[''][0]}: ')
    if code not in list(products.keys()):
        print(menu[''][14])
    else:
        listMenu = f'{menu[''][7][0]:20}{menu[''][7][1]:15}{menu[''][7][2]:25}{menu[''][7][3]:20}{menu[''][7][4]:10}{menu[''][7][5]:{len(menu[''][7][5])}}'
        for i in range(round(len(listMenu) / 2) - round(len(menu[''][17]) / 2)):
            print('=', end='')
        print(menu[''][17], end='')
        for i in range(len(listMenu)-round(len(listMenu) / 2) - round(len(menu[''][17]) / 2)):
            print('=', end='')
        print('\n', listMenu, sep='')
        for i in range(len(listMenu) + 1):
            print('=', end='')
        print('')
        print(f'{code:20}{products[code]['name']:15}{products[code]['type']:25}{products[code]['material']:20}{products[code]['price']:10}{products[code]['stock']:{len(menu[''][7][5])}}')
    input(f'{menu[''][15]}...')

menu = {}
print(f'|{'Select a language':^25}|{'Seleccioneu un idioma':^25}|{'Selecciona un idioma':^25}|')
print(f'|{'A. English':^25}|{'B. Catala':^25}|{'C. Castellano':^25}|')
lang = input('> ').upper()
langsel(lang)


while current != '':
    printMenu()