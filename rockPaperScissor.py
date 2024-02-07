import random

def computer():
    return random.randint(1,3)

def player():
    return int(input("choose one rock(1),paper(2),scissor(3)--->"))

computerMove=computer()
#print(computerMove)
playerMove=player()
if(computerMove==playerMove):
    print("tie !!! both have chosen same")
else:
    if(computerMove==1):
        if(playerMove==2):
            print("you won!!!")
        else:
            print("you lose!!!")
    if(computerMove==2):
        if(playerMove==3):
            print("you won!!!")
        else:
            print("you lose!!!")
    if(computerMove==3):
        if(playerMove==1):
            print("you won!!!")
        else:
            print("you lose!!!")
    