# the days in a months for user entered year.
dict_month={
    "31" : ["January","March","May","July","August","October","December"],
    "30" : [] # for left months.
}
import leap_year
from leap_year import flag,y # importing a variable (object) from a system file.
month_Name=input("Enter the month : ")
if month_Name == "February"  :
        if flag == True : # leap year    
            print(f"As {y} is a leap year , the days in february are 28")
        else :
            print(f"As {y} is a not leap year , the days in february are 29")
elif month_Name in dict_month["31"] :  # other month
    print(f"The days in {month_Name} is 31")
else :
    print(f"The days in {month_Name} is 30")