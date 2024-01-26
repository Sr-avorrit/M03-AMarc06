from El_Super.app import options, functions as f


def printMenu():
    option = 'z'
    while f.isValidOption(option, ["a", "b", "c", "d", "e", "f", "g", "h", "i", "q"]):
        print("\n\na) Insert product into the warehouse",
              "b) Insert customers",
              "c) Most expensive product",
              "d) Total price of all products in the warehouse",
              "e) Total income from sales",
              "f) Product with the highest revenue",
              "g) Customer who has spent the most",
              "h) Total sales for the month",
              "i) Date of the last sale of a product",
              "q) Quit", sep="\n")
        option = input("\nEnter the option: ").lower()
    return option


def menuSelector(option):
    match option:
        case 'a':
            options.insertProduct()
        case 'b':
            options.insertClient()
        case 'c':
            options.expensiveProduct()
        case 'd':
            options.totalPrice()
        case 'e':
            options.totalPricePerSale()
        case 'f':
            options.mostIncomeProduct()
        case 'g':
            options.clientMostExpenses()
        case 'h':
            options.totalMonthSales()
        case 'i':
            options.lastSaleDate()
        case default:
            print("Goodbye, have a nice day")