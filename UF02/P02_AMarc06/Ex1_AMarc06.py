import datetime

listaImmobles = [{'any': 2000, 'metres': 100, 'habitacions': 3, 'garatge': True, 'zona': 'A'},
                 {'any': 2012, 'metres': 60, 'habitacions': 2, 'garatge': True, 'zona': 'B'},
                 {'any': 1980, 'metres': 120, 'habitacions': 4, 'garatge': False, 'zona': 'A'},
                 {'any': 2005, 'metres': 75, 'habitacions': 3, 'garatge': True, 'zona': 'B'},
                 {'any': 2015, 'metres': 90, 'habitacions': 2, 'garatge': False, 'zona': 'A'}]


def antiguitat(any: int):
    return datetime.date.today().year - any


def preuImmoble(immoble: dict):
    preu = (immoble['metres'] * 1000 + immoble['habitacions'] * 5000 + immoble['garatge'] * 15000) * (1-antiguitat(immoble['any'])/100)
    if immoble['zona'] == 'B':
        preu *= 1.5
    return preu


def cercadorImmobles(immobles: list, preu: float):
    res = []
    for immoble in immobles:
        if preuImmoble(immoble) <= preu:
            res.append(immoble)
    return res


print(cercadorImmobles(listaImmobles, 1000000))
