size=input("Enter the size of pizza , small ,medium or large   : ")
if size == "small" :
    cost=100
if size == "medium" :
    cost=200
if size == "large" :
    cost=300
pep=input("Do you want to add pepproni enter yes or no : ") # pep for pepperoni
ec=input("Do you want to add extra cheese enter yes or no : ") # ec for extra cheese.
if pep == "yes" :
    if ec == "yes" :
        print(f"Your total amount is {cost+30+20}")
    else :
        print(f"Your total amount is {cost+30}")
else :
    if ec == "yes" :
        print(f"Your total amount is {cost+20}")
    else :
        print(f"Your total amount is {cost}")