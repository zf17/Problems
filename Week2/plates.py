# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
# “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate;
# AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
# “No periods, spaces, or punctuation marks are allowed.”

# In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or 
# Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein 
# is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement 
# additional functions for is_valid to call (e.g., one function per requirement).


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    elif s[0:2].isalpha() == False:
        return False
    elif s.isalnum() == False:
        return False
    for i in range(len(s)):
        if s[i].isnumeric() and s[i::].isnumeric() == False:
            return False
        if s[i] == "0" and s[i-1].isnumeric() == False:
            return False
    return True

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

if __name__ == "__main__":
    main()

