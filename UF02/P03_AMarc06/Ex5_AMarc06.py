registre = {}


def registre_vendes(producte: str, *args: int, **kwargs):
    global registre
    registre[len(registre)] = {
        "producte": producte,
        "vendes": args,
        "detalls": kwargs
    }


registre_vendes("Samarreta", 10, 15, 20, client="Joan", data="2023-01-15", lloc="Barcelona")
print(registre)
