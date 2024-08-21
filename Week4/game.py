import random
while True:
    try:
        level = int(input("Level: "))
        if level>0:
            break
    except ValueError:
        pass

rand = random.randint(1, level)
guess = 0
while guess != rand:
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                break
        except ValueError:
            pass
    if guess < rand:
        print("Too small!")
    elif guess > rand:
        print("Too large!")
print("Just right!")

# In a file called game.py, implement a program that:
#   Prompts the user for a level n, If the user does not input a positive integer, the program should prompt again.
#   Randomly generates an integer between 1 and n inclusive, using the random module.
#   Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
#     If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
#     If the guess is larger than that integer, the program should output Too large! and prompt the user again.
#     If the guess is the same as that integer, the program should output Just right! and exit.
