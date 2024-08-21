answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()
if answer == "42" or answer == "forty-two" or answer == "forty two" or "42" in answer:
    print("Yes")
else:
    print("No")


# In deep.py, implement a program that prompts the user for the answer to the Great 
# Question of Life, the Universe and Everything, outputting Yes if the user inputs 
# 42 or (case-insensitively) forty-two or forty two. Otherwise output No.
