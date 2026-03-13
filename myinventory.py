"""UI File for MyInventory"""

# imports
import time
import menus as menu

# TODO: Create a CLI Menu for the MyInventory app
# menu loop -- show menu
while True:
    print("\n-- MyInventory --")
    print("1) fridge\n2) personals\n3) books\n4) exit")

    # prompt for choice
    choice = input("please enter a choice (1-4): ")

    # handle choices
    try:
        # fridge menu
        if choice == "1":
            menu.fridge_menu()
        # personals menu
        elif choice == "2":
            menu.personals_menu()
        # books menu
        elif choice == "3":
            menu.books_menu()
        # exit
        elif choice == "4":
            print("exiting...")
            time.sleep(1)
            break
    except Exception as e:
        print(f"ERROR: {e}")
