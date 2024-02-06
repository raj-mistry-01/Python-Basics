# rock paper scissor game.
# 0 for rock.
# 1 for paper.
# 2 for scissor.
import random
userchoice=int(input("Enter 0 for Rock , 1 for Paper , 2 for scissor : "))
computerChoice=random.randint(0,2)
print(computerChoice)
if computerChoice == userchoice :
    print("It's a draw.")
elif userchoice == 0 and computerChoice == 2 :
    print("You win.")
elif computerChoice > userchoice :
    print("You loss.")
elif userchoice > computerChoice :
    print("You win.")
elif computerChoice == 0 and userchoice == 2 :
    print("You loss.")