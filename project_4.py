# the silent auction.
import os
entry_Dictitionary={
    "name":[],
    "bid" :[]
}
def add(p,q) : 
    entry_Dictitionary["name"].append(p)
    entry_Dictitionary["bid"].append(q)
print("*********** Welcome to Silent Auction **************")
def main() :
    name_=input("Enter your Name : ")
    bid_amount=int(input("Enter your biding amount : "))
    add(name_,bid_amount)
    choice = input("Is there any other bidders , Type 'yes' or 'No' : ")
    if  choice == "Yes" :
        os.system('cls') # for clearing the previous entry detail on the screen
        main()
    elif choice == "No" :
        maxBid_index=entry_Dictitionary["bid"].index(max(entry_Dictitionary["bid"]))
        print(f"The winner is {entry_Dictitionary["name"][maxBid_index]} , the max bid is {max(entry_Dictitionary["bid"])}")
main()
