# calculate the natural sum of a given number by using while loop.
n=int(input("Enter a number : "))
n1=n
sum_n=0
while n!=0 : 
    sum_n+=n
    n-=1
print(f"The natural sum to {n1} number is {sum_n}")