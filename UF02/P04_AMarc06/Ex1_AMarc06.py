import random

tipus = ["Corazones", "Diamantes", "Picas", "Tréboles"]
valors = ["2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]
mall = []


def iniciar_partida(*args, **kwargs):
    print()


def jugar_carta(*args):
    print()


def calcular_puntuacio(**kwargs):
    print()


def crear_mall():
    global mall
    for i in tipus:
        for j in valors:
            mall.append((j, i))
    random.shuffle(mall)


def repartir_cartas():
    print()


def fibo(n, fib):
    if n == 1:
        return fib
    elif n > 1:
        fib.append(fib[len(fib)-1]+fib[len(fib)-2])
        fib = fibo(n-1, fib)
    return fib

def fiboStart(n):
    if n < 1:
        fib = []
    elif n == 1:
        fib = [0]
    else:
        fib = [0, 1]
        fib = fibo(n-1, fib)
    return fib


print(fiboStart(365))