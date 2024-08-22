# In a file called lines.py, implement a program that expects exactly one command-line argument, the name (or path) of a Python file,
# and outputs the number of lines of code in that file, excluding comments and blank lines. If the user does not specify exactly 
# one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program 
# should instead exit via sys.exit. Assume that any line that starts with #, optionally preceded by whitespace, is a comment. (A docstring 
# should not be considered a comment.) Assume that any line that only contains whitespace is blank.

import sys
count = 0
lines = []

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-2:] != "py":
    sys.exit("Not a python file")

with open("test.py", "w") as test:
    test.write("code\n")
    test.write("code\n")
    test.write("code\n")
    test.write("code\n")
    test.write("code\n")
    test.write("#code\n")
    test.write(" ")


try:
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    sys.exit("File does not exist")

for line in lines:
    line = line.strip()
    if line.startswith("#") == False and len(line) != 0:
        count += 1
print(count)
