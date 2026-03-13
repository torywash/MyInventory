"""General Functions File for MyInventory"""

# imports
import json
from pathlib import Path
import datetime

# variables
data = {}
file_path = Path("MyInventory/data.json")


# functions
# initialize data file
def init_data_file(path, menu="fridge"):
    if not path.exists():
        with open(path, "w") as f:
            json.dump({menu: []}, f, indent=4)
        print(f"\n{menu} file initialized")
    else:  # ensure it passes if the menu key already exists
        pass


# show items
def show_items(path, menu):
    if not path.exists():
        with open(path, "w") as f:
            json.dump({menu: []}, f, indent=4)
        return f"\n{menu} file created, returning to menu"

    with open(path, "r") as f:
        data = json.load(f)

    # ensure the menu key exists in the data
    if menu not in data:
        data[menu] = []
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        return f"\n{menu} created in data file, returning to menu"

    # handle empty menu lists
    if not data[menu]:
        if menu == "fridge":
            return f"\nyour {menu} is empty! go add some food!"
        elif menu == "personals":
            return f"\nyour {menu} is empty! go add some personals!"
        elif menu == "books":
            return f"\nyour {menu} are empty! go add some books!"

    # list items
    items = f"\nitems in {menu}:\n"
    for item in data[menu]:
        items += f"- {item['name']} (added: {item['added']})\n"
    return f"{items}\ntotal items: {len(data[menu])}"


# add function
def add_items(path, menu):
    # if path does not exist
    if not path.exists():
        with open(path, "w") as f:
            json.dump({menu: []}, f, indent=4)
        return f"\n{menu} file created, returning to menu"

    # open file
    with path.open("r") as f:
        data = json.load(f)

    # ensure the menu key exists
    if menu not in data:
        data[menu] = []
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        return f"\n{menu} created in data file, returning to menu"

    # append to dict
    data.setdefault(menu, [])
    item = input(f"enter the name of the {menu} item: ")
    if menu == "books":
        author = input("enter the author of the book: ")
        vol = input("enter the volume of the book (leave blank if not applicable): ")
        if vol:
            item += f", vol. {vol}"
        if author:
            item += f" by {author}"
    entry = {"name": item, "added": datetime.datetime.now().strftime("%m/%d/%Y")}
    data[menu].append(entry)

    # write to file
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    # return success message
    print(f"\n{item} added to {menu}!")


# edit function
def edit_items(path, menu):
    # if path does not exist
    if not path.exists():
        with open(path, "w") as f:
            json.dump({menu: []}, f, indent=4)
        return f"\n{menu} file created, returning to menu"

    # open file
    with path.open("r") as f:
        data = json.load(f)

    # ensure the menu key exists
    if menu not in data:
        data[menu] = []
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        return f"\n{menu} created in data file, returning to menu"

    # nothing to edit
    if not data[menu]:
        print(f"\nno items in {menu} to edit, returning to menu")
        return False

    # list items
    for index, item in enumerate(data[menu]):
        print(f"{index+1}) {item}")

    # prompt for item choice
    e_choice = input(f"please enter a choice (1-{len(data[menu])})")

    # handle choice
    try:
        item = data[menu][int(e_choice) - 1]
        new_name = input(f"enter new name for {item['name']}: ")
        if not new_name:
            new_name = item["name"]
        else:
            item["name"] = new_name
        if menu == "books":
            new_author = input(
                "enter new author for the book (leave blank to keep current): "
            )
            if new_author:
                item["name"] = f"{new_name} by {new_author}"
            new_vol = input(
                "enter new volume for the book (leave blank to keep current): "
            )
            if new_vol:
                item["name"] += f", vol. {new_vol}"

        # write to file
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

        # return success message
        print(f"\n{item['name']} updated!")
    except Exception as e:
        print(f"ERROR: {e}, returning to menu...")
        return False


# remove function
def remove_items(path, menu):
    # if path does not exist
    if not path.exists():
        with open(path, "w") as f:
            json.dump({menu: []}, f, indent=4)
        return f"\n{menu} file created, returning to menu"

    # open file
    with path.open("r") as f:
        data = json.load(f)

    # ensure the menu key exists
    if menu not in data:
        data[menu] = []
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
        return f"\n{menu} created in data file, returning to menu"

    # nothing to remove
    if not data[menu]:
        print(f"\nno items in {menu} to remove, returning to menu")
        return False

    # list items
    for index, item in enumerate(data[menu]):
        print(f"{index+1}) {item}")

    # prompt for item choice
    r_choice = input(f"please enter a choice (1-{len(data[menu])})")

    # handle choice
    try:
        item = data[menu][int(r_choice) - 1]
        item_name = item["name"]
        data[menu].remove(item)

        # write to file
        with open(path, "w") as f:
            json.dump(data, f, indent=4)

        # success message
        print(f"\n{item_name} has been removed!")
    except Exception as e:
        print(f"ERROR: {e}, returning to menu...")
        return False
