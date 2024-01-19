primerPlat = 0
segonPlat = 0
preu = 0

print("""
Benvingut al restaurant SIS1
Tria el teu menú per emportar\n""")

while primerPlat not in range(1, 5):
    print("""Escull el teu primer plat:
    1 - Primer plat 1. (5 euros)
    2 - Primer plat 2. (6 euros)
    3 - Primer plat 3. (5,5 euros)
    4 - Primer plat 4. (4 euros)""")
    primerPlat = int(input("\nQin primer plat bols: "))
if primerPlat == 1:
    preu = 5
elif primerPlat == 2:
    preu = 6
elif primerPlat == 3:
    preu = 5.5
else:
    preu = 4

while segonPlat not in range(1, 5):
    print("""
Escull el teu segon plat:
    1 - Segon plat 1. (3,5 euros)
    2 - Segon plat 2. (7 euros)
    3 - Segon plat 3. (4 euros)
    4 - Segon plat 4. (6 euros)""")
    segonPlat = int(input("\nQin segon plat bols: "))
if segonPlat == 1:
    preu += 3.5
elif segonPlat == 2:
    preu += 7
elif segonPlat == 3:
    preu += 4
else:
    preu += 6

print(f"""
    Has triat:
    Primer plat {primerPlat}, Segon plat {segonPlat}
    Total a pagar: {preu} euros\n""")