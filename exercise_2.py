age=input("Enter your age  : ")
# life is untill 90 ages.
a=90-int(age) # left years
b=a*365 # left days
c=a*52 # left weeks
print(f"You have {b} days , {c} weeks ,{a} years left")
# more in advanced you can write
#print(f"You have {int(90-age)*365} days,{int(90-age)*52 weeks,{int(90-age) years}}")