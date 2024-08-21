# In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

# convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a percentage
# rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert
# should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.

# gauge expects an int and returns a str that is:
#   "E" if that int is less than or equal to 1,
#   "F" if that int is greater than or equal to 99,
#   and "Z%" otherwise, wherein Z is that same int.

# def main():
#     ...


# def convert(fraction):
#     ...


# def gauge(percentage):
#     ...


# if __name__ == "__main__":
#     main()

# Note: The code is purposefully incorrect to check if my test file can catch these errors and show which function has failed


def convert(fraction):
    try:
        nmrtr, dnmntr = map(int,fraction.split("/"))
    except ValueError:
        raise ValueError
    if dnmntr == 0:
        raise ZeroDivisionError
    else:
        percentage = round((nmrtr/dnmntr)*99)
    return percentage

def gauge(percentage):
    if percentage < 1:
        return "E"
    elif percentage > 99:
        return "F"
    else:
        return f"{percentage}%"

def main():
    fraction = input("Fraction: ")
    while True:
        try:
            percentage = convert(fraction)
            return gauge(percentage)
        except ValueError:
            fraction = input("Fraction: ")
        except ZeroDivisionError:
            fraction = input("Fraction: ")
            
if __name__ == "__main__":
    print(main())

