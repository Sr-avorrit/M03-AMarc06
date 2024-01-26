from El_Super.DAO import itemDAO as iDAO, productDAO as pDAO, salesDAO as sDAO, clientDAO as cDAO
from El_Super.app import functions as f


def lastSaleDate():
    products = pDAO.getProductsNames()
    aux = ''
    while aux not in products:
        print("You can choose between the following products: \n", end="")
        for product in products:
            print(f"| {product} |", end="")
        aux = input("\nWitch is the product for which you want to know the date of the last sale?: ")
    if pDAO.getProductIdByName(aux) in iDAO.getItemsProductsIds():
        date = sDAO.getDateBySaleId(iDAO.getSaleIdByProductId(pDAO.getProductIdByName(aux)))
        print(f"\nThe last sell of the product {aux} was the: {f.day(date)}/{f.month(date)}/{f.year(date)}")
    else:
        print("This product has not been sold yet.\n")


def insertProduct():
    pId = ''
    while not f.checkProductId(pId):
        pId = input("Enter the product ID of the product you want to add: ")
        if f.checkProductId(pId):
            if pDAO.isProduct(pId):
                op = ''
                while f.isValidOption(op, ['y', 'n']):
                    op = input(f'The product ID {pId} you entered correspond to {pDAO.getProductNameById(pId)} '
                               'do you want to add stock of the product? [y/n] ').lower()
                if op == 'y':
                    amount = ''
                    while not amount.isnumeric():
                        amount = input("Enter the amount you want to add to the actual Stock: ")
                        if amount.isnumeric():
                            pDAO.addStock(pId, amount)
                        else:
                            print("ERROR: You must enter an integer.")
            else:
                pName = input("Enter the name of the product: ")
                pPrice = ''
                while not f.isValidFloat(pPrice):
                    pPrice = input("Enter the price of the product: ")
                    if not f.isValidFloat(pPrice):
                        print('ERROR: The price must be a float.')
                amount = ''
                while not amount.isnumeric():
                    amount = input("Enter the amount you want to add to the actual Stock: ")
                    if not amount.isnumeric():
                        print("ERROR: You must enter an integer.")
                pDAO.addProduct(pId, pName, pPrice, amount)
        else:
            print("ERROR: The product ID you have entered does not have a valid format.\n" +
                  "The product ID is formed by 5 numbers [xxxxx]")


def insertClient():
    cId = ''
    while not f.checkClientId(cId):
        cId = input("Enter a client ID for the client you want to add: ")
        if f.checkClientId(cId):
            if cDAO.isClient(cId):
                print(f'The client ID {cId} you entered is already assigned to {cDAO.getClientNameById(cId)}')
            else:
                cName = input("Enter the name of the new client: ")
                cDAO.addClient(cId, cName)
        else:
            print("ERROR: The client ID you have entered does not have a valid format.\n" +
                  "The client ID has the following format [xxxxxxxx-x]")


def expensiveProduct():
    prod = (00000, '', 0.0, 0)
    products = pDAO.getProducts()
    product = ''
    for product in products:
        if prod[2] < product[2]:
            prod = product
    (pCode, pName, pPrice, pStock) = product
    print(f'The most expensive product name is {pName} with ID {pCode} and a price of {pPrice:.2f}')


def totalPrice():
    total = 0
    products = pDAO.getProducts()
    for product in products:
        total += product[2]*product[3]
    print(f'The total price of all the products of the warehouse is {total:.2f}')


def totalPricePerSale():
    salesList = []
    priceList = []
    clientNames = []
    items = iDAO.getItems()
    for item in items:
        if item[0] not in salesList:
            salesList.append(item[0])
            priceList.append(pDAO.getProductPriceById(item[1])*item[2])
            clientNames.append(cDAO.getClientNameById(sDAO.getClientBySaleId(item[0])))
        else:
            priceList[salesList.index(item[0])] += pDAO.getProductPriceById(item[1])*item[2]
    print(f'| Sale Id |   Total   |         Client         |\n'
          f'-----------------------------------------------')
    for i in range(len(salesList)):
        print(f'|{salesList[i]:^8}|{priceList[i]:^11.2f}|{clientNames[i]:^24}|')


def mostIncomeProduct():
    productList = []
    priceList = []
    items = iDAO.getItems()
    for item in items:
        if item[1] not in productList:
            productList.append(item[1])
            priceList.append(pDAO.getProductPriceById(item[1]) * item[2])
        else:
            priceList[productList.index(item[1])] += pDAO.getProductPriceById(item[1]) * item[2]
    pName = pDAO.getProductNameById(productList[priceList.index(max(priceList))])
    print(f'The product with the major earnings is {pName} with a total income of {max(priceList):.2f}')


def totalMonthSales():
    month = ''
    while f.isValidMonth(month):
        month = input("Enter the month for which you want to know the total purchases: ").lower()
        if not f.isValidMonth(month):
            month = f.monthNameToNum(month)
        else:
            print('ERROR: The month you entered is not a valid month name or number.')
    year = ''
    while not f.isValidYear(year):
        year = input("Enter the year for which you want to know the total purchases: ").lower()
        if f.isValidYear(month):
            year = int(year)
        else:
            print('ERROR: The year you entered is not valid.')
    sales = sDAO.getSalesIds()
    amount = 0
    for sale in sales:
        date = sDAO.getDateBySaleId(sale)
        amount += 1 if f.month(date) == month and f.year(date) == year else 0
    print(f'The total amount of sales performed in the month of {f.monthNumToName(month)} of {year} are {amount}')


def clientMostExpenses():
    clientsExpenses = []
    clientCode = []
    for sId in sDAO.getSalesIds():
        if sDAO.getClientBySaleId(sId) not in clientCode:
            clientCode.append(sDAO.getClientBySaleId(sId))
            for item in iDAO.getItems():
                if item[0] == sId:
                    clientsExpenses.append(pDAO.getProductPriceById(item[1])*item[2])
        else:
            for item in iDAO.getItems():
                if item[0] == sId:
                    index = clientCode.index(sDAO.getClientBySaleId(sId))
                    clientsExpenses[index] += pDAO.getProductPriceById(item[1])*item[2]
    cName = cDAO.getClientNameById(clientCode[clientsExpenses.index(max(clientsExpenses))])
    cCode = clientCode[clientsExpenses.index(max(clientsExpenses))]
    print(f'The client that have expended the most ' +
          f'is {cName} with client Code {cCode} ' +
          f'and a total expense amount of {max(clientsExpenses):.2f}')