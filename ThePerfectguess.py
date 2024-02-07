import random
randNum=random.randint(1,100)       # randint will give a randum number between 1 and 100 including 1 and 100
#print(randNum)
guess=0
userGuess=None
while(randNum !=userGuess):
    guess+=1
    userGuess=int(input("guess a number between 1 to 100 : "))
    if(randNum==userGuess):
        print(f"you guessed it right in  {guess} guesses")
    else:
        if(randNum>userGuess):
            print("you guessed it wrong! enter a greater number")
        else:
            print("you guessed it wrong! enter a smaller number")



#writing the highscore in harddisc
f=open("highScore.txt",'r')
score=int(f.read())
f.close()
if(score>guess):
    print("new highscore!!!")
    f=open("highScore.txt",'w')
    f.write(str(guess))
    f.close()


