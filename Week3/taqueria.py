# In a file called taqueria.py, implement a program that enables a user to place an order, prompting them for items, 
# one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). After each 
# inputted item, display the total cost of all items inputted thus far, prefixed with a dollar sign ($) and formatted to 
# two decimal places. Treat the user’s input case insensitively. Ignore any input that isn’t an item. Assume that every 
# item on the menu will be titlecased.
# the dictionary entrees was given by the problem.

entrees = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}
total = 0
while True:
    item = ""
    while item not in entrees:
        try:
            item = input("Item: ").lower()
        except EOFError:
            print()
            quit()
    total += entrees[item]
    print(f"Total: ${total:.2f}")
