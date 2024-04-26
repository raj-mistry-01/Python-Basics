# taking head or tails from user and guessing it is correct or not.
import random
print("-----------------------------")
print("Tossing the coin ...")
print("-----------------------------")
x=input("Head or Tail : ")
list_=["Head","Tail"]
y=random.choice(list_)
if x==y :
    print("Yes won the tose.")
else :
    print("You loss the lose.")