import random 
from random import randint

def checker(computer, user):
    if (computer == user):
        return 0
    elif (computer == 0 and user == 1):
        return -1
    elif (computer == 1 and user == 2):
        return -1
    elif (computer == 2 and user == 0):
        return -1
    else:
        return 1

computer = randint(0,2)
user = int(input("Press 0 for Snake, Press 1 for Water or Press 2 for Gun: "))
    
score = checker(computer,user)

print("You: ",user)
print("Computer: ",computer)

if (score == 0):
    print("DRAW!")
elif (score == -1):
    print("COMPUTER WINS!")
    print("PLAYER LOSES!")
else:
    print("PLAYER WINS!")
    print("COMPUTER LOSES!")
    
