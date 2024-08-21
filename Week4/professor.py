import random

def main():

    level = get_level()
    score = 0

    for i in range(10): # create 10 problems
        wrong_count = 0

        X = generate_integer(level) # generate X and Y randomly
        Y = generate_integer(level)

        while True:
            try:
                ans = int(input(f"{X} + {Y} =")) # display problem

                if ans == X+Y: # if correct, increment score
                    score += 1
                elif ans != X+Y and wrong_count < 2: # if wrong and not 3rd time getting it wrong, display message, increment wrong_count and start the next loop
                    print("EEE")
                    wrong_count += 1
                    continue
                elif ans != X+Y and wrong_count == 2: # if wrong and its 3rd time getting it wrong, display message and answer
                    print("EEE")
                    print(f"{X} + {Y} = {X+Y}")
                break # break out of while loop

            except ValueError: # if answer inputted is not a integer

                if wrong_count < 2: # same code as in the try statement
                    print("EEE")
                    wrong_count += 1
                    continue
                else:
                    print("EEE")
                    print(f"{X} + {Y} = {X+Y}")
                break

    print(f"Score: {score}") # displaying score

def get_level():
    while True: # repeating until correct input is given
        try:
            level = int(input("Level: "))
            if level > 0 and level < 4: # only returning the level if its 1, 2 or 3
                return level
        except ValueError:
            pass # catching the error


def generate_integer(level): # generating an integer based on the level
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100,999)
    else:
        raise ValueError # if level is not valid, raise value error

if __name__ == "__main__":
    main()

# In a file called professor.py, implement a program that:

#   Prompts the user for a level n, If the user does not input 1, 2, or 3, the program should prompt again.
#   Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative 
#   integer with n digits. No need to support operations other than addition (+).
#   Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the 
#   program should output EEE and prompt the user again, allowing the user up to three tries in total for that 
#   problem. If the user has still not answered correctly after three tries, the program should output the correct 
#   answer.
#   The program should ultimately output the user’s score: the number of correct answers out of 10.

# Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and
# returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises
# a ValueError if level is not 1, 2, or 3:
