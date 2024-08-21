# In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, 
# wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it
# does not, but main is only called if the value of __name__ is "__main__":

# def main():
#     ...


# def is_valid(s):
#     ...


# if __name__ == "__main__":
#     main()


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

