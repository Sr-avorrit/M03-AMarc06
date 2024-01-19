def isValidOption(option, options):
    return option not in options


def isValidFloat(isFloat):
    try:
        float(isFloat)
        return True
    except ValueError:
        return False


def checkProductId(pId):
    pId = str(pId)
    if len(pId) == 5 and pId.isnumeric():
        return True
    else:
        return False


def checkClientId(cId):
    return len(cId) == 10 and cId[:8].isnumeric() and cId[8] == '-' and cId[9].isnumeric()


def year(date):
    return date[0]


def month(date):
    return date[1]


def day(date):
    return date[2]


def isValidMonth(monthN):
    monthN = str(monthN)
    if monthN.isnumeric():
        if int(monthN) >= 1 and int(monthN) >= 12:
            return True
    else:
        return isValidOption(monthN, ["january", "february", "march", "april", "may", "june", "july", "august",
                                     "september", "october", "november", "december"])


def monthNameToNum(month):
    if month.isnumeric():
        return int(month)
    else:
        if month == "january":
            return 1
        elif month == "february":
            return 2
        elif month == "march":
            return 3
        elif month == "april":
            return 4
        elif month == "may":
            return 5
        elif month == "june":
            return 6
        elif month == "july":
            return 7
        elif month == "august":
            return 8
        elif month == "september":
            return 9
        elif month == "october":
            return 10
        elif month == "november":
            return 11
        elif month == "december":
            return 12


def monthNumToName(month):
    month = int(month)
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]
    return months[month-1]


def isValidYear(year):
    year = str(year)
    return year.isnumeric()
