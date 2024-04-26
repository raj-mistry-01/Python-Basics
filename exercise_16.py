marks={
"Jenny":92,
"Rahul": 41,
"Aniket":99,
"Prem":34
}
grades={}
for i in marks : # jenny
    marks_=marks[i] # 92
    if marks_ > 90 :
        grades[i]="A+"
    elif marks_ > 80 and marks_ < 90 :
        grades[i]="A"
    elif marks_ > 70 and marks_ <80 :
        grades[i]="B+"
    elif marks_ > 50 and marks_ < 70 :
        grades[i]="C+"
    elif marks_ > 30 and marks_ < 50 :
        grades[i]="C"
    else :
        grades[i]="F"

print(grades)