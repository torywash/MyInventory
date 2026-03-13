"""Books Functions File for MyInventory"""

# imports
import gen_funcs as gf
from pathlib import Path

# variables
data = {}
file_path = Path("MyInventory/data.json")

# imports
import gen_funcs as gf


def menu_loop(menu_name: str):
    # initialize data file for menu
    gf.init_data_file(file_path, menu_name)

    # menu options
    prompt = "please enter a choice (1-5): "
    options_text = (
        "1) show items\n2) add items\n3) edit items\n4) remove items\n5) return to menu"
    )

    # menu loop
    while True:
        print(f"\n--{menu_name}--")
        print(options_text)
        choice = input(prompt)

        try:
            if choice == "1":
                print(gf.show_items(file_path, menu_name))
            elif choice == "2":
                gf.add_items(file_path, menu_name)
            elif choice == "3":
                gf.edit_items(file_path, menu_name)
            elif choice == "4":
                gf.remove_items(file_path, menu_name)
            elif choice == "5":
                return False
            else:
                print("invalid choice, please try again")
        except Exception as e:
            print(f"ERROR: {e}, returning to menu...")
            return False


def fridge_menu():
    return menu_loop("fridge")


def personals_menu():
    return menu_loop("personals")


def books_menu():
    return menu_loop("books")
