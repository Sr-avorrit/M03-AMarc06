from El_Super.app import menu

if __name__ == "__main__":
    option = ''
    while option != 'q':
        option = menu.printMenu()
        menu.menuSelector(option)
