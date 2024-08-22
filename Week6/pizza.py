# In a file called pizza.py, implement a program that expects exactly one command-line argument, the name (or path)
# of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate, a package on PyPI
# at pypi.org/project/tabulate. Format the table using the library’s grid format. If the user does not specify exactly
# one command-line argument, or if the specified file’s name does not end in .csv, or if the specified file does not 
# exist, the program should instead exit via sys.exit.

from tabulate import tabulate
import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-3:] != "csv":
    sys.exit("Not a csv file")

menu = []
try:
    with open(sys.argv[1]) as file:
        for line in file:
            menu.append(line.strip().split(","))
except FileNotFoundError:
    sys.exit("File does not exist")
print(tabulate(menu, headers = "firstrow", tablefmt = "grid"))
