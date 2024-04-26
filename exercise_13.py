# fizzbuzz Question -- 
# You have to print 1 to n number where n taken from user.S
# if the number is divisble by 3 then print fizz
# if the number is divisble by 3 then print buzz
# if the number is divisble by 3 and 5 print fizzbuzz
# othwerwise print number itself.
n=int(input("Enter a number : "))
for i in range(1,n,1) : 
    if  i%3==0 and i%5==0:
        print("Fizzbuzz")
    elif i%3==0 :
        print("Fizz")
    elif i%5==0 :
        print("Buzz")
    else : 
        print(i)