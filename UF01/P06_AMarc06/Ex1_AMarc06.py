for i in range (1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("Múltiple doble")
    elif i % 3 == 0:
        print("Múltiple de 3")
    elif i % 5 == 0:
        print("Múltiple de 5")
    else:
        print(i)