#rock paper scissors
import random

#1 paper
#2 rock
#3 scissors
#4 exit
user_result = 0

while user_result != 4:

    print(" #1 Paper\n #2 Rock \n #3 Scissors \n #4 Stop Game")

    user_result = int(input("inter your choise: "))

    num_random = random.randrange(1, 3)

    print("bot select: ", num_random)

    if user_result == num_random:
        print("draw")
    elif user_result == 1 and num_random == 2 or user_result == 2 and num_random == 3 or user_result == 3 and num_random == 1:
        print("you win")
    elif user_result == 4:
        print("exit")
    else:
        print("you lose")


