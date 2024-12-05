# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y,
# wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer,
# how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank
# is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not 
# necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.


try:
    nmrtr, dnmntr = input("Fraction: ").split("/")
except ValueError as ve:
    nmrtr, dnmntr = input("Fraction: ").split("/")
while nmrtr.isalpha() == True or "." in nmrtr or dnmntr.isalpha() == True or "." in dnmntr or int(nmrtr) > int(dnmntr) or dnmntr == 0:
    nmrtr, dnmntr = input("Fraction: ").split("/")
percentage = round((int(nmrtr)/int(dnmntr))*100)
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")