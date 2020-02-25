#1:
filename = "corrected_import_exercises.py"
with open(filename, "r") as f:
    contents = f.readlines()
    for i, line in enumerate(contents, start = 1):
        print(i, ": ", line)

#2:

grocery_list = ["milk", "eggs", "tea"]

def make_grocery_list(grocery_list):
    filename = "my_grocery_list.txt"
    with open(filename, "w") as f:
        for item in grocery_list:
            f.write(item, "\n")
# This worked.  It created a file called 'my_grocery_list.txt' and listed all the items in the original variable grocery_list

def show_grocery_list():
    with open("my_grocery_list.txt") as f:
        # print(f.contents) - my original next line
        contents = f.readlines()
        for item in contents:
            print(item)

show_grocery_list()

def buy_item(item, grocery_list):
    grocery_list.remove(item)
    make_grocery_list(grocery_list)
    print(grocery_list)

buy_item("eggs", grocery_list)

# --- Original brainstorming-----

# with open("my_grocery_list.txt", "w") as fw:
#         for i in witem_name:
#             purchased_items.append(i)
# grocery_list = ["milk", "eggs", "tea"]

# with open("my_grocery_list.txt", "w") as w:
#     for i in grocery_list:
#         w.write("%s\n" % i)

# def show_grocery_list(contents):
#     with open("my_grocery_list.txt") as f:
#         return(contents)

# def buy_item(item_name):
#     current_list = grocery_list
#     purchased_items = []
#     with open("my_grocery_list.txt", "w") as fw:
#         for i in item_name:
#             purchased_items.append(i)


