# calculate average height from usergiven list of heights. (using for loop)
heights=input("Enter all heights : ")
list_height=heights.split()
print(list_height)
sum_height=0
n=0
for i in list_height :
    sum_height=sum_height+int(i)
    n+=1
print(sum_height)
print(n)
print(f"The mean height is {sum_height/n}")