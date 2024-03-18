# Objective:
# The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.
list = []
def addItem(*items):
    global list
    for x in items:
        list.append(x)

yourItems = input("What do you want to add to the list? Use the format: bananas cherries apples etc.").split()
addItem(*yourItems)
print(f"your grocery list contains: {list}")

# Task 2: Include a feature to remove items from the list.

list = []
def addItem(*items):
    global list
    for x in items:
        list.append(x)

def removeItem(*removeItems):
    global list
    for x in removeItems:
        if x in list:
            list.remove(x)
        else:
            print(f"{x} is not in your grocery list. Make sure you correctly enter the name of the object your want to remove next time!")


yourItems = input("What do you want to add to the list?").split()
addItem(*yourItems)
print(f"your grocery list contains: {list}")


removeList = input(f"""
                   Do you want to remove any items from the list: {list}. If so, enter the items in the format: 
                   bananas apples cherries etc. If not leave blank.")
                   """).split()

if removeList:
    removeItem(*removeList)
    print(f"Your list now contains: {list}")
else:
    print(f"You didn't remove anything from the list! Your grocery list still contains: {list}")

# Task 3: Add a function that prints out the entire list in a formatted way.
    

list = []
def addItem(*items):
    global list
    for x in items:
        list.append(x)

def removeItem(*removeItems):
    global list
    for x in removeItems:
        if x in list:
            list.remove(x)
        else:
            print(f"{x} is not in your grocery list. Make sure you correctly enter the name of the object your want to remove next time!")


yourItems = input("What do you want to add to the list? (Use the format: bananas cherries blueberries etc.)").split()
addItem(*yourItems)
print(f"your grocery list contains: {list}")


removeList = input(f"""
                   Do you want to remove any items from your list? {list}. If so, enter the items in the format: 
                   bananas apples cherries etc. If not - leave it blank!")
                   """).split()


def sortList(groceryList):
    sortedList = []
    sortedList = groceryList.sort()
    return sortedList
    

if removeList:
    removeItem(*removeList)
    print(f"Your list now contains: {list}")
else:
    print(f"You didn't remove anything from the list! Your grocery list still contains: {list}")

sortedList = sortList(list)
print(f"Your grocery list in alphabetical order looks like this: {list}")