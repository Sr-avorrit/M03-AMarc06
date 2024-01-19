from El_Super.DAO.data import sales


def getSales():
    return sales


def getDateBySaleId(sId):
    (saleId, date, clientId) = getSaleBySaleId(sId)
    return date


def getClientBySaleId(sId):
    (saleId, date, clientId) = getSaleBySaleId(sId)
    return clientId


def getSaleBySaleId(sId):
    sale = getSalesIds()
    return sales[sale.index(sId)]


def getSalesIds():
    salesIds = []
    for sale in sales:
        (saleId, date, clientId) = sale
        salesIds.append(saleId)
    return salesIds
