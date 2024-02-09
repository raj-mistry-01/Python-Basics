# higher , lower game 
import os
data = [
    {
        "name" : "Reserve Bank Of India",
        "followerCount" : 9,
        "decreption" : "Na12ional Bank Of India",
        "country" : "India"
},{
        "name" : "Bank Of China",
        "followerCount" : 11,
        "decreption" : "National Bank Of Chaina",
        "country" : "Chaina"
},{
        "name" : "Virat Kohli",
        "followerCount" : 100,
        "decreption" : "World Class Batter",
        "country" : "India"
},{
        "name" : "BJP",
        "followerCount" : 80,
        "decreption" : "National Political Party",
        "country" : "India"
},{
        "name" : "T-series",
        "followerCount" : 122,
        "decreption" : "A bollywood Youtube channel",
        "country" : "India"
},{
        "name" : "Narendra Modi",
        "followerCount" : 140,
        "decreption" : "Leader of the BJP",
        "country" : "India"
}]
def main() :
    score = 0
    for i in range(0,len(data)-1,1) :
        print(f"Compare 1: {data[i]["name"]} , {data[i]["decreption"]} from {data[i]["country"]}")
        print("VS")
        print(f"Compare 2: {data[i+1]["name"]} , {data[i+1]["decreption"]} from {data[i+1]["country"]}")
        choice = input("Enter the compare number who has more followers : ")
        if choice  == "2" : # check that i+1 is large or not
            if data[i+1]["followerCount"] > data[i]["followerCount"] :
                score +=1
                print(f"You won , You score is {score}.")
            else :
                print(f"You lost , Your score is {score}.")
                break
        elif choice == "1" : # check that i is large or not
            if data[i]["followerCount"] > data[i+1]["followerCount"] :
                score += 1
                print(f"You won , Your score is {score}.")
            else : 
                print(f"You lost , You score is {score}.")
                break
        elif choice == "Exit" :
                print("Thank You for Playing !!!!!")
                print(f"You left the game with {score}")
                break
    if score == 5 :
        print("Full Score !! , You have won the game.")
main()