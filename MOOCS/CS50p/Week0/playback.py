# In a file called playback.py, implement a program in Python that prompts the user for input and 
# then outputs that same input, replacing each space with ... (i.e., three periods).

# Updated: replace any double spaces with an underscore
inp = input()
inp = inp.replace("  ", "_")
inp = inp.replace(" ", "...")
print(inp)


