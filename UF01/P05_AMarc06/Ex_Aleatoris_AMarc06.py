import random as rand

kilometers = 0
thirsty = 0
tiredness = 0
hunters = -20
canteen = rand.randint(4, 10)
canteenOr = canteen
alive = True
drinkingTimes = 0

def menu():
    print("""
A. Beure de la cantimplora.
B. Velocitat moderada cap endavant.
C. A tota velocitat cap endavant.
D. Para i descansa.
E. Comprova el teu estat.
Q. Sortir.
    """)

def quit():
    print("\nGracies per jugar, esperem tornarte a veure d'aqui poc.\n")


def drinck():
    global thirsty
    global drinkingTimes
    global canteen
    if canteen > 0:
        thirsty = 0
        canteen -= 1
        drinkingTimes += 1    
    else:
        print("\nNo et queda aigua a la cantimplora, No pots beure.")


def walk():
    global kilometers
    global tiredness
    global hunters
    global thirsty
    km = rand.randint(5, 12)
    kilometers += km
    tiredness += 1
    thirsty += 1
    hunters += rand.randint(7, 14)
    print(f"\nHas recoregut {km}.")
    oasis()

def run():
    global kilometers
    global tiredness
    global hunters
    global thirsty
    km = rand.randint(10, 20)
    kilometers += km
    tiredness += rand.randint(1, 3)
    thirsty += 1
    hunters += rand.randint(7, 14)
    print(f"\nHas recoregut {km}.")
    oasis()

def rest():
    global tiredness
    global hunters
    tiredness = 0
    hunters += rand.randint(7, 14)
    print("\nEstas descansant i has recuperat energia.\n El teu elefant s'alegra :)")

def checkStats():
    global thirsty
    global canteen
    global kilometers
    global hunters
    global drinkingTimes
    print(f"""Estat actuals del joc:\n-------------------------
Kilometres recorreguts: {kilometers}
Vegades que has begut de la cantimplora: {drinkingTimes} 
Glops que et queden: {canteen}
Els bosquimanos són a {abs(kilometers-hunters)} kilòmetres darrere teu
          """)
    
def oasis():
    global canteen
    global canteenOr
    global thirsty
    global tiredness
    if rand.randint(1, 20) == 20:
        canteen = canteenOr
        thirsty = 0
        tiredness = 0
        print("Has trobat un oasis, has reomplert la teva cantimplora, as vegut aigua i el teu elefant a descansat.")

    



def optionSelector(optionq):
    if option == 'a':
        drinck()
    elif option == 'b':
        walk()
    elif option == 'c':
        run()
    elif option == 'd':
        rest()
    elif option == 'e':
        checkStats()
    else:
        quit()

def checkOption(option):
    dict = ["a", "b", "c", "d", "e", "q"]
    return option not in dict

def inform():
    global thirsty
    global canteen
    global kilometers
    global hunters
    global drinkingTimes
    global tiredness
    global alive
    if thirsty >= 4 and thirsty <= 6:
        print("\nEstàs assedegat")
    elif thirsty > 6:
        print("\nHas mort de set")
        alive = False
    if tiredness >= 5 and tiredness <= 8:
        print("\nEl teu elefant s'està cansant.")
    elif tiredness > 8:
        print("\nEl teu elefant ha mort.")
    if abs(kilometers-hunters) < 15 and hunters < kilometers:
        print("\nEls caçadors s'estan acostant!")
    if hunters >= kilometers:
        print("\nEls caçadors t'han capturat i t'han matat per recuperar el seu elefant.")
        alive = False
    if kilometers >= 200 and alive:
        print("Felicitats has Guanyat")
        alive = False




if __name__ == "__main__":
    option = ''
    print("""
Benvingut a Botswana!
Has robat un elefant per salvar-lo de les cruels matances, per aconseguir-ho has de
travessar 200 km el desert del Kalahari.

Els caçadors furtius volen recuperar el seu elefant i surten en persecució teva! hauràs
de sobreviure al desert i córrer més que els caçadors bosquimanos.
    """)
    while option != 'q' and alive:
        option = ''
        while checkOption(option):
            menu()
            option = input("Què tries? ").lower()
            optionSelector(option)
            inform()
        

