#1:

with open("functions_exercise.py") as f:
    lines = f.readlines()

file_contents = """
one
two
three
"""

with open("functions_exercise.py", "w") as f:
    f.write(file_contents)

#2:

grocery_list = ["milk", "eggs", "tea"]

with open("my_grocery_list.txt", "w") as w:
    for i in grocery_list:
        w.write("%s\n" % i)
    print("my_grocery_list")

def show_grocery_list(contents):
    with open("my_grocery_list.txt") as f:
        return(contents)

def buy_item(item_name):
    current_list = grocery_list
    purchased_items = []
    with open("my_grocery_list.txt", "w") as fw:
        for i in item_name:
            purchased_items.append(i)
grocery_list = ["milk", "eggs", "tea"]

with open("my_grocery_list.txt", "w") as w:
    for i in grocery_list:
        w.write("%s\n" % i)

def show_grocery_list(contents):
    with open("my_grocery_list.txt") as f:
        return(contents)

def buy_item(item_name):
    current_list = grocery_list
    purchased_items = []
    with open("my_grocery_list.txt", "w") as fw:
        for i in item_name:
            purchased_items.append(i)


