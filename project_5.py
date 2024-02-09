# simple calculator.
# Use the concept of buffer memory.
print("-------------------Calculator-------------------")
buffer = 0
n1 = float(input("Enter the first number : ")) # local varible but making global by passing it to main() function.
def add(n1,q) : # q is formal parameter for n2
    buffer = n1 + q
    return buffer

def substract(n1,q) :
    buffer = n1 - q
    return buffer

def multiply(n1,q) :
    buffer = n1*q
    return buffer

def divide(n1,q) :
    buffer = n1/q
    return buffer

def main(n1) :
    operation = input("Enter the arithmetic operation : ")
    n2 = float(input("Enter the second number : "))
    if operation == "+" :
        buffer=add(n1,n2)
        print(f"{n1}+{n2}={buffer}")
    elif operation == "-" :
        buffer = substract(n1,n2)
        print(f"{n1}-{n2}={buffer}")
    elif operation == "*" :
        buffer = multiply(n1,n2)
        print(f"{n1}*{n2}={buffer}")
    elif operation == "/" :
        buffer = divide(n1,n2)
        print(f"{n1}/{n2}={buffer}")
    else :
        print("Please choose a valid operator .")
        main(n1)
    choice = input(f"Type 'Yes' to continue with the output {buffer},'New' to start with the new calculation ,  or 'No' to exit ")
    if choice == "Yes" :
        n1 = buffer 
        main(n1)
    elif choice == "New" : 
        buffer = 0
        n1 = float(input("Enter the first number : ")) # redefination of the n1 for the new calculation. 
        main(n1)
    elif choice == "No" :
        print("Thank You for the visit !!!!!!")
        print("-------------------Calculator-------------------")
main(n1)