from El_Super.DAO.data import products


def getProducts():
    return products


def getProductByName(pName):
    pNames = getProductsNames()
    return products[pNames.index(pName)]


def getProductById(pId):
    pId = int(pId)
    pIds = getProductsIds()
    return products[pIds.index(pId)]


def getProductIdByName(pName):
    (pCode, pName, Price, Stock) = getProductByName(pName)
    return pCode


def getProductNameById(pId):
    pId = int(pId)
    (pCode, pName, Price, Stock) = getProductById(pId)
    return pName


def getProductsNames():
    pNames = []
    for product in products:
        (pCode, pName, Price, Stock) = product
        pNames.append(pName)
    return pNames


def getProductsIds():
    pIds = []
    for product in products:
        (pCode, pName, Price, Stock) = product
        pIds.append(pCode)
    return pIds


def isProduct(pId):
    pId = int(pId)
    if pId in getProductsIds():
        return True
    else:
        return False


def addStock(pId, amount):
    pId = int(pId)
    product = getProductById(pId)
    product = list(product)
    product[3] += int(amount)
    product = tuple(product)
    products[products.index(getProductById(pId))] = product


def addProduct(pCode, pName, Price, Stock):
    product = (int(pCode), pName, float(Price), int(Stock))
    products.append(product)


def getProductPriceById(pId):
    pId = int(pId)
    (pCode, pName, pPrice, pStock) = getProductById(pId)
    return pPrice
