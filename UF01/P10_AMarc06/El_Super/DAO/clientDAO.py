from El_Super.DAO.data import clients


def getClientsIds():
    cIds = []
    for client in clients:
        (cCode, cName) = client
        cIds.append(cCode)
    return cIds


def getClientsNames():
    cNames = []
    for client in clients:
        (cCode, cName) = client
        cNames.append(cName)
    return cNames


def isClient(cId):
    return cId in getClientsIds()


def getClientNameById(cId):
    return getClientsNames()[getClientsIds().index(cId)]


def addClient(cCode, cName):
    client = (cCode, cName)
    clients.append(client)
