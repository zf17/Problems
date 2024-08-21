# In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below,
# wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether
# inputted in uppercase or lowercase.

# def main():
#     ...


# def shorten(word):
#     ...


# if __name__ == "__main__":
#     main()



def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    new_text = ""
    for letter in word:
        if letter.lower() not in vowels:
            new_text += letter
    return new_text

def main():
    text = input("Input: ")
    print(f"Output: {shorten(text)}")

if __name__ == "__main__":
    main()



