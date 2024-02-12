# bank account
import random
accno  = random.randint(100000000000,999999999999)
import datetime
class main :
    def __init__(self, name, balance) -> None:
        self.name = name
        self.balance = balance
    def dispinfo(self) : 
        print(f"""
    SBI 
    Account type   : Personal 
    Account Holder : {self.name}
    Account No.    : {accno}
    Transaction summary : 
    Date     Time                        balance 
    {datetime.datetime.now()}            ₹{self.balance}/-
""")
    
    def withdraw(self) :
        choice1 = input("Want to withdraw , Yes or No :")
        if choice1 == "Yes" :
            self.amount = float(input("Enter the withdrawl amount : "))
            if self.balance >= self.amount :
                self.balance = self.balance - self.amount
                acc.dispinfo()
            else :
                print("Not enough money.") 
                acc.dispinfo()
    def deposit(self) :
        choice2 = input("Want to deposit , Yes or No : ")
        if choice2 == "Yes" :
            self.amount = float(input("Enter the deposit amount : "))
            self.balance = self.balance + self.amount
            acc.dispinfo()


print("----------------------Welcome To SBI----------------------")
choice = input("Wanna make an bank account ?? Yes or No : ")
if choice == "Yes" :
    print("Enter your name and your intial banlance .")
    x  = input("Enter your name : ")
    y = float(input("Enter the intial balance : "))
    acc = main(x,y)
    print("Account created successfully.")
    for i in range(0,1000,1) : # max operarions 1000.
        todo = input("Any Bank operations : ")
        if todo == "Yes" :
            acc.dispinfo()
            acc.withdraw()
            acc.deposit()
            acc.dispinfo()
        else :
            print("Thank for visiting us.")
            break
else :
    print("Thanks for visiing us.")