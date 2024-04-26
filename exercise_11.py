# find the maximum number from a list
numbers=input("Enter the numbers by separating by a space : ")
n_list=numbers.split()
max_n=int(n_list[0])
for i in n_list :
    if int(i) > max_n :
        max_n=i
print(f"The max number among the entered numbers is  : {max_n}")