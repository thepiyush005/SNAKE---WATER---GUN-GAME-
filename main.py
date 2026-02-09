'''

SNAKE, WATER, GUN GAME

'''

import random

print("SNAKE - WATER - GUN GAME🎮")
print("")

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s/w/g): ")

if youstr not in ["s", "w", "g"]:
    print(" ❌ Invalid choice! Please enter s/w/g.")
    exit()

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0:"Gun"}

you = youDict[youstr]

#By now we have two numbers (variables), you and computer

print(f"You chose {reverseDict[you]} \n Computer chose {reverseDict[computer]}")

if(computer == you):
    print("Its a draw! 🤝")

else:
    if(computer == -1 and you == 1):
        print("You Win! 🎉")

    elif(computer == -1 and you == 0):
        print("You Lose! 😢")

    elif(computer == 1 and you == -1):
        print("You Lose! 😢")

    elif(computer == 1 and you == 0):
        print("You Win! 🎉")

    elif(computer == 0 and you == -1):
        print("You Win! 🎉")

    elif(computer == 0 and you == 1):
        print("You Lose! 😢")

    else:
        print("Something went wrong!")