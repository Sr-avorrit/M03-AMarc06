#Llibreries
import random as ran
import os

#Variables
censImperi={
"AR1":{"nom":"Claudia","region":"Roma","edat":23,"sexe":"I","categoria":"centurio"},
"AD3":{"nom":"Maximo","region":"Hispania","edat":30,"sexe":"H","categoria":"soldat"},
"AC2":{"nom":"Marco","region":"Hispania","edat":28,"sexe":"H","categoria":"soldat"},
"AV6":{"nom":"Julius","region":"Roma","edat":35,"sexe":"H","categoria":"cesar"},
"SS5":{"nom":"Augustus","region":"Hispania","edat":21,"sexe":"H","categoria":"soldat"},
"WQ6":{"nom":"Eugenia","region":"Hispania","edat":28,"sexe":"D","categoria":"centurio"},
"JU8":{"nom":"Anastacia","region":"Hispania","edat":17,"sexe":"I","categoria":"soldat"},
"DF5":{"nom":"Aurelia","region":"Hispania","edat":20,"sexe":"D","categoria":"poble"},
"BR1":{"nom":"Antistia","region":"Roma","edat":16,"sexe":"D","categoria":"centurio"},
"KR9":{"nom":"Apolonia","region":"Roma","edat":25,"sexe":"I","categoria":"centurio"},
"KH7":{"nom":"Acucia","region":"Roma","edat":29,"sexe":"D","categoria":"centurio"},
"XH4":{"nom":"Titus","region":"Roma","edat":39,"sexe":"I","categoria":"poble"},
"KA2":{"nom":"Aurelio","region":"Roma","edat":15,"sexe":"H","categoria":"poble"},
"MJ8":{"nom":"Tiberius","region":"Roma","edat":22,"sexe":"H","categoria":"poble"},
}

categoria=["soldat","cesar","centurio","poble"]
regio=["Roma","Hispania"]

#Variables Menu
datos=("Incloure persona en el cens",
       "Buscar persona en el cens",
       "Mostrar soldats Hispania",
       "Visualitzar categoria del cens")
titol="CENS ROMA"
capsalera="_"

#Variables Personals
flag = False
sexe=['H','D','I']

while True:
    # MENU
    print(f'\n{titol:^35}')
    for i in range(35):
        print(capsalera, end='')
    print()
    for i in range(len(datos)):
        print(f'{i + 1}. {datos[i]}')
    flag = False
    option = input('Escull una opcio: ')
    while not flag:
        if option.isnumeric():
            option = int(option)
            if option > len(datos) or option < 1:
                print("Error: The option number you entered is out of range.")
            else:
                flag = True
        else:
            print("Error: The option you enter is not numeric.")
        if not flag:
            option = input('Escull una opcio: ')

    if option == 1:  #INCLOURE PERSONA EN EL CENS
        person = {}
        person["nom"] = input('Nom: ').capitalize()
        person["region"] = input('Regió: ').capitalize()
        while person["region"] not in regio:
            person["region"] = input('Error:Regió no valida\nRegió: ').capitalize()
        flag = False
        person["edat"] = input('Edat: ')
        while not flag:
            if person["edat"].isnumeric():
                person["edat"] = int(person["edat"])
                if person["edat"] > 100 or person["edat"] < 0:
                    print("Error: The age number you entered is out of range. [0 - 100]")
                else:
                    flag = True
            else:
                print("Error: The age you enter is not numeric.")
            if not flag:
                person["edat"] = input('Edat: ')
        person["sexe"] = input('Sexe: ').upper()
        while person["sexe"] not in sexe:
            person["sexe"] = input(f'Error: Sexe no valida {sexe}\nSexe: ').upper()
        person["forca"] = ran.uniform(50, 200)
        person["categoria"] = input('Categoria: ').lower()
        while person["categoria"] not in categoria:
            person["categoria"] = input(f'Error: Categoria no valida {categoria}\nCategoria: ').lower()
        pId = input("Id de la persona: ")
        if len(pId) == 3 and pId[:2].isalpha() and pId[2].isnumeric():
            pId = pId[:2].upper() + pId[2]
        while not (len(pId) == 3 and pId[:2].isalpha() and pId[2].isnumeric()) or pId in list(censImperi.keys()):
            if pId in list(censImperi.keys()):
                print('Error: la ID de la persona a de ser unica')
            else:
                print('Error: La ID ha de estar formada per dos lletres i un numero [XXN]')
            pId = input("Id de la persona: ")
        censImperi[pId] = person

    elif option == 2: #BUSCAR PERSONA EN EL CENSO
        flag = False
        nom = input('Introdueixi Nom: ').capitalize()
        for codi, persona in censImperi.items():
            if persona["nom"].find(nom) == 0:
                if not flag:
                    print(f'{'DADES DEMANADES':^70}')
                    print(f'{'NOM':15}{'REGION':20}{'EDAT':15}{'SEXE':15}{'CATEGORIA':20}')
                    flag = True
                print(f'{persona['nom']:15}{persona['region']:20}{persona['edat']:<15}{persona['sexe']:15}{persona['categoria']:20}')
        if not flag:
            print(f'Error: {nom} no ha estat censat.')

    elif option == 3: #MOSTRAR ELS SOLDATS D’HISPANIA
        flag = False
        for codi, persona in censImperi.items():
            if persona["region"] == 'Hispania' and persona['categoria'] == 'soldat':
                if not flag:
                    print(f'{'SOLDATS DE HISPANIA':^70}')
                    print(f'{'NOM':15}{'REGION':20}{'EDAT':15}{'SEXE':15}{'CATEGORIA':20}')
                    flag = True
                print(f'{persona['nom']:15}{persona['region']:20}{persona['edat']:<15}{persona['sexe']:15}{persona['categoria']:20}')
        if not flag:
            print(f'Error: No s han trobat soldats d hispania')

    elif option == 4:
        count = 0
        cat = input('Introdueixi la categoria: ').lower()
        while cat not in categoria:
            cat = input(f'Error: Categoria no valida {categoria}\nIntrodueixi la categoria: ').lower()
        for codi, persona in censImperi.items():
            if persona['categoria'] == cat:
                print(f'\nNom: {persona['nom']}'
                      f'\nRegió: {persona['region']}'
                      f'\nEdat: {persona['edat']}'
                      f'\nSexe: {persona['sexe']}'
                      f'\nCategoria: {persona['categoria']}')
                count += 1
                input('Presiona enter per continuar...')
        print('No hi ha més persones censades de aquesta categoria.')
        print(f'Total de persones en la categoria {cat.upper()}: {count}')
