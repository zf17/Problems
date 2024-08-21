# In a file called einstein.py, implement a program in Python that prompts the user for mass
# as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer
# using E = mc^2. Assume that the user will input an integer.

# Updated: Make sure the input is a number

while True:
    try:
        mass = int(input())
        break
    except ValueError:
        print("Not a number")

c = 300000000
print(mass*(300000000**2))

