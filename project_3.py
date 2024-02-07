# the Caeser Cipher
"""

what is it ?

the secret message 
The encrpytion and decrpytion of the message.
caesar cipher is the simple moethod to do it.
After applying the encrpytion to the simple text  , not it is cipher text.

Plain text : A B C D ....
Shift No.  : 1
Cipher text : B C D ....

so  for the encryption function is E(x) = (x+n) % 26
function for the decrption funciton if D(x) = (x-n) % 26
where x is a letter 
    n= shift count
if (x-n) becomes negative than add 26 to that.
"""

list_=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrpytion() :
    message = input("Enter the message : ")
    shift=int(input("Enter the shift count : "))
    encrypted_list = []
    for i in message :
        if i in list_ :
            for j in range(0,len(list_),1) : 
                if i == list_[j] :
                    letter_shift = j+shift 
                    encrpytedLetter_index = (letter_shift) % 26
                    encrypted_list.append(list_[encrpytedLetter_index])
        else :
            encrypted_list.append(i)
    print("The encryted message : ",end="")
    for i in encrypted_list :
        print(i,end="")

def decrption() :
    message = input("Enter the message : ")
    shift=int(input("Enter the shift count : "))
    decrypted_list = []
    for i in message :
        if i in list_ :
            for j in range(0,len(list_),1) : 
                if i == list_[j] :
                    letter_shift = j-shift 
                    if letter_shift < 0 :
                        decrpytedLetter_index = (letter_shift+26) % 26
                        decrypted_list.append(list_[decrpytedLetter_index])
                    else :
                        decrpytedLetter_index = (letter_shift) % 26
                        decrypted_list.append(list_[decrpytedLetter_index])
        else :
            decrypted_list.append(i)
    print("The decryted message : ",end="")
    for i in decrypted_list :
        print(i,end="")
def main() :
    choice=input("Type 'encrypt' for the encryption , type 'decrypt' for the decryption : ")
    if choice == "encrypt" :
        encrpytion()
    if choice == "decrypt" :
        decrption()
    continueOrNot()
    
def continueOrNot() :
    print("\n")
    choice1=input("Want to continue , Type 'Yes' or 'No'")
    if choice1 == "Yes" :
        main()
    elif choice1 == "No" : 
        print("Good Bye!!!!")

main()