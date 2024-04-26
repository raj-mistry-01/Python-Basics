w=input("Enter your weight in kilograms : ") # w = weight
h=input("Enter your height in meters : ")
bmi=int(w)//float(h) **2
print("BMI = " + str(int(bmi)))
if bmi > 16 : 
    print("You are underweight and severe thinness.")
elif bmi > 16 and bmi < 16.9 :
    print("You are underweight and MOderate thinness.")
elif bmi > 17 and bmi < 18.4 :
    print("You are underweight and Mild thinness.")
elif bmi > 18.5 and bmi < 24.9 :
    print("YOu are in Normal Range .")
elif bmi > 25 and bmi < 29 :
    print("You are overweight but normal .")
else :
    print("You are not overweight.")