from El_Super.DAO.data import items


def getItems():
    return items


def getSaleIdByProductId(pId):
    (saleId, pCode, quantity) = getItemByProductId(pId)
    return saleId


def getItemByProductId(pId):
    item = getItemsProductsIds()
    return items[item.index(pId)]


def getItemsProductsIds():
    productsId = []
    for item in items:
        (saleId, pCode, quantity) = item
        productsId.append(pCode)
    return productsId
