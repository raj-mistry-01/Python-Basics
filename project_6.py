# guessing number game .
# for easy level 10 attempts and for hard 5 attempts.
import random 
randomNum = random.randint(1,100)
print(randomNum)
print("------------Number Guessing Game----------------")
def compare(attemptNo,n) :
    flag = 0 #  all incorrect guess , loose the game
    print(f"You have {attemptNo} attempts.")
    for i in range(0,attemptNo,1) :
        if n == randomNum :
            print(f"You won, The random number generated was {randomNum}")
            flag = 1 # won the game.
            break
        elif n > randomNum :
            print(f"You have {attemptNo-i} attempts left.")
            print("Your number is high , Guess Low ")
            n = int(input("Enter a number : "))
        else :
            print(f"You have {attemptNo-i} attempts left.")
            print("Your number is low , guess high")
            n = int(input("Enter a number : "))
    if flag == 0 :
        print(f"You attempts are over ,Random number was {randomNum} You have lost the game .")

def main() :
    choice = input("Enter the level 'Easy' or 'Hard'")
    n = int(input("Guess A number between 1 to 100 including both."))
    if choice == "Easy" :
        attemptNo = 10
        compare(attemptNo,n)
    else : 
        attemptNo = 5
        compare(attemptNo,n)
main()
