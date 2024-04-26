# wall color paint can
# per can 7 liter 
import math
def calculate(w,h) :
    return math.ceil((w*h) / 7)
def main() :
     w=int(input("Enter the width of the wall :"))
     h=int(input("Enter the hieght of the wall :"))
     can=calculate(w,h)
     print(f"The number of can needed = {can}")
main()
