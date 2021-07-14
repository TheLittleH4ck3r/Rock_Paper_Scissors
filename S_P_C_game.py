import random

def gameWin(computer, you):
    if computer == you:
        return None
    elif computer == 'stone':
        if you =='caesar':
            return False
        elif you =='paper':
            return True
    elif computer == 'paper':
        if you=='stone':
            return False
        elif you =='caesar':
            return True
    elif computer == 'caesar':
        if you =='stone':
            return True
        elif you=='paper':
            return False



print("Computer True : Stone, Paper, or Caesar?")
randNo = random.randint(1, 3)
if randNo == 1:
    computer = 'stone'
elif randNo == 2:
    computer = 'paper'
elif randNo == 3:
    computer = 'caesar'

you = input ("Your turn: Stone, Paper, or Caesar?\n")
a = gameWin(computer, you)

print(f"Computer chose {computer}")
print(f"You chose {you}")
 
if a ==None:
    print("The game is tie!")
elif a :
    print("You Win!")
else:
    print("You Lose!")
