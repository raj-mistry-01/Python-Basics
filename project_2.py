# Password Generator.
import random
print("------------------------ Password Generator ------------------------")
letters=["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R",
"S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","k","l","m"
"n","o","p","q","r","s","t","u","v","w","x","y","z"]
specialCharacters=["~","!","@","#","$","%","^","&","*","|","[","]","{","}","(",")"]
numbers=["1","2","3","4","5","6","7","8","9"]
n_letters=int(input("Enter the number of letters you want in passord : "))
n_sp=int(input("Enter the number of special characters  you want in passord : "))
n_num=int(input("Enter the number of numbers  you want in passord : "))
str1=""
for i in range(0,n_letters,1) :
    str1+=random.choice(letters) # choice method returns the string value.
for i in range(0,n_sp,1) : 
    str1+=random.choice(specialCharacters)
for i in range(0,n_num,1) : 
    str1+=random.choice(numbers)
list_=list(str1) # because we can not use shuffle method to strings.
random.shuffle(list_)
print("Password : ",end="")
for i in list_ : 
    print(i,end="")