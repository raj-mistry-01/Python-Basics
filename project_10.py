# quiz game project
print("***********************")
print("Welcome to my quiz Game")
print("***********************")
from datafor_project10 import list_Option , list_quiz
score = 0
for i in range (0,len(list_quiz),1) :
    print(list_quiz[i][i],end="") 
    print(list_Option[i][i],end="")
    user_input = input("Enter your Answer (A/B/C/D) :")
    if user_input ==list_quiz[i]["answer"] :
        score +=1
        print("Your answer is correct.")
        print(f"Your score is {score}/{i+1}.",)
        print("")
    else :
        print("Your answer is incorrect.")
        print(f"Your score is {score}/{i+1}.")
        print("")

print(f"The score is {(score/5)*100}%.")